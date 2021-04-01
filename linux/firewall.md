# Centos中iptables和firewall防火墙开启、关闭、查看状态、基本设置等

## iptables防火墙

### 1、基本操作

```shell
# 查看防火墙状态
service iptables status  
# 停止防火墙
service iptables stop  
# 启动防火墙
service iptables start  
# 重启防火墙
service iptables restart
  
# 永久关闭防火墙
chkconfig iptables off  
# 永久关闭后重启
chkconfig iptables on
```

### 2、开启80端口

```shell
vim /etc/sysconfig/iptables
# 加入如下代码-A INPUT -m state --state NEW -m tcp -p tcp --dport 80 -j ACCEPT
```

保存退出后重启防火墙

```shell
service iptables restart
```

## firewall防火墙

### 1、查看firewall服务状态

```shell
systemctl status firewalld
```

### 2、查看firewall的状态

```shell
firewall-cmd --state
```

### 3、开启、重启、关闭、firewalld.service服务

```shell
# 开启service firewalld start# 重启service firewalld restart# 关闭service firewalld stop
```

### 4、查看防火墙规则

```shell
firewall-cmd --list-all 
```

### 5、查询、开放、关闭端口

```shell

# 查询端口是否开放
firewall-cmd --query-port=8080/tcp
# 开放80端口
firewall-cmd --permanent --add-port=80/tcp
# 移除端口
firewall-cmd --permanent --remove-port=8080/tcp
 
#重启防火墙(修改配置后要重启防火墙)
firewall-cmd --reload
# 参数解释
1、firwall-cmd：是Linux提供的操作firewall的一个工具；
2、--permanent：表示设置为持久；
3、--add-port：标识添加的端口；

```

# Ubuntu 防火墙

```shell
ubuntu 9.10默认的是UFW防火墙，已经支持界面操作了。在命令行运行ufw命令就可以看到提示的一系列可进行的操作。
最简单的一个操作：sudo ufw status可检查防火墙的状态，我的返回的是：不活动

sudo ufw version防火墙版本： 
ufw 0.29-4ubuntu1 
Copyright 2008-2009 Canonical Ltd.

ubuntu 系统默认已安装ufw.

1.安装

sudo apt-get install ufw

2.启用

sudo ufw enable

sudo ufw default deny

运行以上两条命令后，开启了防火墙，并在系统启动时自动开启。关闭所有外部对本机的访问，但本机访问外部正常。

3.开启/禁用

sudo ufw allow|deny [service]

打开或关闭某个端口，例如：

sudo ufw allow smtp　允许所有的外部IP访问本机的25/tcp (smtp)端口

sudo ufw allow 22/tcp 允许所有的外部IP访问本机的22/tcp (ssh)端口

sudo ufw allow 53 允许外部访问53端口(tcp/udp)

sudo ufw allow from 192.168.1.100 允许此IP访问所有的本机端口

sudo ufw allow proto udp 192.168.0.1 port 53 to 192.168.0.2 port 53

sudo ufw deny smtp 禁止外部访问smtp服务

sudo ufw delete allow smtp 删除上面建立的某条规则

4.查看防火墙状态

sudo ufw status

一般用户，只需如下设置：

sudo apt-get install ufw

sudo ufw enable

sudo ufw default deny

以上三条命令已经足够安全了，如果你需要开放某些服务，再使用sudo ufw allow开启。

开启/关闭防火墙 (默认设置是’disable’)

sudo ufw enable|disable

转换日志状态

sudo ufw logging on|off

设置默认策略 (比如 “mostly open” vs “mostly closed”)

sudo ufw default allow|deny

许 可或者屏蔽端口 (可以在“status” 中查看到服务列表)。可以用“协议：端口”的方式指定一个存在于/etc/services中的服务名称，也可以通过包的meta-data。 ‘allow’ 参数将把条目加入 /etc/ufw/maps ，而 ‘deny’ 则相反。基本语法如下：

sudo ufw allow|deny [service]

显示防火墙和端口的侦听状态，参见 /var/lib/ufw/maps。括号中的数字将不会被显示出来。

sudo ufw status

UFW 使用范例：

允许 53 端口

$ sudo ufw allow 53

禁用 53 端口

$ sudo ufw delete allow 53

允许 80 端口

$ sudo ufw allow 80/tcp

禁用 80 端口

$ sudo ufw delete allow 80/tcp

允许 smtp 端口

$ sudo ufw allow smtp

删除 smtp 端口的许可

$ sudo ufw delete allow smtp

允许某特定 IP

$ sudo ufw allow from 192.168.254.254

删除上面的规则

$ sudo ufw delete allow from 192.168.254.254

Linux 2.4内核以后提供了一个非常优秀的防火墙工具：netfilter/iptables,他免费且功能强大，可以对流入、流出的信息进行细化控制，它可以 实现防火墙、NAT（网络地址翻译）和数据包的分割等功能。netfilter工作在内核内部，而iptables则是让用户定义规则集的表结构。

但是iptables的规则稍微有些“复杂”，因此ubuntu提供了ufw这个设定工具，以简化iptables的某些设定，其后台仍然是 iptables。ufw 即uncomplicated firewall的简称，一些复杂的设定还是要去iptables。

ufw相关的文件和文件夹有：

/etc /ufw/：里面是一些ufw的环境设定文件，如 before.rules、after.rules、sysctl.conf、ufw.conf，及 for ip6 的 before6.rule 及 after6.rules。这些文件一般按照默认的设置进行就ok。

若开启ufw之 后，/etc/ufw/sysctl.conf会覆盖默认的/etc/sysctl.conf文件，若你原来的/etc/sysctl.conf做了修 改，启动ufw后，若/etc/ufw/sysctl.conf中有新赋值，则会覆盖/etc/sysctl.conf的，否则还以/etc /sysctl.conf为准。当然你可以通过修改/etc/default/ufw中的“IPT_SYSCTL=”条目来设置使用哪个 sysctrl.conf.

/var/lib/ufw/user.rules 这个文件中是我们设置的一些防火墙规则，打开大概就能看明白，有时我们可以直接修改这个文件，不用使用命令来设定。修改后记得ufw reload重启ufw使得新规则生效。

下面是ufw命令行的一些示例：

ufw enable/disable:打开/关闭ufw

ufw status：查看已经定义的ufw规则

ufw default allow/deny:外来访问默认允许/拒绝

ufw allow/deny 20：允许/拒绝 访问20端口,20后可跟/tcp或/udp，表示tcp或udp封包。

ufw allow/deny servicename:ufw从/etc/services中找到对应service的端口，进行过滤。

ufw allow proto tcp from 10.0.1.0/10 to 本机ip port 25:允许自10.0.1.0/10的tcp封包访问本机的25端口。

ufw delete allow/deny 20:删除以前定义的"允许/拒绝访问20端口"的规则
```

