1，下面是一个播放视频的最简单样例 
（controls属性告诉浏览器要有基本播放控件）

 ![img](https://images2018.cnblogs.com/blog/1301686/201804/1301686-20180411223938674-1491136678.png)

 

<video src="hangge.mp4" controls></video>

**2****，通过****width****和****height****设置视频窗口大小**

<video src="hangge.mp4" controls width="400" height="300"></video>

**3****，预加载媒体文件** 
设置preload不同的属性值，可以告诉浏览器应该怎样加载一个媒体文件： 
（1）值为auto：让浏览器自动下载整个文件 
（2）值为none：让浏览器不必预先下载文件 
（3）值为metadata：让浏览器先获取视频文件开头的数据块，从而足以确定一些基本信息（比如视频的总时长，第一帧图像等）

<!-- 用户点击播放才开始下载 -->

<video src="hangge.mp4" controls preload="none"></video>

**4****，自动播放** 
（1）使用autoplay属性可以让浏览器加载完视频文件后立即播放。

<video src="hangge.mp4" controls autoplay></video>

（2）如果启用自动播放，可以将播放器设置为muted状态。这样自动播放时会静音，防止用户厌烦。用户需要的话可以点击播放器扬声器图标重新打开声音。

<video src="hangge.mp4" controls autoplay muted></video>

**5****，循环播放** 
使用loop属性让视频播放结束时，再从头开始播放。

<video src="hangge.mp4" controls loop></video>

**6****，设置替换视频的图片（封面图片）** 
通过poster属性可以设置，浏览器在下面三种情况下会使用这个图片： 
（1）视频第一帧未加载完毕 
（2）把preload属性设置为none 
（3）没有找到指定的视频文件

<video src="hangge.mp4" controls poster="hangge.png"></video>

**7****，浏览器兼容，如何让每一个浏览器都能顺利播放视频** 
现在大部分浏览器都能支持H.264格式的视频，但Opera浏览器却一直不支持。我们需要通过后备措施保证每个人都能看到视频，通常有下面几种方案： 
**（****1****）使用多种视频格式** 
<video>和<audio>元素有个内置的格式后备系统。我们不使用src属性，而是在其内部嵌套一组<source>元素，浏览器会选择播放第一个它所支持的文件。 
我们可以添加WebM格式的视频提供对Opera的支持。

<video controls>

  <source src="hangge.mp4" type="video/mp4">

  <source src="hangge.webm" type="video/webm">

</video>

**（****2****）添加****Flash****后备措施（推荐）** 
上面那个方法不推荐，应为Opera浏览器只占不到1%的份额。特意为它把视频都转码一边太费事。使用Flash作为备用播放方案还是很方便的，同时Flash还能兼容IE8这种连<video>元素都不支持的老浏览器。

这里使用[Flowplayer Flash](http://flash.flowplayer.org/)作为备用播放器（本地下载 ：[flowplayer-3.2.18.zip](http://www.hangge.com/blog_uploads/201510/2015100911210214653.zip)）

<video controls>

  <source src="hangge.mp4" type="video/mp4">

  <source src="hangge.webm" type="video/webm">

 

  <object id="flowplayer" width="400" height="300"

​    data="flowplayer-3.2.18.swf"

​    type="application/x-shockwave-flash">

​    <param name="movie" value="flowplayer-3.2.18.swf">

​    <param name="flashvars" value='config={"clip":"hangge.mp4"}'>

  </object>

</video>

**（****3****）也有人优先使用****Flash****，而****HTML5****作为后备措施。** 
这么做是因为Flash普及率比较高，而HTML5作为后备可以扩展iPad和iPhone用户

<object id="flowplayer" width="400" height="300"

  data="flowplayer-3.2.18.swf"

  type="application/x-shockwave-flash">

  <param name="movie" value="flowplayer-3.2.18.swf">

  <param name="flashvars" value='config={"clip":"hangge.mp4"}'>

    <video controls>

​    <source src="hangge.mp4" type="video/mp4">

​    <source src="hangge.webm" type="video/webm">

  </video>

</object>