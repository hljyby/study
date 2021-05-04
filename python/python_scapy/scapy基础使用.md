# [python中的scapy模块](https://www.cnblogs.com/Yunzhonghe/p/12301151.html)

 

 

### 文章目录

- - - [模块简介](https://www.cnblogs.com/Yunzhonghe/p/12301151.html#_1)
    - [基本用法](https://www.cnblogs.com/Yunzhonghe/p/12301151.html#_10)
    - [Scapy的基本操作](https://www.cnblogs.com/Yunzhonghe/p/12301151.html#Scapy_19)
    - [Scapy模块中的函数](https://www.cnblogs.com/Yunzhonghe/p/12301151.html#Scapy_61)
    - [Scapy模块的常用简单实例](https://www.cnblogs.com/Yunzhonghe/p/12301151.html#Scapy_164)
    - [编写端口扫描器](https://www.cnblogs.com/Yunzhonghe/p/12301151.html#_187)

 

### 模块简介

Scapy是一个由Python编写的强大工具，目前很多优秀的网络扫描攻击工具都使用了这个模块。也可以在自己的程序中使用这个模块来实现对网络数据包的发送、监听和解析。这个模块相对于Nmap来说，更为底层。可以更直观的了解网络中的各类扫描攻击行为。

相对于Nmap来说，Scapy模块只会把收到的数据包展示给你，并不会告诉你这个包意味着什么。

例如，当你去医院检查身体时，医院会给你一份关于身体各项指标的检查结果，而医生也会告诉你得了什么病或者没有任何病。那么Nmap就像是一-个医生，它会替你搞定-切，按照它的经验提供给你结果。而Scapy则像是一个体检的设备， 它只会告诉你各种检查的结果，如果你自己就是-一个经验丰富的医生，显然检查的结果要比同行的建议更值得参考。

### 基本用法

在Kali里边已经集成了Scapy这个工具，我们在终端下输入Scapy就可以启动它了。
![在这里插入图片描述](..\images\watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmaeV0L3FxXzQzNTczNjc2,size_16,color_FFFFFF,t_70)

Scapy提供了和Python一样的交互式命令行，在这里需要说一下，接下来的实例我都会在这个命令行里运行。

### Scapy的基本操作

首先使用几个实例来演示一下Scapy的用法，在Scapy中每一个协议就是一个类。只需要实例化一个协议类，就可以创建一个该协议的数据包，例如，如果要创建一个IP类型的数据包，就可以使用如下命令。

```bash
ip = IP() 
```

IP数据包最重要的属性就是源地址和目的地址，这两个属性可以使用src和dst来设置，例如，要构造一个发往“192.168.1.107”的数据包，可以这么写。

```bash
ip = IP(dst="192.168.1.107")
```

![在这里插入图片描述](..\images\20200208145549858.png)
这个目标dst值可以是一个IP地址，也可以是一个网段，例如192.168.1.0/24，这时产生的就不是一个数据包，而是256个数据包。
![在这里插入图片描述](..\images\20200208145944245.png)
如果想要查看每个数据包，可以使用 **[p for p in ip]** 。
![在这里插入图片描述](..\images\20200208150119209.png)
Scapy采用分层的形式来构造数据包，通常最下面的一个协议为Ether，然后是IP，在之后是TCP或者UDP。IP()函数无法用来构造ARP请求和应答数据包，所以这时可以使用Ether()，这个函数可以设置发送方和接收方的MAC地址。那么现在来产生一个广播数据包，执行的命令如下。

```bash
Ether(dst="ff:ff:ff:ff:ff:ff")
```

执行后如图。
![在这里插入图片描述](..\images\20200208153250102.png)
如果要构造一个HTTP数据包，也可以使用如下这种方式。

```bash
IP()/TCP()/"GET/HTTP/1.0\r\n\r\n"
```

Scapy目前使用频率最高的类要数**Ether、IP、TCP和UDP**，但是这些类都具有哪些属性呢？Ether类中显然要有源地址、目的地址和类型。IP类的属性则复杂了许多，除了最重要的源地址和目的地址之外，还有版本、长度、协议类型、校验和等，TCP类中需要有源端口和目的端口。这里可以使用 **ls()** 函数来查看一个类拥有那些属性。

例如，使用ls(Ether())来查看Ether类的属性。
![在这里插入图片描述](..\images\20200208154105151.png)
也可以看一下IP()类中的属性。

![在这里插入图片描述](..\images\watermark,type_ZmFuZ3poZW5naGVprddGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQzNTczNjc2,size_16,color_FFFFFF,t_70)
可以对里边对应的属性进行设置，例如，将ttl的值设置为32，可以使用如下方式。

```python
IP(src="192.168.1.1",dst="192.168.1.107"ttl=32)
```

### Scapy模块中的函数

除了这些对应着协议类和它们的属性之外，还需要一些可以完成各种功能的函数。需要注意的一点是，刚才使用的IP()的作用是产生了一个IP数据包，但是并没有将其发送出去，因此，现在首先来看的就是如何将产生的报文发送出去，Scapy中提供了多个用来完成发送数据包的函数，首先来看一下其中的**send()\**和\**sendp()**。这两个函数的区别在于send()工作在第三层，而sendp()工作在第二层。简单地说，send()是用来发送IP数据包的，而sendp()是用来发送Ether数据包的。
例如，构造一个目的地址为“192.168.1.107”的ICMP数据包，并将其发送出去，可以使用如下语句。

```python
send(IP(dst="192.168.1.107")/ICMP())
```

执行结果。
![在这里插入图片描述](..\images\20200208155419455.png)如果成功了就会出现一个“Sent 1 packets.”的显示

```python
send(Ether(dst="ff:ff:ff:ff:ff:ff"))
```

执行结果。
![在这里插入图片描述](..\images\20200208155730819.png)
**注：这两个函数，只发不收**

如果希望发送一个内容是随机填充的数据包，而且又要保证这个数据包的正确性，那么可以是**fuzz()函数**。例如，可以使用如下命令来创建一个发往192.168.1.107的tcp数据包。

```python
IP(dst="192.168.1.107")/fuzz(TCP())
```

执行结果。
![在这里插入图片描述](..\images\20200208160205566.png)
在Scapy中提供了三个用来发送接收数据包的函数，分别是**sr()、sr1()和srp()**其中sr()和sr1()工作在第三层，例如IP和ARP等，而srp()工作在第二层。
这里仍然向192.168.1.107发送一个ICMP数据包来比较一下sr()和send()的区别。

```python
sr(IP(dst="192.168.1.107")/ICMP())
```

执行结果。
![在这里插入图片描述](..\images\20200208160852505.png)
当禅城==产生的数据包发送出去之后，Scapy就会监听接收到的数据包个数，answers表示对应的应答数据包。
sr()函数是Scapy的核心，它的返回值是两个列表，第一个列表是收到了应答的包和对应的应答，多伊尔戈列表是未收到应答的包。所以使用两个列表来保存sr()的返回值。
![在这里插入图片描述](..\images\20200208161445554.png)
这里使用ans和unans来保存sr()的返回值，因为发出的是一个ICMP请求数据包，而且也收到了一个应答包，所以这个发送的数据包和收到的应答包都被保存到了ans列表中，使用ans.summary()可以查看两个数据包的内容，而unans列表为空。

sr1()函数和sr()函数作用基本一样，但是值返回一个应答包。只需要使用一个列表就可以保存这个函数的返回值。例如，使用p来保存sr1(IP(dst=“192.168.1.107”)/ICMP())的返回值。
![在这里插入图片描述](..\images\watermark,type_ZmFuZ3poZW5naGVpdGk,sjhadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQzNTczNjc2,size_16,color_FFFFFF,t_70)
可以使用sr1()函数来测试目标的某个端口是否开放，采用半开扫描(SYN)的办法。

执行结果如图所示。
![在这里插入图片描述](..\images\watermark,type_ZmFuZ3poZ11W5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQzNTczNjc2,size_16,color_FFFFFF,t_70)

从上面p的值可以看出，192.168.1.107回应了发出设置了SYN标志位的TCP数据包，这表明他开放了80端口。

另外一个十分重要的函数就是sniff()，如果使用过Tcpdump，那么对这个函数的使用就不会感到陌生。通过这个函数可以在自己的程序中捕获经过本机网卡的数据包。
![在这里插入图片描述](..\images\2020020817001683.png)

这里有个比较坑的地方，就是他不能实时回显，你必须得终止嗅探他才会回显他嗅探到的包。

这个函数强大的地方在于可以使用番薯filter对数据包进行过滤。例如，指定之捕获与192.168.1.107有关的数据包，可以使用“host 192.168.1.107”：

```python
sniff(filter="192.168.1.107")
```

同样，也可以使用filter来过滤指定的协议，例如ICMP类型的数据包。

```python
sniff(filter="icmp")
```

如果要同时满足多个条件，可以使用“and”、“or”等关系运算符来表达：

```python
sniff(filter=" host 192.168.1.107 and icmp")
```

另外两个很重要的参数是**iface、count**。iface可以用来指定所要进行监听的网卡，例如，指定eth0作为监听网卡，就可以使用：

```python
sniff(iface="eth0")
```

而count则用来指定监听到数据包的数量，达到指定的数量就会停止监听，例如，只监听30个数据包：

```python
sniff(count=30)
```

现在设计一个综合性的监听器他会在网卡eth0上监听源地址或者目标地址为192.168.1.107的ICMP数据包，到收到3个这样的数据包就停止：

```python
sniff(filter="icmp and host 192.168.1.107",count=30,iface="eth0")
```

运行结果：
![在这里插入图片描述](..\images\20200208171714680.png)如果要查看这三个数据包的内容，可以使用"_"，在Scapy中这个符号表示是上一条语句的执行结果。例如：

```python
a=_
a.nsummart()
```

运行结果：
![在这里插入图片描述](..\images\20200208172000741.png)刚刚使用过的函数 pkt.summary()用来以摘要的形式显示pkt的内容，这个摘要长度为一行。

```python
p=IP(dst="www.baidu.com")
p.summary()
```

运行结果：
![在这里插入图片描述](..\images\20200208172217356.png)**注：函数pkt.summary的作用与pkt.nsummary()相同，只是操作对象是单个数据包**

### Scapy模块的常用简单实例

由于scapy功能极为强大，可以构造目前各种常见的协议类型的数据包，因此几乎可以使用这个模块完成任何任务，下面看看一些简单的应用。

使用scapy来实现一次ACK类型的端口扫描，对192.168.1.107的21、22、23、135、443、445这些端口是否被屏蔽进行扫描， **注意是屏蔽，不是关闭！** 采用ACK扫描模式，可以构造一下命令方式。

```python
ans,unans = sr(IP(dst="192.168.1.107")/TCP(dport=[21,22,23,135,443,445],flags="A"))
```

运行结果：
![在这里插入图片描述](..\images\20200208173719973.png)
正常的时候，如果一个开放的端口会回应ACK数据包，而关闭则回应RST数据包。在网络中，一些安全设备会过滤一部分端口，这些端口不会响应来自外界的数据包一切发往这些端口的数据包都石沉大海，这些端口的状态并非是开放或者关闭的这是网络安全管理常用的方法。

首先查看未被过滤的端口：

```python
 for s,r in ans:
    if s[TCP].dport == r[TCP].sport:
        print("The port "+str(s[TCP].dport)+" is unfiltered")
```

运行结果：
![在这里插入图片描述](..\images\11watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQzNTczNjc2,size_16,color_FFFFFF,t_70)

### 编写端口扫描器

下面使用Scapy强大的包处理功能来设计一个端口是否开放的扫描器。注意，这里还是要注意和前面例子的区别，如果-一个端口处于屏蔽状态，那么它将不会产生任何响应报文。如果一个端口处于开放状态，那么它在收到syn数据包之后，就会回应- -个ack数据包。反之，如果一个端口处于关闭状态，那么它在收到syn数据包之后，就会回应-一个rst数据包。首先在Kali Linux 2中启动一个终端，在终端中打开Python。先导入需要使用的模块文

```python
from scapy.all import fuzz,TCP,IP,sr #导入模块与函数
```

接下来产生一个目标为“192.168.1.107”的80端口的SYN数据包，将此标志位设置为“S”：

```python
ans,unans = sr(IP(dst="192.168.1.1")/fuzz(TCP(dport=80,flags="S"))) //指定目标地址以及端口
```

接下来使用循环查看，如果r[TCP].flags==18,则表示目标端口开放，若为20则为关闭状态。

```python
for s,r in ans:                    		#把ans的值赋给s，r并开始遍历
	if r[TCP].flags==18:		   		#判断返回值是否等于18
		print("This port is Open") 		#输出判断结果
	if r[TCP].flags==20:				#判断返回值是否等于20
		print("This port is Closed")	#输出判断结果
```

运行结果：
![在这里插入图片描述](..\images\watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQzNTczNjc2,size_16,color_FFFFFF,t_70)