# 网络工程师的Python之路---Scapy基础篇

笔者在《[网络工程师的Python之路---初级篇](https://zhuanlan.zhihu.com/p/34932386)》中曾提到要写一篇关于Scapy的教程，当时还有热衷用Python玩爬虫的朋友把Scapy和Scrapy搞混了，这是两个风马牛不相及的东西，虽然它俩名字确实很像。相比爬虫工具Scrapy，Scapy更适合网络工程师学习和使用。

《Scapy篇》我将由浅入深讲解scapy的基础应用以及如何用scapy编写黑客工具，包括如何使用scapy执行SYN flooding攻击、ARP欺骗、DHCP饥饿攻击、DHCP rogue server攻击等等的脚本编写，本文将分为《scapy基础篇》和《scapy应用篇》

## **什么是Scapy?**

**根据scapy官方的定义：**

> Scapy is a Python program that enables the user to send, sniff and dissect and forge network packets. This capability allows construction of tools that can probe, scan or attack networks.
> In other words, Scapy is a powerful interactive packet manipulation program. It is able to forge or decode packets of a wide number of protocols, send them on the wire, capture them, match requests and replies, and much more. Scapy can easily handle most classical tasks like scanning, tracerouting, probing, unit tests, attacks or network discovery. It can replace hping, arpspoof, arp-sk, arping, p0f and even some parts of Nmap, tcpdump, and tshark).

大意就是：Scapy是一个强大的，用Python编写的交互式数据包处理程序，它能让用户发送、嗅探、解析，以及伪造网络报文，从而用来侦测、扫描和向网络发动攻击。Scapy可以轻松地处理扫描(scanning)、路由跟踪(tracerouting)、探测(probing)、单元测试(unit tests)、攻击(attacks)和发现网络(network discorvery)之类的传统任务。它可以代替`hping`,`arpspoof`,`arp-sk`,`arping`,`p0f` 甚至是部分的`Nmap`,`tcpdump`和`tshark` 的功能。

## **Scapy实验运行环境和拓扑：**

**本篇的实验运行环境以及网络实验拓扑和《**网络工程师的Python之路---[初级篇](https://zhuanlan.zhihu.com/p/34932386)**》完全一样，这里简单回顾一下：**

操作系统：Windows 8.1上跑CentOS 7(VMware虚拟机)

网络设备：GNS3运行的思科三层交换机

网络设备版本：思科IOS (vios_12-ADVENTERPRISEK9-M)

**Python版本：2.7.5 **

局域网IP地址段：192.168.2.0 /24

运行Scapy的客户端: 192.168.2.1

Layer3Switch-1: 192.168.2.11

Layer3Switch-2: 192.168.2.12

Layer3Switch-3: 192.168.2.13

Layer3Switch-4: 192.168.2.14

Layer3Switch-5: 192.168.2.15

**所有的交换机已经预配好了SSH，用户名: python 密码:123**

![img](..\images\v2-9e70a3358461218295d81e34803b5230_720w.jpg)

1. 安装Scapy

![img](..\images\v2-5169239750215b99abcc1ccd3df50dc8_720w.jpg)

2. 进入scapy, 如果你不是root账户，需要用sudo scapy。

![img](..\images\v2-71433680da7c51f2b9ad3bdcd0c9b90e_720w.jpg)

3. 进入scapy后，可以用ls()函数来查看scapy支持的网络协议, （由于输出内容太长，只截取部分以供参考）。

可以看到网工们耳熟能详的ARP, BOOTP, Dot1Q, DHCP, DNS, GRE, HSRP, ICMP, IP, NTP, RIP, SNMP, STP, PPPoE, TCP, TFTP, UDP等等统统都支持。

![img](..\images\v2-f2172b67c815d10e49075688a1c8211d_720w.jpg)



4. 除了ls()外，还可以用lsc()函数来查看scapy的指令集（函数）。比较常用的函数包括arpcachepoison（用于arp毒化攻击，也叫arp欺骗攻击），arping（用于构造一个ARP的who-has包） ，send(用于发3层报文)，sendp（用于发2层报文）, sniff（用于网络嗅探，类似Wireshark和tcpdump）, sr（发送+接收3层报文），srp（发送+接收2层报文）等等

![img](..\images\v2-59d33c736a4b024c6e0ffbee8377c9c8_720w.jpg)



5. 这里还可以用使用ls()的携带参数模式，比如ls(IP)来查看IP包的各种默认参数。

![img](..\images\v2-269028f6fda424a283c516da2c8880a6_720w.jpg)

是不是让你回想起了IP报文的格式图？

![img](..\images\v2-572ee5e1fd3dc34025e7ec0c5e551cda_720w.jpg)



## **实验1**

**实验目的：使用IP()函数构造一个目的地址为192.168.2.11（即拓扑中的交换机S1）的IP报文，然后用send()函数将该IP报文发送给S1，在S1上开启debug ip packet以验证是否收到该报文。**

a. 首先用IP()函数构造一个目的地址为192.168.2.11的IP报文，将它实例化给ip这个变量。

```text
ip = IP(dst='192.168.2.11')
```

![img](..\images\v2-a9449d3b6e181378a389798c1f3cc399_720w.jpg)

b. 用ls(ip)查看该IP报文的内容，可以发现src已经变为192.168.2.1（本机的IP），dst变为了192.168.2.11。 一个最基本的IP报文就构造好了。

```text
ls(ip)
```

![img](..\images\v2-9e81a685e9d1ec66537a9d64e73b0a2b_720w.jpg)

c. 构造好了IP报文(src=192.168.2.1, dst=192.168.2.11)后，我们就可以用send()这个函数来把它发送出去了，发送给谁呢？当然是192.168.2.11，也就是我们的S1。

为了验证S1确实接收到了我们发送的报文，首先在S1上开启debug ip packet.

![img](..\images\v2-6c8c1220bb65fd30c4df04925759c129_720w.jpg)

然后在scapy上输入send(ip, iface='ens33')将该报文发出去，注意后面的iface参数用来指定端口，该参数可选。

```text
send(ip,iface='ens33')
```

![img](..\images\v2-f68afd1b59ac36a357ae33ff931bb50a_720w.jpg)

d. 再回到S1上，这时可以看到我们已经抓到了从192.168.2.1发来的IP报文，注意右下角的unknown protocol，这是因为该包的proto位为0, 不代表任何协议。

![img](..\images\v2-b586e888f41283f13a6602acfbc5390b_720w.jpg)

![img](..\images\v2-104deaba3cf24f72636b2ece55a1d17b_720w.jpg)

------

## **实验2**

**实验目的：除了send()外，scapy还有个sendp()函数，两者的区别是前者是发送三层报文，后者则是发送二层报文，实验2将演示如何用sendp()来构造二层报文。**


a. 用sendp()配合Ether()和arp()函数来构造一个ARP报文，命令如下

```text
sendp(Ether(dst='ff:ff:ff:ff:ff:ff') / ARP(hwsrc = '00:0c:29:72:b2:b5', psrc = '192.168.2.1', hwdst = 'ff:ff:ff:ff:ff:ff', pdst = '192.168.2.11') / 'abc', iface='ens33')
```

这里我们构造了一个源MAC地址为00:0c:29:72:b2:b5, 源IP地址为192.168.2.1, 目标MAC地址为ff:ff:ff:ff:ff:ff，目标IP地址为192.168.2.11，payload为abc的ARP报文。



b. 另开一个putty客户端，再次进入scapy，启用sniff()来抓包，并将抓包的内容实例化到data这个变量上。

```text
data = sniff()
```

![img](..\images\v2-0d9de4a73990acc4bf9279315a57296e_720w.jpg)

另外一边，在交换机S1，也就是192.168.2.11上开启debug arp，用来验证S1从scapy (192.168.2.1)收到了该ARP包。

![img](..\images\v2-364f91c83e0887db31c4ede774b14359_720w.jpg)



c. 回到之前的putty窗口，用sendp()将下面的ARP报文发出去

![img](..\images\v2-45f3868a5775c1c7fe0ce597b9013b6c_720w.jpg)



d. 回到正在抓包的putty，ctrl+c结束抓包，然后输入data.show()来查看抓到的包，这里可以看到我们刚才发的ARP包被抓到了，序列号为0007。

![img](..\images\v2-1325b78d2e3ad827a32383796af8c926_720w.jpg)

回到S1，这里可以看到S1收到了从192.168.2.1发来的ARP报文。

![img](..\images\v2-ca9e28811d96b49947f444aac9737572_720w.jpg)



e. 因为该ARP包的序列号为0007, 继续用data[7]和data[7].show()深挖该arp报文的内容

![img](..\images\v2-12681d6c460c0c97aec22e45810fb80a_720w.jpg)

可以看到该报文ARP部分的内容和ARP报文的结构完全一致

![img](..\images\v2-406d7469c3606736a55cff9953742954_720w.jpg)



**hardware type(HTPYE)为0x0001的时候，表示Ethernet**

**protocol type(PTPYE)为0x0800的时候，表示IPv4**

**hardware length (HLEN)为0x06的时候，表示MAC地址长度为6byte**

**protocol length(PLEN)为0x04的时候，表示IP地址长度为4byte**

**ARP包有request和response之分，request包的OPER(Opcode)位为0x0001 （也就是这里的who has）, response包的OPER位为0x0002。**

**最后的payload位(padding)即为我们自己定制的内容'abc'。**

------

## **实验3**

**实验目的：从实验1和实验2的例子可以看出：send()和sendp()函数只能发送报文，而不能接收返回的报文。如果要想查看返回的3层报文，需要用到sr()函数，实验3将演示如何使用sr()函数。**



a. 用sr()向S1发一个ICMP包，可以看到返回的结果是一个tuple（元组），该元组里的元素是两个列表，其中一个列表叫Results（响应），另一个叫Unanswered（未响应）。

```text
sr(IP(dst = '192.168.2.11') / ICMP())
```

![img](..\images\v2-43570445b820a6d6335d206898da7406_720w.jpg)

**这里可以看到192.168.2.11响应了这个ICMP包，所以在Results后面的ICMP:显示1。**



b. 如果向一个不存在的IP，比如192.168.2.2发ICMP包，那么这时会看到scapy在找不到该IP的MAC地址（因为目标IP 192.168.2.2和我们的主机192.168.2.1在同一个网段下，这里要触发ARP寻找目标IP对应的MAC地址）的时候，转用广播。当然广播也找不到目标IP，这里可以Ctrl+C强行终止。

```text
sr(IP(dst = '192.168.2.2') / ICMP())
```

![img](..\images\v2-157bff7fc5047f040cd7cf14c94ec2fc_720w.jpg)

**由于没有响应，所以你能看到Unanswered后面的ICMP:显示了1.**



c. 我们可以将sr()函数返回的元组里的两个元素分别赋值给两个变量，第一个变量叫ans，对应Results（响应）这个元素，第二个变量叫unans，对应Unanswered（未响应）这个元素。

```text
ans, unans = sr(IP(dst = '192.168.2.11') / ICMP())
```

![img](..\images\v2-e377ce1681d8b1107f7924d751b6caf6_720w.jpg)



d. 这里还可以进一步用show(), summary(), nsummary()等方法来查看ans的内容，这里可以看到192.168.2.1向192.168.2.11发送了echo-request的ICMP包，192.168.2.11向192.168.2.1回了一个echo-reply的ICMP包。



![img](..\images\v2-807276306b6e01a63a4abe43aa6a9461_720w.jpg)



e. 如果想要查看该ICMP包更多的信息，还可以用ans[0]（ans本身是个列表）来查看，因为这里我们只向192.168.2.11发送了一个echo-request包，所以用[0]来查看列表里的第一个元素。

```text
ans[0]
```

![img](..\images\v2-74859815a11b5bfb2f9dbb63aea684f9_720w.jpg)

可以看到ans[0]本身又是一个包含了两个元素的元组，我们可以继续用ans[0][0]和ans[0][1]查看这两个元素。

```text
ans[0][0]
ans[0][1]
```

![img](..\images\v2-28b57652a3593908569b38bf9cee8396_720w.jpg)



------

## **实验4**

**实验目的：实验3讲到了sr(),它是用来接收返回的3层报文。实验4将使用srp()来接收返回的2层报文。**

a. 用srp()配合Ether()和ARP()构造一个arp报文，二层目的地址为ff:ff:ff:ff:ff:ff，三层目的地址为192.168.2.0/24, 因为我们是向整个/24网络发送arp, 耗时会很长，所以这里用timeout = 5，表示将整个过程限制在5秒钟之内完成，最后的iface参数前面讲过就不解释了。

```text
ans, unans = srp(Ether(dst = "ff:ff:ff:ff:ff:ff") / ARP(pdst = "192.168.2.0/24"), timeout = 5, iface = "ens33")
```

![img](..\images\v2-9f17903879397020f15f6a7ffd52acad_720w.jpg)



b. 我们的实验环境里有5台交换机，S1到S5的管理IP都在192.168.2.0/24这个范围，从上图可以看到我们收到了5个answers，符合我们的实验环境，下面用ans.summary()来具体看看到底是哪5个IP响应了我们的'who has'类型的arp报文。

```text
ans.summary()
```

![img](..\images\v2-562e3e246ad1eeeb0217dc3f4ffd6d42_720w.jpg)

这里可以看到192.168.2.11 （S1）, 192.168.2.12（S2）, 192.168.2.13 （S3）， 192.168.2.14 （S4）， 192.168.2.15 （S5）响应了我们的'who has'类型的arp报文，并且能看到它们各自对应的MAC地址。



c. 用unans.summary()来查看那些没有给予我们'who has'类型arp报文回复的IP地址

```text
unans.summary()
```

![img](..\images\v2-a07fb188aac3eab5271409443ca19b3a_720w.jpg)

可以看到询问其他IP的'who has'类型arp报文没有人响应。

------

## **实验5**

**实验目的：使用tcp()函数构造四层报文，理解和应用RandShort()，RandNum()和Fuzz()函数。**

a. 实验开始前，首先在S1上启用HTTP服务，打开TCP 80端口，并开启debug ip tcp packet。

![img](..\images\v2-4d593609b69b69daa2e5a382027b42b1_720w.jpg)



b. 在scapy上使用ip()和tcp()函数来构造一个目的地IP为192.168.2.11（即S1），源端口为30，目的端口为80的TCP SYN报文。

```text
ans, unans = sr(IP(dst = "192.168.2.11") / TCP(sport = 30, dport = 80, flags = "S"))
```

![img](..\images\v2-182e4ef34fda2709a6460d7b88f1e014_720w.jpg)



c. TCP SYN报文发送后，回到S1上，可以看到S1已经收到了该报文，而且S1向scapy主机回复了一个ACK报文。

![img](..\images\v2-5f81f6ec32246148368bd37aa38bf8c3_720w.jpg)



d. 在scapy上输入ans[0]继续验证从主机发出的包，以及从S1收到的包。

```text
ans[0] 
```

![img](..\images\v2-1462984654aa03fbe78930512b70b7e9_720w.jpg)



e. TCP端口号除了手动指定外，还可以使用RandShort(), RandNum()和Fuzz()这几个函数来让scapy帮你自动生成一个随机的端口号，通常可以用作sport(源端口号)。

首先来看RandShort()，RandShort()会在1-65535的范围内随机生成一个TCP端口号，将上面的sport = 30 替换成 sport = RandShort()即可使用。

```text
ans, unans = sr(IP(dst = "192.168.2.11") / TCP(sport = RandShort(), dport = 80, flags = "S"))
```

![img](..\images\v2-5d7992051475ff584ade8ebd549b0143_720w.jpg)

**这里可以看到RandShort()替我们随机生成了13904这个TCP源端口号**



f. 如果你想指定scapy生成端口号的范围，可以使用RandNum()，比如你只想在1000-1500这个范围内生成端口号，可以使用RandNum(1000,1500)来指定，举例如下：

```text
ans, unans = sr(IP(dst = "192.168.2.11") / TCP(sport = RandNum(1000,1500), dport = 80, flags = "S"))
```

![img](..\images\v2-d47d833bccbe78435435c59d05e6d1ea_720w.jpg)

**这里RandNum()帮我们生成了1008这个源端口号**

**由于我们指定的范围是1000-1500，很有可能和一些知名的端口号重复，这个时候会出现sport显示的不是端口号，而是具体的网络协议名字的情况，比如这里重复上面的命令再次构造一个TCP包：**

![img](..\images\v2-cb7666777d0e370c7b4ef6a283185c47_720w.jpg)

**这时sport = blueberry_lm, 不再是具体的端口号**。在google查询一下，blueberry_lm对应的TCP端口号为1432，说明RandNum()帮我们随机生成了1432这个源端口号。



g. 最后来讲下fuzz()函数，前面的RandShort()和RandNum()都是写在sport后面的（当然也可以写在dport后面用来随机生成目的端口号），用fuzz()的话则可以省略sport这部分，fuzz()会帮你检测到你漏写了sport，然后帮你随机生成一个sport也就是源端口号。

使用fuzz()的命令如下：

```text
ans, unans = sr(IP(dst = "192.168.2.11") / fuzz(TCP(dport = 80, flags = "S")))
```

![img](..\images\v2-dbbf7528c9b1bd8303c420f21b7a5f8b_720w.jpg)

**这里看到fuzz()函数已经替我们随机生成了39246这个源端口号**