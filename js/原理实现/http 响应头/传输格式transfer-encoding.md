# [HTTP协议响应头之Transfer-Encoding：分块传输详解](https://www.cnblogs.com/javaminer/p/3381312.html)

Http Connection有两种连接方式：短连接和长连接；短连接即一次请求对应一次TCP连接的建立和销毁过程，而长连接是多个请求共用同一个连接这样可以节省大量连接建立时间提高通信效率。目前主流浏览器都会在请求头里面包含Connection:keep-alive字段，该字段的作用就是告诉HTTP服务器响应结束后不要关闭连接，浏览器会将建立的连接缓存起来，当在有限时效内有再次对相同服务器发送请求时则直接从缓存中取出连接进行通信。当然被缓存的连接如果空闲时间超过了设定值（如firefox为115s，IE为60s）则会关闭连接。

![img](https://images0.cnblogs.com/blog/572610/201310/22115634-a3037387e89249fc94892c435bd66ec2.png)

当使用短连接的时候Recipient可以通过服务器端对Connection的关闭来正确获得消息体的结束位置；但长连接的时候Recipient怎么正确得知相邻两次请求的响应内容的分界位置呢？主要是采用设置响应头Content-Length或者Transfer-Encoding:chunked的方法来解决这一问题。

Chunked transfer encoding是一种数据传输机制,将消息体分成若干块从Server传输到Recipient(接收者);目前采用chunked传输方式比较多，为什么要采用chunked下面会说；如果不采用chunked传输方式则必须设置Content-Length字段，以便使Recipient能够正确获知消息体的结束位置，而为什么采用chunked不用设置Content-Length字段呢？因为chunked传输方式特定的格式可以使Recipient正确获知消息体的结束。

Chunked传输即分块传输：将响应主体分成若干块，并在每一块前面加上该块数据的长度以及回车换行，这样Recipient（如浏览器）就可以根据这个长度值正确接收每一块数据，最后以一个0长度的分块作为消息体的结束标志。采用该传输方式Sender在开始传输响应内容到Recipient前不需要知道内容的长度。

 

Chunked消息体格式如下：

hex的分块长度+<CR>回车+<LF>换行

chunked data

结束块的分块长度为0

如要发送的内容(消息体)为：123456789那么消息体的格式为：

9<CR><LF>

123456789<CR><LF>

0<CR><LF>

采用分块传输方式的好处：

（1）由于在服务器发送数据到Recipient前不需要知道数据的字节长度，所以可以动态产生响应内容而不用先将所有数据进行缓存；由于当消息体结束的时候有明确的信号标识（0<CR><LF>），因此后面对同一HTTP服务器的请求可以复用本次连接。

（2）允许服务器在消息体后面发送额外的响应头字段，这个非常重要当一个字段的值要等到响应内容全部产生后才能确定的情况下，如响应内容的数字签名，如果不使用分块传输服务器为了计算响应内容的算数字签名则必须先缓存所有内容直到内容产生完成。（如果不采用Chunked分块传输则在消息体后面发送的响应头不能被Recipient正确获取）

（3）HTTP服务器有时使用compression(gzip或者deflate)方法优化传输即对被传输的字节进行压缩，chunked和gzip编码相互之间作用在HTTP编码的两个阶段；第一阶段响应内容字节流采用gzip进行压缩编码,压缩完成后产生的字节流采用chunked的方式进行传输编码，这意味着chunked和compression可以同时使用，只是作用于不同的阶段。