# [HLS（HTTP Live Streaming）协议之m3u8文件生成方式](https://www.cnblogs.com/qazwsxwtc/p/5144604.html)

   HLS（HTTP Live Streaming）是Apple的动态码率[自适应技术](http://baike.baidu.com/view/829451.htm)。主要用于PC和Apple终端的音视频服务。包括一个m3u(8)的索引文件，TS媒体分片文件和key加密串文件。

   HLS的关键其实是生成m3u8索引文件和TS媒体分片，下面我将通过以下几个步骤讲述m3u8及TS媒体分片的生成：

**第一步**---获取TS文件：

   TS(Transport Stream)既传输流，标准制定于mpeg2文档协议中，当时TS格式主要是为了数字电视传输而制定，制定的年限相当早，在网上能找到很完备的mpeg2文档介绍。大家可以参考mpege-2文档标准中TS流介绍学习该格式。

   现在的我们下载的高清电影以mkv格式居多，早期的的电影可能一rmvb和avi居多，更早的甚至还有mpg格式，现在流行的视频网站下载的视频基本都是flv格式。这些格式都是非TS格式，不过不要紧，现在视频转码的软件也非常多，我们可以通过以下两种方式进行转码。

  1，通过格式工厂软件，这是一个比较成熟的软件，网上百度下载即可，不过只有软件，不利于后期源码的直接开发；

　　　　下载地址：http://www.pcfreetime.com/CN/index.html

  2，通过ffmpeg进行格式转换，该工程为开源项目，我们在实际开发的过程中可以直接集成该源码，（具体的集成方式该篇文章不讲解，后期将对怎么封装调用ffmpeg做出相应介绍）。目前我们只是想获取TS文件用于生产m3u8索引文件和TS分片而已，直接下载ffmpeg的可执行程序，通过ffmpeg.exe转换即可：  

​      下载地址：http://ffmpeg.org/

  通过命令行模式进入到ffmpeg.exe所在的目录，在命令行中输入：ffmpeg.exe -i XXX.flv xxx.ts 即可，如下图：

​     ![img](https://images2015.cnblogs.com/blog/880365/201601/880365-20160120110944297-1502257990.png)

​                          图1

 

**第二步**--生成m3u8索引文件和TS媒体分片

 1, m3u8 源码下，

 下载地址：

​      https://github.com/johnf/m3u8-segmenter/archive/master.zip 该地址的源码主要是在linux系统编译，不过也能修改成在windows下编译。

 windows的源码下载 ：

​     官网:[ http://www.espend.de/artikel/iphone-ipad-ipod-http-streaming-segmenter-and-m3u8-windows.html  ](http://www.cnblogs.com/ http:/www.espend.de/artikel/iphone-ipad-ipod-http-streaming-segmenter-and-m3u8-windows.html  )   源码地址http://code.google.com/p/httpsegmenter/  不过也要依赖ffmpeg库，稍微修改下即可。

   其实以上两个路径的源码其实是一样滴，下面那个是德国人修改写的，看后缀de就知道了，可能需要翻墙才能打开。

   下面是截取segmenter.c中的代码分片片段：

```
    do {
        double segment_time = 0.0;
        AVPacket packet;
        double packetStartTime = 0.0;
        double packetDuration = 0.0;
        
        if (!decode_done)
        {
            decode_done = av_read_frame(ic, &packet);
            if (!decode_done)
            {
                if (packet.stream_index != video_index &&
                    packet.stream_index != audio_index)
                {
                    av_free_packet(&packet);
                    continue;
                }
                
                timeStamp = 
                    (double)(packet.pts) * 
                    (double)(ic->streams[packet.stream_index]->time_base.num) /
                    (double)(ic->streams[packet.stream_index]->time_base.den);
                
                if (av_dup_packet(&packet) < 0)
                {
                    fprintf(stderr, "Could not duplicate packet\n");
                    av_free_packet(&packet);
                    break;
                }
                
                insertPacket(streamLace, &packet, timeStamp);
            }
        }
        
        if (countPackets(streamLace) < 50 && !decode_done)
        {
            /* allow the queue to fill up so that the packets can be sorted properly */
            continue;
        }
        
        if (!removePacket(streamLace, &packet))
        {
            if (decode_done)
            {
                /* the queue is empty, we are done */
                break;
            }
            
            assert(decode_done);
            continue;
        }
        
        packetStartTime = 
            (double)(packet.pts) * 
            (double)(ic->streams[packet.stream_index]->time_base.num) /
            (double)(ic->streams[packet.stream_index]->time_base.den);
        
        packetDuration =
            (double)(packet.duration) *
            (double)(ic->streams[packet.stream_index]->time_base.num) /
            (double)(ic->streams[packet.stream_index]->time_base.den);
        
#if !defined(NDEBUG) && (defined(DEBUG) || defined(_DEBUG))
        if (av_log_get_level() >= AV_LOG_VERBOSE)
            fprintf(stderr,
                    "stream %i, packet [%f, %f)\n",
                    packet.stream_index,
                    packetStartTime,
                    packetStartTime + packetDuration);
#endif

        segment_duration = packetStartTime + packetDuration - prev_segment_time;

        // NOTE: segments are supposed to start on a keyframe.
        // If the keyframe interval and segment duration do not match
        // forcing the segment creation for "better seeking behavior"
        // will result in decoding artifacts after seeking or stream switching.
        if (packet.stream_index == video_index && (packet.flags & AV_PKT_FLAG_KEY || strict_segment_duration)) {
            segment_time = packetStartTime;
        }
        else if (video_index < 0) {
            segment_time = packetStartTime;
        }
        else {
            segment_time = prev_segment_time;
        }

        if (segment_time - prev_segment_time + segment_duration_error_tolerance >
            target_segment_duration + extra_duration_needed) 
        {
            avio_flush(oc->pb);
            avio_close(oc->pb);

            // Keep track of accumulated rounding error to account for it in later chunks.
            segment_duration = segment_time - prev_segment_time;
            rounded_segment_duration = (int)(segment_duration + 0.5);
            extra_duration_needed += (double)rounded_segment_duration - segment_duration;

            updatePlaylist(playlist,
                           playlist_filename,
                           output_filename,
                           output_index,
                           rounded_segment_duration);
            
            _snprintf(output_filename, strlen(output_prefix) + 15, "%s-%u.ts", output_prefix, ++output_index);
            if (avio_open(&oc->pb, output_filename, AVIO_FLAG_WRITE) < 0) {
                fprintf(stderr, "Could not open '%s'\n", output_filename);
                break;
            }

            // close when we find the 'kill' file
            if (kill_file) {
                FILE* fp = fopen("kill", "rb");
                if (fp) {
                    fprintf(stderr, "user abort: found kill file\n");
                    fclose(fp);
                    remove("kill");
                    decode_done = 1;
                    removeAllPackets(streamLace);
                }
            }
            prev_segment_time = segment_time;
        }

        ret = av_interleaved_write_frame(oc, &packet);
        if (ret < 0) {
            fprintf(stderr, "Warning: Could not write frame of stream\n");
        }
        else if (ret > 0) {
            fprintf(stderr, "End of stream requested\n");
            av_free_packet(&packet);
            break;
        }

        av_free_packet(&packet);
    } while (!decode_done || countPackets(streamLace) > 0);
```

2, 把下载下来的源码直接在vs中编译生成exe即可， 如我生成的exe为m3u8.exe：

![img](https://images2015.cnblogs.com/blog/880365/201601/880365-20160120112835218-1779689157.png)

​                   图2

3, 通过命令行进入该目录，并在命令行中输入: m3u8.exe -d 10 -x m3u8list.m3u8 即可生成.m3u8文件和ts分片文件，如图2目录文件的m3u8list.m3u8 和-1.ts、-2.ts和-3.ts文件。

 ![img](https://images2015.cnblogs.com/blog/880365/201601/880365-20160120113352281-1537722939.png)

​        图3

4， 如以图2的目录列表，直接用VLC播放器就可以播放m3u8list.m3u8文件， 用写字板查看m3u8文件内容为：

\#EXTM3U
\#EXT-X-TARGETDURATION:10
\#EXTINF:10,
-1.ts
\#EXTINF:10,
-2.ts
\#EXTINF:9,
-3.ts
\#EXT-X-ENDLIST

 

 

好了，大功告成！  我们可以直接播放m3u8list.m3u8 和-1.ts、-2.ts、-3.ts文件 ，  也可以直接用http协议传输这些文件，就成了hls协议了 

# m3u8 文件格式详解

## 简介

> [M3U8](https://links.jianshu.com/go?to=https%3A%2F%2Fzh.wikipedia.org%2Fwiki%2FM3U%23M3U8) 是 Unicode 版本的 [M3U](https://links.jianshu.com/go?to=https%3A%2F%2Fzh.wikipedia.org%2Fwiki%2FM3U)，用 UTF-8 编码。"M3U" 和 "M3U8" 文件都是苹果公司使用的 [HTTP Live Streaming（HLS）](https://links.jianshu.com/go?to=https%3A%2F%2Fzh.wikipedia.org%2Fwiki%2FHTTP_Live_Streaming) 协议格式的基础，这种协议格式可以在 iPhone 和 Macbook 等设备播放。

上述文字定义来自于[维基百科](https://links.jianshu.com/go?to=https%3A%2F%2Fzh.wikipedia.org%2Fwiki%2FWikipedia%3A%E9%A6%96%E9%A1%B5)。可以看到，[m3u8](https://links.jianshu.com/go?to=https%3A%2F%2Fzh.wikipedia.org%2Fwiki%2FM3U%23M3U8) 文件其实是 [HTTP Live Streaming（缩写为 HLS）](https://links.jianshu.com/go?to=https%3A%2F%2Fzh.wikipedia.org%2Fwiki%2FHTTP_Live_Streaming) 协议的部分内容，而 [HLS](https://links.jianshu.com/go?to=https%3A%2F%2Fzh.wikipedia.org%2Fwiki%2FHTTP_Live_Streaming) 是一个由苹果公司提出的基于 [HTTP](https://links.jianshu.com/go?to=https%3A%2F%2Fzh.wikipedia.org%2Fwiki%2FHTTP) 的[流媒体](https://links.jianshu.com/go?to=https%3A%2F%2Fzh.wikipedia.org%2Fwiki%2F%E6%B5%81%E5%AA%92%E4%BD%93)[网络传输协议](https://links.jianshu.com/go?to=https%3A%2F%2Fzh.wikipedia.org%2Fwiki%2F%E7%BD%91%E7%BB%9C%E4%BC%A0%E8%BE%93%E5%8D%8F%E8%AE%AE)。

> [HLS](https://links.jianshu.com/go?to=https%3A%2F%2Fzh.wikipedia.org%2Fwiki%2FHTTP_Live_Streaming) 的工作原理是把整个流分成一个个小的基于 [HTTP](https://links.jianshu.com/go?to=https%3A%2F%2Fzh.wikipedia.org%2Fwiki%2FHTTP) 的文件来下载，每次只下载一些。当媒体流正在播放时，客户端可以选择从许多不同的备用源中以不同的速率下载同样的资源，允许流媒体会话适应不同的数据速率。在开始一个流媒体会话时，客户端会下载一个包含元数据的 extended M3U (m3u8) playlist文件，用于寻找可用的媒体流。
> [HLS](https://links.jianshu.com/go?to=https%3A%2F%2Fzh.wikipedia.org%2Fwiki%2FHTTP_Live_Streaming) 只请求基本的 [HTTP](https://links.jianshu.com/go?to=https%3A%2F%2Fzh.wikipedia.org%2Fwiki%2FHTTP) 报文，与[实时传输协议（RTP）](https://links.jianshu.com/go?to=https%3A%2F%2Fzh.wikipedia.org%2Fwiki%2F%E5%AE%9E%E6%97%B6%E4%BC%A0%E8%BE%93%E5%8D%8F%E8%AE%AE)不同，[HLS](https://links.jianshu.com/go?to=https%3A%2F%2Fzh.wikipedia.org%2Fwiki%2FHTTP_Live_Streaming) 可以穿过任何允许 [HTTP](https://links.jianshu.com/go?to=https%3A%2F%2Fzh.wikipedia.org%2Fwiki%2FHTTP) 数据通过的防火墙或者代理服务器。它也很容易使用[内容分发网络](https://links.jianshu.com/go?to=https%3A%2F%2Fzh.wikipedia.org%2Fwiki%2F%E5%85%A7%E5%AE%B9%E5%88%86%E7%99%BC%E7%B6%B2%E7%B5%A1)来传输媒体流。

简而言之，[HLS](https://links.jianshu.com/go?to=https%3A%2F%2Fzh.wikipedia.org%2Fwiki%2FHTTP_Live_Streaming) 是新一代流媒体传输协议，其基本实现原理为将一个大的媒体文件进行分片，将该分片文件资源路径记录于 m3u8 文件（即 playlist）内，其中附带一些额外描述（比如该资源的多带宽信息···）用于提供给客户端。客户端依据该 m3u8 文件即可获取对应的媒体资源，进行播放。

因此，客户端获取 [HLS](https://links.jianshu.com/go?to=https%3A%2F%2Fzh.wikipedia.org%2Fwiki%2FHTTP_Live_Streaming) 流文件，主要就是对 m3u8 文件进行解析操作。

那么，下面就简单介绍下 m3u8 文件。

## M3U8 文件简介

m3u8 文件实质是一个播放列表（playlist），其可能是一个媒体播放列表（Media Playlist），或者是一个主列表（Master Playlist）。但无论是哪种播放列表，其内部文字使用的都是 utf-8 编码。

当 m3u8 文件作为媒体播放列表（Meida Playlist）时，其内部信息记录的是一系列媒体片段资源，顺序播放该片段资源，即可完整展示多媒体资源。其格式如下所示：



```txt
#EXTM3U
#EXT-X-TARGETDURATION:10

#EXTINF:9.009,
http://media.example.com/first.ts
#EXTINF:9.009,
http://media.example.com/second.ts
#EXTINF:3.003,
http://media.example.com/third.ts
```

对于点播来说，客户端只需按顺序下载上述片段资源，依次进行播放即可。而对于直播来说，客户端需要 **定时重新请求** 该 m3u8 文件，看下是否有新的片段数据需要进行下载并播放。

当 m3u8 作为主播放列表（Master Playlist）时，其内部提供的是同一份媒体资源的多份流列表资源（Variant Stream）。其格式如下所示：



```txt
#EXTM3U
#EXT-X-STREAM-INF:BANDWIDTH=150000,RESOLUTION=416x234,CODECS="avc1.42e00a,mp4a.40.2"
http://example.com/low/index.m3u8
#EXT-X-STREAM-INF:BANDWIDTH=240000,RESOLUTION=416x234,CODECS="avc1.42e00a,mp4a.40.2"
http://example.com/lo_mid/index.m3u8
#EXT-X-STREAM-INF:BANDWIDTH=440000,RESOLUTION=416x234,CODECS="avc1.42e00a,mp4a.40.2"
http://example.com/hi_mid/index.m3u8
#EXT-X-STREAM-INF:BANDWIDTH=640000,RESOLUTION=640x360,CODECS="avc1.42e00a,mp4a.40.2"
http://example.com/high/index.m3u8
#EXT-X-STREAM-INF:BANDWIDTH=64000,CODECS="mp4a.40.5"
http://example.com/audio/index.m3u8
```

该备用流资源指定了多种不同码率，不同格式的媒体播放列表，并且，该备用流资源也可同时提供不同版本的资源内容，比如不同语言的音频文件，不同角度拍摄的视屏文件等等。客户可以根据不同的网络状态选取合适码流的资源，并且最好根据用户喜好选择合适的资源内容。

更多详细内容，可查看：

- [Creating a Master Playlist](https://links.jianshu.com/go?to=https%3A%2F%2Fdeveloper.apple.com%2Fdocumentation%2Fhttp_live_streaming%2Fexample_playlists_for_http_live_streaming%2Fcreating_a_master_playlist)
- [Adding Alternate Media to a Playlist](https://links.jianshu.com/go?to=https%3A%2F%2Fdeveloper.apple.com%2Fdocumentation%2Fhttp_live_streaming%2Fexample_playlists_for_http_live_streaming%2Fadding_alternate_media_to_a_playlist)

以上，就是 m3u8 文件的大概内容。下面，我们就对 m3u8 内容格式进行讲解。

## m3u8 文件格式简解

m3u8 的文件格式主要包含三方面内容：

1. **[文件播放列表格式定义](https://links.jianshu.com/go?to=https%3A%2F%2Ftools.ietf.org%2Fhtml%2Frfc8216%23page-10)**：播放列表（Playlist，也即 m3u8 文件） 内容需严格满足[规范定义](https://links.jianshu.com/go?to=https%3A%2F%2Ftools.ietf.org%2Fhtml%2Frfc8216%23page-10)所提要求。下面罗列一些主要遵循的条件：

- m3u8 文件必须以 utf-8 进行编码，不能使用 Byte Order Mark（BOM）字节序， 不能包含 utf-8 控制字符（U+0000 ~ U_001F 和 U+007F ~ u+009F）。
- m3u8 文件的每一行要么是一个 URI，要么是空行，要么就是以 **#** 开头的字符串。不能出现空白字符，除了显示声明的元素。
- m3u8 文件中以 **#** 开头的字符串要么是注释，要么就是标签。标签以 **#EXT** 开头，大小写敏感。

1. **[属性列表（Attribute Lists）](https://links.jianshu.com/go?to=https%3A%2F%2Ftools.ietf.org%2Fhtml%2Frfc8216%23page-11)**：某些特定的标签的值为属性列表。标签后面的属性列表以 *逗号* 作为分隔符，分离出多组不带空格的 *属性/值* 对。
   **属性/值** 对的语法格式如下：



```txt
AttributeName=AttributeValue
```

其中：

- **属性`AttributeName`**是由 [A..Z],[0..9] 和 `-` 组成的不带引号的字符串。因此，**属性`AttributeName`只能使用大写字母，不能使用小写字母**，并且`AttributeName`和`=`中间不能有空格，同理，`=`和`AttributeValue`之间也不能有空格。
- **值`AttributeValue`**的只能取以下类型：
  - **十进制整型（decimal-interger）**：由 [0..9] 之间组成的十进制不带引号的字符串，范围为 ![0](https://math.jianshu.com/math?formula=0) ~ ![2^{64}](https://math.jianshu.com/math?formula=2%5E%7B64%7D)（18446744073709551615），字符长度为 1 ~ 20 之间。
  - **十六进制序列**：由 [0..9] 和 [A..F] 且前缀为 0x 或 0X 组合成的不带引号的字符串。其序列的最大长度取决于他的属性名`AttributeNames`。
  - **带符号十进制浮点型（signed-decimal-floating-point）**：由 [0..9]，`-`和`.`组合成的不带引号的字符串。
  - **字符串（quoted-string）**：由双引号包裹表示的字符串。其中，0xA，0xD 和 双引号`"`不能出现在该字符串中。该字符串区分大小写。
  - **可枚举字符串（enumerated-string）**：由`AttributeName`显示定义的一系列不带引号的字符串。该字符串不能包含双引号`"`，逗号`,`和空白字符。
  - **decimal-resolution**：由字符`x`进行隔离的两个十进制整型数。第一个整型表示水平宽度大小，第二个整型数表示垂直方向高度大小（单位：像素）。

1. **[标签](https://links.jianshu.com/go?to=https%3A%2F%2Ftools.ietf.org%2Fhtml%2Frfc8216%23page-12)**：标签用于指定 m3u8 文件的全局参数或在其后面的切片文件/媒体播放列表的一些信息。

标签的类型可分为五种类型：**[基础标签（Basic Tags）](https://links.jianshu.com/go?to=https%3A%2F%2Ftools.ietf.org%2Fhtml%2Frfc8216%23section-4.3.1)**，**[媒体片段类型标签（Media Segment Tags）](https://links.jianshu.com/go?to=https%3A%2F%2Ftools.ietf.org%2Fhtml%2Frfc8216%23page-13)**，**[媒体播放列表类型标签](https://links.jianshu.com/go?to=https%3A%2F%2Ftools.ietf.org%2Fhtml%2Frfc8216%23page-22)**，**[主播放列表类型标签](https://links.jianshu.com/go?to=https%3A%2F%2Ftools.ietf.org%2Fhtml%2Frfc8216%23page-25)** 和 **[播放列表类型标签](https://links.jianshu.com/go?to=https%3A%2F%2Ftools.ietf.org%2Fhtml%2Frfc8216%23page-35)**。其具体内容如下所示：

- **[基础标签（Basic Tags）](https://links.jianshu.com/go?to=https%3A%2F%2Ftools.ietf.org%2Fhtml%2Frfc8216%23section-4.3.1)**：可同时适用于媒体播放列表（Media Playlist）和主播放列表（Master Playlist）。具体标签如下：

  - **[EXTM3U](https://links.jianshu.com/go?to=https%3A%2F%2Ftools.ietf.org%2Fhtml%2Frfc8216%23page-12)**：表明该文件是一个 m3u8 文件。每个 [M3U](https://links.jianshu.com/go?to=https%3A%2F%2Fzh.wikipedia.org%2Fwiki%2FM3U) 文件必须将该标签放置在第一行。
  - **[EXT-X-VERSION](https://links.jianshu.com/go?to=https%3A%2F%2Ftools.ietf.org%2Fhtml%2Frfc8216%23page-12)**：表示 [HLS](https://links.jianshu.com/go?to=https%3A%2F%2Fzh.wikipedia.org%2Fwiki%2FHTTP_Live_Streaming) 的协议版本号，该标签与流媒体的兼容性相关。该标签为全局作用域，使能整个 m3u8 文件；每个 m3u8 文件内最多只能出现一个该标签定义。如果 m3u8 文件不包含该标签，则默认为协议的第一个版本。

- **[媒体片段类型标签（Media Segment Tags）](https://links.jianshu.com/go?to=https%3A%2F%2Ftools.ietf.org%2Fhtml%2Frfc8216%23page-13)**：每个切片 URI 前面都有一系列媒体片段标签对其进行描述。有些片段标签只对其后切片资源有效；有些片段标签对其后所有切片都有效，直到后续遇到另一个该标签描述。**媒体片段类型标签不能出现在主播放列表（Master Playlist）中**。具体标签如下：

  - **[EXTINF](https://links.jianshu.com/go?to=https%3A%2F%2Ftools.ietf.org%2Fhtml%2Frfc8216%23page-13)**：表示其后 URL 指定的媒体片段时长（单位为秒）。每个 URL 媒体片段之前必须指定该标签。该标签的使用格式为：

    

    ```m3u8
    #EXTINF:<duration>,[<title>]
    ```

    其中：

    - `duration`：可以为十进制的整型或者浮点型，其值必须小于或等于 **EXT-X-TARGETDURATION** 指定的值。
      注：建议始终使用浮点型指定时长，这可以让客户端在定位流时，减少四舍五入错误。但是如果兼容版本号 **EXT-X-VERSION** 小于 3，那么必须使用整型。

  - **[EXT-X-BYTERANGE](https://links.jianshu.com/go?to=https%3A%2F%2Ftools.ietf.org%2Fhtml%2Frfc8216%23page-14)**：该标签表示接下来的切片资源是其后 URI 指定的媒体片段资源的局部范围（即截取 URI 媒体资源部分内容作为下一个切片）。该标签只对其后一个 URI 起作用。其格式为：

    

    ```m3u8
    #EXT-X-BYTERANGE:<n>[@<o>]
    ```

    其中：

    - `n`是一个十进制整型，表示截取片段大小（单位：字节）。
    - 可选参数`o`也是一个十进制整型，指示截取起始位置（以字节表示，在 URI 指定的资源开头移动该字节位置后进行截取）。
      如果`o`未指定，则截取起始位置从上一个该标签截取完成的下一个字节（即上一个`n+o+1`）开始截取。
      如果没有指定该标签，则表明的切分范围为整个 URI 资源片段。
      注：使用 **EXT-X-BYTERANGE** 标签要求兼容版本号 **EXT-X-VERSION** 大于等于 4。

  - **[EXT-X-DISCONTINUITY](https://links.jianshu.com/go?to=https%3A%2F%2Ftools.ietf.org%2Fhtml%2Frfc8216%23page-14)**：该标签表明其前一个切片与下一个切片之间存在中断。其格式为：

    

    ```m3u8
    #EXT-X-DISCONTINUITY
    ```

    当以下任一情况变化时，必须使用该标签：

    - 文件格式（file format）
    - 数字（number），类型（type），媒体标识符（identifiers of tracks）
    - 时间戳序列（timestamp sequence）

    当以下任一情况变化时，应当使用该标签：

    - 编码参数（encoding parameters）
    - 编码序列（encoding sequence）

    注：**EXT-X-DISCONTINUITY** 的一个经典使用场景就是在视屏流中插入广告，由于视屏流与广告视屏流不是同一份资源，因此在这两种流切换时使用 **EXT-X-DISCONTINUITY** 进行指明，客户端看到该标签后，就会处理这种切换中断问题，让体验更佳。
    更多详细内容，请查看：[Incorporating Ads into a Playlist](https://links.jianshu.com/go?to=https%3A%2F%2Fdeveloper.apple.com%2Fdocumentation%2Fhttp_live_streaming%2Fexample_playlists_for_http_live_streaming%2Fincorporating_ads_into_a_playlist)

  - **[EXT-X-KEY](https://links.jianshu.com/go?to=https%3A%2F%2Ftools.ietf.org%2Fhtml%2Frfc8216%23page-15)**：媒体片段可以进行加密，而该标签可以指定解密方法。
    该标签对所有 *媒体片段* 和 由标签 **EXT-X-MAP** 声明的围绕其间的所有 *媒体初始化块（Meida Initialization Section）* 都起作用，直到遇到下一个 **EXT-X-KEY**（若 m3u8 文件只有一个 **EXT-X-KEY** 标签，则其作用于所有媒体片段）。
    多个 **EXT-X-KEY** 标签如果最终生成的是同样的秘钥，则他们都可作用于同一个媒体片段。
    该标签使用格式为：

    

    ```m3u8
    #EXT-X-KEY:<attribute-list>
    ```

    属性列表可以包含如下几个键：

    - **METHOD**：该值是一个可枚举的字符串，指定了加密方法。
      该键是必须参数。其值可为`NONE`，`AES-128`，`SAMPLE-AES`当中的一个。
      其中：
      `NONE`：表示切片未进行加密（此时其他属性不能出现）；
      `AES-128`：表示表示使用 [AES-128](https://links.jianshu.com/go?to=https%3A%2F%2Ftools.ietf.org%2Fhtml%2Frfc8216%23ref-AES_128) 进行加密。
      `SAMPLE-AES`：意味着媒体片段当中包含样本媒体，比如音频或视频，它们使用 [AES-128](https://links.jianshu.com/go?to=https%3A%2F%2Ftools.ietf.org%2Fhtml%2Frfc8216%23ref-AES_128) 进行加密。这种情况下 **IV** 属性可以出现也可以不出现。
    - **URI**：指定密钥路径。
      该密钥是一个 16 字节的数据。
      该键是必须参数，除非 **METHOD** 为`NONE`。
    - **IV**：该值是一个 128 位的十六进制数值。
      [AES-128](https://links.jianshu.com/go?to=https%3A%2F%2Ftools.ietf.org%2Fhtml%2Frfc8216%23ref-AES_128) 要求使用相同的 16字节 IV 值进行加密和解密。使用不同的 IV 值可以增强密码强度。
      如果属性列表出现 **IV**，则使用该值；如果未出现，则默认使用媒体片段序列号（即 **EXT-X-MEDIA-SEQUENCE**）作为其 **IV** 值，使用大端字节序，往左填充 0 直到序列号满足 16 字节（128 位）。
    - **KEYFORMAT**：由双引号包裹的字符串，标识密钥在密钥文件中的存储方式（密钥文件中的 [AES-128](https://links.jianshu.com/go?to=https%3A%2F%2Ftools.ietf.org%2Fhtml%2Frfc8216%23ref-AES_128) 密钥是以二进制方式存储的16个字节的密钥）。
      该属性为可选参数，其默认值为`"identity"`。
      使用该属性要求兼容版本号 **EXT-X-VERSION** 大于等于 5。
    - **KEYFORMATVERSIONS**：由一个或多个被`/`分割的正整型数值构成的带引号的字符串（比如：`"1"`，`"1/2"`，`"1/2/5"`）。
      如果有一个或多特定的 **KEYFORMT** 版本被定义了，则可使用该属性指示具体版本进行编译。
      该属性为可选参数，其默认值为`"1"`。
      使用该属性要求兼容版本号 **EXT-X-VERSION** 大于等于 5。

  - **[EXT-X-MAP](https://links.jianshu.com/go?to=https%3A%2F%2Ftools.ietf.org%2Fhtml%2Frfc8216%23page-17)**：该标签指明了获取媒体初始化块（Meida Initialization Section）的方法。
    该标签对其后所有媒体片段生效，直至遇到另一个 **EXT-X-MAP** 标签。
    其格式为：

    

    ```m3u8
    #EXT-X-MAP:<attribute-list>
    ```

    其属性列表取值范围如下：

    - **URI**：由引号包裹的字符串，指定了包含媒体初始化块的资源的路径。该属性为必选参数。
    - **BYTERANGE**：由引号包裹的字符串，指定了媒体初始化块在 **URI** 指定的资源的位置（片段）。
      该属性指定的范围应当只包含媒体初始化块。
      该属性为可选参数，如果未指定，则表示 **URI** 指定的资源就是全部的媒体初始化块。

  - **[EXT-X-PROGRAM-DATE-TIME](https://links.jianshu.com/go?to=https%3A%2F%2Ftools.ietf.org%2Fhtml%2Frfc8216%23page-18)**：该标签使用一个绝对日期/时间表明第一个样本片段的取样时间。
    其格式为：

    

    ```m3u8
    #EXT-X-PROGRAM-DATE-TIME:<date-time-msec>
    ```

    其中，`date-time-msec`是一个 ISO/IEC 8601:2004 规定的日期格式，形如：YYYY-MM-DDThh:mm:ss.SSSZ。

  - **EXT-X-DATERANGE**：该标签定义了一系列由属性/值对组成的日期范围。
    其格式为：

    

    ```m3u8
    #EXT-X-DATERANGE:<attribute-list>
    ```

    其属性列表取值如下：

    - **ID**：双引号包裹的唯一指明日期范围的标识。
      该属性为必选参数。
    - **CLASS**：双引号包裹的由客户定义的一系列属性与与之对应的语意值。
      所有拥有同一 **CLASS** 属性的日期范围必须遵守对应的语意。
      该属性为可选参数。
    - **START-DATE**：双引号包裹的日期范围起始值。
      该属性为必选参数。
    - **END-DATE**：双引号包裹的日期范围结束值。
      该属性值必须大于或等于 **START-DATE**。
      该属性为可选参数。
    - **DURATION**：日期范围的持续时间是一个十进制浮点型数值类型（单位：秒）。
      该属性值不能为负数。
      当表达立即时间时，将该属性值设为 0 即可。
      该属性为可选参数。
    - **PLANNED-DURATION**：该属性为日期范围的期望持续时长。
      其值为一个十进制浮点数值类型（单位：秒）。
      该属性值不能为负数。
      在预先无法得知真实持续时长的情况下，可使用该属性作为日期范围的期望预估时长。
      该属性为可选参数。

  - **X-**：`X-`前缀是预留给客户端自定义属性的命名空间。
    客户端自定义属性名时，应当使用反向 DNS（reverse-DNS）语法来避免冲突。
    自定义属性值必须是使用双引号包裹的字符串，或者是十六进制序列，或者是十进制浮点数，比如：`X-COM-EXAMPLE-AD-ID="XYZ123"`。
    该属性为可选参数。

  - **SCTE35-CMD, SCTE35-OUT, SCTE35-IN**：用于携带 SCET-35 数据。
    该属性为可选参数。

  - **END-ON-NEXT**：该属性值为一个可枚举字符串，其值必须为`YES`。
    该属性表明达到该范围末尾，也即等于后续范围的起始位置 **START-DATE**。后续范围是指具有相同 **CLASS** 的，在该标签 **START-DATE** 之后的具有最早 **START-DATE** 值的日期范围。
    该属性时可选参数。

- **[媒体播放列表类型标签](https://links.jianshu.com/go?to=https%3A%2F%2Ftools.ietf.org%2Fhtml%2Frfc8216%23page-22)**：媒体播放列表标签为 m3u8 文件的全局参数信息。
  这些标签只能在 m3u8 文件中至多出现一次。
  媒体播放列表（Media Playlist）标签不能出现在主播放列表（Master Playlist）中。
  媒体播放列表具体标签如下所示：

  - **[EXT-X-TARGETDURATION](https://links.jianshu.com/go?to=https%3A%2F%2Ftools.ietf.org%2Fhtml%2Frfc8216%23page-22)**：表示每个视频分段最大的时长（单位秒）。
    该标签为必选标签。
    其格式为：

    

    ```m3u8
    #EXT-X-TARGETDURATION:<s>
    ```

    其中：参数`s`表示目标时长（单位：秒）。

  - **[EXT-X-MEDIA-SEQUENCE](https://links.jianshu.com/go?to=https%3A%2F%2Ftools.ietf.org%2Fhtml%2Frfc8216%23page-22)**：表示播放列表第一个 URL 片段文件的序列号。
    每个媒体片段 URL 都拥有一个唯一的整型序列号。
    每个媒体片段序列号按出现顺序依次加 1。
    如果该标签未指定，则默认序列号从 0 开始。
    媒体片段序列号与片段文件名无关。
    其格式为：

    

    ```m3u8
    #EXT-X-MEDIA-SEQUENCE:<number>
    ```

    其中：参数`number`即为切片序列号。

  - **[EXT-X-DISCONTINUITY-SEQUENCE](https://links.jianshu.com/go?to=https%3A%2F%2Ftools.ietf.org%2Fhtml%2Frfc8216%23page-23)**：该标签使能同步相同流的不同 Rendition 和 具备 **EXT-X-DISCONTINUITY** 标签的不同备份流。
    其格式为：

    

    ```m3u8
    #EXT-X-DISCONTINUITY-SEQUENCE:<number>
    ```

    其中：参数`number`为一个十进制整型数值。
    如果播放列表未设置 **EXT-X-DISCONTINUITY-SEQUENCE** 标签，那么对于第一个切片的中断序列号应当为 0。

  - **[EXT-X-ENDLIST](https://links.jianshu.com/go?to=https%3A%2F%2Ftools.ietf.org%2Fhtml%2Frfc8216%23page-23)**：表明 m3u8 文件的结束。
    该标签可出现在 m3u8 文件任意位置，一般是结尾。
    其格式为：

    

    ```m3u8
    #EXT-X-ENDLIST
    ```

  - **[EXT-X-PLAYLIST-TYPE](https://links.jianshu.com/go?to=https%3A%2F%2Ftools.ietf.org%2Fhtml%2Frfc8216%23page-24)**：表明流媒体类型。全局生效。
    该标签为可选标签。
    其格式为：

    

    ```m3u8
    #EXT-X-PLAYLIST-TYPE:<type-enum>
    ```

    其中：`type-enum`可选值如下：

    - **VOD**：即 Video on Demand，表示该视屏流为点播源，因此服务器不能更改该 m3u8 文件；
    - **EVENT**：表示该视频流为直播源，因此服务器不能更改或删除该文件任意部分内容（但是可以在文件末尾添加新内容）。
      注：**VOD** 文件通常带有 **EXT-X-ENDLIST** 标签，因为其为点播源，不会改变；而 **EVEVT** 文件初始化时一般不会有 **EXT-X-ENDLIST** 标签，暗示有新的文件会添加到播放列表末尾，因此也需要客户端定时获取该 m3u8 文件，以获取新的媒体片段资源，直到访问到 **EXT-X-ENDLIST** 标签才停止）。

  - **[EXT-X-I-FRAMES-ONLY](https://links.jianshu.com/go?to=https%3A%2F%2Ftools.ietf.org%2Fhtml%2Frfc8216%23page-24)**：该标签表示每个媒体片段都是一个 **I-frame**。**I-frames** 帧视屏编码不依赖于其他帧数，因此可以通过 **I-frame** 进行快速播放，急速翻转等操作。
    该标签全局生效。
    其格式为：

    

    ```m3u8
    #EXT-X-I-FRAMES-ONLY
    ```

    如果播放列表设置了 **EXT-X-I-FRAMES-ONLY**，那么切片的时长（**EXTINF** 标签的值）即为当前切片 **I-frame** 帧开始到下一个 **I-frame** 帧出现的时长。
    媒体资源如果包含 **I-frame** 切片，那么必须提供媒体初始化块或者通过 **EXT-X-MAP** 标签提供媒体初始化块的获取途径，这样客户端就能通过这些 **I-frame** 切片以任意顺序进行加载和解码。
    如果 **I-frame** 切片设置了 **EXT-BYTERANGE**，那么就绝对不能提供媒体初始化块。
    使用 **EXT-X-I-FRAMES-ONLY** 要求的兼容版本号 **EXT-X-VERSION** 大于等于 4。

- **[主播放列表类型标签](https://links.jianshu.com/go?to=https%3A%2F%2Ftools.ietf.org%2Fhtml%2Frfc8216%23page-25)**：主播放列表（Master Playlist）定义了备份流，多语言翻译流和其他全局参数。
  主播放列表标签绝不能出现在媒体播放列表（Media Playlist）中。
  其具体标签如下：

  - **[EXT-X-MEDIA](https://links.jianshu.com/go?to=https%3A%2F%2Ftools.ietf.org%2Fhtml%2Frfc8216%23page-25)**：用于指定相同内容的可替换的多语言翻译播放媒体列表资源。
    比如，通过三个 **EXT-X-MEIDA** 标签，可以提供包含英文，法语和西班牙语版本的相同内容的音频资源，或者通过两个 **EXT-X-MEDIA** 提供两个不同拍摄角度的视屏资源。
    其格式为：

    

    ```m3u8
    #EXT-X-MEDIA:<attribute-list>
    ```

    其中，属性列表取值范围如下：

    - **TYPE**：该属性值为一个可枚举字符串。
      其值有如下四种：`AUDIO`，`VIDEO`，`SUBTITLES`，`CLOSED-CAPTIONS`。
      通常使用的都是`CLOSED-CAPTIONS`。
      该属性为必选参数。
    - **URI**：双引号包裹的媒体资源播放列表路径。
      如果 **TYPE** 属性值为 `CLOSED-CAPTIONS`，那么则不能提供 **URI**。
      该属性为可选参数。
    - **GROUP-ID**：双引号包裹的字符串，表示多语言翻译流所属组。
      该属性为必选参数。
    - **LANGUAGE**：双引号包裹的字符串，用于指定流主要使用的语言。
      该属性为可选参数。
    - **ASSOC-LANGUAGE**：双引号包裹的字符串，其内包含一个语言标签，用于提供多语言流的其中一种语言版本。
      该参数为可选参数。
    - **NAME**：双引号包裹的字符串，用于为翻译流提供可读的描述信息。
      如果设置了 **LANGUAGE** 属性，那么也应当设置 **NAME** 属性。
      该属性为必选参数。
    - **DEFAULT**：该属性值为一个可枚举字符串。
      可选值为`YES`和`NO`。
      该属性未指定时默认值为`NO`。
      如果该属性设为`YES`，那么客户端在缺乏其他可选信息时应当播放该翻译流。
      该属性为可选参数。
    - **AUTOSELECT**：该属性值为一个可枚举字符串。
      其有效值为`YES`或`NO`。
      未指定时，默认设为`NO`。
      如果该属性设置`YES`，那么客户端在用户没有显示进行设置时，可以选择播放该翻译流，因为其能配置当前播放环境，比如系统语言选择。
      如果设置了该属性，那么当 **DEFAULT** 设置`YES`时，该属性也必须设置为`YES`。
      该属性为可选参数。
    - **FORCED**：该属性值为一个可枚举字符串。
      其有效值为`YES`或`NO`。
      未指定时，默认设为`NO`。
      只有在设置了 **TYPE** 为 **SUBTITLES** 时，才可以设置该属性。
      当该属性设为`YES`时，则暗示该翻译流包含重要内容。当设置了该属性，客户端应当选择播放匹配当前播放环境最佳的翻译流。
      当该属性设为`NO`时，则表示该翻译流内容意图用于回复用户显示进行请求。
      该属性为可选参数。
    - **INSTREAM-ID**：由双引号包裹的字符串，用于指示切片的语言（Rendition）版本。
      当 **TYPE** 设为 **CLOSED-CAPTIONS** 时，必须设置该属性。
      其可选值为：`"CC1"`, `"CC2"`, `"CC3"`, `"CC4"` 和 `"SERVICEn"`（`n`的值为 1~63）。
      对于其他 **TYPE** 值，该属性绝不能进行设置。
    - **CHARACTERISTICS**：由双引号包裹的由一个或多个由逗号分隔的 UTI 构成的字符串。
      每个 UTI 表示一种翻译流的特征。
      该属性可包含私有 UTI。
      该属性为可选参数。
    - **CHANNELS**：由双引号包裹的有序，由反斜杠`/`分隔的参数列表组成的字符串。
      所有音频 **EXT-X-MEDIA** 标签应当都设置 **CHANNELS** 属性。
      如果主播放列表包含两个相同编码但是具有不同数目 channed 的翻译流，则必须设置 **CHANNELS** 属性；否则，**CHANNELS** 属性为可选参数。

  - **[EXT-X-STREAM-INF](https://links.jianshu.com/go?to=https%3A%2F%2Ftools.ietf.org%2Fhtml%2Frfc8216%23page-29)**：该属性指定了一个备份源。该属性值提供了该备份源的相关信息。
    其格式为：

    

    ```objectivec
    #EXT-X-STREAM-INF:<attribute-list>
    <URI>
    ```

    其中：

    - **URI** 指定的媒体播放列表携带了该标签指定的翻译备份源。
      **URI** 为必选参数。
    - **EXT-X-STREAM-INF** 标签的参数属性列表有如下选项：
      - **BANDWIDTH**：该属性为每秒传输的比特数，也即带宽。代表该备份流的巅峰速率。
        该属性为必选参数。
      - **AVERAGE-BANDWIDTH**：该属性为备份流的平均切片传输速率。
        该属性为可选参数。
      - **CODECS**：双引号包裹的包含由逗号分隔的格式列表组成的字符串。
        每个 **EXT-X-STREAM-INF** 标签都应当携带 **CODECS** 属性。
      - **RESOLUTION**：该属性描述备份流视屏源的最佳像素方案。
        该属性为可选参数，但对于包含视屏源的备份流建议增加该属性设置。
      - **FRAME-RATE**：该属性用一个十进制浮点型数值作为描述备份流所有视屏最大帧率。
        对于备份流中任意视屏源帧数超过每秒 30 帧的，应当增加该属性设置。
        该属性为可选参数，但对于包含视屏源的备份流建议增加该属性设置。
      - **HDCP-LEVEL**：该属性值为一个可枚举字符串。
        其有效值为`TYPE-0`或`NONE`。
        值为`TYPE-0`表示该备份流可能会播放失败，除非输出被高带宽数字内容保护（HDCP）。
        值为`NONE`表示流内容无需输出拷贝保护。
        使用不同程度的 HDCP 加密备份流应当使用不同的媒体加密密钥。
        该属性为可选参数。在缺乏 HDCP 可能存在播放失败的情况下，应当提供该属性。
      - **AUDIO**：属性值由双引号包裹，其值必须与定义在主播放列表某处的设置了 **TYPE** 属性值为 **AUDIO** 的 **EXT-X-MEDIA** 标签的 **GROUP-ID** 属性值相匹配。
        该属性为可选参数。
      - **VIDEO**：属性值由双引号包裹，其值必须与定义在主播放列表某处的设置了 **TYPE** 属性值为 **VIDEO** 的 **EXT-X-MEDIA** 标签的 **GROUP-ID** 属性值相匹配。
        该属性为可选参数。
      - **SUBTITLES**：属性值由双引号包裹，其值必须与定义在主播放列表某处的设置了 **TYPE** 属性值为 **SUBTITLES** 的 **EXT-X-MEDIA** 标签的 **GROUP-ID** 属性值相匹配。
        该属性为可选参数。
      - **CLOSED-CAPTIONS**：该属性值可以是一个双引号包裹的字符串或`NONE`。
        如果其值为一个字符串，则必须与定义在主播放列表某处的设置了 **TYPE** 属性值为 **CLOSED-CAPTIONS** 的 **EXT-X-MEDIA** 标签的 **GROUP-ID** 属性值相匹配。
        如果其值为`NONE`，则所有的 **ext-x-stream-inf** 标签必须同样将该属性设置`NONE`，表示主播放列表备份流均没有关闭的标题。对于某个备份流具备关闭标题，另一个备份流不具备关闭标题可能会触发播放中断。
        该属性为可选参数。

  - **[EXT-X-I-FRAME-STREAM-INF](https://links.jianshu.com/go?to=https%3A%2F%2Ftools.ietf.org%2Fhtml%2Frfc8216%23page-33)**：该标签表明媒体播放列表文件包含多种媒体资源的 **I-frame** 帧。
    其格式为：

    

    ```m3u8
    #EXT-X-I-FRAME-STREAM-INF:<attribute-list>
    ```

    该标签的属性列表包含了 **EXT-X-I-FRAME-STREAM-INF** 标签同样的属性列表选项，除了 **FRAME-RATE**，**AUDIO**，**SUBTITLES** 和 **CLOSED-CAPTIONS**。除此之外，其他的属性还有：

    - **URI**：该属性值由双引号包裹的字符串，指示了 **I-frame** 媒体播放列表文件的路径，该媒体播放列表文件必须包含 **EXT-X-I-FRAMES-ONLY** 标签。

  - **[EXT-X-SESSION-DATA](https://links.jianshu.com/go?to=https%3A%2F%2Ftools.ietf.org%2Fhtml%2Frfc8216%23page-34)**：该标签允许主播放列表携带任意 session 数据。
    该标签为可选参数。
    其格式为：

    

    ```m3u8
    #EXT-X-SESSION-DATA:<attribute-list>
    ```

    其中，其参数属性列表值如下可选项:

    - **DATA-ID**：由双引号包裹的字符串，代表一个特定的数据值。
      该属性应当使用反向 DNS 进行命名，如`"com.example.movie.title"`。然而，由于没有中央注册机构，所以可能出现冲突情况。
      该属性为必选参数。
    - **VALUE**：该属性值为一个双引号包裹的字符串，其包含 **DATA-ID** 指定的值。
      如果设置了 **LANGUAGE**，则 **VALUE** 应当包含一个用该语言书写的可读字符串。
    - **URI**：由双引号包裹的 URI 字符串。由该 URI 指示的资源必选使用 JSON 格式，否则，客户端可能会解析失败。
    - **LANGUAGE**：由双引号包裹的，包含一个语言标签的字符串。指示了 **VALUE** 所使用的语言。

- [EXT-X-SESSION-KEY](https://links.jianshu.com/go?to=https%3A%2F%2Ftools.ietf.org%2Fhtml%2Frfc8216%23page-35)

  ：该标签允许主播放列表（Master Playlist）指定媒体播放列表（Meida Playlist）的加密密钥。这使得客户端可以预先加载这些密钥，而无需从媒体播放列表中获取。

  该标签为可选参数。

  其格式为：

  

  ```m3u8
  #EXT-X-SESSION-KEY:<attribute-list>
  ```

  其属性列表与

   

  EXT-X-KEY

   

  相同，除了

   

  METHOD

   

  属性的值必须不为

  ```
  NONE
  ```

  。

- **[播放列表类型标签](https://links.jianshu.com/go?to=https%3A%2F%2Ftools.ietf.org%2Fhtml%2Frfc8216%23page-35)**：以下标签可同时设置于主播放列表（Master Playlist）和媒体播放列表（Media Playlist）中。
  但是对于在主播放列表中设置了的标签，不应当再次设置在主播放列表指向的媒体播放列表中。
  同时出现在两者播放列表的相同标签必须具备相同的值。这些标签在播放列表中不能出现多次（只能使用一次）。具体标签如下所示：

  - **[EXT-X-INDEPENDENT-SEGMENTS](https://links.jianshu.com/go?to=https%3A%2F%2Ftools.ietf.org%2Fhtml%2Frfc8216%23page-35)**：该标签表明对于一个媒体片段中的所有媒体样本均可独立进行解码，而无须依赖其他媒体片段信息。
    该标签对列表内所有媒体片段均有效。
    其格式为：

    

    ```m3u8
    #EXT-X-INDEPENDENT-SEGMENTS
    ```

    如果该标签出现在主播放列表中，则其对所有媒体播放列表的所有媒体片段都生效。

  - **[EXT-X-START](https://links.jianshu.com/go?to=https%3A%2F%2Ftools.ietf.org%2Fhtml%2Frfc8216%23page-36)**：该标签表示播放列表播放起始位置。
    默认情况下，客户端开启一个播放会话时，应当使用该标签指定的位置进行播放。
    该标签为可选标签。
    其格式为：

    

    ```m3u8
    #EXT-X-START:<attribute-list>
    ```

    其参数属性列表的取值范围如下：

    - **TIME-OFFSET**：该属性值为一个带符号十进制浮点数（单位：秒）。
      一个正数表示以播放列表起始位置开始的时间偏移量。
      一个负数表示播放列表上一个媒体片段最后位置往前的时间偏移量。
      该属性的绝对值应当不超过播放列表的时长。如果超过，则表示到达文件结尾（数值为正数），或者达到文件起始（数值为负数）。
      如果播放列表不包含 **EXT-X-ENDLIST** 标签，那么 **TIME-OFFSET** 属性值不应当在播放文件末尾三个切片时长之内。
    - **PRECISE**：该值为一个可枚举字符串。
      有效的取值为`YES` 或 `NO`。
      如果值为`YES`，客户端应当播放包含 **TIME-OFFSET** 的媒体片段，但不要渲染该块内优先于 **TIME-OFFSET** 的样本块。
      如果值为`NO`，客户端应当尝试渲染在媒体片段内的所有样本块。
      该属性为可选参数，未指定则认为`NO`。

到此，m3u8 相关的标签我们已经完全介绍完毕。

下面我们再简单介绍下资源文件的获取具体操作。

上文提到，m3u8 文件要么是媒体播放列表（Meida Playlist），要么是主播放列表（Master Playlist）。但无论是哪种列表，其有效内容均由两部分结构组成：

- 以 **#EXT** 开头的为标签信息，作为对媒体资源的进一步描述；
- 剩余的为资源信息，要么是片段资源（Media Playlist）路径，要么是 m3u8 资源（Master Playlist）路径；

我们先简单介绍下 m3u8 文件媒体片段的表示方法：

- m3u8 文件中，媒体片段可以采用全路径表示。如下所示：



```m3u8
#EXTINF:10.0,
http://example.com/movie1/fileSequenceA.ts
```

这样，获取资源片段的路径就是 m3u8 文件内指定的路径，即：`http://example.com/movie1/fileSequenceA.ts`

- m3u8 文件中，媒体片段还可以使用相对路径表示。如下所示：



```txt
#EXTINF:10.0,
fileSequenceA.ts
```

这表示片段文件的路径是相对于 m3u8 文件路径的，即假设当前 m3u8 的路径为：`https://127.0.0.1/hls/m3u8`，那么，片段文件 fileSequenceA.ts 的路径即为：`https://127.0.0.1/hls/fileSequenceA.ts`

尽管可以在 m3u8 文件中使用绝对路径指定媒体片段资源路径，但是更好的选择是使用相对路径。相对路径相较于绝对路径更轻便，同时是相对于 m3u8 文件的 URL。相比之下，绝对路径增加了 m3u8 文件内容（更多字符），增大了文件内容，同时也增大了网络传输量。

## 其余一些注意事项

- 有两种请求 m3u8 播放列表的方法：一是通过 m3u8 的 URI 进行请求，则该文件必须以 .m3u8 或 .m3u 结尾；
  二是通过 [HTTP](https://links.jianshu.com/go?to=https%3A%2F%2Fzh.wikipedia.org%2Fwiki%2FHTTP) 进行请求，则请求头`Content-Type`必须设置为 `application/vnd.apple.mpegurl`或者`audio/mpegurl`。
- 空行和注释行在解析时都忽略。
- 媒体播放列表（Media Playlist）的流资源总时长就是各切片资源的时长之和。
- 每个切片的码率（bit rate）就是切片的大小除以它对应的时长（**EXTINF** 指定的时长）。
- 一个标签的属性列表的同一个属性`AttributeName`只能出现一次。
- **EXT-X-TARGETDURATION** 指定的时长绝对不能进行更改。通常该值指定的时长为 10 秒。
- 对于指定了 **EXT-X-I-FRAMES-ONLY** 且 第一个媒体片段（或者第一个尾随 **EXT-X-DISCONTINUITY** 的片段）其资源没有立即携带媒体初始化块的切片，应当增加使用标签 **EXT-X-MAP** 指定媒体初始化块获取途径。
- 使用 **EXT-X-MAP** 标签内含标签 **EXT-X-I-FRAMES-ONLY** 要求的兼容版本号 **EXT-X-VERSION** 要大于等于 5；只使用 **EXT-X-MAP** 要求的兼容版本号要大于等于 6。
- 由标签 **EXT-X-MAP** 声明的媒体初始化块可使用 [AES-128](https://links.jianshu.com/go?to=https%3A%2F%2Ftools.ietf.org%2Fhtml%2Frfc8216%23ref-AES_128) 方法进行加密，此时，作用于 **EXT-X-MAP** 标签的 **EXT-X-KEY** 标签必须设置 **IV** 属性。
- 带有属性 **END-ON-NEXT=YES** 的标签 **EXT-X-DATERANGE** 必须携带 **CLASS** 属性，但不能携带 **DURATION** 和 **END-DATE** 属性。其余带有相同 **CLASS** 的标签 **EXT-X-DATERANGE** 不能指定重叠的日期范围。
- 日期范围如果未指明 **DURATION**，**END_DATE**,**END-ON-NEXT=YES** 属性时，则其时长（duration）未知，即使其设置了 **PLANNED-DURATION** 属性。
- 如果播放列表设置了 **EXT-X-DATERANGE** 标签，则必须同时设置 **EXT-X-PROGRAM-DATE-TIME** 标签。
- 如果播放列表设置了拥有相同 **ID** 属性值的两个 **EXT-X-DATERANGE** 标签，则对于相同的属性名，在这两个 **EXT-X-DATERANGE** 中对应的值必须一致。
- 如果 **EXT-X-DATERANGE** 同时设置了 **DURATION** 和 **END-DATE** 属性，则 **END-DATE** 属性值必须等于 **START-DATE** 属性值加上 **DURATION** 属性值。
- **EXT-X-MEDIA-SEQUENCE** 标签必须出现在播放列表第一个切片之前。
- **EXT-X-DISCONTINUITY-DEQUENCE** 标签必须出现在播放列表第一个切片之前。
- **EXT-X-DISCONTINUITY-DEQUENCE** 标签必须出现在任意 **EXT-X-DISCONTINUITY** 标签之前。
- m3u8 文件如果没有设置 **EXT-X-PLAYLIST-TYPE** 标签，那么播放列表可以随时进行更改。比如，可以更新或删除播放列表中的媒体片段。
- 每个 **EXT-X-I-FRAME-STREAM-INF** 标签必须包含一个 **BANDWIDTH** 和 **URI** 属性。
- 每个 **EXT-X-SESSION-DATA** 标签都必须包含一个 **VALUE** 或 **URI** 属性，但不能同时包含两者。
- 一个播放列表可以包含多个携带相同 **DATA-ID** 属性的 **EXT-X-SESSION-DATA** 标签。但是不能包含多个携带相同 **DATA-ID** 和相同 **LANGUAGE** 属性的 **EXT-X-SESSION-DATA** 标签。
- 如果设置了 **EXT-X-SESSION-KEY**，那么其 **METHOD**，**KEYFORMAT** 和 **KEYFORMATVERSIONS** 属性值必须与任意相同 **URI** 的 **EXT-X-KEY** 标签值相同。
- 如果多份备用流或者多语言流使用相同的加密密钥和格式，则应当设置 **EXT-X-SESSION-KEY** 标签。
- 主播放列表必须不能设置多个具有相同 **METHOD**，**URI**，**IV**，**KEYFORMAT** 和 **KEYFORMATVERSIONS** 属性值得 **EXT-X-SESSION-KEY** 标签。