# 网络工程师的Python之路---Scapy应用篇

《[Scapy基础篇](https://zhuanlan.zhihu.com/p/51002301)》里已经向大家介绍了Scapy的一些基础知识，这篇将重点讲解Scapy的实际应用，包括怎么使用Scapy进行TCP的SYN扫描、ACK扫描、FIN扫描、Xmas扫描, Null扫描，怎么使用Scapy执行TCP SYN flooding攻击，ARP欺骗攻击，DHCP饥饿攻击，怎么用Scapy探测rogue DHCP服务器等等。以上所有扫描、攻击方法都可以借助黑客工具完成，比如上述TCP各种类型的扫描靠大名鼎鼎的Nmap都能实现，而实现其他上述攻击的工具更是数不胜数，但是很少有人知道或者深挖过这些工具背后的原理，“知其然还要知其所以然”是笔者写这篇《Scapy应用篇》的初衷。

本篇将融合Python代码讲解，如果你对Python不熟，可以参考我专栏置顶的《网络工程师的Python之路--初级篇》。同以往一样，本篇会以实验的方式一一对上述知识点进行呈现和讲解，文章一星期一更。



## **Scapy实验运行环境和拓扑：**

**本篇的实验运行环境以及网络实验拓扑和**《[Scapy基础篇](https://zhuanlan.zhihu.com/p/51002301)》**完全一样，这里简单回顾一下：**

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



![img](https://pic3.zhimg.com/80/v2-0bf401115fae4b26d88cd76b39dc5822_720w.jpg)



## **实验1 -- TCP SYN扫描**

**实验目的：**使用TCP SYN扫描交换机S1(192.168.2.11)的22（SSH）， 80 （HTTP）， 123 （NTP）端口，知道如何判断端口是被关闭了(closed)还是被过滤了(filtered)，两者各自有什么特征。

**实验原理：**TCP三次握手的原理和过程相信大家都知道。根据RFC 793，当发送端的TCP SYN包发出后，大致会有下面四种情况发生:

1. 目的端口在接收端打开（也可以说接收端正在侦听该端口），收到SYN包的接收端回复**SYN/ACK包**给发送端，收到SYN/ACK包的发送端此时知道**目的端口是打开的(open)。**
2. 目的端口在接收端被关闭，收到SYN包的接收端回复**RST包**给发送端，告知发送端**该目的端口已经被关闭了(closed)。**
3. 如果发送端和接收端之间有防火墙或者使用ACL进行包过滤的路由器，那么**SYN包在到达接收端之前就被防火墙或路由器拦截下来，**此时防火墙或路由器会回复一个类型3（Unreachable，不可达）的ICMP包（注意不再是TCP包）给发送端告知**该目的端口已经被过滤了(filtered)。**
4. 如果ICMP在防火墙或路由器上被关闭了，这时SYN包会被防火墙、路由器"静悄悄"地丢弃，路由器和防火墙不会发送类型3的ICMP包告知发送端。此时发送端收不到任何回应(no response)，这里我们同样可以判断**该目的端口已经被过滤了(filtered)。**

知道实验原理后来看代码：

```python
from scapy.all import *

target = '192.168.2.11'

ans, unans = sr(IP(dst = target) / TCP(sport = RandShort(), dport = [22, 80, 123], flags = "S"), timeout = 5)

for sent, received in ans:
        if received.haslayer(TCP) and str(received[TCP].flags) == "SA":
                print "Port " + str(sent[TCP].dport) + " of " + target + " is OPEN!"
        elif received.haslayer(TCP) and str(received[TCP].flags) == "RA":
                print "Port " + str(sent[TCP].dport) + " of " + target + " is closed!"
        elif received.haslayer(ICMP) and str(received[ICMP].type) == "3":
                print "Port " + str(sent[TCP].dport) + " of " + target + " is filtered!"

for sent in unans:
        print str(sent[TCP].dport) + " is filtered!"
```

- 代码里涉及到的Scapy的sr()，IP(), TCP()，RandShort()等函数在《Scapy基础篇》里已经讲过了，这里不再赘述。
- 这里我们使用sr()函数对192.168.2.11(即S1)做端口22，80，123的TCP SYN扫描（注意flags = "S"）, timeout设为5秒。sr()函数返回的是一个元组，该元组下面有两个元素，一个是Results，一个是Unanswered，我们用ans来表示Results，也就是被响应的包，用unans来表示Unanswered，表示没有被响应的包。

```python
ans, unans = sr(IP(dst = target) / TCP(sport = RandShort(), dport = [22, 80, 123], flags = "S"), timeout = 5)
```

- ans和unans各自又含两个包，一个是发出去的包，一个是接收到的包，以ans[0][0]和ans[0][1]为例，第一个[0]表示抓到的第一个包，第二个[0]和[1]分别表示第一个包里发出的包和接收到的包。举例如下：

```text
>>> ans[0][0] （第一个包里发出的包）
<IP frag=0 proto=tcp dst=192.168.2.11 |<TCP dport=sunrpc flags=A |>>
>>> ans[0][1] （第一个包里接收到的包）
<IP version=4 ihl=5 tos=0x0 len=40 id=10338 flags= frag=0 ttl=255 proto=tcp chksum=0xe11 src=192.168.2.11 dst=192.168.2.1 options=[] |<TCP sport=sunrpc dport=ftp_data seq=0 ack=0 dataofs=5 reserved=0 flags=R window=0 chksum=0x2a01 urgptr=0 |<Padding load='\x00\x00\x00\x00\x00\x00' |>>>
```

- 正因如此，所以下面for loop里的sent, received分别代表的是ans[0][0]、ans[0][1](抓到的第一个端口为22的包)，ans[1][0]、ans[1][1]（抓到的第二个端口为80的包）以及ans[2][0]、ans[2][1]（抓到的第三个端口为123的包）里的内容

```python
for sent, received in ans:
```

- haslayer()函数返回的是布尔值，用来判断**从接收端返回的包(received)**里所含协议的类型，这里用来判断该received包是否包含TCP协议，并且该包里TCP的flag位是否为SA, SA代表SYN/ACK，如果这两个条件都满足，则说明该端口在接收端是打开的(Open)，然后将该信息打印出来。

```python
        if received.haslayer(TCP) and str(received[TCP].flags) == "SA":
                print "Port " + str(sent[TCP].dport) + " of " + target + " is OPEN!"
```

- 同理，如果返回的包是TCP包，并且该TCP包的flag位为RA（RA表示Reset+），则说明该端口在接收端已经被关闭(closed)，将该信息打印出来。

```python
        elif received.haslayer(TCP) and str(received[TCP].flags) == "RA":
                print "Port " + str(sent[TCP].dport) + " of " + target + " is closed!"
```

- 如果返回的包是ICMP包，并且该ICMP包的类型为3，则说明该端口被路由器或者防火墙过滤了(filtered)，将该信息打印出来。

```python
        elif received.haslayer(ICMP) and str(received[ICMP].type) == "3":
                print "Port " + str(sent[TCP].dport) + " of " + target + " is filtered!"
```

- 最后，如果发送端没有收到任何回复(no response)，我们同样可以判断该端口被路由器或者防火墙过滤了(filtered)，将该信息打印出来。

```python
for sent in unans:
        print str(sent[TCP].dport) + " is filtered!"
```



**执行代码看效果：**

- 执行代码前，我们的S1上面只开启了SSH,也就是端口22，另外两个端口80和123是被关闭的，S1上面没有开启ACL做包过滤，S1和我们的Scapy主机之间也没有防火墙。

![img](..\images\v2-8a3cf10d25847b71896b61ee7acaa2ca_720w.jpg)

- 执行代码后，你会看到端口22是打开的，端口80和123是关闭的(我们收到了S1发来的TCP RST包）
- 这时在S1上开启http server，打开80端口

![img](..\images\v2-1fc76d2f3df220cb04fcf714a81367bc_720w.jpg)

- 再次运行我们的scapy代码，可以发现现在端口80也打开了。

![img](..\images\v2-fe2ed5ae8235fc6665b230fea867e0eb_720w.jpg)

- 在S1上配置ACL，deny掉80端口。

![img](..\images\v2-90242864f00bc0dcdc1d304b4502e574_720w.jpg)

- 再次执行scapy代码，可以看到此时“80端口已经被过滤，路径上存在防火墙或者带有ACL的路由器！”的信息。

![img](..\images\v2-8544692bc872a0a4b745dc8f18772e27_720w.jpg)