### 5.1.3通用命令行参数

 预览窗口 
–preview, -p 预览窗口设置 <‘x,y,w,h’> 
   允许用户在屏幕上定义预览窗口的大小和位置。注意，这将在所有其它窗口/图像的上层显示。 
–fullscreen, -f 全屏预览模式 
   强制预览屏幕全屏显示。注意，这将会保留输入图像的长宽比例，所以可能会在图像的边缘出现填充条。 
–nopreview, -n 不显示预览窗口 
  完全禁用预览窗口。注意，尽管预览窗口被禁用，但摄像头仍然在进行处理，所以会继续消耗资源。 
–opacity, -op 设置预览窗口透明度 
  设置预览窗口的透明度。0 为完全透明，255 为完全不透明。 
 摄像头控制参数 
–sharpness, -sh 设置图像锐度（-100 – 100） 
   设置图像的锐度，默认为 0。 
–contrast, -co 设置图像对比度（-100 – 100） 
   设置图像的对比度，默认为 0。 
–brightness, -br 设置图像亮度（0 – 100） 
   设置图像的亮度，默认为 50。0 为最暗，100 为最亮。 
–saturation, -sa 设置图像饱和度（-100 – 100） 
  设置图像色彩饱和度。默认为 0。 
–ISO, -ISO 设置捕捉 ISO 
  为捕捉图像设置 ISO。范围为 100 到 800。 
–vstab, -vs 打开视频稳定 
  仅用于视频模式，用于开启视频稳定。 
–ev, -ev 设置曝光补偿 
  设置图像的曝光补偿。范围为 -10 到 10，默认为 0。 
–exposure, -ex 设置曝光模式 
  可能用到的参数为： 
  auto – 使用自动曝光模式 
  night – 夜间拍摄模式 
  nightpreview -夜间预览拍摄模式（暂且这么称呼） 
  backlight – 逆光拍摄模式 
  spotlight – 聚光灯拍摄模式 
  sports – 运动拍摄模式（高速快门等） 
  snow – 雪景优化拍摄模式 
  beach – 海滩优化拍摄模式 
  verylong – 长时间曝光拍摄模式 
  fixedfps – 帧约束拍摄模式 
  antishake – 防抖模式 
  fireworks – 烟火优化拍摄模式 
  注意，不是所有的设置都会在对摄像头进行微调时得到相应作用。 
–awb, -awb 设置自动白平衡 
  可能用到的参数为： 
  off – 关闭白平衡测算 
  auto – 自动模式（默认） 
  sun – 日光模式 
  cloud – 多云模式 
  shade – 阴影模式 
  tungsten – 钨灯模式 
  fluorescent – 荧光灯模式 
  incandescent – 白炽灯模式 
  flash – 闪光模式 
  horizon – 地平线模式 
–imxfx, -ifx 设置图像特效 
  设置应用于图像上的特效 
  可能用到的参数为： 
  none – 无特效（默认） 
  negative – 反色图像 
  solarise – 曝光过度图像 
  posterize – 色调图像 
  whiteboard – 白板特效 
  blackboard – 黑板特效 
  sketch – 素描风格特效 
  denoise – 降噪图像 
  emboss – 浮雕图像 
  oilpaint – 油画风格特效 
  hatch – 草图特效 
  gpen – 马克笔特效 
  pastel – 柔化风格特效 
  watercolour – 水彩风格特效 
  film – 胶片颗粒风格特效 
  blur – 模糊图像 
  saturation – 色彩饱和图像 
  colourswap – 暂未可用 
  washedout – 暂未可用 
  posterise – 暂未可用 
  colourpoint – 暂未可用 
  colourbalance – 暂未可用 
  cartoon – 暂未可用 
  –colfx, -cfx 设置色彩特效 
  指定图像 U 和 V 通道的参数（范围 0 到 255）。例如：–colfx 128:128 将得到一张单色图像。 
 –metering, -mm 设置测光模式 
  为预览和捕捉指定测光模式 
  可能用到的参数为： 
  average – 全画面平衡测光 
  spot – 点测光 
  backlit – 模拟背光图像 
  matrix – 阵列测光 
–rotation, -rot 设置图像旋转（0 – 359） 
对取景器和最终得到的图像进行旋转。可以接受 0 以上任何值，但由于硬件限制，只支持 0、90、180、270 度。 
  –hflip, -hf 设置水平翻转 
  水平翻转预览和保存的图像。 
  –vflip, -vf 设置垂直翻转 
  垂直翻转预览和保存的图像。 
  –roi, -roi 设置传感器感光区域 
允许指定用于预览和捕捉的源所使用的传感器区域。该功能中 x 和 y 参数指定了坐上角的坐标，以及定义了宽度和高度值，并且所有值都为标准化坐标（0.0 到 1.0）。那么，感光[区域设置](https://www.baidu.com/s?wd=区域设置&tn=24004469_oem_dg&rsv_dl=gh_pl_sl_csd)为横向和纵向都为一半，并且宽度和高度都为传感器的四分之一时，可以写为： 
-roi 0.5,0.5,0.25,0.25 
–shutter, -ss 设置快门速度 
设置快门的速度为指定的值（单位为微秒）。据当前的考证，目前未定义时，快门速度上限大约为 330000us（330ms 或 0.33s）。

### 5.1.4应用程序专有设置

 raspistill 
–width, -w 设置图像宽度 
–height, -h 设置图像高度 
–quality, -q 设置 JPEG 品质，品质为 100 时几乎等同于未压缩。75 相对是比较好的选择。 
–raw, -r 向 JPEG 元数据中添加 RAW 信息，该参数将从摄像头获取到的 RAW 信息插入到 JPEG 元数据中。 
–output, -o 输出文件名，指定输出的文件名。如果不指定，将不保存到文件。如果文件名为“-”，将输出发送至标准输出设备。 
–latest, -l 链接最后一帧到文件名，基于该名称做一个指向最后一帧的文件系统链接。 
–verbose, -v 在运行过程中输出详细信息，在程序运行过程中，输出调试/详细信息。 
–timeout, -t 获取图片前的时间，程序将执行指定的时长，然后进行获取操作（前提是 output 已指定）。如果未指定，将设置为 5 秒。 
–timelapse, -tl [间隔拍摄](https://www.baidu.com/s?wd=间隔拍摄&tn=24004469_oem_dg&rsv_dl=gh_pl_sl_csd)模式，指定多次拍摄之间所间隔的毫秒值。注意，您需要在文件名中加入 %04d 做为画面计数。 
-t 30000 -tl 2000 -o image%04d.jpg，将会在 30 秒的时间内，每两秒拍摄一次，并且将文件命名为：image1.jpg、image0002.jpg…image0015.jpg。注意 %04d 表示在文件名中数字部分加入前导零，使其成为 4 位数。例如，%08d 将生成 8 位数字。如果间隔时间设置为 0，程序将不间断（取决于系统负担及存储速度）进行拍摄。不过需要注意，每次捕捉前还是会有 30ms 的最小暂停时间，用于曝光计算操作。 
–thumb, -th 设置缩略图参数（x:y:quality），允许指定插入到 JPEG 文件中缩略图信息。如果不指定，将为默认的 64×48 质量为 35 的缩略图。如果设置为 –thumb none，那么将不会向文件中插入缩略图信息。文件的尺寸也会稍微变小。 
–demo, -d 运行演示模式，该参数将循环使用所有摄像头参数，并且不会捕捉。而且无论是否完成所有的循环，在超时周期到达时都会停止演示操作。循环之前的时间需要设置毫秒值。 
–encoding, -e 指定输出文件的编码，可用的参数为 jpg、bmp、gif、png。注意，未被硬件加速支持的图像格式（gif、png、bmp）在保存的时候要比 jpg 格式耗时更长。还需要注意，文件扩展名在编码时将被完全忽略。 
–exif, -x 在捕捉的内容中加入 EXIF 标签（格式为 ‘key=value’），允许在 JPEG 图像中插入特定的 EXIF 标签。您可以插入 32 条记录。这是非常实用的功能，比如插入 GPS 元数据。例如设置经度。 
–exif GPS.GPSLongitude=5/1,10/1,15/100，该命令将会设置经度为 5 度 10 分 15 秒。查看 EXIF 文档获得所有可用标签的详细信息。支持的标签如下： 
IFD0. 或 IFD1. 

```
$raspivid -o test.h264 -t 25000 -timed 2500,5000
```

-  

 

 

  将进行 25 秒的录制操作。录制操作包括若干个 2500 毫秒（2.5 秒）录制和 5000 毫秒（5秒）暂停的操作，并且重复时长超过 20 秒。所以该录制过程中实际只录制了 10 秒的内容。包括 4 段 2.5 秒的视频片断 = 被若干个 5 秒钟暂停操作分隔开的 10 秒钟视频。 
–keypress, -k 使用回车键在录制和暂停两种状态间进行切换，每次点击回车键将会暂停或重新开始录制进程。点击 X 键后点击回车键将停止录制并关闭程序。注意，超时设置值将影响录制结束时间，但仅在每次回车键点击后进行检查，所以如果系统正在等待按键操作，尽管超时设置已过期，录制进程退出前也会等待按键操作。 
–signal, -s 使用 SIGUSR1 信号在录制和暂停两种状态间进行切换，向 Raspivid 进程发送 USR1 信号来切换录制和暂停。该操作可以通过使用 kill 命令来实现。您可以使用“pgrep raspivid” 命令找到 raspivid 的进程 ID。 
kill -USR1 
【注意】超时设置值将影响录制结束时间，但仅在每次发送 SIGUSR1 信号后进行检查，所以如果系统正在等待信号，尽管超时设置已过期，录制进程退出前也会等待信号的发送操作。 
–initial, -i 定义启动时的初始状态。定义摄像头初始状态为暂停或立即开始录像。选项可以为“record”（录像）或“pause”（暂停）。注意，如果您设置的超时时长很短，而且初始状态设置为“暂停”，那么将不会录制任何输出的内容。 


–segment, -sg 将视频流分段存储到多个文件，与存储在单个文件中不同，该参数将视频分段存储在以毫秒为单位所指定长度的数个文件中。为了将生成的文件命名为不同的名称，您需要在文件名中合适的位置添加 %04d 或类似的参数来让文件名中显示计数值。例如： 
–segment 3000 -o video%04d.h264，将分割成每段长度 3000 毫秒（3 秒）并且命名为 video0001.h264，video0002.h264 等。每个段落都是可无缝连接的（段落之间不会丢帧），但每个片段的长度将取决于帧内周期值，原因是每个分割的段落都需要起始于 I-frame 处。因此，每个段落都会等于或大于指定的时间长度。 


–wrap, -wr 设置最大分段数，当输出分段视频时，该参数设置了最大分段数，并且达到最大值时，将返回到初始的第一个段落。该参数赋予了录制分段视频的功能，但是将覆盖之前生成的文件。所以，如果设置为4，那么上面的例子中所生成的文件名为 video0001.h264，video0002.h264，video0003.h264，video0004.h264。而且，一旦 video0004.h264 文件录制完毕后，计数将回到 1，并且 video0001.h264 将被覆盖。 
–start, -sn 设置初始段落数，当输出分段视频时，该参数为初始的段落数，它允许从指定的段落恢复之前的录制操作。默认值为 1。

### 5.1.5应用示例

 

 图像捕捉 
  默认情况下，传感器将以其支持的最高分辨率进行捕捉。可以在命令行中通过使用 -w 和 -h 参数进行更改。 
\# 两秒钟（时间单位为毫秒）延迟后拍摄一张照片，并保存为 image.jpg 
raspistill -t 2000 -o image.jpg 

 


\# 拍摄一张自定义大小的照片。 
raspistill -t 2000 -o image.jpg -w 640 -h 480 

 


\# 降低图像质量，减小文件尺寸 
raspistill -t 2000 -o image.jpg -q 5 

 


\# 强制使预览窗口出现在坐标为 100,100 的位置，并且尺寸为宽 300 和高 200 像素。 
raspistill -t 2000 -o image.jpg -p 100,100,300,200 

 


\# 禁用预览窗口 
raspistill -t 2000 -o image.jpg -n 

 


\# 将图像保存为 PNG 文件（无损压缩格式，但是要比 JPEG 速度慢）。注意，当选择图像编码时，文件扩展名将被忽略。 
raspistill -t 2000 -o image.png –e png 

 


\# 向 JPEG 文件中添加一些 EXIF 信息。该命令将会把作者名称标签设置为 Dreamcolor，GPS 海拔高度为 123.5米。 
raspistill -t 2000 -o image.jpg -x IFD0.Artist=Dreamcolor -x GPS.GPSAltitude=1235/10 
\# 设置浮雕风格图像特效 
raspistill -t 2000 -o image.jpg -ifx emboss 
\# 设置 YUV 图像的 U 和 V 通道为指定的值（128:128 为黑白图像） 
raspistill -t 2000 -o image.jpg -cfx 128:128 
\# 仅显示两秒钟预览图像，而不对图像进行保存。 
raspistill -t 2000 
\# 间隔获取图片，在 10 分钟（10 分钟 = 600000 毫秒）的时间里，每 10 秒获取一张，并且命名为 image_number_001_today.jpg，image_number_002_today.jpg… 的形式，并且最后一张照片将命名为 latest.jpg。 
raspistill -t 600000 -tl 10000 -o image_num_%03d_today.jpg -l latest.jpg 
\# 获取一张照片并发送至标准输出设备 
raspistill -t 2000 -o - 
\# 获取一张照片并保存为一个文件 
raspistill -t 2000 -o - > my_file.jpg 
\#摄像头一直工作，当按下回车键时获取一张照片。 
raspistill -t 0 -k -o my_pics%02d.jpg 
 视频捕捉 
图像尺寸和预览设置与图像捕捉相同。录制的视频默认尺寸为 1080p（1920×1080） 
\# 使用默认设置录制一段 5 秒钟的视频片段（1080p30） 
raspivid -t 5000 -o video.h264 

 


\# 使用指定码率（3.5Mbits/s）录制一段 5 秒钟的视频片段 
raspivid -t 5000 -o video.h264 -b 3500000 

 


\# 使用指定帧率（5fps）录制一段 5 秒钟的视频片段 
raspivid -t 5000 -o video.h264 -f 5 

 


\# 发送到标准输出设备一段 5 秒钟经过编码的摄像头流图像 
raspivid -t 5000 -o - 


\# 保存到文件一段 5 秒钟经过编码的摄像头流图像 
raspivid -t 5000 -o - > my_file.h264

### 6.1.6查看图片

 方式一 
安装可以通过终端打开截图的shotwell。

```
$sudo apt-get install shotwell
```

- 1

查看图片命令。

```
$ sudo shotwell image.jpg
```

- 1

 方式二 
安装可以通过终端打开截图的gpicview，这个应用树莓派系统出厂自带了。

```
$sudo apt-get install gpicview 
```

-  

查看图片命令。

```
$sudo gpicview image.jpg
```

-    

### 6.1.7截图

想在树莓派上面截图或截屏用截图工具scrot 通过命令行就能做到。 
1.安装 
在Raspbian上安装scrot： 
命令： sudo apt-get install scrot 
2.截屏 
截取整个屏幕：scrot （截取图片的默认名称通常会有日期时间和分辨率，比如：“2016-10-10-062821_1024x768_scrot.png”） 
指定截取图片的名字：scrot example.png （那么文件名就会叫“example” ，扩展名不要丢，另外改变扩展名也不能改变文件格式） 
  指定文件位置：scrot /home/pi/Desktop/example.png（截图文件“example.png”就会被保存在 “/home/pi/Desktop/” ，注意，只有路径没有文件名是不行的） 
截取部分图片：scrot -s 然后拖动要截图的区域（scrot -s /home/pi/Desktop/example.png 命名和指定路径） 
 其他命令参数： 
-h 显示更多帮助 
-v 获取当前版本 
-d x 添加X秒的延迟拍摄 
-c 添加一个倒计时延迟拍摄 
-s 允许用户用鼠标捕捉特定区域 
-u 捕捉当前活动窗口 
-q X 指定图像质量百分率X（默认75） 
-t X 创建一个百分比大小为X的缩略图 
-e 在截图后指定一个命令来运行

### 6.1.8视屏播放

 MP4Box 
raspivid 通常会将录制的视频保存为 .h264 格式的文件。而我们使用的很多播放器可能无法正常播放该格式的视频文件。这就需要我们将生成的 .h264 格式的文件封装到播放器能够识别的视频容器格式中（比如封装为 mp4 格式）。有很多视频处理软件可以达到这个目的，您也可以直接在 Raspberry Pi 上直接进行封装。这里介绍的是“gpac”中的“MP4Box”。安装和使用的方法如下：

```html
 
```

1. `$sudo apt-get update`
2. `$sudo apt-get install gpac`
3. `$sudo MP4Box -add filename.h264 filename.mp4`

-  

 Omxplayer 
 播放

```
$sudo omxplayer –o hdmi 文件名
```

-  

 播放控制 
Key Action 
　　加速 
　　减速 
j 　　上一条音轨 
k 　　下一条音轨 
i 　　上一节 
o 　　下一节 
n 　　上一条字幕轨 
m 　　下一条字幕轨 
s 　　显示/不显示字幕 
q 　　退出 
空格或p　　暂停/继续 
\- 　　减小音量 
\+ 　　增加音量 
左 　　后退30 
右 　　前进30 
上 　　后退600 
下 　　前进600

### 5.1.9 扩展阅读

 树莓派专用CSI摄像头插到树莓派的CSI口上并在在raspi-config中打开后就可以使用Raspistill命令直接使用，但如果在OpenCV中调用CSI摄像头会出现无数据的现象（cv2.VideoCapture（0）这时不会报错）。 
这是因为树莓派中的camera module是放在/boot/目录中以固件形式加载的，不是一个标准的V4L2的摄像头驱动，所以加载起来之后会找不到/dev/video0的设备节点。我们在/etc/modules里面添加一行bcm2835-v4l2（小写的L）就能解决问题。

```
$sudo vi /etc/modules
```

- 添加：bcm2835-v4l2 

![这里写图片描述](https://img-blog.csdn.net/20171120104021977?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvdTAxMzE2MjAzNQ==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)

 

## 6.2树莓派实现动作捕捉、抓拍并存储照片

### 6.2.1开通树莓派SSH、VNC服务、开通摄像头

将树莓派接上键盘、鼠标和显示屏。进入Raspbian系统，打开命令行终端，输入：

```
$ sudo raspi-config
```

- 1

 

![这里写图片描述](https://img-blog.csdn.net/20171120104110521?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvdTAxMzE2MjAzNQ==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)

 

图3


当然也可直接在树莓派上配置。 
远程登录，默认用户名：pi, 默认密码：raspberry

 

### 6.2.2 PC机远程操作树莓派

使用PC机远程通过命令行或VNC操作树莓派要比树莓派接上键盘鼠标，盯着小屏幕看方便很多。具体操作步骤如下： 
1）树莓派接入网络，在PC终端输入：(注：Windows下要用PuTTY软件作为命令行终端，Mac电脑可以直接输入)

```
$ ssh pi@树莓派的IP地址
```

- 1

输入远程连接密码。如果跳到： 
pi@raspberrypi:~ $ 
说明连接成功，你现在可以在pc机上用命令行操作树莓派了。 
2）在pc机上用VNC连接树莓派。关于SVN的使用请读者看前面的章节。

### 6.2.3安装动作捕捉脚本

将附件的脚本拷贝到树莓派的 /home/pi 目录下创建一个新目录用来保存抓拍的照片：

```
$ sudo mkdir picam  
```

-  

然后就可以执行脚本了：

```
$ sudo python picam.py  
```

-  

  这时，如果有任何物体在移动，树莓派的摄像头就会抓拍，并保存到/home/pi/picam文件夹，在pc机上，就可以远程用VNC查看这些照片。 
**【附件】picam.py的代码**

```html
 
```

1. `#!/usr/bin/python`
2.  
3. `# original script by brainflakes, improved by pageauc, peewee2 and Kesthal`
4. `# www.raspberrypi.org/phpBB3/viewtopic.php?f=43&t=45235`
5.  
6. `# You need to install PIL to run this script`
7. `# type "sudo apt-get install python-imaging-tk" in an terminal window to do this`
8.  
9. `import StringIO`
10. `import subprocess`
11. `import os`
12. `import time`
13. `from datetime import datetime`
14. `from PIL import Image`
15.  
16. `# Motion detection settings:`
17. `# Threshold - how much a pixel has to change by to be marked as "changed"`
18. `# Sensitivity - how many changed pixels before capturing an image, needs to be higher if noisy view`
19. `# ForceCapture - whether to force an image to be captured every forceCaptureTime seconds, values True or False`
20. `# filepath - location of folder to save photos`
21. `# filenamePrefix - string that prefixes the file name for easier identification of files.`
22. `# diskSpaceToReserve - Delete oldest images to avoid filling disk. How much byte to keep free on disk.`
23. `# cameraSettings - "" = no extra settings; "-hf" = Set horizontal flip of image; "-vf" = Set vertical flip; "-hf -vf" = both horizontal and vertical flip`
24. `threshold = 10`
25. `sensitivity = 20`
26. `forceCapture = True`
27. `forceCaptureTime = 60 * 60 # Once an hour`
28. `filepath = "/home/pi/picam"`
29. `filenamePrefix = "capture"`
30. `diskSpaceToReserve = 40 * 1024 * 1024 # Keep 40 mb free on disk`
31. `cameraSettings = ""`
32.  
33. `# settings of the photos to save`
34. `saveWidth = 1296`
35. `saveHeight = 972`
36. `saveQuality = 15 # Set jpeg quality (0 to 100)`
37.  
38. `# Test-Image settings`
39. `testWidth = 100`
40. `testHeight = 75`
41.  
42. `# this is the default setting, if the whole image should be scanned for changed pixel`
43. `testAreaCount = 1`
44. `testBorders = [ [[1,testWidth],[1,testHeight]] ] # [ [[start pixel on left side,end pixel on right side],[start pixel on top side,stop pixel on bottom side]] ]`
45. `# testBorders are NOT zero-based, the first pixel is 1 and the last pixel is testWith or testHeight`
46.  
47. `# with "testBorders", you can define areas, where the script should scan for changed pixel`
48. `# for example, if your picture looks like this:`
49. `#`
50. `# ....XXXX`
51. `# ........`
52. `# ........`
53. `#`
54. `# "." is a street or a house, "X" are trees which move arround like crazy when the wind is blowing`
55. `# because of the wind in the trees, there will be taken photos all the time. to prevent this, your setting might look like this:`
56.  
57. `# testAreaCount = 2`
58. `# testBorders = [ [[1,50],[1,75]], [[51,100],[26,75]] ] # area y=1 to 25 not scanned in x=51 to 100`
59.  
60. `# even more complex example`
61. `# testAreaCount = 4`
62. `# testBorders = [ [[1,39],[1,75]], [[40,67],[43,75]], [[68,85],[48,75]], [[86,100],[41,75]] ]`
63.  
64. `# in debug mode, a file debug.bmp is written to disk with marked changed pixel an with marked border of scan-area`
65. `# debug mode should only be turned on while testing the parameters above`
66. `debugMode = False # False or True`
67.  
68. `# Capture a small test image (for motion detection)`
69. `def captureTestImage(settings, width, height):`
70. `command = "raspistill %s -w %s -h %s -t 200 -e bmp -n -o -" % (settings, width, height)`
71. `imageData = StringIO.StringIO()`
72. `imageData.write(subprocess.check_output(command, shell=True))`
73. `imageData.seek(0)`
74. `im = Image.open(imageData)`
75. `buffer = im.load()`
76. `imageData.close()`
77. `return im, buffer`
78.  
79. `# Save a full size image to disk`
80. `def saveImage(settings, width, height, quality, diskSpaceToReserve):`
81. `keepDiskSpaceFree(diskSpaceToReserve)`
82. `time = datetime.now()`
83. `filename = filepath + "/" + filenamePrefix + "-%04d%02d%02d-%02d%02d%02d.jpg" % (time.year, time.month, time.day, time.hour, time.minute, time.second)`
84. `subprocess.call("raspistill %s -w %s -h %s -t 200 -e jpg -q %s -n -o %s" % (settings, width, height, quality, filename), shell=True)`
85. `print "Captured %s" % filename`
86.  
87. `# Keep free space above given level`
88. `def keepDiskSpaceFree(bytesToReserve):`
89. `if (getFreeSpace() < bytesToReserve):`
90. `for filename in sorted(os.listdir(filepath + "/")):`
91. `if filename.startswith(filenamePrefix) and filename.endswith(".jpg"):`
92. `os.remove(filepath + "/" + filename)`
93. `print "Deleted %s/%s to avoid filling disk" % (filepath,filename)`
94. `if (getFreeSpace() > bytesToReserve):`
95. `return`
96.  
97. `# Get available disk space`
98. `def getFreeSpace():`
99. `st = os.statvfs(filepath + "/")`
100. `du = st.f_bavail * st.f_frsize`
101. `return du`
102.  
103. `# Get first image`
104. `image1, buffer1 = captureTestImage(cameraSettings, testWidth, testHeight)`
105.  
106. `# Reset last capture time`
107. `lastCapture = time.time()`
108.  
109. `while (True):`
110.  
111. `# Get comparison image`
112. `image2, buffer2 = captureTestImage(cameraSettings, testWidth, testHeight)`
113.  
114. `# Count changed pixels`
115. `changedPixels = 0`
116. `takePicture = False`
117.  
118. `if (debugMode): # in debug mode, save a bitmap-file with marked changed pixels and with visible testarea-borders`
119. `debugimage = Image.new("RGB",(testWidth, testHeight))`
120. `debugim = debugimage.load()`
121.  
122. `for z in xrange(0, testAreaCount): # = xrange(0,1) with default-values = z will only have the value of 0 = only one scan-area = whole picture`
123. `for x in xrange(testBorders[z][0][0]-1, testBorders[z][0][1]): # = xrange(0,100) with default-values`
124. `for y in xrange(testBorders[z][1][0]-1, testBorders[z][1][1]): # = xrange(0,75) with default-values; testBorders are NOT zero-based, buffer1[x,y] are zero-based (0,0 is top left of image, testWidth-1,testHeight-1 is botton right)`
125. `if (debugMode):`
126. `debugim[x,y] = buffer2[x,y]`
127. `if ((x == testBorders[z][0][0]-1) or (x == testBorders[z][0][1]-1) or (y == testBorders[z][1][0]-1) or (y == testBorders[z][1][1]-1)):`
128. `# print "Border %s %s" % (x,y)`
129. `debugim[x,y] = (0, 0, 255) # in debug mode, mark all border pixel to blue`
130. `# Just check green channel as it's the highest quality channel`
131. `pixdiff = abs(buffer1[x,y][1] - buffer2[x,y][1])`
132. `if pixdiff > threshold:`
133. `changedPixels += 1`
134. `if (debugMode):`
135. `debugim[x,y] = (0, 255, 0) # in debug mode, mark all changed pixel to green`
136. `# Save an image if pixels changed`
137. `if (changedPixels > sensitivity):`
138. `takePicture = True # will shoot the photo later`
139. `if ((debugMode == False) and (changedPixels > sensitivity)):`
140. `break # break the y loop`
141. `if ((debugMode == False) and (changedPixels > sensitivity)):`
142. `break # break the x loop`
143. `if ((debugMode == False) and (changedPixels > sensitivity)):`
144. `break # break the z loop`
145.  
146. `if (debugMode):`
147. `debugimage.save(filepath + "/debug.bmp") # save debug image as bmp`
148. `print "debug.bmp saved, %s changed pixel" % changedPixels`
149. `# else:`
150. `# print "%s changed pixel" % changedPixels`
151.  
152. `# Check force capture`
153. `if forceCapture:`
154. `if time.time() - lastCapture > forceCaptureTime:`
155. `takePicture = True`
156.  
157. `if takePicture:`
158. `lastCapture = time.time()`
159. `saveImage(cameraSettings, saveWidth, saveHeight, saveQuality, diskSpaceToReserve)`
160.  
161. `# Swap comparison buffers`
162. `image1 = image2`
163. `buffer1 = buffer2`

-  

### 6.2.4设置脚本开机启动

在终端上输入：

```
$ sudo vi /etc/rc.local  
```

-  

就会出现一个文本编辑器， 
在文本内容的exit 0 上面添加一行：

```
$ python /home/pi/picam.py  
```

-  

然后保存更改。 
重启树莓派：

```
$ sudo reboot  
```

-  

  即可实现开机自动运行。之所以选择这个脚本是因为它简洁，有效，而且还能自动清除过期的图片。相比之下，motion这个软件就显得比较复杂。有兴趣的同学还可以修改脚本实现抓拍后自动上传到网盘，或发送邮件等功能。

## 5.3树莓派+motion 搭建摄像头监控系统

\1. 安装

```
$sudo apt install motion
```

-  

\2. 配置motion选项 
备份配置文件

```
$sudo cp /etc/motion/motion.conf /etc/motion/motion.conf.bak
```

-  

打开配置文档

```
$sudo vim /etc/motion/motion.conf
```

-  

更改文档中以下内容

```html
 
```

1. `daemon on #开启守护进程（选配）`
2. `target_dir /home/pi/motion-images #图片保存的路径`
3. `#videodevice /dev/video0 #摄像头设备（默认）可修改`
4. `stream_localhost off #允许通过网页查看摄像头`
5. `stream_auth_method 2 #开启密码认证`
6. `stream_authentication 用户名:密码 #网页查看摄像头的用户名和密码`

-  

创建一个目录来存储Motion拍下的照片

```
$mkdir ~/motion-images
```

-  

官方详细配置说明：http://lavrsen.dk/foswiki/bin/view/Motion/ConfigFileOptions 
3.开启motion

```html
 
```

1. `$ sudo service motion start`
2. `$ sudo motion`

-  

   用浏览器登陆树莓派的网址 192.168.8.105：8081 ，会弹出用户名和密码的对话框，输入用户名和密码后看到图像就成功了。需要登录两次。 

![这里写图片描述](https://img-blog.csdn.net/20171120111400601?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvdTAxMzE2MjAzNQ==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)

 

图4


\4. 设置为开机运行（选配）

 

```
$sudo vim /etc/rc.local
```

-  

在exit 0前添加 motion , 保存，就会开机自动运行了。 
\5. 部分详细配置选项的翻译 

表1

 

ffmpeg_duplicate_frames 调试模式，只看到变化的图像

| 选项                        | Range/Values Default                                         | 说明                                                         |
| --------------------------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| auto_brightness             | Values: on,off Default: off                                  | 让motion自动调节视频的的亮度，只适用于不带有自动亮度调节的摄像机 |
| brightness                  | Values: 0-255 Default: 0 (disabled)                          | 调整摄像机的亮度                                             |
| saturation                  | Values: 0 - 255 Default: 0 (disabled)                        | 调整摄像机的颜色饱和度                                       |
| hue                         | Values: 0 - 255 Default: 0 (disabled)                        | 调整摄像机的色调                                             |
| contrast                    | Values: 0-255 Default: 0 (disabled)                          | 调整摄像机的对比度                                           |
| daemon                      | Values: on,off Default: off                                  | 以守护进程在后台运行。这个选项只能放在motion.conf，不能放在 thread config file |
| emulate_motion              | Values: on, off Default: off                                 | 即使没有运动物体也要保存图像                                 |
| ffmpeg_output_movies        | Values: on, off Default: off                                 | 是否保存视频                                                 |
| ffmpeg_bps                  | Values: 0 - 9999999 Default: 400000                          | 视频比特率                                                   |
| ffmpeg_variable_bitrate     | Values: 0, 2 -31 Default: 0 (disabled)                       | 动态比特率，如果开启这个功能ffmpeg_bps将被忽略，0为关闭，2为最好质量，31为最差质量 |
| Values: on, off Default: on | 为了达到每秒的帧数要求，会复制一下帧填充空白时间，关掉这个功能后每个帧都紧接下一个帧，看起来像快进 |                                                              |
| ffmpeg_output_debug_movies  | Values: on, off Default: off                                 |                                                              |
| ffmpeg_video_codec          | Values:mpeg4, msmpeg4, swf, flv, ffv1, mov, ogg, mp4, mkv, hevc Default: mpeg4 | 视频格式                                                     |
| framerate                   | Values: 2 - 100 Default: 100 (no limit)                      | 帧速率，每秒多少帧                                           |
| frequency                   | Values: 0 - 999999 Default: 0 (Not set)                      | 频率协调 Hz                                                  |
| lightswitch                 | Values: 0 - 100 Default: 0 (disabled)                        | 忽略光照强度改变引起的变化                                   |
| locate_motion_mode          | Values: on, off, preview Default: off                        | 给运动物体用方框标出                                         |
| locate_motion_style         | Values: box, redbox, cross, redcross Default: box            | 标记风格                                                     |
| max_movie_time              | Values: 0 (infinite) - 2147483647 Default: 3600              | 最大视频时间                                                 |
| minimum_frame_time          | Values: 0 - 2147483647 Default: 0                            | 最小帧间隔，设置为0表示采用摄像头的帧率                      |
| minimum_motion_frames       | Values: 1 - 1000s Default: 1                                 | 捕捉持续至少指定时间的运动帧                                 |
| movie_filename              | Values: Max 4095 characters Default: %v-%Y%m%d%H%M%S         | 视频的文件名                                                 |
| ffmpeg_timelapse            | Values: 0-2147483647 Default: 0 (disabled)                   | 间隔时间，拍摄延时视频                                       |
| ffmpeg_timelapse_mode       | Values: hourly, daily, weekly-sunday, weekly-monday, monthly, manual Default: daily | 延时拍摄模式                                                 |
| timelapse_filename          | Values: Max 4095 characters Default: %v-%Y%m%d-timelapse     | 延时拍摄的文件名                                             |
| output_pictures             | Values: on,off,first,best,center Default: on                 | 是否保存图片和模式设置                                       |
| output_debug_pictures       | Values: on,off Default: off                                  | 图片调试模式，只输出运动物体                                 |
| picture_filename            | Values: Max 4095 characters Default: %v-%Y%m%d%H%M%S-%q      | 图片文件名                                                   |
| picture_type                | Values: jpeg,ppm Default: jpeg                               | 图片类型                                                     |
| post_capture                | Values: 0 - 2147483647 Default: 0 (disabled)                 | 运动在持续多少帧之后才被捕捉                                 |
| pre_capture                 | Values: 0 - 100s Default: 0 (disabled)                       | 输出图像包括捕捉到运动的前几秒                               |
| quality                     | Values: 1 - 100 Default: 75                                  | jpg图像的质量                                                |
| quiet                       | Values: on, off Default: off                                 | 安静模式，检测到运动不输出哔                                 |
| rotate                      | Values: 0, 90, 180, 270 Default: 0 (not rotated)             | 旋转图像角度                                                 |
| stream_auth_method          | Values: 0,1,2 Default: 0                                     | 网页监控身份认证方法：0-无，1-基本，2-MD5                    |
| stream_authentication       | Values: username:password Default: Not defined               | 网页监控用户名和密码                                         |
| stream_limit                | Values: 0 - 2147483647 Default: 0 (unlimited)                | 限制帧的数量                                                 |
| stream_localhost            | Values: on, off Default: on                                  | 是否只能本地访问网络摄像头                                   |
| stream_maxrate              | Values: 1 - 100 Default: 1                                   | 限制网络摄像头帧速率                                         |
| stream_port                 | Values: 0 - 65535 Default: 0 (disabled)                      | 网络摄像头端口                                               |
| stream_quality              | Values: 1 - 100 Default: 50                                  | 网络摄像头传输质量                                           |
| switchfilter                | Values: on, off Default: off                                 | 过滤器开关，过滤器用来区分真正的运动和噪声                   |
| target_dir                  | Values: Max 4095 characters Default: Not defined = current working directory | 视频和图片的保存路径                                         |
| videodevice                 | Values: Max 4095 characters Default: /dev/video0             | 摄像头设备名                                                 |
| height                      | Values: Device Dependent Default: 288                        | 图像高度，范围跟摄像机相关                                   |
| width                       | Values: Device Dependent Default: 352                        | 图像宽度，范围跟摄像机相关                                   |
| process_id_file             | Values: Max 4095 characters Default: Not defined             | 保存PID的文件，推荐/var/run/motion.pid                       |
| database_busy_timeout       | Values: 0 .. positive integer Default: 0                     | 数据库等待超时时间，毫秒                                     |