# aria2（命令行下载器）使用

> [aria2](https://link.jianshu.com/?t=https%3A%2F%2Faria2.github.io%2F) 是一个自由、开源、轻量级多协议和多源的命令行下载工具。它支持 HTTP/HTTPS、FTP、SFTP、 BitTorrent 和 Metalink 协议。aria2 可以通过内建的 JSON-RPC 和 XML-RPC 接口来操纵。aria2 下载文件的时候，自动验证数据块。它可以通过多个来源或者多个协议下载一个文件，并且会尝试利用你的最大下载带宽。默认情况下，所有的 Linux 发行版都包括 aria2，所以我们可以从官方库中很容易的安装。一些 GUI 下载管理器例如 [uget](https://link.jianshu.com/?t=http%3A%2F%2Fwww.2daygeek.com%2Finstall-uget-download-manager-on-ubuntu-centos-debian-fedora-mint-rhel-opensuse%2F) 使用 aria2 作为插件来提高下载速度。

**aria2特性：**

- 支持 HTTP/HTTPS GET
- 支持 HTTP 代理
- 支持 HTTP BASIC 认证
- 支持 HTTP 代理认证
- 支持 FTP （主动、被动模式）
- 通过 HTTP 代理的 FTP（GET 命令行或者隧道）
- 分段下载
- 支持 Cookie
- 可以作为守护进程运行。
- 支持使用 fast 扩展的 BitTorrent 协议
- 支持在多文件 torrent 中选择文件
- 支持 Metalink 3.0 版本（HTTP/FTP/BitTorrent）
- 限制下载、上传速度

### 1、安装

我们可以很容易的在所有的 Linux 发行版上安装 aria2 命令行下载器，例如 Debian、 Ubuntu、 Mint、 RHEL、 CentOS、 Fedora、 suse、 openSUSE、 Arch Linux、 Manjaro、 Mageia 等等……只需要输入下面的命令安装即可。对于 CentOS、 RHEL 系统，我们需要开启 [uget](https://link.jianshu.com/?t=http%3A%2F%2Fwww.2daygeek.com%2Faria2-command-line-download-utility-tool%2F) 或者 [RPMForge](https://link.jianshu.com/?t=http%3A%2F%2Fwww.2daygeek.com%2Faria2-command-line-download-utility-tool%2F) 库的支持。



```csharp
[对于 Debian、 Ubuntu 和 Mint]
$ sudo apt-get install aria2

[对于 CentOS、 RHEL、 Fedora 21 和更早些的操作系统]
# yum install aria2

[Fedora 22 和 之后的系统]
# dnf install aria2

[对于 suse 和 openSUSE]
# zypper install wget

[Mageia]
# urpmi aria2

[对于 Arch Linux]
$ sudo pacman -S aria2
```

### 2、简单使用

#### 2.1 下载单个文件

下面的命令将会从指定的 URL 中下载一个文件，并且保存在当前目录，在下载文件的过程中，我们可以看到文件的（日期、时间、下载速度和下载进度）。



```ruby
# aria2c https://download.owncloud.org/community/owncloud-9.0.0.tar.bz2
[#986c80 19MiB/21MiB(90%) CN:1 DL:3.0MiB]
03/22 09:49:13 [NOTICE] Download complete: /opt/owncloud-9.0.0.tar.bz2
Download Results:
gid   |stat|avg speed  |path/URI
======+====+===========+=======================================================
986c80|OK  |   3.0MiB/s|/opt/owncloud-9.0.0.tar.bz2
Status Legend:
(OK):download completed.
```

#### 2.2 使用不同的名字保存文件

在初始化下载的时候，我们可以使用`-o`（小写）选项在保存文件的时候使用不同的名字。这儿我们将要使用 owncloud.zip 文件名来保存文件。



```ruby
# aria2c -o owncloud.zip https://download.owncloud.org/community/owncloud-9.0.0.tar.bz2
[#d31304 16MiB/21MiB(74%) CN:1 DL:6.2MiB]
03/22 09:51:02 [NOTICE] Download complete: /opt/owncloud.zip
Download Results:
gid   |stat|avg speed  |path/URI
======+====+===========+=======================================================
d31304|OK  |   7.3MiB/s|/opt/owncloud.zip
Status Legend:
(OK):download completed.
```

#### 2.3 下载速度限制

默认情况下，aria2 会利用全部带宽来下载文件，在文件下载完成之前，我们在服务器就什么也做不了（这将会影响其他服务访问带宽）。所以在下载大文件时最好使用 `--max-download-limit` 选项来避免进一步的问题。



```ruby
# aria2c --max-download-limit=500k https://download.owncloud.org/community/owncloud-9.0.0.tar.bz2
[#7f9fbf 21MiB/21MiB(99%) CN:1 DL:466KiB]
03/22 09:54:51 [NOTICE] Download complete: /opt/owncloud-9.0.0.tar.bz2
Download Results:
gid   |stat|avg speed  |path/URI
======+====+===========+=======================================================
7f9fbf|OK  |   462KiB/s|/opt/owncloud-9.0.0.tar.bz2
Status Legend:
(OK):download completed.
```

#### 2.4 下载多个文件

下面的命令将会从指定位置下载超过一个的文件并保存到当前目录，在下载文件的过程中，我们可以看到文件的（日期、时间、下载速度和下载进度）。



```ruby
# aria2c -Z https://download.owncloud.org/community/owncloud-9.0.0.tar.bz2 ftp://ftp.gnu.org/gnu/wget/wget-1.17.tar.gz
[DL:1.7MiB][#53533c 272KiB/21MiB(1%)][#b52bb1 768KiB/3.6MiB(20%)]
03/22 10:25:54 [NOTICE] Download complete: /opt/wget-1.17.tar.gz
[#53533c 18MiB/21MiB(86%) CN:1 DL:3.2MiB]
03/22 10:25:59 [NOTICE] Download complete: /opt/owncloud-9.0.0.tar.bz2
Download Results:
gid   |stat|avg speed  |path/URI
======+====+===========+=======================================================
b52bb1|OK  |   2.8MiB/s|/opt/wget-1.17.tar.gz
53533c|OK  |   3.4MiB/s|/opt/owncloud-9.0.0.tar.bz2
Status Legend:
(OK):download completed.
```

使用 `-P` 参数来扩展下载地址：



```csharp
[11:30 sxuan@hulab ~/gatk4_practice]$ aria2c -Z -P "http://host/image{1,2,3}_{A,B,C}.png"
5da2af|ERR |       0B/s|http://host/image1_A.png%0A
3c98a4|ERR |       0B/s|http://host/image1_B.png%0A
17ba0a|ERR |       0B/s|http://host/image1_C.png%0A
e7afa3|ERR |       0B/s|http://host/image2_A.png%0A
e99fcf|ERR |       0B/s|http://host/image2_B.png%0A
1f151a|ERR |       0B/s|http://host/image2_C.png%0A
2da0f1|ERR |       0B/s|http://host/image3_A.png%0A
17b599|ERR |       0B/s|http://host/image3_B.png%0A
d9f5ad|ERR |       0B/s|http://host/image3_C.png%0A
```

#### 2.5 续传未完成的下载

当你遇到一些网络连接问题或者系统问题的时候，并将要下载一个大文件（例如： ISO 镜像文件），我建议你使用 `-c` 选项，它可以帮助我们从该状态续传未完成的下载，并且像往常一样完成。不然的话，当你再次下载，它将会初始化新的下载，并保存成一个不同的文件名（自动的在文件名后面添加 .1 ）。注意：如果出现了任何中断，aria2 使用 .aria2 后缀保存（未完成的）文件。



```ruby
# aria2c -c https://download.owncloud.org/community/owncloud-9.0.0.tar.bz2
[#db0b08 8.2MiB/21MiB(38%) CN:1 DL:3.1MiB ETA:4s]^C
03/22 10:09:26 [NOTICE] Shutdown sequence commencing... Press Ctrl-C again for emergency shutdown.
03/22 10:09:26 [NOTICE] Download GID#db0b08bf55d5908d not complete: /opt/owncloud-9.0.0.tar.bz2
Download Results:
gid   |stat|avg speed  |path/URI
======+====+===========+=======================================================
db0b08|INPR|   3.3MiB/s|/opt/owncloud-9.0.0.tar.bz2
Status Legend:
(INPR):download in-progress.
如果重新启动传输，aria2 将会恢复下载。
# aria2c -c https://download.owncloud.org/community/owncloud-9.0.0.tar.bz2
[#873d08 21MiB/21MiB(98%) CN:1 DL:2.7MiB]
03/22 10:09:57 [NOTICE] Download complete: /opt/owncloud-9.0.0.tar.bz2
Download Results:
gid   |stat|avg speed  |path/URI
======+====+===========+=======================================================
873d08|OK  |   1.9MiB/s|/opt/owncloud-9.0.0.tar.bz2
Status Legend:
(OK):download completed.
```

#### 2.6 从文件获取输入

就像 `wget` 可以从一个文件获取输入的 URL 列表来下载一样。我们需要创建一个文件，将每一个 URL 存储在单独的行中。`aria2` 命令行可以添加 `-i` 选项来执行此操作。



```ruby
# aria2c -i test-aria2.txt
[DL:3.9MiB][#b97984 192KiB/21MiB(0%)][#673c8e 2.5MiB/3.6MiB(69%)]
03/22 10:14:22 [NOTICE] Download complete: /opt/wget-1.17.tar.gz
[#b97984 19MiB/21MiB(90%) CN:1 DL:2.5MiB]
03/22 10:14:30 [NOTICE] Download complete: /opt/owncloud-9.0.0.tar.bz2
Download Results:
gid   |stat|avg speed  |path/URI
======+====+===========+=======================================================
673c8e|OK  |   4.3MiB/s|/opt/wget-1.17.tar.gz
b97984|OK  |   2.5MiB/s|/opt/owncloud-9.0.0.tar.bz2
Status Legend:
(OK):download completed.
```

### 2.7 每个主机使用两个连接来下载

默认情况，每次下载连接到一台服务器的最大数目，对于一条主机只能建立一条。我们可以通过 aria2 命令行添加 `-x2`（2 表示两个连接）来创建到每台主机的多个连接，以加快下载速度。



```ruby
# aria2c -x2 https://download.owncloud.org/community/owncloud-9.0.0.tar.bz2
[#ddd4cd 18MiB/21MiB(83%) CN:1 DL:5.0MiB]
03/22 10:16:27 [NOTICE] Download complete: /opt/owncloud-9.0.0.tar.bz2
Download Results:
gid   |stat|avg speed  |path/URI
======+====+===========+=======================================================
ddd4cd|OK  |   5.5MiB/s|/opt/owncloud-9.0.0.tar.bz2
Status Legend:
(OK):download completed.
```

#### 2.8 下载 BitTorrent 种子文件

我们可以使用 aria2 命令行直接下载一个 BitTorrent 种子文件：



```ruby
# aria2c https://torcache.net/torrent/C86F4E743253E0EBF3090CCFFCC9B56FA38451A3.torrent?title=[kat.cr]irudhi.suttru.2015.official.teaser.full.hd.1080p.pathi.team.sr
[#388321 0B/0B CN:1 DL:0B]                                                                                                                    
03/22 20:06:14 [NOTICE] Download complete: /opt/[kat.cr]irudhi.suttru.2015.official.teaser.full.hd.1080p.pathi.team.sr.torrent
03/22 20:06:14 [ERROR] Exception caught
Exception: [BtPostDownloadHandler.cc:98] errorCode=25 Could not parse BitTorrent metainfo
Download Results:
gid   |stat|avg speed  |path/URI
======+====+===========+=======================================================
388321|OK  |    11MiB/s|/opt/[kat.cr]irudhi.suttru.2015.official.teaser.full.hd.1080p.pathi.team.sr.torrent
Status Legend:
(OK):download completed.
```

#### 2.9 下载 BitTorrent 磁力链接

使用 aria2 我们也可以通过 BitTorrent 磁力链接直接下载一个种子文件：



```bash
# aria2c 'magnet:?xt=urn:btih:248D0A1CD08284299DE78D5C1ED359BB46717D8C'
```

#### 2.10 下载 BitTorrent Metalink 种子

我们也可以通过 aria2 命令行直接下载一个 Metalink 文件。



```bash
# aria2c https://curl.haxx.se/metalink.cgi?curl=tar.bz2
```

#### 2.11 从密码保护的网站下载一个文件

或者，我们也可以从一个密码保护网站下载一个文件。下面的命令行将会从一个密码保护网站中下载文件。



```bash
# aria2c --http-user=xxx --http-password=xxx https://download.owncloud.org/community/owncloud-9.0.0.tar.bz2
# aria2c --ftp-user=xxx --ftp-password=xxx ftp://ftp.gnu.org/gnu/wget/wget-1.17.tar.gz
```

#### 2.12 更多命令

使用`man aria2c`或`aria2c -h`查看更多详细参数信息。

### 3、aria2配置



```bash
## 全局设置 ## ============================================================
# 日志
#log-level=warn
#log=/PATH/.aria2/aria2.log

# 后台运行
daemon=true

# 下载位置, 默认: 当前启动位置
dir=/PATH/Downloads

# 从会话文件中读取下载任务
input-file=/PATH/.aria2/aria2.session

# 在Aria2退出时保存`错误/未完成`的下载任务到会话文件
save-session=/PATH/.aria2/aria2.session

# 定时保存会话, 0为退出时才保存, 需1.16.1以上版本, 默认:0
save-session-interval=30

# 断点续传
continue=true

# 启用磁盘缓存, 0为禁用缓存, 需1.16以上版本, 默认:16M
#disk-cache=32M

# 文件预分配方式, 能有效降低磁盘碎片, 默认:prealloc
# 预分配所需时间: none < falloc ? trunc < prealloc
# falloc和trunc则需要文件系统和内核支持
# NTFS建议使用falloc, EXT3/4建议trunc, MAC 下需要注释此项
file-allocation=none

# 客户端伪装
user-agent=netdisk;5.2.6;PC;PC-Windows;6.2.9200;WindowsBaiduYunGuanJia
referer=http://pan.baidu.com/disk/home

# 禁用IPv6, 默认:false
disable-ipv6=true

# 其他
always-resume=true
check-integrity=true

## 下载位置 ## ============================================================
# 最大同时下载任务数, 运行时可修改, 默认:5
max-concurrent-downloads=5

# 同一服务器连接数, 添加时可指定, 默认:1
max-connection-per-server=5

# 最小文件分片大小, 添加时可指定, 取值范围1M -1024M, 默认:20M
# 假定size=10M, 文件为20MiB 则使用两个来源下载; 文件为15MiB 则使用一个来源下载
min-split-size=10M

# 单个任务最大线程数, 添加时可指定, 默认:5
split=5

# 整体下载速度限制, 运行时可修改, 默认:0
#max-overall-download-limit=0

# 单个任务下载速度限制, 默认:0
#max-download-limit=0

# 整体上传速度限制, 运行时可修改, 默认:0
#max-overall-upload-limit=0

# 单个任务上传速度限制, 默认:0
#max-upload-limit=0

## RPC设置 ## ============================================================
# 启用RPC, 默认:false
enable-rpc=true

# 允许所有来源, 默认:false
rpc-allow-origin-all=true

# 允许非外部访问, 默认:false
rpc-listen-all=true

# 事件轮询方式, 取值:[epoll, kqueue, port, poll, select], 不同系统默认值不同
#event-poll=select

# RPC监听端口, 端口被占用时可以修改, 默认:6800
rpc-listen-port=6800

# 设置的RPC授权令牌, v1.18.4新增功能, 取代 --rpc-user 和 --rpc-passwd 选项
#rpc-secret=<TOKEN>

# 是否启用 RPC 服务的 SSL/TLS 加密,
# 启用加密后 RPC 服务需要使用 https 或者 wss 协议连接
#rpc-secure=true

# 在 RPC 服务中启用 SSL/TLS 加密时的证书文件,
# 使用 PEM 格式时，您必须通过 --rpc-private-key 指定私钥
#rpc-certificate=/path/to/certificate.pem

# 在 RPC 服务中启用 SSL/TLS 加密时的私钥文件
#rpc-private-key=/path/to/certificate.key

## BT/PT下载相关 ## ============================================================
# 当下载的是一个种子(以.torrent结尾)时, 自动开始BT任务, 默认:true
#follow-torrent=true

# BT监听端口, 当端口被屏蔽时使用, 默认:6881-6999
listen-port=51413

# 单个种子最大连接数, 默认:55
#bt-max-peers=55

# 打开DHT功能, PT需要禁用, 默认:true
enable-dht=false

# 打开IPv6 DHT功能, PT需要禁用
#enable-dht6=false

# DHT网络监听端口, 默认:6881-6999
#dht-listen-port=6881-6999

dht-file-path=/opt/var/aria2/dht.dat
dht-file-path6=/opt/var/aria2/dht6.dat

# 本地节点查找, PT需要禁用, 默认:false
#bt-enable-lpd=false

# 种子交换, PT需要禁用, 默认:true
enable-peer-exchange=false

# 每个种子限速, 对少种的PT很有用, 默认:50K
#bt-request-peer-speed-limit=50K

# 设置 peer id 前缀
peer-id-prefix=-TR2770-

# 当种子的分享率达到这个数时, 自动停止做种, 0为一直做种, 默认:1.0
seed-ratio=0

# 强制保存会话, 即使任务已经完成, 默认:false
# 较新的版本开启后会在任务完成后依然保留.aria2文件
#force-save=false

# BT校验相关, 默认:true
#bt-hash-check-seed=true

# 继续之前的BT任务时, 无需再次校验, 默认:false
bt-seed-unverified=true

# 保存磁力链接元数据为种子文件(.torrent文件), 默认:false
bt-save-metadata=true

bt-max-open-files=16
```

参考：
[aria2 （命令行下载器）实例](https://link.jianshu.com/?t=https%3A%2F%2Flinux.cn%2Farticle-7982-1.html)
[aria2 配置详解](https://www.jianshu.com/p/6adf79d29add)
[aria2官方文档](https://link.jianshu.com/?t=https%3A%2F%2Faria2.github.io%2Fmanual%2Fen%2Fhtml%2Findex.html)
[aria2 使用说明](https://link.jianshu.com/?t=https%3A%2F%2Fgithub.com%2Ferasin%2Fnotes%2Fblob%2Fmaster%2Flinux%2Fsoft%2Faria2.md)