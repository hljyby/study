# 挂在开头保命

```shell
我的centos 网卡配置
PREFIX=24 # 代表子网掩码 255.255.255.0 也可以写成 NETMASK=255.255.255.0
我试了好多次，最终发现虚拟机连不上外网是因为我的宿主机没有重启。FUCK
DNS1=114.114.114.114 也是可以的，线图的配置是指向网关的 DNS2=8.8.8.8
如果你是DHCP 自动分配 BOOTOTO=DHCP [ONBOOT=no => 开机不加载这个配置文件]
cd /etc/sysconfig/network-scripts/
vim ifcfg-ens160
把下图打上
nmcli c reload # 重新加载网卡的配置文件
重启宿主机
```

![image-20210504123908537](\images\image-20210504123908537.png)



# 一：相关网络配置的文件

## 1、网卡名配置相关文件

### **网卡名命名规则文件：**

`/etc/udev/rules.d/70-persistent-net.rules`

```
# PCI device 0x8086:0x100f (e1000)
SUBSYSTEM=="net", ACTION=="add", DRIVERS=="?*", ATTR{address}=="00:0c:29:db:c9:5c", ATTR{type}=="1", KERNEL=="eth*", NAME="eth0"
PCI device 0x8086:0x100f (e1000)
SUBSYSTEM"net", ACTION"add", DRIVERS"?*", ATTR{address}"00:0c:29:db:c9:66", ATTR{type}"1", KERNEL"eth*", NAME="eth1"
```



**修改网卡命名示例：**

1、查看网卡的驱动并且卸载网卡驱动

```
[root@rhel6 ~]# ethtool -i eth0
driver: e1000 #网卡驱动
[root@rhel6 ~]# modprobe -r e1000 #卸载网卡驱动
```

2、修改70-persistent-net.rules文件

3、重新加载网卡驱动并且重启网络服务

```
[root@rhel6 ~]# modprobe e1000   #重新加载网卡驱动
[root@rhel6 ~]# /etc/rc.d/init.d/network restart #重启网络服务
```

### 将CentOS7.x网卡名改为传统命名方式：

1、修改/etc/default/grbu文件

```
# sed -i.bak -r 's/(GRUB_CMDLINE_LINUX=.*)"/\1 net.ifnames=0"/' /etc/default/grub
```

2、生成新的grub配置文件并重启生效

```
grub2-mkconfig -o /etc/grub2.cfg
```

## 2、网络配置相关文件

网络配置参考文件：/usr/share/doc/initscripts-9.03.53/sysconfig.txt

网卡的配置在：/etc/sysconfig/network-scripts/下，配置文件：ifcfg-网卡名

**配置文件示例：**

```shell
[root@rhel6 ~]# cat /etc/sysconfig/network-scripts/ifcfg-eth0
DEVICE=eth0
BOOTPROTO=static|dhcp|none
IPADDR=192.168.0.6
NETMASK=255.255.255.0
#PREFIX=24 #子网掩码
GATEWAY=192.168.0.1
DNS1=114.114.114.114
DNS2=8.8.8.8
DNS3=1.1.1.1
TYPE=Ethernet
ONBOOT=yes
HWADDR=00:0C:29:DB:C9:5C
#MACADDR=00:0C:29:DB:C9:5A #修改MAC地址
UUID=38d329c5-b1bb-491b-a669-47422cfda764
NM_CONTROLLED=no
```




**网络配置文件常用配置参数详解：**

- DEVICE：此配置文件应用到的设备
- HWADDR：对应的设备的MAC地址
- BOOTPROTO：激活此设备时使用的地址配置协议，常用的dhcp, static, none, bootp
- NM_CONTROLLED：NM是NetworkManager的简写，此网卡是否接受NM控制；建议为“no”(NetworkManager:图形界面的网络配置工具，不支持桥接，强烈建议关闭)
- ONBOOT：在系统引导时是否激活此设备
- TYPE：接口类型，常见有的Ethernet, Bridge
- UUID：设备的惟一标识
- IPADDR：指明IP地址
- NETMASK：子网掩码
- GATEWAY: 默认网关
- DNS1：第一个DNS服务器指向
- DNS2：第二个DNS服务器指向
- USERCTL：普通用户是否可控制此设备
- PEERDNS：如果BOOTPROTO的值为“dhcp”，是否允许dhcp server分配的dns服务器指向信息直接覆盖至/etc/resolv.conf文件中

## 3、其他相关配置文件

路由配置文：/etc/sysconfig/network-scripts/route-interface

- NETWOEK/NETMASK via GATEWAY

DNS配置文件：/etc/resolv.conf

- nameserver DNS_IP

本地网络解析配置文件：/etc/hosts

- IP　　hostname alias

主机名配置文件：

- centos6.x：/etc/sysconfig/network
- centos7.x：/etc/hostname

# 二：关于网络的配置Tools

## ①ifconfig

- -a：查看启用和被禁用的网卡信息
- interface {up|down}：启用或禁用网卡
- interface IP/NETMASK：临时设置IP
- interface [-]promisc：设置网卡的工作在混杂模式
- -s interface：查看指定网卡的流量信息

## ②route

- -n：以数字方式显示，不解析，提高效率
- add {-net | -host} NETWORK/NETMASK gw GATEWAY dev DEVICE 添加路由
- {add | del} default gw GATEWAY 添加或删除默认路由
- del {-net | -host} NETWORK/NETMASK gw GATEWAY 删除路由

```
route add -net 10.0.0.0/8 gw 172.20.0.1 dev eth1 #添加一条到10.0.0.0网段的路由route del -net 10.0.0.0/8 gw 172.20.0.1 #删除10.0.0.0网段的路由
```

## ③netstat

- -n：以数字方式显示，不解析，提高效率
- -r：查看路由表
- -t：TCP相关
- -u：UDP相关
- -w：裸套接字
- -l：查看处于监听状态的端口
- -a：查看所有状态的端口
- -e：显示更详细的信息
- -p：查看相关的进程PID
- -i：显示网卡流量
- -Iinterface：查看指定网卡的流量信息 == ifconfig -s interface

```
[root@centos7 ~]# netstat -tnulp  #显示TCP，UDP的监听状态及相关进程的端口    
```

## ④ip

- link

  - set interface {up|down}：启用或禁用网卡
  - show interface：显示指定网卡信息

- addr

  - add IP/NETMASK [label interface:#] [scope {global | link | host}] [broadcast IP] dev interface：添加配置临时地址

    - label：指定别名

    - scope：作用域

    - - global：作用域为全局
      - link：仅和此网卡相连的网络生效
      - host：仅主机可用

    - broadcast：设定广播地址

  - del dev interface [label interface:#]：删除IP

  - flush dev interface [label interface:#]：清空IP

- route
  - add IP/NETMASK via GATEWAY dev interface：添加路由
  - add default via GATEWAY dev interface：添加默认路由
  - del IP/NETMASK via GATEWAY dev interface：删除路由
  - flush：清空路由表
  - show：查看路由表

```
[root@centos7 ~]# ip addr add 192.168.1.100/24 label eth0:0 dev eth0 #设置临时IP地址
```

 

## ⑤ss

- -n：以数字方式显示，不解析，提高效率
- -t：TCP相关
- -u：UDP相关
- -w：裸套接字
- -x：显示unix sock相关信息
- -l：查看处于监听状态的端口
- -a：查看所有状态的端口
- -e：显示更详细的信息
- -p：查看相关的进程PID
- -m：内存用量
- -o：计时器信息
- -s：显示当前socket详细信息
- state TCP_STATE '( dport = :ssh or sport = :ssh )'
  - established
  - listen
  - fin_wait_1
  - fin_wait_2
  - syn_sent
  - syn_recv

```
[root@centos7 ~]# ss state established '( dport = :ssh or sport = :ssh )' #查看已连接状态的ssh
```

 

## ⑥nmcli：地址配置工具（CentOS7.x）（NetworkManager-cli）

子命令补全功能：yum install bash-completion ，依赖epel源

1、查看信息

```
[root@centos7 ~]# nmcli device status[root@centos7 ~]# nmcli connection show
```

2、删除配置

```
[root@centos7 ~]# nmcli connection delete ens33
```

3、增加配置

```
[root@centos7 ~]# nmcli connection add con-name ens33 ifname ens33 type ethernet ipv4.method auto connection.autoconnect yes
```

- con-name ens33：配置文件名称
- ifname ens33：指定网卡设备
- type ethernet：网络类型以太网
- ipv4.method auto：自动获取IP
- connection.autoconnect yes：开机自启动

 4、切换配置

```
[root@centos7 ~]# nmcli connection up ens33
```

 5、修改配置文件名ens33 --> ens33-static

```
[root@centos7 ~]# nmcli connection modify ens33 con-name ens33-static
```

 6、修改配置IP

```
[root@centos7 ~]# nmcli connection modify ens33-static ipv4.addresses 192.168.0.100/24 ipv4.gateway 192.168.0.1 ipv4.method manual
```

- ipv4.addresses 192.168.0.100/24：IP地址
- ipv4.gateway 192.168.0.1：网关
- ipv4.method manual：手动获取，静态地址必须配置为手动，否则默认动态

7、重新读取配置文件

```
[root@centos7 ~]# nmcli connection reload
```

8、断开和连接网络连接

```
[root@centos7 ~]# nmcli device disconnect ens33[root@centos7 ~]# nmcli device connect ens33
```

9、查看网络配置的详细信息

```
[root@centos7 ~]# nmcli connection show ens33
```

10、在配置中再添加一个地址

```
[root@centos7 ~]# nmcli connection modify ens33-static +ipv4.addresses 10.0.0.2/8
```

**一、CentOS 7和CentOS 8网络配置区别：**

VMware Workstation 15 Pro中安装了CentOS 8.0.1905，但在配置IP地址过程中发现没有了network.service，并且/etc/sysconfig/network-scripts目录中也没有任何脚本文件，CentOS 7中同时支持network.service和NetworkManager.service（简称NM）2种方式配置网络，而在CentOS 8中已经废弃network.service，必须通过NetworkManager.service配置网络。

![image.png](images\2019102910031017.png)

![image.png](images\2019102910031118.png)

**二、NetworkManager的命令行工具nmcli简单使用说明：**

1、查看IP（类似于ifconfig、ip a）：# nmcli

![image.png](images\2019102910031119.png)

2、激活网卡的3种方式（相当于ifup）：

（1）# nmcli c up ens33

![image.png](images\2019102910031120.png)

备注：nmcli c | connection，连接，可理解为配置文件，相当于ifcfg-ethX或ifcfg-ensX

（2）# nmcli d connect ens33

![image.png](images\2019102910031121.png)

备注：nmcli d | device，设备，可理解为实际存在的网卡（包括物理网卡和虚拟网卡）

（3）# nmcli d reapply ens33

![image.png](images\2019102910031122.png)

3、禁用网卡（相当于ifdown）：# nmcli c down ens33

4、查看connection列表：# nmcli c show

![image.png](images\2019102910031123.png)

5、查看connection详细信息：# nmcli c show ens33

6、重载所有ifcfg或route到connection（不会立即生效）：# nmcli c reload

7、查看device列表：# nmcli d

![image.png](images\2019102910031124.png)

备注：device有4种状态

（1）connected：已被NM管理，并且当前有活跃的connection

（2）disconnected：已被NM管理，但是当前没有活跃的connection

（3）unmanaged：未被NM管理

（4）unavailable：不可用，NM无法管理，通常出现于网卡link为down时（如：ip link set ethX down）

8、查看所有device详细信息：# nmcli d show

9、查看指定device详细信息：# nmcli d show ens33

![image.png](images\2019102910031125.png)

10、查看NM管理状态：# nmcli n

![image.png](images\2019102910031126.png)

11、开启NM管理：# nmcli n on

12、检测NM是否在线可用：# nm-online

![image.png](images\2019102910031227.png)

**说明：有关** **nmcli** **命令的详细使用说明可以参考** **# man nmcli** **或** **# nmcli -h** **，具体对象的用法如** **device** **，可参考** **# man nmcli d** **或** **# nmcli d -h **

# 三：其他相关工具

ping：测试网络命令

- -c count：ping的次数
- -W timeout：超时时间，配合-c使用
- -I ipaddress：指定用自己主机的IP去ping对方主机
- -s size：每次ping发出的数据包大小，最大值65507
- -f：竭尽自己主机的能力发出数据包

```
[root@centos7 ~]# ping -c1 -W1 192.168.0.6 #脚本中常用的ping测试，ping一次，超时时间1s
[root@centos7 ~]# ping -s 65507 -f 192.168.0.6 #竭尽自己所能，向192.168.0.6发出大数据包，ddos攻击
```

tcpdump：抓包工具

- -n：禁止解析IP
- -i interface：指定网卡接口
- tcp|udp|icmp|arp：指定包协议

mtr：网络诊断工具

traceroute：跟踪路由

tracepath：跟踪路由

ifup：启用网卡

ifdown：禁用网卡

setup：字符界面配置工具（centos6.x）

system-config-network-tui：字符界面网络配置工具（centos6.x）

hostnamectl：设置主机名工具（centos7.x）

- status
- set-hostname HOSTNAME

mm-connection-editor：图形界面网络配置工具（centos7.x）

nmtui：字符界面配置工具（centos7.x）

- nmtui-connect
- nmtui-edit
- nmtui-hostname

lftp | lftp [-u user[,pass]] [-p port] [-e cmd] FTPSERVER：FTP客户端工具

- get
- mget
- put
- mput
- mirror DIR

lftpget URL：非交互式下载ftp服务器的文件

wget：网络下载工具

- -q：静默模式
- -c：断点续传
- -P /path/DIRNAME：下载的文件保存到指定文件夹
- -O /path/FILENAME：下载的文件保存到指定位置，并重命名
- --limit-rate=# K|M：限速至# K|M

elinks | links：字符界面web浏览器

- -source：查看网页源代码
- -dump：只显示文字

# 四：Bonding和Team

## ++Bonding++

绑定：将多块网卡绑定同一IP地址对外提供服务，可以实现高可用或者负载均衡。


### **工作模式：**

mode 0：balance-rr 轮调策略：多张网卡可以轮流发数据包，实现负载均衡的功能

mode 1：active-backup 主备策略：其中active网卡的发数据包，其他备用

mode 3：broadcast 广播策略：每个网卡都会发一份包


### **配置示例：**

1、创建bonding的设备配置文件


```
# cat >/etc/sysconfig/network-scripts/ifcfg-bond0 <<EOF
DEVICE=bond0
BOOTPROTO=none
BONDING_OPTS="miimon=100 mode=1"
IPADDR=192.168.0.6
PREFIX=24
EOF
```



miimon=100：每100ms进行一次链路检测

2、配置bonding的从属网卡


```
[root@rhel6 ~]# cat >/etc/sysconfig/network-scripts/ifcfg-eth0 <<EOF
DEVICE=eth0
BOOTPROTO=none
MASTER=bond0
SLAVE=yes
EOF
[root@rhel6 ~]# cat >/etc/sysconfig/network-scripts/ifcfg-eth1 <<EOF
DEVICE=eth1
BOOTPROTO=none
MASTER=bond0
SLAVE=yes
EOF
```



3、重启网络服务并查看bonding状态


```
# /etc/rc.d/init.d/network restart
[root@rhel6 ~]# cat /proc/net/bonding/bond0 |head
Ethernet Channel Bonding Driver: v3.7.1 (April 27, 2011)
Bonding Mode: fault-tolerance (active-backup)
Primary Slave: None
Currently Active Slave: eth0 #现在eth0在工作状态
MII Status: up
MII Polling Interval (ms): 100
Up Delay (ms): 0
Down Delay (ms): 0
```



### 删除bonding配置示例：

1、禁用bond0并卸载bonding模块

```
# ip link set bond0 down# modprobe -r bonding
```

2、还原配置文件，重启网络

附：[官方文档链接](https://www.kernel.org/doc/Documentation/networking/bonding.txt)

## ++Team++

网络组：是将多个网卡聚合在一起方法，从而实现冗错和提高吞吐量。

工作模式：runner

- broadcast：广播
- roundrobin：轮调
- activebackup：主备

1、创建一个网络组接口

```
[root@centos7 ~]# nmcli connection add type team con-name team0 ifname team0 config '{"runner":{"name":"activebackup"}}'
```

2、配置team0

```
[root@centos7 ~]# nmcli connection modify team0 ipv4.addresses 172.20.108.244/16 ipv4.method manual ipv4.gateway 172.20.0.1
```

3、创建port接口

```
[root@centos7 ~]# nmcli connection add con-name team0-eth1 type team-slave ifname eth1 master team0
[root@centos7 ~]# nmcli connection add con-name team0-eth2 type team-slave ifname eth2 master team0
```

 4、启动team0及从属接口

```
[root@centos7 ~]# nmcli connection up team0
[root@centos7 ~]# nmcli connection up team0-eth1
[root@centos7 ~]# nmcli connection up team0-eth2
```

5、查看工作状态

```
[root@centos7 ~]# teamdctl team0 state
```

6、配置文件示例：

![img](https://images.cnblogs.com/OutliningIndicators/ContractedBlock.gif) ifcfg-team0配置文件

7、删除team0

```
[root@centos7 ~]# nmcli connection down team0
[root@centos7 ~]# nmcli connectioni delete team0-eth0
[root@centos7 ~]# nmcli connectioni delete team0-eth1
```

# 五：Bridge

桥接：把一台机器上的若干个网络接口“连接”起来。其结果是，其中一个网口收到的报文会被复制给其他网口并发送出去。以使得网口之间的报文能够互相转发。网桥就是这样一个设备，它有若干个网口，并且这些网口是桥接起来的。与网桥相连的主机就能通过交换机的报文转发而互相通信。

![img](images\1331725-20180503151528958-1714978532.png)

主机A发送的报文被送到交换机S1的eth0口，由于eth0与eth1、eth2桥接在一起，故而报文被复制到eth1和eth2，并且发送出去，然后被主机B和交换机S2接收到。而S2又会将报文转发给主机C、D。

1、创建一个网桥

```
[root@centos7 ~]# nmcli connection add type bridge con-name br0 ifname br0
```

 

2、配置网桥

```
[root@centos7 ~]# nmcli connection modify br0 ipv4.addresses 192.168.0.7/24 ipv4.method manual
```

 

3、将从属网卡加入网桥

```
[root@centos7 ~]# nmcli connection add type bridge-slave con-name br0-eth0 ifname eth0 master br0
```

 

4、启用网桥并查看状态

```
[root@centos7 ~]# nmcli connection up br0
[root@centos7 ~]# nmcli connection up br0-eth0
[root@centos7 ~]# brctl show
bridge name     bridge id               STP enabled     interfaces
br0             8000.000c295df21e       yes             eth0
```

 

5、配置文件示例：

![img](https://images.cnblogs.com/OutliningIndicators/ExpandedBlockStart.gif)

```
[root@centos7 ~]# cat /etc/sysconfig/network-scripts/ifcfg-br0
DEVICE=br0
STP=yes
BRIDGING_OPTS=priority=32768
TYPE=Bridge
PROXY_METHOD=none
BROWSER_ONLY=no
BOOTPROTO=none
DEFROUTE=yes
IPV4_FAILURE_FATAL=no
IPV6INIT=yes
IPV6_AUTOCONF=yes
IPV6_DEFROUTE=yes
IPV6_FAILURE_FATAL=no
IPV6_ADDR_GEN_MODE=stable-privacy
NAME=br0
UUID=94582afc-01a1-406d-a25a-91be7c350c23
ONBOOT=yes
IPADDR=192.168.0.7
PREFIX=24
[root@centos7 ~]# cat /etc/sysconfig/network-scripts/ifcfg-br0-eth0
TYPE=Ethernet
NAME=br0-eth0
UUID=9dd2a7fc-f143-4243-89ca-85f223e34348
DEVICE=eth0
ONBOOT=yes
BRIDGE=br0
```



# Centos 修改IP地址、网关、DNS

## 一、CentOS 修改IP地址

 

修改对应网卡的IP地址的配置文件

\# vi /etc/sysconfig/network-scripts/ifcfg-eth0  电信

\# vi /etc/sysconfig/network-scripts/ifcfg-eth0:1 网通

 

修改以下内容

DEVICE=eth0 #描述网卡对应的设备别名，例如ifcfg-eth0的文件中它为eth0

BOOTPROTO=static #设置网卡获得ip地址的方式，可能的选项为static，dhcp或bootp，分别对应静态指定的 ip地址，通过dhcp协议获得的ip地址，通过bootp协议获得的ip地址

BROADCAST=192.168.0.255 #对应的子网广播地址

HWADDR=00:07:E9:05:E8:B4 #对应的网卡物理地址

IPADDR=12.168.1.2 #如果设置网卡获得 ip地址的方式为静态指定，此字段就指定了网卡对应的ip地址

IPV6INIT=no

IPV6_AUTOCONF=no

NETMASK=255.255.255.0 #网卡对应的网络掩码

NETWORK=192.168.1.0 #网卡对应的网络地址

ONBOOT=yes #系统启动时是否设置此网络接口，设置为yes时，系统启动时激活此设备

 

## 二、CentOS 修改网关

修改对应网卡的网关的配置文件

[root@centos]# vi /etc/sysconfig/network

 

修改以下内容

NETWORKING=yes(表示系统是否使用网络，一般设置为yes。如果设为no，则不能使用网络，而且很多系统服务程序将无法启动)

HOSTNAME=centos(设置本机的主机名，这里设置的主机名要和/etc/hosts中设置的主机名对应)

GATEWAY=192.168.1.1(设置本机连接的网关的IP地址。例如，网关为10.0.0.2)

 

## 三、CentOS 修改DNS

修改对应网卡的DNS的配置文件

\# vi /etc/resolv.conf

修改以下内容

nameserver 8.8.8.8 #google域名服务器

nameserver 8.8.4.4 #google域名服务器

 

## 四、重新启动网络配置

\# service network restart

或

\# /etc/init.d/network restart

 

### 修改 IP 地址

即时生效:

\# ifconfig eth0 192.168.0.2 netmask 255.255.255.0

启动生效:

修改 /etc/sysconfig/network-scripts/ifcfg-eth0

 

### 修改网关 Default Gateway

即时生效:

\# route add default gw 192.168.0.1 dev eth0

启动生效:

修改 /etc/sysconfig/network

 

### 修改 DNS

修改/etc/resolv.conf

修改后可即时生效，启动同样有效

 

### 修改 host name

即时生效:

\# hostname centos1

启动生效:

修改/etc/sysconfig/network



## 问题情况：

1、虚机centos8 修改为静态ip后，由于网卡网段变更，无法上网

2、最小化安装，没有ifconfig

3、firewalld，selinux关闭

4、ping 不通物理机

 

根本原因：

　　静态路由配置错误

### 解决方案：

1、linux命令==> 　　ip:ip addr　　查看网络配置

[![img](\images\1150273-20191023111005966-607300092.png)](https://img2018.cnblogs.com/blog/1150273/201910/1150273-20191023111005966-607300092.png)

　　　　　　　　　　nmcli:　　　查看网络配置

[![img](\images\1150273-20191023110919154-364787888.png)

 2、修改为DHCP或修改默认路由为正确的默认路由地址

修改配置文件：vi /etc/sysconfig/network-scripts/ifcfg-ens160

将BOOTPROTO修改为DHCP

如果配置IPADDR和GATEWAY，需要删去或修改为正确的默认路由地址，如果不知道，可以使用DHCP

[![img](G:\新知识\linux\images\1150273-20191023111318325-485940392.png)

 3、重启网卡

不能使用service和systemctl

[![img](images\1150273-20191023111854532-1705824657.png)

 方法：nmcli c reload +网卡名

例：nmcli c reload ens160

如果不行，可尝试以下命令

\# 重载所有ifcfg或route到connection（不会立即生效）
nmcli c reload ifcfg-xxx
\# 重载指定ifcfg或route到connection（不会立即生效）
nmcli c load /etc/sysconfig/network-scripts/ifcfg-ethX
nmcli c load /etc/sysconfig/network-scripts/route-ethX
\# 立即生效connection，有3种方法
nmcli c up ethX
nmcli d reapply ethX
nmcli d connect ethX

4、测试

[![img](\images\1150273-20191023112422834-1816796961.png)

 