# XFTP 

- **Secure File Transfer Protocol**的缩写，安全[文件传送协议](http://baike.baidu.com/view/97055.htm)

```
cd 路径                        更改远程目录到“路径”
lcd 路径                       更改本地目录到“路径”
chgrp group path               将文件“path”的组更改为“group”
chmod mode path                将文件“path”的权限更改为“mode”
chown owner path               将文件“path”的属主更改为“owner”
exit                           退出 sftp
help                           显示这个帮助文本
get 远程路径                   下载文件
ln existingpath linkpath       符号链接远程文件
ls [选项] [路径]               显示远程目录列表
lls [选项] [路径]              显示本地目录列表
mkdir 路径                     创建远程目录
lmkdir 路径                    创建本地目录
mv oldpath newpath             移动远程文件
open [用户@]主机[:端口]        连接到远程主机
put 本地路径                   上传文件
pwd                            显示远程工作目录
lpwd                           打印本地工作目录
quit                           退出 sftp
rmdir 路径                     移除远程目录
lrmdir 路径                    移除本地目录
rm 路径                        删除远程文件
lrm 路径                       删除本地文件
symlink existingpath linkpath  符号链接远程文件
version                        显示协议版本
```

```
常用的方式
格式：sftp <host>
通过sftp连接<host>，端口为默认的22，用户为Linux当前登录用户。

格式：sftp -oPort=<port> <host>

通过sftp连接<host>，指定端口<port>，用户为Linux当前登录用户。

格式：sftp <user>@<host>

通过sftp连接<host>，端口为默认的22，指定用户<user>。

格式：sftp -oPort=<port> <user>@<host>

通过sftp连接<host>，端口为<port>，用户为<user>。
```

```python
# SFTP 进行 上传 下载操作

# 可以相对路径，也可以绝对路径
# -r 代表可迭代 和 rm -rf 的 r 一样

get 文件路径 下载到什么位置路径
put 文件路径 上传到什么位置路径

get -r 文件路径 下载到什么位置路径
put -r 文件路径/. 下载到什么位置  # 你需要在服务器上有一个和你要上传的文件夹名 一样 的文件夹 并且文件路径后面要加 ‘.’

# 我实验 在window get put 单个文件好使 文件夹不好使不知道为什么，查遍了。日！！！！！！！
# linux 互传好使
```

