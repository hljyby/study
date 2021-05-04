# Centos设置 ip_forward路由转发

工作原理： 内网主机向公网发送数据包时，由于目的主机跟源主机不在同一网段，所以数据包暂时发往内网默认网关处理，而本网段的主机对此数据包不做任何回应。由于源主机ip是私有的，禁止在公网使用，所以必须将数据包的源发送地址修改成公网上的可用ip，这就是网关收到数据包之后首先要做的工作–ip转换。然后网关再把数据包发往目的主机。目的主机收到数据包之后，只认为这是网关发送的请求，并不知道内网主机的存在，也没必要知道，目的主机处理完请求，把回应信息发还给网关。网关收到后，将目的主机发还的数据包的目的ip地址修改为发出请求的内网主机的ip地址，并将其发给内网主机。这就是网关的第二个工作–数据包的路由转发。内网的主机只要查看数据包的目的ip与发送请求的源主机ip地址相同，就会回应，这就完成了一次请求。 出于安全考虑，Linux系统默认是禁止数据包转发的。所谓转发即当主机拥有多于一块的网卡时，其中一块收到数据包，根据数据包的目的ip地址将包发往本机另一网卡，该网卡根据路由表继续发送数据包。这通常就是路由器所要实现的功能。

Centos系统缺省并没有打开IP转发功能，要确认IP转发功能的状态，可以查看/proc文件系统，使用下面命令： cat /proc/sys/net/ipv4/ip_forward 如果上述文件中的值为0,说明禁止进行IP转发；如果是1,则说明IP转发功能已经打开。 要想打开IP转发功能，可以直接修改上述文件： echo 1 > /proc/sys/net/ipv4/ip_forward 把文件的内容由0修改为1。禁用IP转发则把1改为0。 上面的命令并没有保存对IP转发配置的更改，下次系统启动时仍会使用原来的值，要想永久修改IP转发，需要修改**/etc/sysctl.conf文件，修 改下面一行的值： net.ipv4.ip_forward = 1** 修改后可以重启系统来使修改生效，也可以执行下面的命令来使修改生效： **sysctl -p /etc/sysctl.conf** 进行了上面的配置后，IP转发功能就永久使能了。

# Centos 使用arpspoof 进行arp欺骗

## 安装arpspoof

`yum -y install libICE  libSM  libXmu libpcap libnet  libXext libXext-devel libXt `

```shell
libnids RPM包地址：wget http://www.rpmfind.net/linux/epel/7/x86_64/Packages/l/libnids-1.24-6.el7.x86_64.rpm
dsniff RPM包地址：wget https://cbs.centos.org/kojifiles/packages/dsniff/2.4/0.17.b1.el7/x86_64/dsniff-2.4-0.17.b1.el7.x86_64.rpm

rpm -ivh libnids-1.24-6.el7.x86_64.rpm
rpm -ivh dsniff-2.4-0.17.b1.el7.x86_64.rpm

缺少基础包可以去 https://pkgs.org/ 搜索安装
```

