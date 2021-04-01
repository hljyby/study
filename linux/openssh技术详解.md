# [OpenSSH技术详解](https://www.cnblogs.com/herui1991/p/9678417.html)

### **一、什么是Openssh**  

  OpenSSH 是 SSH （Secure SHell） 协议的免费开源实现。SSH协议族可以用来进行远程控制， 或在计算机之间传送文件。而实现此功能的传统方式，如telnet(终端仿真协议)、 rcp ftp、 rlogin、rsh都是极为不安全的，并且会使用明文传送密码。OpenSSH提供了服务端后台程序和客户端工具，用来加密远程控件和文件传输过程中的数据，并由此来代替原来的类似服务。

```shell
知识延伸：
    ssh协议有两个版本：
        v1:基于CRC-32 做MAC，不安全； （一般用于实现主机认证）
        v2:基于协议协商选择双方都支持的最安全的MAC机制
            基于DH做密钥交换，基于RSA或DSA实现身份认证，从而实现无需输入账号面膜
            客户端通过检查服务器端的主机秘钥来判断是否能够继续通信；
    认证方式：
        1、基于口令的认证
        2、基于密钥的认证
```

### **二、为什么要使用OpenSSH**

  由于传统的telne、rcp ftp等工具是明文传输数据的，对数据安全性存在很大的安全隐患，而OpenSSH可以对传输的数据进行加密从而大大提高了数据的安全性。

### **三、OpenSSH程序简介**

 1、OpenSSH的分为客户端和服务端两部分

  Clients端的配置文件：/etc/ssh/ssh_config
   Server端的配置文件：/etc/ssh/sshd_config
  Server端服务脚本：/etc/rc.d/init.d/sshd

  OpenSSH在Linux系统中默认是安装并启动的

```shell
openssh 主要的关键包有四个
openssh.x86_64                       5.3p1-104.el6   //服务端和客户端的公共组件        
openssh-askpass.x86_64               5.3p1-104.el6   //     
openssh-clients.x86_64               5.3p1-104.el6   //客户端安装包    
openssh-server.x86_64                5.3p1-104.el6   //服务端安装包
```

  openssl-clients 几个常用文件

```shell
[root@1inux ssh]# rpm -ql openssh-clients
/etc/ssh/ssh_config  //客户端配置文件
/usr/bin/scp    //远程复制文件
/usr/bin/sftp    //远程文件共享
/usr/bin/slogin
/usr/bin/ssh
/usr/bin/ssh-add
/usr/bin/ssh-agent
/usr/bin/ssh-copy-id
/usr/bin/ssh-keyscan
```

 

  openssl-server 几个常用文件

```shell
/etc/rc.d/init.d/sshd
/etc/ssh/sshd_config
/etc/sysconfig/sshd
```

 

 2、服务器端配置文件/etc/ssh/sshd_config 主要参数详解

```shell
服务端配置文件是让别人登陆时使用的
注:配置文件中使用“#”注释掉的一般就是使用默认
    #Port 22    //默认端口号，为了其安全一般要更改为其他端口
    #AddressFamily any    //说明要监听任意地址
    #ListenAddress 0.0.0.0 //监听本机所有IPV4的ip
    #ListenAddress ::        //监听本机所有的IPV6的地址
     Protocol 2   监听的协议版本
    # HostKey for protocol version 1   //说明key的协议版本
    SyslogFacility AUTHPRIV        //使用AUTHPRIV 记录日志  
    #LogLevel INFO    //log日志级别
                
                
    #Authentication:            //认证相关
    #LoginGraceTime 2m    //登陆宽限时长  默认2分钟不登录自动关闭
    #PermitRootLogin yes    //是否支持管理员直接登陆
    #StrictModes yes    //是否使用严格模式 （严格检查用户的某些相关信息）
    #MaxAuthTries 6        //最大尝试次数  （6次以后终端断开）
    #MaxSessions 10        //最大并发允许链接数 （超过 将拒绝）
    #RSAAuthentication yes    //是否支持RSA密钥认证
    #PubkeyAuthentication yes    //是否支持公钥认证
    #AuthorizedKeysFile     .ssh/authorized_keys  //默认保存口令的文件
    #PermitEmptyPasswords no        //是否支持空密码登陆
    PasswordAuthentication yes
                
    UsePAM yes //是否使用PAM 认证（ 是一种统一认证框架）
    X11Forwarding yes     //是否转发图形界面请求 (可以打开远程服务器图形界面)
    Subsystem       sftp    /usr/libexec/openssh/sftp-server  
    #UseDNS yes        //是否允许DNS反解  比较浪费时间一般更改为no
                    /etc/ssh/ssh_known_hosts  //保存已经认可主机的文件
```

 

 3、客户端配置文件/etc/ssh/ssh_config 主要参数详解

```shell
客户端配置文件时登陆别人的ssh使用的
    #Host *        //表示连接所有主机
    #Port 22        //默认连接端口
    #Cipher 3des        //加密时使用的加密机制
    #StrictHostKeyChecking ask    //严格的主机秘钥检查 即第一次连接时是否询问
```

 

### **四、客户端ssh的使用**

  1、ssh的基本语法
     ssh [OPTIONS] [user]@server [COMMAND]
           
```shell
   -l user: 以指定用户身份连接至服务器；默认使用本地用户为远程登录时的用户；
     ssh user@server
     ssh -l user server
```


```shell
[root@1inux ~]# ssh centos@172.16.66.81
The authenticity of host '172.16.66.81 (172.16.66.81)' can't be established.
RSA key fingerprint is d6:3b:33:71:32:69:7a:dd:47:c2:49:03:ec:03:a1:5e.
Are you sure you want to continue connecting (yes/no)? 
[root@1inux ~]# ssh -l centos 172.16.66.81
The authenticity of host '172.16.66.81 (172.16.66.81)' can't be established.
RSA key fingerprint is d6:3b:33:71:32:69:7a:dd:47:c2:49:03:ec:03:a1:5e.
Are you sure you want to continue connecting (yes/no)?
```




​       -p PORT：指明要连接的端口：

```shell
[root@1inux ~]# ssh -p 22 -l centos 172.16.66.81
The authenticity of host '172.16.66.81 (172.16.66.81)' can't be established.
RSA key fingerprint is d6:3b:33:71:32:69:7a:dd:47:c2:49:03:ec:03:a1:5e.
Are you sure you want to continue connecting (yes/no)?
```

​       -X ：启用X11Forwarding,即转发X界面的请求；
​       -x： 禁用；
​       -Y: 启用信任的X11Forwarding

  2、ssh 基于秘钥的认证
    2.1、ssh-keygen语法：
      ssh-keygen [OPTIONS]
       
```shell
  -t {rsa|dsa} 密钥类型 一般使用rsa
  -b # 指明密钥长度
  -f /PATH/TO/OUTPUT_KEYFILE 指明密钥文件
  -P '' ：指明加密密钥的密码，表示使用空密码
```


```shell
[root@1inux ~]# ssh-keygen -t rsa    //生成密钥对
Generating public/private rsa key pair.
Enter file in which to save the key (/root/.ssh/id_rsa): /root/.ssh/id_90  //定义保存的密钥文件名
Enter passphrase (empty for no passphrase):         //要求对生成的密钥对加密，也可以不加密  输入两次回车就OK 
Enter same passphrase again: 
Your identification has been saved in /root/.ssh/id_90.        //说明已经生成密钥
Your public key has been saved in /root/.ssh/id_90.pub.        //说明已经生成公钥
The key fingerprint is:
7a:17:b3:e7:6f:54:a1:30:23:62:7c:04:37:10:52:08 root@1inux
The key's randomart image is:
+--[ RSA 2048]----+
|   E..+==+       |
|     ..+.o.+   . |
|      . o . + . .|
|             .  .|
|        S o    . |
|       .   +  .  |
|      . . o ..   |
|       . . o  .  |
|            .o.  |
+-----------------+
[root@1inux ~]# 
[root@1inux ~]# ls .ssh/
id_90  id_90.pub  known_hosts
[root@1inux ~]# 
------------------------- 
```


也可以指明秘钥路径 及密码


```shell
[root@1inux .ssh]# ssh-keygen -t rsa -f /root/.ssh/id_rsa -P ''  //经测试 名字必须为id_rsa
Generating public/private rsa key pair.
Your identification has been saved in /root/.ssh/id_rsa.
Your public key has been saved in /root/.ssh/id_rsa.pub.
The key fingerprint is:
33:c3:f8:f3:2c:ed:88:cc:db:7a:97:5f:d0:de:ce:d9 root@1inux
The key's randomart image is:
+--[ RSA 2048]----+
|                 |
|                 |
|                 |
|       o     .   |
|      . S   . .  |
|       . +   o . |
|        o. .  o .|
|     o oo=+  . oo|
|      *+o++..  .E|
+-----------------+
[root@1inux ~]# ls .ssh/
id_rsa  id_rsa.pub  id_www  id_www.pub  known_hosts
```

​    2.2、把公钥部分复制到要登陆远程主机的特定用户（可不同于本地用户）的家目录下，追加保存至.ssh 目录中的authorized_keys文件中；


```shell
ssh-copy-id -i /PATH/TO/PUBKEY_FILE [user]@server 
//使用此命令会自动将公钥复制到目标主机指定用户的家目录下的.ssh/authorized_keys文件中

[root@1inux ~]# ssh-copy-id -i /root/.ssh/id_rsa.pub henan@172.16.66.81
henan@172.16.66.81's password: 
Now try logging into the machine, with "ssh 'henan@172.16.66.81'", and check in:
  .ssh/authorized_keys
to make sure we haven't added extra keys that you weren't expecting.
[root@1inux ~]#
```

 

​    2.3、验证：


```shell
[root@1inux .ssh]# ssh lfs@172.16.66.81
Last login: Wed Apr  8 14:31:52 2015 from 172.16.66.90
[lfs@1inux ~]$         //可以看到已经登录成功
[henan@1inux ~]$ whoami
henan
[henan@1inux ~]$ ifconfig | grep "172.16.66"
          inet addr:172.16.66.81  Bcast:172.16.255.255  Mask:255.255.0.0
```




基于密钥的命令总结

```shell
1、[root@1inux .ssh]# ssh-keygen -t rsa -f /root/.ssh/id_rsa -P '' 
2、[root@1inux ~]# ssh-copy-id -i /root/.ssh/id_rsa.pub henan@172.16.66.81
3、ssh lfs@172.16.66.81
```

 

​    2.4、通过ssh直接执行命令

```shell
[root@1inux ~]# ssh -l henan 172.16.66.81 date    //由于此用于已经基于密钥认证所以没有要求输入密码
Wed Apr  8 15:01:15 CST 2015 
```

### **五、scp远程复制工具的使用简介**

   语法：
     scp [OPTIONS] SRC...DEST
   常用选项：
     

```shell
 -r: 递归复制，复制目录及内部文件时使用；
 -p: 保存源文件元数据信息中的属主、属组及权限；
 -q: 静默模式
 -P PORT: 指明远程服务器使用的端口；
```

   两种模式：
     PUSH: scp [OPTIONS] /PATH/FROM/SOMEFILE ... user@server:/PATH/TO/DEST  

​            //复制本地文件至远程主机 （但远程目录一定要有写权限）
​     
​     PULL: SCP [OPTIONS] user@server:/PATH/FROM/SOMEFILE /PATH/TO/DEST  

​           //远程目标主机文件至本地 
eg1:复制当前主机上的/etc/ssh/sshd_config至172.16.66.90主机的/tmp/aa目录下

```shell
[root@1inux ~]# scp -p /etc/ssh/sshd_config henan@172.16.66.90:/tmp/aa    
henan@172.16.66.90's password: 
sshd_config                                                                  100% 3879     3.8KB/s   00:00    
```

 

eg2：复制远程主机/etc/fstab至当前主机当前目录下


```shell
[root@1inux ~]# ls
anaconda-ks.cfg  Documents  grub.conf           install.log         Music     Public     Videos
Desktop          Downloads  henan@172.16.66.90  install.log.syslog  Pictures  Templates
[root@1inux ~]# scp root@172.16.66.90:/etc/fstab ./
root@172.16.66.90's password: 
fstab                                                                        100%  921     0.9KB/s   00:00    
[root@1inux ~]# ls
anaconda-ks.cfg  Documents  fstab      henan@172.16.66.90  install.log.syslog  Pictures  Templates
Desktop          Downloads  grub.conf  install.log         Music               Public    Videos
```

### **六、sftp的使用**

   要使用sftp需要编辑/etc/ssh/sshd_config 开启Subsystem 即：
   Subsystem    sftp  /usr/libexec/openssh/sftp-server  

   语法：

```shell
sftp [USER]@server
```


   常用命令：put get


```shell
eg：

[root@1inux ~]# sftp root@172.16.66.90
Connecting to 172.16.66.90...
root@172.16.66.90's password:         //输入密码
sftp> help            //可以使用help查看其支持的命令
Available commands:
bye                                Quit sftp
cd path                            Change remote directory to 'path'
chgrp grp path                     Change group of file 'path' to 'grp'
chmod mode path                    Change permissions of file 'path' to 'mode'
chown own path                     Change owner of file 'path' to 'own'
df [-hi] [path]                    Display statistics for current directory or
                                   filesystem containing 'path'
exit                               Quit sftp
get [-P] remote-path [local-path]  Download file
help                               Display this help text
lcd path                           Change local directory to 'path'
lls [ls-options [path]]            Display local directory listing
lmkdir path                        Create local directory
ln oldpath newpath                 Symlink remote file
lpwd                               Print local working directory
ls [-1aflnrSt] [path]              Display remote directory listing
lumask umask                       Set local umask to 'umask'
mkdir path                         Create remote directory
progress                           Toggle display of progress meter
put [-P] local-path [remote-path]  Upload file
pwd                                Display remote working directory
quit                               Quit sftp
rename oldpath newpath             Rename remote file
rm path                            Delete remote file
rmdir path                         Remove remote directory
symlink oldpath newpath            Symlink remote file
version                            Show SFTP version
!command                           Execute 'command' in local shell
!                                  Escape to local shell
?                                  Synonym for help
====================================================================================
```



### **七、增强服务端sshd配置指南**

```shell
1、不要使用默认端口；（修改默认端口为其他端口）
      配置文件：/etc/ssh/sshd_config   
         Port 22
         service sshd restart  //修改后需要重启服务
2、不要使用v1版本协议：
     Protocol 2          
3、限制可登陆的用户 {需要添加}
   AllowUsers：允许登陆的用户白名单 (多个用户使用空格隔开)
   AllowGroups:允许登陆的组的白名单           
   DenyUsers
   DenyGroups           
   /etc/ssh/sshd_config
     
    \# service sshd reload 
    ==》 获取配置文件详细信息；【 man sshd_conifg 】
4、设定空闲会话超时时长：
5、利用防火墙设置ssh访问策略：
  限定ssh服务仅允许***服务器分配有限的地址段内的主机访问         
6、仅监听特定的IP地址：       
7、使用强密码策略：      
```
```shell
[root@1inux ssh]# tr -dc A-Za-z0-9 < /dev/urandom | head -c 30 | xargs
Qe6zOmB2sBNpEONVcKhWS8T4bVrcb0
```

```shell
8、使用基于密钥的认证；       
9、禁止使用空密码       
10、禁止root直接登陆
PermitRootLogin no 
11、限制ssh的访问频度       
12、做好日志、经常做日志分析
/var/log/secure 
```

