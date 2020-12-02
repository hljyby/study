[TOC]

# 为什么配置文件后缀都有d

```js
 // 守护进程，也就是通常说的Daemon进程
 // 一般配置文件后面都加d 代表守护进程
```

# curl 是什么 各种配置

## 简介

curl 是常用的命令行工具，用来请求 Web 服务器。它的名字就是客户端（client）的 URL 工具的意思。

它的功能非常强大，命令行参数多达几十种。如果熟练的话，完全可以取代 Postman 这一类的图形界面工具。

![img](https://www.wangbase.com/blogimg/asset/201909/bg2019090501.jpg)

本文介绍它的主要命令行参数，作为日常的参考，方便查阅。内容主要翻译自[《curl cookbook》](https://catonmat.net/cookbooks/curl)。为了节约篇幅，下面的例子不包括运行时的输出，初学者可以先看我以前写的[《curl 初学者教程》](http://www.ruanyifeng.com/blog/2011/09/curl.html)。

不带有任何参数时，curl 就是发出 GET 请求。

> ```bash
> $ curl https://www.example.com
> ```

上面命令向`www.example.com`发出 GET 请求，服务器返回的内容会在命令行输出。

## **-A**

`-A`参数指定客户端的用户代理标头，即`User-Agent`。curl 的默认用户代理字符串是`curl/[version]`。

> ```bash
> $ curl -A 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36' https://google.com
> ```

上面命令将`User-Agent`改成 Chrome 浏览器。

> ```bash
> $ curl -A '' https://google.com
> ```

上面命令会移除`User-Agent`标头。

也可以通过`-H`参数直接指定标头，更改`User-Agent`。

> ```bash
> $ curl -H 'User-Agent: php/1.0' https://google.com
> ```

## **-b**

`-b`参数用来向服务器发送 Cookie。

> ```bash
> $ curl -b 'foo=bar' https://google.com
> ```

上面命令会生成一个标头`Cookie: foo=bar`，向服务器发送一个名为`foo`、值为`bar`的 Cookie。

> ```bash
> $ curl -b 'foo1=bar;foo2=bar2' https://google.com
> ```

上面命令发送两个 Cookie。

> ```bash
> $ curl -b cookies.txt https://www.google.com
> ```

上面命令读取本地文件`cookies.txt`，里面是服务器设置的 Cookie（参见`-c`参数），将其发送到服务器。

## **-c**

`-c`参数将服务器设置的 Cookie 写入一个文件。

> ```bash
> $ curl -c cookies.txt https://www.google.com
> ```

上面命令将服务器的 HTTP 回应所设置 Cookie 写入文本文件`cookies.txt`。

## **-d**

`-d`参数用于发送 POST 请求的数据体。

> ```bash
> $ curl -d'login=emma＆password=123'-X POST https://google.com/login
> # 或者
> $ curl -d 'login=emma' -d 'password=123' -X POST  https://google.com/login
> ```

使用`-d`参数以后，HTTP 请求会自动加上标头`Content-Type : application/x-www-form-urlencoded`。并且会自动将请求转为 POST 方法，因此可以省略`-X POST`。

`-d`参数可以读取本地文本文件的数据，向服务器发送。

> ```bash
> $ curl -d '@data.txt' https://google.com/login
> ```

上面命令读取`data.txt`文件的内容，作为数据体向服务器发送。

## **--data-urlencode**

`--data-urlencode`参数等同于`-d`，发送 POST 请求的数据体，区别在于会自动将发送的数据进行 URL 编码。

> ```bash
> $ curl --data-urlencode 'comment=hello world' https://google.com/login
> ```

上面代码中，发送的数据`hello world`之间有一个空格，需要进行 URL 编码。

## **-e**

`-e`参数用来设置 HTTP 的标头`Referer`，表示请求的来源。

> ```bash
> curl -e 'https://google.com?q=example' https://www.example.com
> ```

上面命令将`Referer`标头设为`https://google.com?q=example`。

`-H`参数可以通过直接添加标头`Referer`，达到同样效果。

> ```bash
> curl -H 'Referer: https://google.com?q=example' https://www.example.com
> ```

## **-F**

`-F`参数用来向服务器上传二进制文件。

> ```bash
> $ curl -F 'file=@photo.png' https://google.com/profile
> ```

上面命令会给 HTTP 请求加上标头`Content-Type: multipart/form-data`，然后将文件`photo.png`作为`file`字段上传。

`-F`参数可以指定 MIME 类型。

> ```bash
> $ curl -F 'file=@photo.png;type=image/png' https://google.com/profile
> ```

上面命令指定 MIME 类型为`image/png`，否则 curl 会把 MIME 类型设为`application/octet-stream`。

`-F`参数也可以指定文件名。

> ```bash
> $ curl -F 'file=@photo.png;filename=me.png' https://google.com/profile
> ```

上面命令中，原始文件名为`photo.png`，但是服务器接收到的文件名为`me.png`。

## **-G**

`-G`参数用来构造 URL 的查询字符串。

> ```bash
> $ curl -G -d 'q=kitties' -d 'count=20' https://google.com/search
> ```

上面命令会发出一个 GET 请求，实际请求的 URL 为`https://google.com/search?q=kitties&count=20`。如果省略`--G`，会发出一个 POST 请求。

如果数据需要 URL 编码，可以结合`--data--urlencode`参数。

> ```bash
> $ curl -G --data-urlencode 'comment=hello world' https://www.example.com
> ```

## **-H**

`-H`参数添加 HTTP 请求的标头。

> ```bash
> $ curl -H 'Accept-Language: en-US' https://google.com
> ```

上面命令添加 HTTP 标头`Accept-Language: en-US`。

> ```bash
> $ curl -H 'Accept-Language: en-US' -H 'Secret-Message: xyzzy' https://google.com
> ```

上面命令添加两个 HTTP 标头。

> ```bash
> $ curl -d '{"login": "emma", "pass": "123"}' -H 'Content-Type: application/json' https://google.com/login
> ```

上面命令添加 HTTP 请求的标头是`Content-Type: application/json`，然后用`-d`参数发送 JSON 数据。

## **-i**

`-i`参数打印出服务器回应的 HTTP 标头。

> ```bash
> $ curl -i https://www.example.com
> ```

上面命令收到服务器回应后，先输出服务器回应的标头，然后空一行，再输出网页的源码。

## **-I**

`-I`参数向服务器发出 HEAD 请求，然会将服务器返回的 HTTP 标头打印出来。

> ```bash
> $ curl -I https://www.example.com
> ```

上面命令输出服务器对 HEAD 请求的回应。

`--head`参数等同于`-I`。

> ```bash
> $ curl --head https://www.example.com
> ```

## **-k**

`-k`参数指定跳过 SSL 检测。

> ```bash
> $ curl -k https://www.example.com
> ```

上面命令不会检查服务器的 SSL 证书是否正确。

## **-L**

`-L`参数会让 HTTP 请求跟随服务器的重定向。curl 默认不跟随重定向。

> ```bash
> $ curl -L -d 'tweet=hi' https://api.twitter.com/tweet
> ```

## **--limit-rate**

`--limit-rate`用来限制 HTTP 请求和回应的带宽，模拟慢网速的环境。

> ```bash
> $ curl --limit-rate 200k https://google.com
> ```

上面命令将带宽限制在每秒 200K 字节。

## **-o**

`-o`参数将服务器的回应保存成文件，等同于`wget`命令。

> ```bash
> $ curl -o example.html https://www.example.com
> ```

上面命令将`www.example.com`保存成`example.html`。

## **-O**

`-O`参数将服务器回应保存成文件，并将 URL 的最后部分当作文件名。

> ```bash
> $ curl -O https://www.example.com/foo/bar.html
> ```

上面命令将服务器回应保存成文件，文件名为`bar.html`。

## **-s**

`-s`参数将不输出错误和进度信息。

> ```bash
> $ curl -s https://www.example.com
> ```

上面命令一旦发生错误，不会显示错误信息。不发生错误的话，会正常显示运行结果。

如果想让 curl 不产生任何输出，可以使用下面的命令。

> ```bash
> $ curl -s -o /dev/null https://google.com
> ```

## **-S**

`-S`参数指定只输出错误信息，通常与`-s`一起使用。

> ```bash
> $ curl -s -o /dev/null https://google.com
> ```

上面命令没有任何输出，除非发生错误。

## **-u**

`-u`参数用来设置服务器认证的用户名和密码。

> ```bash
> $ curl -u 'bob:12345' https://google.com/login
> ```

上面命令设置用户名为`bob`，密码为`12345`，然后将其转为 HTTP 标头`Authorization: Basic Ym9iOjEyMzQ1`。

curl 能够识别 URL 里面的用户名和密码。

> ```bash
> $ curl https://bob:12345@google.com/login
> ```

上面命令能够识别 URL 里面的用户名和密码，将其转为上个例子里面的 HTTP 标头。

> ```bash
> $ curl -u 'bob' https://google.com/login
> ```

上面命令只设置了用户名，执行后，curl 会提示用户输入密码。

## **-v**

`-v`参数输出通信的整个过程，用于调试。

> ```bash
> $ curl -v https://www.example.com
> ```

`--trace`参数也可以用于调试，还会输出原始的二进制数据。

> ```bash
> $ curl --trace - https://www.example.com
> ```

## **-x**

`-x`参数指定 HTTP 请求的代理。

> ```bash
> $ curl -x socks5://james:cats@myproxy.com:8080 https://www.example.com
> ```

上面命令指定 HTTP 请求通过`myproxy.com:8080`的 socks5 代理发出。

如果没有指定代理协议，默认为 HTTP。

> ```bash
> $ curl -x james:cats@myproxy.com:8080 https://www.example.com
> ```

上面命令中，请求的代理使用 HTTP 协议。

## **-X**

`-X`参数指定 HTTP 请求的方法。

> ```bash
> $ curl -X POST https://www.example.com
> ```

上面命令对`https://www.example.com`发出 POST 请求。

# 一、简单说明 init.d

　　/etc/init.d 是 /etc/rc.d/init.d 的软链接(soft link)。可以通过 ll 命令查看。

```
ls -ld /etc/init.d
lrwxrwxrwx. 1 root root 11 Aug 30 2015 /etc/init.d -> rc.d/init.d
```

　　都是用来放服务脚本的，当Linux启动时，会寻找这些目录中的服务脚本，并根据脚本的run level确定不同的启动级别。

　　在制作服务脚本的过程中，使用了Linux的两个版本，CentOS和Ubuntu，需要在两个版本中都可以开机启动服务。但Ubuntu没有 /etc/rc.d/init.d这个目录，所以，为了保持同一种服务在CentOS和Ubuntu使用的统一性，将服务脚本（注：服务脚本在两个不同版本中是不同的）都放在 /etc/init.d 目录下，最终达到的效果是相同的。

　　需要说明的是：在CentOS和Ubuntu两个版本中，除了服务脚本放置的目录是相同的，服务脚本的编写及服务配置都是不同的。比如CentOS使用Chkconfig进行配置，而Ubuntu使用sysv-rc-conf进行配置。

　　

　　2 系统启动过程

　　1）BIOS自检 ，BIOS的功能由两部分组成，分别是POST码和Runtime服务。POST阶段完成后它将从存储器中被清除，而Runtime服务会被一直保留，用于目标操作系统的启动。BIOS两个阶段所做的详细工作如下：

　　**步骤1：**上电自检POST(Power-on self test)，主要负责检测系统外围关键设备（如：CPU、内存、显卡、I/O、键盘鼠标等）是否正常。例如，最常见的是内存松动的情况，BIOS自检阶段会报错，系统就无法启动起来；

　　**步骤2：**步骤1成功后，便会执行一段小程序用来枚举本地设备并对其初始化。这一步主要是根据我们在BIOS中设置的系统启动顺序来搜索用于启动系统的驱动器，如硬盘、光盘、U盘、软盘和网络等。我们以硬盘启动为例，BIOS此时去读取硬盘驱动器的第一个扇区(MBR，512字节)，然后执行里面的代码。实际上这里BIOS并不关心启动设备第一个扇区中是什么内容，它只是负责读取该扇区内容、并执行。

　　至此，BIOS的任务就完成了，此后将系统启动的控制权移交到MBR部分的代码。

　　2）系统引导，通常情况下，诸如lilo、grub这些常见的引导程序都直接安装在MBR中。详细过程，请自行google

　　3）启动内核，它首先会去解析grub的配置文件/boot/grub/grub.conf，然后加载内核镜像到内存中，并将控制权转交给内核。而内核会立即初始化系统中各设备并做相关的配置工作，其中包括CPU、I/O、存储设备等。

　　关于Linux的设备驱动程序的加载，有一部分驱动程序直接被编译进内核镜像中，另一部分驱动程序则是以模块的形式放在initrd(ramdisk)中。

　　 Linux内核需要适应多种不同的硬件架构，但是将所有的硬件驱动编入内核又是不实际的，而且内核也不可能每新出一种硬件结构，就将该硬件的设备驱动写入内核。实际上Linux的内核镜像仅是包含了基本的硬件驱动，在系统安装过程中会检测系统硬件信息，根据安装信息和系统硬件信息将一部分设备驱动写入 initrd 。这样在以后启动系统时，一部分设备驱动就放在initrd中来加载。这里有必要给大家再多介绍一下initrd这个东东：

　　 initrd 的英文含义是 bootloader initialized RAM disk，就是由 boot loader 初始化的内存盘。在 linu2.6内核启动前，boot loader 会将存储介质中的 initrd 文件加载到内存，内核启动时会在访问真正的根文件系统前先访问该内存中的 initrd 文件系统。在 boot loader 配置了 initrd 的情况下，内核启动被分成了两个阶段，第一阶段先执行 initrd 文件系统中的init，完成加载驱动模块等任务，第二阶段才会执行真正的根文件系统中的 /sbin/init 进程。

　　通过以上分析，grub的stage2将initrd加载到内存里，让后将其中的内容释放到内容中，内核便去执行initrd中的init脚本，这时内核将控制权交给了init文件处理。我们简单浏览一下init脚本的内容，发现它也主要是加载各种存储介质相关的设备驱动程序。当所需的驱动程序加载完后，会创建一个根设备，然后将根文件系统rootfs以只读的方式挂载。这一步结束后，释放未使用的内存，转换到真正的根文件系统上面去，同时运行/sbin/init程序，执行系统的1号进程。此后系统的控制权就全权交给/sbin/init进程了。

 

　　初始化系统，接下来就是初始化系统的工作了，/sbin/init进程是系统其他所有进程的父进程，当它接管了系统的控制权先之后，它首先会去读取/etc/inittab文件来执行相应的脚本进行系统初始化，如设置键盘、字体，装载模块，设置网络等。主要包括以下工作：

　　（1）执行系统初始化脚本(/etc/rc.d/rc.sysinit)，对系统进行基本的配置，以读写方式挂载根文件系统及其它文件系统，到此系统算是基本运行起来了，后面需要进行运行级别的确定及相应服务的启动。

　　（2）执行/etc/rc.d/rc脚本。该文件定义了服务启动的顺序是先K后S，而具体的每个运行级别的服务状态是放在/etc/rc.d/rc*.d（*=0~6）目录下，所有的文件均是指向/etc/init.d下相应文件的符号链接。rc.sysinit通过分析/etc/inittab文件来确定系统的启动级别，然后才去执行/etc/rc.d/rc*.d下的文件。

/etc/init.d-> /etc/rc.d/init.d

/etc/rc ->/etc/rc.d/rc

/etc/rc*.d ->/etc/rc.d/rc*.d

/etc/rc.local-> /etc/rc.d/rc.local

/etc/rc.sysinit-> /etc/rc.d/rc.sysinit

　　我们以启动级别3为例来简要说明一下，/etc/rc.d/rc3.d目录，该目录下的内容全部都是以 S 或 K 开头的链接文件，都链接到"/etc/rc.d/init.d"目录下的各种shell脚本。S表示的是启动时需要start的服务内容，K表示关机时需要关闭的服务内容。/etc/rc.d/rc*.d中的系统服务会在系统后台启动，如果要对某个运行级别中的服务进行更具体的定制，通过chkconfig命令来操作，或者通过setup、ntsys、system-config-services来进行定制。如果我们需要自己增加启动的内容，可以在init.d目录中增加相关的shell脚本，然后在rc*.d目录中建立链接文件指向该shell脚本。这些shell脚本的启动或结束顺序是由S或K字母后面的数字决定，数字越小的脚本越先执行。例如，/etc/rc.d/rc3.d /S01sysstat就比/etc/rc.d/rc3.d /S99local先执行。

　　（3）执行用户自定义引导程序/etc/rc.d/rc.local。其实当执行/etc/rc.d/rc3.d/S99local时，它就是在执行/etc/rc.d/rc.local。S99local是指向rc.local的符号链接。就是一般来说，自定义的程序不需要执行上面所说的繁琐的建立shell增加链接文件的步骤，只需要将命令放在rc.local里面就可以了，这个shell脚本就是保留给用户自定义启动内容的。

　　（4）完成了系统所有的启动任务后，linux会启动终端或X-Window来等待用户登录。tty1,tty2,tty3...这表示在运行等级1，2，3，4的时候，都会执行"/sbin/mingetty"，而且执行了6个，所以linux会有6个纯文本终端，mingetty就是启动终端的命令。除了这6个之外还会执行"/etc/X11/prefdm-nodaemon"这个主要启动X-Window

**至此，系统就启动完毕了。**

**接下来就是执行/bin/login程序，进入登录状态**

 

**二、 init.d目录包含许多系统各种服务的启动和停止脚本。**

　　/etc/init.d里的shell脚本能够响应start，stop，restart，reload命令来管理某个具体的应用。比如经常看到的命令： `/etc/init.d/networking start` 这些脚本也可被其他trigger直接激活执行，这些trigger被软连接在/etc/rcN.d/中。这些原理似乎可以用来写daemon程序，让某些程序在开关机时运行。

# cpu架构

## 两种指令集

- CISC 复杂指令集计算机
- RISC 精简指令集计算机
  Arm与x86 基础概念

## 四大CPU体系

ARM/MIPS/PowerPC均是基于精简指令集机器处理器的架构；X86则是基于复杂指令集的架构，Atom是x86或者是x86指令集的精简版

### 1.ARM

ARM架构，过去称作进阶精简指令集机器（Advanced RISC Machine，更早称作：Acorn RISC Machine），是一个32位精简指令集（RISC）处理器架构，其广泛地使用在许多嵌入式系统设计。由于节能的特点，ARM处理器非常适用于行动通讯领域，符合其主要设计目标为低耗电的特性。

### 2.x86系列/Atom(安腾)

IA 是Intel Architecture(英特尔体系架构)的简称，有IA-32和IA-64，均属于X86体系结构。

x86或80x86是英代尔Intel首先开发制造的一种微处理器体系结构的泛称。x86架构是重要地可变指令长度的CISC（复杂指令集电脑，Complex Instruction Set Computer）。

Intel Atom（中文：凌动，开发代号：Silverthorne）是Intel的一个超低电压处理器系列。处理器采用45纳米工艺制造，集成4700万个晶体管。L2缓存为512KB，支持SSE3指令集，和VT虚拟化技术（部份型号）。

### 3.MIPS系列

MIPS是世界上很流行的一种RISC处理器。MIPS的意思是“无内部互锁流水级的微处理器”(Microprocessor without interlockedpipedstages)，其机制是尽量利用软件办法避免流水线中的数据相关问题。它最早是在80年代初期由斯坦福(Stanford)大学Hennessy教授领导的研究小组研制出来的。MIPS公司的R系列就是在此基础上开发的RISC工业产品的微处理器。这些系列产品为很多计算机公司采用构成各种工作站和计算机系统。

MIPS技术公司是美国著名的芯片设计公司，它采用精简指令系统计算结构(RISC)来设计芯片。和英特尔采用的复杂指令系统计算结构(CISC)相比，RISC具有设计更简单、设计周期更短等优点，并可以应用更多先进的技术，开发更快的下一代处理器。MIPS是出现最早的商业RISC架构芯片之一，新的架构集成了所有原来MIPS指令集，并增加了许多更强大的功能。MIPS自己只进行CPU的设计，之后把设计方案授权给客户，使得客户能够制造出高性能的CPU。

### 4.PowerPC系列

PowerPC 是一种精简指令集（RISC）架构的中央处理器（CPU），其基本的设计源自IBM（国际商用机器公司）的IBM PowerPC 601 微处理器POWER（Performance Optimized With Enhanced RISC；《IBM Connect 电子报》2007年8月号译为“增强RISC性能优化”）架构。二十世纪九十年代，IBM(国际商用机器公司)、Apple（苹果公司）和Motorola（摩托罗拉）公司开发PowerPC芯片成功，并制造出基于PowerPC的多处理器计算机。PowerPC架构的特点是可伸缩性好、方便灵活。

## x86与ARM区别（冯诺依曼和arm）

[original](https://www.cnblogs.com/crazyValen/archive/2016/04/13/5389316.html)
现代的CPU基本上归为冯洛伊曼结构（也成普林斯顿结构）和哈佛结构。冯洛伊曼结构就是我们所说的X86架构，而哈佛结构就是ARM架构。一个广泛用于桌面端（台式/笔记本/服务器/工作站等），一个雄踞移动领域，我们的手持设备（平板\手机用的大多就是他了）。
他们的如区别如下：
一、冯洛伊曼的体系核心是：数据和指令混在一起，统一编址。区分哪些是指令和哪些是数据大致上有以下方法：
　　1、用寄存器和指令周期来区分数据和指令。例如：CS段（codesegment代码段）和DS段（datasegment数据段），前者CPU是认为存放的都是指令，后者CPU认为存放的都是数据；
　　2、通过不同的时间段来区分指令和数据，在取指阶段取出的就是指令，执行阶段取出的就是数据。这个都很好理解吧。
二、哈佛架构的核心是：数据和指令是区分开的。独立编址，就算地址一样，数据也是不一样的。
![在这里插入图片描述](https://img-blog.csdnimg.cn/20200609152325691.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dhbnhpYW9kZXJlbg==,size_16,color_FFFFFF,t_70)
再来讨论下两个架构的效率区别
经过上面的描述，各位已经知道这两个架构的主要区别了。
CPU大致工作如下：取指令、指令译码和执行指令。
指令1至指令3均为存、取数指令，对冯诺伊曼结构处理器，由于取指令和存取数据要从同一个存储空间存取，经由同一总线传输，因而它们无法重叠执行，只有一个完成后再进行下一个。如下图所示：
![在这里插入图片描述](https://img-blog.csdnimg.cn/20200609152339449.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dhbnhpYW9kZXJlbg==,size_16,color_FFFFFF,t_70)

采用哈佛结构，由于取指令和存取数据分别经由不同的存储空间和不同的总线，使得各条指令可以重叠执行，这样，也就克服了数据流传输的瓶颈，提高了运算速度。 哈佛结构强调了总的系统速度以及通讯和处理器配置方面的灵活性。
下面是对上图的几个引申知识点：
时钟周期也称为振荡周期：CPU无非就是开关闭合电路组成，定义为时钟脉冲的倒数。是计算机中的最基本的、最小的时间单位。 在一个时钟周期内，CPU仅完成一个最基本的动作。时钟脉冲是计算机的基本工作脉冲，控制着计算机的工作节奏。时钟频率越高，工作速度就越快。
机器周期：常把一条指令的执行过程划分为若干个阶段，每一个阶段完成一项工作。每一项工作称为一个基本操作，完成一个基本操作所需要的时间称为机器周期。
指令周期：执行一条指令所需要的时间，一般由若干个机器周期组成。指令不同，所需的机器周期也不同。
关系：指令周期通常用若干个机器周期表示，而机器周期时间又包含有若干个时钟周期。