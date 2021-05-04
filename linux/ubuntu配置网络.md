# [Ubuntu 18.04配置静态IP地址](https://www.cnblogs.com/blueyunchao0618/p/11394640.html)

在本文中，我们将解释如何使用Netplan实用程序在Ubuntu 18.04中为网络接口配置网络静态或动态IP地址。

 

想把ubuntu的ip地址设置成静态ip，折腾了一段时间，还是无法成功，特从网上搜了一下，发现设置ip的方式改了。

特整理一下，放这儿！

转自：http://blog.sina.com.cn/s/blog_5373bcf40102xk5g.html

 

2018年4月26日，ubuntu 18.04发行，第一时间下载安装了SERVER版本。使用VM14版本的虚拟机，开始使用DHCP获得IP地址，没有意外，可以直接上网。然而在更改VM的网络模式为桥接模式时，想把虚拟机设为固定IP时，出现故障，一直不能获得地址，也上不了网。经常无数次测试，有以下经验可供参考。

ubuntu从17.10开始，已放弃在/etc/network/interfaces里固定IP的配置，即使配置也不会生效，而是改成netplan方式 ，配置写在/etc/netplan/01-netcfg.yaml或者类似名称的yaml文件里，18.04的server版本安装好以后，配置文件是：/etc/netplan/50-cloud-init.yaml，修改配置以后不用重启，执行 netplan apply 命令可以让配置直接生效。以前的重启网络服务命令/etc/init.d/networking restart或者services network restrart也都会提示为无效命令。

$sudo vim /etc/netplan/50-cloud-init.yaml，配置文件可按如下内容修改。

```
network:
  version: 2
  renderer: networkd
  ethernets:
    ens33:   #配置的网卡名称
      dhcp4: no    #dhcp4关闭
      dhcp6: no    #dhcp6关闭
      addresses: [192.168.1.55/24]   #设置本机IP及掩码
      gateway4: 192.168.1.254   #设置网关
      nameservers:
          addresses: [114.114.114.114, 8.8.8.8]   #设置DNS
```

注意点：

1.以上配置文件共11行，其中第2，3，6，7四行可以不写，测试过没有这四行，网络也能工作正常，第5行的ens33为虚拟网卡，可以使用ifconfig -a查看本机的网卡。

2.配置文件里在冒号：号出现的后面一定要空一格，不空格则在运行netplan apply时提示出错。

3.关键之关键是看清配置总共分为五个层次，逐层向后至少空一格，

第一层－network:

第二层－－ ethernets:

第三层－－－ ens33:

第四层－－－－addresses:  [192.168.1.55/24]

第四层－－－－gateway4:  192.168.1.254

第四层－－－－nameservers:

第五层－－－－－addresses: [114.114.114.114, 8.8.8.8]

 

出现类似错误：line8 column 6:cloud not find expected ':'  #提示是冒号：后面没加空格

出现类似错误：netplan found character that cannot start any token，#提示是没有按五个层次写配置文档，一定要下一层比上一层多空一格或以上。

 

**Netplan**是**Ubuntu 17.10中**引入的一种新的命令行网络配置实用程序，用于在Ubuntu系统中轻松管理和配置网络设置。 它允许您使用**YAML**抽象来配置网络接口。 它可与**NetworkManager**和**systemd-networkd**网络守护程序（称为**渲染程序** ，您可以选择使用其中的哪一个）一起作为内核的接口。

它读取**/etc/netplan/\*.yaml中**描述的网络配置，并且可以将所有网络接口的配置存储在这些文件中。

在本文中，我们将解释如何使用**Netplan**实用程序在**Ubuntu 18.04中**为网络接口配置网络静态或动态IP地址。

### 列出Ubuntu上的所有活动网络接口

首先，您需要确定要配置的网络接口。 您可以使用[ifconfig命令](https://www.howtoing.com/ifconfig-command-examples/)列出系统中所有连接的网络接口，如图所示。

```
$ ifconfig -a
```

检查Ubuntu中的网络接口

从上述命令的输出中，我们有**3个**连接到Ubuntu系统的**接口** ： **2个以太网接口**和**环回接口** 。 但是， `enp0s8`以太网接口尚未配置，并且没有静态IP地址。

### 在Ubuntu 18.04中设置静态IP地址

在这个例子中，我们将为`enp0s8`以太网网络接口配置一个静态IP。 如图所示，使用文本编辑器打开netplan配置文件。

**重要提示** ：如果**YAML**文件不是由发行版安装程序创建的，则可以使用此命令为渲染器生成所需的配置。

```
$ sudo netplan generate 
```

另外，自动生成的文件可能在桌面，服务器，云实例等（例如**01-network-manager-all.yaml**或**01-netcfg.yaml** ）上有不同的文件名，但是**/etc/netplan/\*.yaml**下的所有文件将被netplan读取。

```
$ sudo vim /etc/netplan/01-netcfg.yaml 
```

然后在`ethernet`部分下添加以下配置。

```
enp0s8:				
dhcp4: no
dhcp6: no
addresses: [192.168.56.110/24, ]
gateway4:  192.168.56.1
nameservers:
addresses: [8.8.8.8, 8.8.4.4]
```

哪里：

- **enp0s8** - 网络接口名称。
- **dhcp4**和**dhcp6** - 接受IPv4和IPv6接口的dhcp属性。
- **地址** - 接口的静态地址序列。
- **gateway4** - 默认网关的IPv4地址。
- **Nameservers** - **Nameservers**的IP地址序列。

添加完成后，您的配置文件现在应该具有以下内容，如以下屏幕截图所示。 第一个接口`enp0s3`配置为使用**DHCP** ， `enp0s8`将使用静态IP地址。

接口的地址属性期望有一个序列条目，例如**[192.168.14.2/24，“2001：1 :: 1/64”]**或**[192.168.56.110/24，]** （有关更多信息**，**请参见**netplan手册页** ）。

```
# This file describes the network interfaces available on your system
# For more information, see netplan(5).
network:
version: 2
renderer: networkd
ethernets:
enp0s3:
dhcp4: yes
enp0s8:
dhcp4: no
dhcp6: no
addresses: [192.168.56.110/24, ]
gateway4:  192.168.56.1
nameservers:
addresses: [8.8.8.8, 8.8.4.4]
```

在Ubuntu中配置静态IP

保存该文件并退出。 然后使用以下**netplan**命令应用最近的网络更改。

```
$ sudo netplan apply
```

现在再次验证所有可用的网络接口， `enp0s8`以太网接口现在应连接到本地网络，并具有IP地址

```
$ ifconfig -a
```

在Ubuntu中验证网络接口

### 在Ubuntu中设置动态DHCP IP地址

要将`enp0s8`以太网接口配置为通过DHCP动态接收IP地址，只需使用以下配置即可。

```
# This file describes the network interfaces available on your system
# For more information, see netplan(5).
network:
version: 2
renderer: networkd
ethernets:
enp0s8:
dhcp4: yes
dhcp6: yes
```

保存该文件并退出。 然后应用最近的网络更改并使用以下命令验证IP地址。

```
$ sudo netplan apply
$ ifconfig -a
```

从现在起，您的系统将从路由器动态获取IP地址。

你可以通过查看netplan手册页找到更多信息和配置选项。

```
$ man netplan
```

恭喜！ 您已成功将网络静态IP地址配置到您的Ubuntu服务器。 如果您有任何疑问，请通过下面的评论表单与我们分享。

# [Ubuntu18.04的网络配置（静态IP和动态IP）](https://www.cnblogs.com/opsprobe/p/9979234.html)

## 查看Ubuntu系统的版本号命令

cat /etc/issue 或者 lsb_release -a

## 切换root命令

sudo -i 或者 sudo -s

**提示：以下操作均在root用户下进行，如在普通用户，请自行加上sudo！**

## 说明

Ubuntu从17.10开始，已放弃在/etc/network/interfaces里配置IP地址，即使配置也不会生效，而是改成netplan方式，配置写在/etc/netplan/01-netcfg.yaml或者类似名称的yaml文件里，如下：

VMware14里安装的Ubuntu18.04.1 Desktop版本下的配置文件名：

![img](images\1404518-20200614223934337-1576886527.png)

VMware14里安装的Ubuntu18.04.4 Server版本下的配置文件名：

![img](images\1404518-20200614224306528-1449186048.png)

阿里云Ubuntu18.04.4 Server版本下的配置文件名：

![img](images\1404518-20200614224537679-1678462440.png)

## 下面以VMware14里安装的Ubuntu 18.04.4 Server版本为例（VMware网络连接选择的桥接模式）

## 一、配置静态IP地址

打开配置文件：vim /etc/netplan/50-cloud-init.yaml，写入以下配置内容：

```
network:
    ethernets:
        ens33:                  # 配置的网卡名称
            dhcp4: no           # 关闭dhcp4
            dhcp6: no           # 关闭dhcp6
            addresses: [192.168.0.120/24]       # 设置本机IP地址及掩码
            gateway4: 192.168.0.1               # 设置网关
            nameservers:
                    addresses: [114.114.114.114, 8.8.8.8]       # 设置DNS
    version: 2
```

截图

![img](images\1404518-20200614231300863-237073454.png)

配置完成后，保存并退出，执行 netplan apply 命令可以让配置直接生效

以前的重启网络服务命令 /etc/init.d/networking restart 或者 service networking restart 都是无法使用的（做测试时发现18.04.1的Desktop版本还是可以使用的，但/etc/netplan/下的yaml配置文件并不会生效）。

## 验证是否配置成功

ifconfig -a

![img](images\1404518-20200614222201955-990276377.png)

## 验证是否能ping通外网

ping -c 4 baidu.com

![img](images\1404518-20200614222251773-819407962.png)

## 二、配置动态IP地址

打开配置文件：vim /etc/netplan/50-cloud-init.yaml，写入以下配置内容（其实只需要开启dhcp就可以）：

![img](images\1404518-20200614230042002-1549179355.png)

保存并退出，执行 netplan apply 命令让配置生效，用上述方法验证是否配置成功！

 

这里顺便也记录下Ubuntu 18.04.1 Desktop版本的配置，和18.04.4 Server版本略有区别（VMware网络连接选择的也是桥接模式）

vim /etc/netplan/01-network-manager-all.yaml

```
network:
  version: 2
  # renderer: NetworkManager
  ethernets:
          ens33:
                  dhcp4: no
                  dhcp6: no
                  addresses: [192.168.0.130/24]
                  gateway4: 192.168.0.1
                  nameservers:
                          addresses: [114.114.114.144, 8.8.8.8]
```

截图

![img](images\1404518-20200615081736202-1829516241.png)

## 这里有几点需要注意：

1、Ubuntu 18.04.1 Desktop版本配置的时候需要将renderer: NetworkManager一行注释掉，否则netplan命令无法生效；

2、配置信息要严格按照yaml语言的语法格式，每个配置项使用空格缩进表示层级关系；缩进不允许使用tab，只允许空格；缩进的空格数不重要，只要相同层级的元素左对齐即可，否则netplan命令会报错；

3、对应配置项后跟着冒号，之后要接个空格，否则netplan命令也会报错。

## 扩展

重新启停以太网卡命令：

ifconfig ens33 down

ifconfig ens33 up

 