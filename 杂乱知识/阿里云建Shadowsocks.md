## 阿里云服务器搭建Shadowsocks Server及使用SwitchyOmega切换代理设置实战教程

**原创**

 2018-08-17 06:18:58

 25219 67 4

分类:

[云服务器](https://blog.sbot.io/?category=云服务器) [LINUX](https://blog.sbot.io/?category=Linux) [VPN](https://blog.sbot.io/?category=vpn)

标签:

[VPN](https://blog.sbot.io/?label=VPN) [OPENVPN](https://blog.sbot.io/?label=OpenVPN) [SHADOWSOCKS](https://blog.sbot.io/?label=shadowsocks) [代理](https://blog.sbot.io/?label=代理) [SOCKS5](https://blog.sbot.io/?label=socks5)

------

 **原创不易 ~ 转载请注明出处哦** 

**严正声明：本文旨在讲解云服务器下如何搭建`Shadowsocks VPN Server`，以技术交流为目的，请勿以任何方式转载或非法谋取利益！**

在去年写过一篇名为[`使用Amazon EC2及OpenVPN搭建属于自己的VPN服务器`](https://blog.sbot.io/articles/5/使用Amazon-EC2及OpenVPN搭建属于自己的VPN服务器)的教程，收到了非常多朋友的正面反馈。但是由于今年度`OpenVPN`搭建的服务器连接并不够稳定，有时会出现连接困难，于是我测试了一下`Shadowsocks`。

还是不多说，先放出几张图给大家看看效果：

![https://blog.sbot.io - youtube](https://sbot.oss-cn-shanghai.aliyuncs.com/blog/uploads/2018-08/QQKhtPouxRY6ORxBGoOiOvOX0FCouUw2uvPUhNYR.jpeg?x-oss-process=style/watermark)
![https://blog.sbot.io - Facebook](https://sbot.oss-cn-shanghai.aliyuncs.com/blog/uploads/2018-08/PX0KiRH0Ja21SGf3uorC7D8Zzt7FBXPRs7j89EYw.png?x-oss-process=style/watermark)
![https://blog.sbot.io - twitter](https://sbot.oss-cn-shanghai.aliyuncs.com/blog/uploads/2018-08/cJzyLykzRn3uMgtjnjuzISEkxfHgmPXMljvHKSjr.png?x-oss-process=style/watermark)
![https://blog.sbot.io - Google](https://sbot.oss-cn-shanghai.aliyuncs.com/blog/uploads/2018-08/VggkF1nwOOtfGGsTDcZS9zd9FNbVm2nzQoJwdYRi.png?x-oss-process=style/watermark)

我的服务器使用的是阿里云香港机房服务器，系统`Ubuntu 16.04 LTS`，实际测试连接速度很快，延迟很低，目前表现比我的`Lantern Pro`稳定和快速。如果你通过我的教程成功上网，可以留言给我个正面的反馈，或者你对教程步骤的建议等以供更多朋友参考！：）

好了，那么我们先来说一下需要准备的工具及环境：

> - 阿里云香港或国外地区云服务器一台，镜像选择`Ubuntu 16.04 LTS`（当然你选`CentOS`也没有问题，不过我会以`Ubuntu`为例进行讲解）。
> - `SSH`工具
>   `Windows`下可以使用阿里云后台远程连接或者使用`Git Bash`（下载地址 https://github.com/git-for-windows/git/releases/tag/v2.18.0.windows.1）
>   `macOS`可以打开终端（`Terminal`）进行操作
>   `Linux`用户直接在`Terminal`命令窗口里进行操作
> - `ShadowSocks`客户端（地址将在后文中以百度网盘的形式给出，如果在`Github`上可以下载，将直接给出`Github`链接）

如果你还没有云服务器并且打算购买，那么请在下面的地址领取代金券，然后参考我的另一篇教程：

> **[手把手教你购买、配置、远程连接属于自己的云服务器以及架设简单的个人网站](https://blog.sbot.io/articles/38/手把手教你购买-配置-远程连接自己的云服务器)**

> **[【阿里云通用代金券领取】](https://promotion.aliyun.com/ntms/yunparter/invite.html?userCode=piiegvp9)**

服务器不需要很高的配置，单核`0.5G`内存或者`1G`内存就够了（只跑`shadowsocks`的话`0.5G`足矣）。香港机房会比内地机房稍稍贵一点，不过总体一年大概也就几百块钱，并不贵。在阿里云官网，选择`云服务器ECS`点击购买进行参数配置就可以了，**唯一需要注意的就是机房选香港或者国外（已测试内地机房不可用，推荐使用香港服务器）**。

接下来我们列出需要做的几个步骤：

> 1. 卸载阿里云盾（安骑士）服务
> 2. 在服务器下载并安装`Shadowsocks`
> 3. 配置`Shadowsocks`（连接参数）并设置安全组规则
> 4. 创建系统服务让`Shadowsocks`自动启动并以`service`身份在后台持续运行
> 5. 下载客户端及设置连接信息
> 6. 使用`Chrome`下载`SwitchyOmega`并设置`Proxy`参数档案

**在开始前最后说一点：本文技术性将比配置`OpenVPN`更强，我会尽量详尽地描述每一步的步骤，但是个人推荐你必须具备一定的`Linux`知识及云服务器操作知识，如果你不知道如何`ssh`或者连接上你的云服务器，那么这个教程对你来说可能难度比较高。如果你完全按照我写的步骤进行操作，那么你应该也可以完成`shadowsocks`的配置。**

------

好了，那么我们开始。首先我们`ssh`进入我们的云服务器：

```
$ ssh root@my-server-public-address
```

注意请使用你的云服务器公共`ip`替换上面的`my-server-public-address`。

------

**1. 卸载阿里云盾（安骑士）服务**

由于阿里会检测服务器是否存在`ss`，如果保留`安骑士`，阿里云会给你发邮件警告。
如果你是首次购买服务器，请在购买时直接反选`安骑士`服务。

如果已经安装了安骑士，那么我们需要使用以下命令移除：

```
$ wget http://update.aegis.aliyun.com/download/uninstall.sh
$ chmod +x uninstall.sh
$ ./uninstall.sh
Stopping aegis                                                           [  OK  ]
umount: /usr/local/aegis/aegis_debug: mountpoint not found
Uninstalling aegis                                                       [  OK  ]

$ wget http://update.aegis.aliyun.com/download/quartz_uninstall.sh
$ chmod +x quartz_uninstall.sh
$ ./quartz_uninstall.sh
Stopping aegis                                                           [  OK  ]
Stopping quartz                                                          [  OK  ]
Uninstalling aegis_quartz                                                [  OK  ]

$ pkill aliyun-service
$ rm -rf /etc/init.d/agentwatch /usr/sbin/aliyun-service /usr/local/aegis*
$ rm uninstall.sh
$ rm quartz_uninstall.sh
```

------

**2. 在服务器下载并安装Shadowsocks**

首先我们访问`shadowsocks-libev`在`Github`上的官方地址：

> https://github.com/shadowsocks/shadowsocks-libev#linux

可以看到，上面有关于所支持系统的安装文档。

如果你的服务器系统为`Ubuntu 16.10`及以上，那么可以直接使用以下命令安装`Shadowsocks-libev`：

```
$ sudo apt update
$ sudo apt install shadowsocks-libev
```

由于目前阿里云服务器`Ubuntu`版本最高为`16.04`，所以我们需要添加一个`ppa`来安装：

```
$ sudo apt-get install software-properties-common -y
$ sudo add-apt-repository ppa:max-c-lv/shadowsocks-libev -y
$ sudo apt-get update
$ sudo apt install shadowsocks-libev
```

完成后，我们就安装好了`shadowsocks-libev`。

------

**3. 配置Shadowsocks（连接参数）**

`shadowsocks-libev`有以下几个命令可以使用：

```
ss-[local|redir|server|tunnel|manager]
```

那么我们在服务端会讲解`ss-server`以及`ss-manager`的使用。
前者用于配置单个端口连接，后者可以配置多个端口及用户连接。

那么我们先来看一下`ss-server`的设置。首先我们打开`/etc/shadowsocks-libev/config.json`这个文件（没有的话我们创建一个）：

```
$ vim /etc/shadowsocks-libev/config.json
```

在这个文件中，我们填入以下信息：

```json
{
    "server": "0.0.0.0",
    "server_port": 5678,
    "local_port":1080,
    "password": "MySecret",
    "timeout":60,
    "method":"chacha20-ietf-poly1305"
}
```

**这里有几个地方需要着重强调一下。**
首先`server`一定要填`0.0.0.0`，而不是填你的服务器公共`ip`。
`server_port`可以填我们想使用的端口号，这里我用了`5678`。
`method`指的是加密方式，推荐使用`chacha20-ietf-poly1305`或`aes-256-gcm`。

这样一来，我们对`ss-server`的配置就完成了。为了尽可能给大家减少混淆，`ss-manager`配置我会放在后文中进行说明。

现在我们来尝试运行一下：

```
$ ss-server -c /etc/shadowsocks-libev/config.json

 2018-08-20 10:08:40 INFO: initializing ciphers... chacha20-ietf-poly1305
 2018-08-20 10:08:40 INFO: tcp server listening at 0.0.0.0:5678
 2018-08-20 10:08:40 INFO: running from root user
```

如果看到这样的信息，说明运行成功。如果你发现`bind() error`等类似的错误提示信息，那么请检查你的配置文件。

接下来，我们需要修改服务器的安全组配置。在阿里云后台，我们在服务器的安全组配置中，新建以下几条规则：
![https://blog.sbot.io - aliyun-security-rules](https://sbot.oss-cn-shanghai.aliyuncs.com/blog/uploads/2018-08/yUbhwBNq62HHSZFbgSxlDSOGJo7StOojaUQ0lnol.jpeg?x-oss-process=style/watermark)

同理，我们需要创建一条`TCP`规则，端口号也填入`5678`。

------

**4. 创建系统服务让Shadowsocks自动启动并以service身份在后台持续运行**

现在我们安装完了`ss`，并且也配置好了`ss-server`，现在我们来看一下如何创建系统服务让`shadowsocks`服务器一直运行在后台。

当然最简单粗暴的方法可以用`screen`这个程序。

```
$ sudo apt-get install -y screen
```

安装完成后，我们运行`screen`：

```
$ screen

Screen version 4.03.01 (GNU) 28-Jun-15
[...]
Capabilities:
+copy +remote-detach +power-detach +multi-attach +multi-user +font +color-256 +utf8 +rxvt +builtin-telnet

                               [Press Space or Return to end.]
```

回车后，我们运行`ss-server`：

```
$ ss-server -c /etc/shadowsocks-libev/config.json
```

接下来，我们按下`ctrl + A`，然后按`D`键，这样`ss-server`就会在后台运行，哪怕我们退出服务器。
要想停止`ss-server`，我们可以先查看`screen`的`id`：

```
$ screen -ls
There is a screen on:
	18529.pts-0.iZj6c5pz734d3dibf225oiZ	(08/20/2018 10:11:13 AM)	(Detached)
1 Socket in /var/run/screen/S-root.
```

可以看到，有一个`sceen`正在运行，要回到该`screen`，我们可以使用以下命令：

```
$ screen -r 18529
```

注意，`18529`是上面我们看到的`screen`的`pid`。
回到`screen`后，我们`ctrl + C`停止`ss-server`即可。接着我们输`exit`退出。

好了，如果我们不想用`screen`呢，那么我们可以创建一个`systemd`服务来控制`ss-server`的启动和停止。

实际上，我们不需要自己创建这个系统服务，因为`shadowsocks-libev`已经帮我们创建好了，我们只需要使用`systemctl`命令就可以启动这个服务：

```
$ sudo systemctl enable shadowsocks-libev.service  
Synchronizing state of shadowsocks-libev.service with SysV init with /lib/systemd/systemd-sysv-install...  
Executing /lib/systemd/systemd-sysv-install enable shadowsocks-libev

$ sudo systemctl start shadowsocks-libev
```

运行上述命令后，我们查看一下服务是否运行成功：

```
$ sudo systemctl status shadowsocks-libev

● shadowsocks-libev.service - Shadowsocks-libev Default Server Service
   Loaded: loaded (/lib/systemd/system/shadowsocks-libev.service; enabled; vendor preset: enabled)
   Active: active (running) since Mon 2018-08-20 10:21:52 CST; 5s ago
     Docs: man:shadowsocks-libev(8)
 Main PID: 18586 (ss-server)
   CGroup: /system.slice/shadowsocks-libev.service
           └─18586 /usr/bin/ss-server -c /etc/shadowsocks-libev/config.json -u

Aug 20 10:21:52 iZj6c5pz734d3dibf225oiZ systemd[1]: Stopped Shadowsocks-libev Default Server Service.
Aug 20 10:21:52 iZj6c5pz734d3dibf225oiZ systemd[1]: Started Shadowsocks-libev Default Server Service.
Aug 20 10:21:52 iZj6c5pz734d3dibf225oiZ ss-server[18586]:  2018-08-20 10:21:52 INFO: UDP relay enabled
Aug 20 10:21:52 iZj6c5pz734d3dibf225oiZ ss-server[18586]:  2018-08-20 10:21:52 INFO: initializing ciphers... chacha20-ietf-poly1305
Aug 20 10:21:52 iZj6c5pz734d3dibf225oiZ ss-server[18586]:  2018-08-20 10:21:52 INFO: tcp server listening at 0.0.0.0:5678
Aug 20 10:21:52 iZj6c5pz734d3dibf225oiZ ss-server[18586]:  2018-08-20 10:21:52 INFO: udp server listening at 0.0.0.0:5678
```

可以看到，服务运行成功了。在`18586 /usr/bin/ss-server -c /etc/shadowsocks-libev/config.json -u`一行，我们看到`ss-server`默认将使用`/etc/shadowsocks-libev/config.json`这个配置文件，并且`-u`表示我们想要开启`UDP Relay`。

------

**5. 下载客户端及设置连接信息**

好了，我们的服务端配置在上一步就已经完成了，现在我们需要在本地下载客户端进行连接。

根据你的系统，我会给出不同的链接，连接配置都很相似，我主要讲解`Linux`系统下的配置，`Windows`及`macOS`下的注意事项我会列出来，其他系统都是一样适用的。

**`Windows`系统用户请前往以下`github`发布页面找到`.zip`后缀的文件进行下载：**

> https://github.com/shadowsocks/shadowsocks-windows/releases

![https://blog.sbot.io - shadowsocks_windows](https://sbot.oss-cn-shanghai.aliyuncs.com/blog/uploads/2018-08/zpQUis8PSin2r7XN1Edq4jpZkDo52Hj44Qck0iwW.jpeg?x-oss-process=style/watermark)

下载完成我们打开程序，并在服务器配置中，填入我们在配置服务器`config.json`时使用的信息。
![shadowsocks-windows-config.png](https://sbot.oss-cn-shanghai.aliyuncs.com/blog/uploads/2018-08/ijfOPfkmNmd7ImnfTp2op0rWX3nwaqzKKqsvM8th.png?x-oss-process=style/watermark)

完成之后点击OK。接下来我们退出程序，会发现在程序所在的文件夹下多出了一个名为`gui-config.json`的文件，我们用记事本打开它，找到其中一段`json`配置：

```json
{
  "proxy": {
    "useProxy": true,
    "proxyType": 0,
    "proxyServer": "127.0.0.1",
    "proxyPort": 1080,
    "proxyTimeout": 5
  }
}
```

注意到，这里`useProxy`的值为`true`, 我们需要将其改为`false`。完成后，保存这个文件。然后我们就可以按照步骤`5`下载安装`Proxy SwitchyOmega`了。

**有几个地方需要注意：**

> - 若程序在`C`盘，请以系统管理员身份运行`shadowsocks`以免发生权限错误。
> - 如果程序出现问题请尝试安装最新的`.NET Framework`：https://www.microsoft.com/net/download

------

**`Mac`用户请前往以下地址下载：**

> https://github.com/shadowsocks/ShadowsocksX-NG/releases

![https://blog.sbot.io - shadowsocks_mac](https://sbot.oss-cn-shanghai.aliyuncs.com/blog/uploads/2018-08/LB090pntVXbcCeNubJq4EOZAZyzfm3qkG4ZcZMGs.jpeg?x-oss-process=style/watermark)

下载完成解压得到`.app`后缀的程序文件，将其放入应用程序文件夹打开即可。注意打开后不会直接有`UI`界面弹出来，你需要看电脑右上角多出一个小飞机图标，点击进行服务器信息设置（具体设置请参考后文`Linux`配置步骤），然后点击`PAC`自动模式就可以上网了。

------

**`Android`用户请前往以下地址下载`apk`安装包：**

> https://github.com/shadowsocks/shadowsocks-android/releases

------

**`ios`用户注意了，你需要美区（或国外）`App Store`账户才能操作。已测试可用，有需要的请单独联系我。**

------

**`Linux`用户请前往以下地址查看版本要求：**

> https://github.com/shadowsocks/shadowsocks-qt5/wiki/Installation

可以看到，如果你的`Linux`版本为`64`位以上且比`Debian Wheezy`新，那么可以下载`AppImage`形式的客户端：

> https://github.com/shadowsocks/shadowsocks-qt5/releases

![https://blog.sbot.io - shadowsocks_linux](https://sbot.oss-cn-shanghai.aliyuncs.com/blog/uploads/2018-08/F8tvxTgbU9vvZOvS2dzHEbAviKl6J0jxFjE1H5hH.jpeg?x-oss-process=style/watermark)

下载完成后，我们需要将客户端的权限修改成可运行：

```
$ chmod a+x Shadowsocks-Qt5-x86_64.AppImage
```

然后我们输入以下命令运行客户端（其他系统用户只需要下载安装点击客户端即可运行）：

```
$ ./Shadowsocks-Qt5-x86_64.AppImage
```

![https://blog.sbot.io - shadowsocks_client_linux](https://sbot.oss-cn-shanghai.aliyuncs.com/blog/uploads/2018-08/enwTzPO5Tk0OlFytwv9WIahYWV6zq2tjWS4Hh3JL.jpeg?x-oss-process=style/watermark)

可以看到，界面非常的简单，我们在`Connection`菜单栏中，点击`add - manually`，然后会弹出一个要我们输入服务器信息的窗口：

![https://blog.sbot.io - shadowsocks_client_linux_profile.jpg](https://sbot.oss-cn-shanghai.aliyuncs.com/blog/uploads/2018-08/Go0AFiOSUhQH4A9ELTRZZ65hpWeJRYthtXdEyv33.jpeg?x-oss-process=style/watermark)

这里我们按照在服务器上`config.json`文件配置的内容填写，`Server Port`填入我们开放的端口号（这里为`5678`），`Password`填入我们的密码，但是注意在`Server Address`一栏填入我们服务器的公共`ip`。其他信息按照上面图片中的填写即可。

点击`OK`，然后在客户端中会显示出我们的连接信息。右键单击，选择`connect`，然后在`Status`及`Latency`中，查看是否连接成功。如果`Latency`中显示类似`30ms`这样的延迟信息，说明连接已经成功。

------

**6. 使用Chrome下载SwitchyOmega并设置Proxy参数档案**

手机端用户做完第四步就已经可以上网了，`Android`客户端点击小飞机后查看底下的连接状态。

而`PC`端用户会发现，这个时候打开浏览器，依然无法上网。这是由于我们设置了`SOCKS5`代理，而系统默认未使用代理协议。

那么解决办法很简单，以`Chrome`为例，我们需要安装一款可以快速切换`proxy`设置。

我们前往以下地址：

> https://github.com/FelisCatus/SwitchyOmega/releases

找到`SwitchyOmega_Chromium.crx`这个文件进行下载。完成后点击插件进行安装。

**注意：在`Windows`下，需要在`chrome`地址栏输入`chrome://extensions/`，在右上角将`Developer mode`（开发者模式）打开才能安装插件。**

完成后，在`chrome`插件中，找到`SwitchyOmega`的设置，在左下方点击`New profile...`新建一个名为`shadowsocks`的档案，右照下图中的设置填入`SOCKS5`代理设置：

![proxy_switchyomega.png](https://sbot.oss-cn-shanghai.aliyuncs.com/blog/uploads/2018-08/F6wiOq6VrmWNAr4cMB2C5fBcUacDYJbwRBZZ3yf1.png?x-oss-process=style/watermark)

完成后保存。以后我们在上网的时候，单击`Chrome`右上方`Proxy SwitchyOmega`的小圆按钮，点击`shadowsocks`这个`profile`即可。不使用的时候，我们点击`[Direct]`取消代理设置。

![proxy-switchyomega.png](https://sbot.oss-cn-shanghai.aliyuncs.com/blog/uploads/2018-08/fPvYbZLMXh2hxFlfpkyCdgQyBVSkv4cFkcKcLvUo.png?x-oss-process=style/watermark)

好了，这样一来我们就顺利完成了`shadowsocks-libev`的配置并且使用本地客户端进行了连接。