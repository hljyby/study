# Docker概述

## Docker为什么会出现

开发环境和上线环境不一样，项目运行很困难

- 镜像

- 容器隔离

## Docker 历史

Docker 原来叫 dotCloud 后来活不下去 开源了 叫Docker

```python
vm : linux centOS(一个电脑) 格力需要开启多个虚拟机 几个G 几分钟
docker 隔离，镜像（最核心环境 4m + jdk + mysql ）十分小巧 运行镜像就可以了 小巧 几 M kb秒级启动
```

> docker 是基于 GO 语言开发的

- 官网 https://www.docker.com/
- 文档 https://docs.docker.com/
- 中文文档 https://docker_practice.gitee.io/zh-cn/
- 仓库地址 https://hub.docker.com/

# Docker 安装

- 镜像（image）
  - docker 镜像就好比一个模板，可以通过这个模板来创建容器服务。tomcat镜像	===>run ===>nginx01(提供服务)通过这个镜像可以创建多个服务（最终服务运行或者项目运行就是在容器中的）
- 容器（container）
  - Docker 利用容器技术，独立运行一个或一组应用，通过镜像来创建的
  - 启动 停止 删除 基本命令
- 仓库（repository）
  - 存放镜像的地方
  - 仓库分为共有仓库和私有仓库
  - DockerHub （默认是国外的）
  - 阿里云...都有容器服务器（配置镜像加速！）

## 安装Docker

> 环境准备

- 需要会一些linux基础操作
- CentOS7
- 使用XShell 链接服务器进行操作

> 环境查看

```shell
# 系统内核 是3.10 以上的
[root@localhost dhcp]# uname -r
4.18.0-193.19.1.el8_2.x86_64
```

```shell
# 系统版本
[root@localhost dhcp]# cat /etc/os-release 
NAME="CentOS Linux"
VERSION="8 (Core)"
ID="centos"
ID_LIKE="rhel fedora"
VERSION_ID="8"
PLATFORM_ID="platform:el8"
PRETTY_NAME="CentOS Linux 8 (Core)"
ANSI_COLOR="0;31"
CPE_NAME="cpe:/o:centos:centos:8"
HOME_URL="https://www.centos.org/"
BUG_REPORT_URL="https://bugs.centos.org/"

CENTOS_MANTISBT_PROJECT="CentOS-8"
CENTOS_MANTISBT_PROJECT_VERSION="8"
REDHAT_SUPPORT_PRODUCT="centos"
REDHAT_SUPPORT_PRODUCT_VERSION="8"
```

```shell
# 第一步卸载 旧版docker
$ sudo yum remove docker \
                  docker-client \
                  docker-client-latest \
                  docker-common \
                  docker-latest \
                  docker-latest-logrotate \
                  docker-logrotate \
                  docker-engine
# yum clean all #清理缓存
# 第二部 需要的安装包
yum install -y yum-utils

# 第三部 设置镜像仓库
sudo yum-config-manager \
    --add-repo \
    https://download.docker.com/linux/centos/docker-ce.repo #默认国外
sudo yum-config-manager \
    --add-repo \
    http://mirrors.aliyun.com/docker-ce/linux/centos/docker-ce.repo
# 更新软件包索引
# centos7
sudo yum makecache fast
	# centos 8
	# sudo yum makecache
# 第四部 docker-ce 社区版 ee 企业版
sudo yum install docker-ce docker-ce-cli containerd.io
# centos 8先安装下面这个在安装上面的命令
# dnf -y install http://mirrors.aliyun.com/docker-ce/linux/centos/8/x86_64/stable/Packages/containerd.io-1.4.3-3.1.el8.x86_64.rpm

# 第五步 启动Docker
sudo systemctl start docker

# 第六步 使用docker version 查看是否安装成功

# 第七步 启动docker
docker run hellow-world

```

```shell
# 运行第七步出现以下错误
Get https://registry-1.docker.io/v2/library/hello-world/manifests/latest: net/http: TLS handshake timeout

或

Get https://registry-1.docker.io/v2/: net/http: request canceled while waiting for connection (Client.Timeout exceeded while awaiting headers).
See 'docker run --help'.

 

解决办法

　　在 vim /etc/docker/daemon.json 添加镜像

　　{"registry-mirrors":["https://registry.docker-cn.com","https://pee6w651.mirror.aliyuncs.com"]}

　　https://registry.docker-cn.com --------> 国内docker官方中国区

　　https://pee6w651.mirror.aliyuncs.com ---------> 阿里云镜像
```

```shell
# 第八步 查看一下下载的hello world image
docker images
[root@localhost yum.repos.d]# docker images
REPOSITORY    TAG       IMAGE ID       CREATED         SIZE
hello-world   latest    bf756fb1ae65   12 months ago   13.3kB

```

```shell
# 卸载Docker
$ sudo yum remove docker-ce docker-ce-cli containerd.io
$ sudo rm -rf /var/lib/docker

```

## 阿里云镜像加速

```
1、登录阿里云找到容器服务

sudo mkdir -p /etc/docker
sudo tee /etc/docker/daemon.json <<-'EOF'
{
  "registry-mirrors": ["https://jl1trdp4.mirror.aliyuncs.com"]
}
EOF
sudo systemctl daemon-reload
sudo systemctl restart docker

```



## 底层原理

### Docker 是怎么工作的 

```python
Docker 是一个 Client-Server结构的系统，Docker 的守护进程运行在主机上，通过Socket客户端访问！
DockerServer 接收到客户端的指令，就会执行这个命令 
```

Docker 为什么会比虚拟机快 

```python
1、Docker 有着比虚拟机更少的抽象层。
2、Docker 用的是宿主机的内核，vm 需要 Guest OS
所以说新建一容器的时候，Docker不需要像虚拟机一样重新加载一个操作系统，避免引导，虚拟机施加在Guest OS ，分钟级别的
而Docker是利用宿主机的操作系统，省略了这个复杂的过程，秒级的。
之后在学习完所有的命令，在回过头来看这段理论，右脑会非常的清晰
```



# Docker 命令

## 帮助命令

```python
docker version # 显示Docker 的版本信息
docker info # 显示Docker的系统信息，包括镜像和容器信息
docker 命令 --help

帮助文档的地址
https://docs.docker.com/reference/
```



## 镜像命令

**docker images** 查看所有本地主机上的镜像

```shell
[root@localhost ~]# docker images
REPOSITORY    TAG       IMAGE ID       CREATED         SIZE
hello-world   latest    bf756fb1ae65   12 months ago   13.3kB

# 解释
REPOSITORY	仓库源 / 镜像的名字
TAG 		镜像的标签
IMAGE ID 镜像的id
CREATED 镜像的创建时间
SIZE 镜像的大小

# 可选项
Options:
  -a, --all             # 列出所有镜像
  -q, --quiet           # 只显示镜像id

```

**docker search **搜索镜像

```shell
[root@localhost ~]# docker search mysql
NAME                 DESCRIPTION                                   STARS     OFFICIAL   AUTOMATED
mysql              MySQL is a widely used, open-source relation…   10380     [OK]       
mariadb            MariaDB is a community-developed fork of MyS…   3848      [OK] 

# 可选项 通过收藏来过滤 
Options:
  -f, --filter filter   Filter output based on conditions provided
--filter=STARS=3000 搜索出来的镜像就是stars大于3000的
```

**docker pull** 拉取镜像

```shell
# 下载镜像 docker pull 镜像名[:tag]
[root@localhost ~]# docker pull mysql
Using default tag: latest # 如果不写tag 默认latest
latest: Pulling from library/mysql
a076a628af6f: Pull complete # 分层下载，docker image的核心 联合文件系统
f6c208f3f991: Pull complete 
88a9455a9165: Pull complete 
406c9b8427c6: Pull complete 
7c88599c0b25: Pull complete 
25b5c6debdaf: Pull complete 
43a5816f1617: Pull complete 
1a8c919e89bf: Pull complete 
9f3cf4bd1a07: Pull complete 
80539cea118d: Pull complete 
201b3cad54ce: Pull complete 
944ba37e1c06: Pull complete 
Digest: sha256:feada149cb8ff54eade1336da7c1d080c4a1c7ed82b5e320efb5beebed85ae8c # 签名
Status: Downloaded newer image for mysql:latest
docker.io/library/mysql:latest # 真实地址

# 等价于它
docker pull mysql
docker pull docker.io/library/mysql:latest

# 指定版本下载
docker pull mysql:5.7
```

**docker rei** 删除镜像

```shell
[root@localhost ~]# docker rmi -f 镜像id  # 删除指定的镜像
[root@localhost ~]# docker rmi -f 镜像id 镜像id 镜像id 镜像id  # 删除多个镜像

[root@localhost ~]# docker rmi -f $(docker images -aq) # 删除全部的镜像

Options:
  -f,  # 强制
```



## 容器命令

**说明：我们有了镜像才可以创建容器，linux，下载一个centos镜像 来测试学习**

`docker pull centos`

**新建容器并启动**

 ```shell
docker run [可选参数] image

# 参数说明
--name="name"	 # 容器名字 nginx01 nginx02 用来区分容器
-d 				# 后台方式运行
-it 			# 使用 交互方式运行，进入容器查看内容
-p 				# 指定容器端口 -p 8080:8080
	-p ip:主机端口:容器端口
	-p 主机端口:容器端口 （常用）
	-p 容器端口
	容器端口
-P				# 随机指定端口

# 测试 启动并进入容器
[root@localhost ~]# docker run -it centos /bin/bash
[root@17ae30f2ce0c /]# 
[root@17ae30f2ce0c /]# ls # 查看容器内的centos,基础版本很多命令都是不完善的
bin  dev  etc  home  lib  lib64  lost+found  media  mnt  opt  proc  root  run  sbin  srv  sys  tmp  usr  var

# 从容器中退到主机
[root@17ae30f2ce0c /]# exit # 退出容器的命令
exit

 ```

**列出所有运行中的容器**

 ```shell
# docker ps 命令
	 # 列出当前正在运行的容器
-a 	 # 列出当前正在运行的容器 + 带出历史运行的容器
-n=? # 显示最近创建的容器
[root@localhost ~]# docker ps -a -n=1
CONTAINER ID   IMAGE     COMMAND       CREATED          STATUS                      PORTS     NAMES
17ae30f2ce0c   centos    "/bin/bash"   13 minutes ago   Exited (0) 10 minutes ago      eager_gates
-q # 只显示容器的编号
[root@localhost ~]#  docker ps -qa
17ae30f2ce0c
c85c1354d051

[root@localhost ~]#    docker ps -a
CONTAINER ID   IMAGE          COMMAND       CREATED          STATUS                     PORTS     NAMES
17ae30f2ce0c   centos         "/bin/bash"   10 minutes ago   Exited (0) 7 minutes ago             eager_gates
c85c1354d051   bf756fb1ae65   "/hello"      22 hours ago     Exited (0) 22 hours ago              sad_cannon

 ```

**退出容器**

```shell
exit # 直接容器停止并退出
Ctrl + P + Q # 容器不停止退出 
```

**删除容器**

```shell
docker rm 容器id # 删除一个容器 不能删除正在运行的容器 强制删除 + -f
docker rm $(docker ps -aq) # 全部容器
docker ps -aq | xargs docker rm
```

**启动和停止容器的操作**

```shell
docker start 容器id		# 启动容器
docker restart 容器id		# 重启容器
docker stop 容器id		# 停止正在运行的容器
docker kill 容器id		# 强制停止当前的容器
```

## 常用的其他命令

**后台启动容器**

```shell
# 命令 docker run -d 镜像名
[root@localhost ~]# docker run -d centos
518fbfd0af374cfd0c9891b65f9b2c362f2b9e85152b44cfb86502cc42218238

# 问题docker ps 发现 centos 停止了

#  常见的坑，docker 容器使用后台运行，就必须有一个前台进程，docker发现没有应用，就会自动停止
# nginx ,容器启动后，发现自己没有提供服务，就会立刻停止，就是没有程序了
```

**查看日志**

```shell
docker logs -f -t --tail [tail 条数] 容器id # 没有日志

# 自己编写一段shell 脚本
docker run -d centos /bin/bash -c "while true;do echo yby;sleep 1;done"

# [root@localhost ~]# docker ps
CONTAINER ID   IMAGE     COMMAND                  CREATED         STATUS         PORTS     NAMES
b395791b8b60   centos    "/bin/bash -c 'while…"   3 seconds ago   Up 2 seconds             pensive_einstein

# 显示日志
-tf		    # 显示所有的 t 时间戳
--tail num	# 要显示的条数
docker logs -f -t --tail 10 容器id
```

**查看容器的进程信息**

```shell
# 命令 docker top 容器id
[root@localhost ~]# docker top b395791b8b60
UID                 PID                 PPID                C                   STIME               
root                453588              453568              0                   02:02               
root                454586              453588              0                   02:10               
 
```

**查看镜像的元数据**

```shell
# 命令
docker inspect 容器id

# 测试
[root@localhost ~]# docker inspect b395791b8b60
[
    {
        "Id": "b395791b8b605a688c5d6a1b49dcbd229101bb073cdbfd1428b213380cd54052",
        "Created": "2021-01-20T07:02:55.926022238Z",
        "Path": "/bin/bash",
        "Args": [
            "-c",
            "while true;do echo yby;sleep 1;done"
        ],
        "State": {
            "Status": "running",
            "Running": true,
            "Paused": false,
            "Restarting": false,
            "OOMKilled": false,
            "Dead": false,
            "Pid": 453588,
            "ExitCode": 0,
            "Error": "",
            "StartedAt": "2021-01-20T07:02:56.727109228Z",
            "FinishedAt": "0001-01-01T00:00:00Z"
        },
        "Image": "sha256:300e315adb2f96afe5f0b2780b87f28ae95231fe3bdd1e16b9ba606307728f55",
        "ResolvConfPath": "/var/lib/docker/containers/b395791b8b605a688c5d6a1b49dcbd229101bb073cdbfd1428b213380cd54052/resolv.conf",
        "HostnamePath": "/var/lib/docker/containers/b395791b8b605a688c5d6a1b49dcbd229101bb073cdbfd1428b213380cd54052/hostname",
        "HostsPath": "/var/lib/docker/containers/b395791b8b605a688c5d6a1b49dcbd229101bb073cdbfd1428b213380cd54052/hosts",
        "LogPath": "/var/lib/docker/containers/b395791b8b605a688c5d6a1b49dcbd229101bb073cdbfd1428b213380cd54052/b395791b8b605a688c5d6a1b49dcbd229101bb073cdbfd1428b213380cd54052-json.log",
        "Name": "/pensive_einstein",
        "RestartCount": 0,
        "Driver": "overlay2",
        "Platform": "linux",
        "MountLabel": "",
        "ProcessLabel": "",
        "AppArmorProfile": "",
        "ExecIDs": null,
        "HostConfig": {
            "Binds": null,
            "ContainerIDFile": "",
            "LogConfig": {
                "Type": "json-file",
                "Config": {}
            },
            "NetworkMode": "default",
            "PortBindings": {},
            "RestartPolicy": {
                "Name": "no",
                "MaximumRetryCount": 0
            },
            "AutoRemove": false,
            "VolumeDriver": "",
            "VolumesFrom": null,
            "CapAdd": null,
            "CapDrop": null,
            "CgroupnsMode": "host",
            "Dns": [],
            "DnsOptions": [],
            "DnsSearch": [],
            "ExtraHosts": null,
            "GroupAdd": null,
            "IpcMode": "private",
            "Cgroup": "",
            "Links": null,
            "OomScoreAdj": 0,
            "PidMode": "",
            "Privileged": false,
            "PublishAllPorts": false,
            "ReadonlyRootfs": false,
            "SecurityOpt": null,
            "UTSMode": "",
            "UsernsMode": "",
            "ShmSize": 67108864,
            "Runtime": "runc",
            "ConsoleSize": [
                0,
                0
            ],
            "Isolation": "",
            "CpuShares": 0,
            "Memory": 0,
            "NanoCpus": 0,
            "CgroupParent": "",
            "BlkioWeight": 0,
            "BlkioWeightDevice": [],
            "BlkioDeviceReadBps": null,
            "BlkioDeviceWriteBps": null,
            "BlkioDeviceReadIOps": null,
            "BlkioDeviceWriteIOps": null,
            "CpuPeriod": 0,
            "CpuQuota": 0,
            "CpuRealtimePeriod": 0,
            "CpuRealtimeRuntime": 0,
            "CpusetCpus": "",
            "CpusetMems": "",
            "Devices": [],
            "DeviceCgroupRules": null,
            "DeviceRequests": null,
            "KernelMemory": 0,
            "KernelMemoryTCP": 0,
            "MemoryReservation": 0,
            "MemorySwap": 0,
            "MemorySwappiness": null,
            "OomKillDisable": false,
            "PidsLimit": null,
            "Ulimits": null,
            "CpuCount": 0,
            "CpuPercent": 0,
            "IOMaximumIOps": 0,
            "IOMaximumBandwidth": 0,
            "MaskedPaths": [
                "/proc/asound",
                "/proc/acpi",
                "/proc/kcore",
                "/proc/keys",
                "/proc/latency_stats",
                "/proc/timer_list",
                "/proc/timer_stats",
                "/proc/sched_debug",
                "/proc/scsi",
                "/sys/firmware"
            ],
            "ReadonlyPaths": [
                "/proc/bus",
                "/proc/fs",
                "/proc/irq",
                "/proc/sys",
                "/proc/sysrq-trigger"
            ]
        },
        "GraphDriver": {
            "Data": {
                "LowerDir": "/var/lib/docker/overlay2/8d01a95fa3be2a4625f51395b4c9d534c09f77d239967124fae2f137816ac104-init/diff:/var/lib/docker/overlay2/9877dc70e3ac36bd8d23682edd34abdc3bed3a08056736618fe0cfbd5d5cd017/diff",
                "MergedDir": "/var/lib/docker/overlay2/8d01a95fa3be2a4625f51395b4c9d534c09f77d239967124fae2f137816ac104/merged",
                "UpperDir": "/var/lib/docker/overlay2/8d01a95fa3be2a4625f51395b4c9d534c09f77d239967124fae2f137816ac104/diff",
                "WorkDir": "/var/lib/docker/overlay2/8d01a95fa3be2a4625f51395b4c9d534c09f77d239967124fae2f137816ac104/work"
            },
            "Name": "overlay2"
        },
        "Mounts": [],
        "Config": {
            "Hostname": "b395791b8b60",
            "Domainname": "",
            "User": "",
            "AttachStdin": false,
            "AttachStdout": false,
            "AttachStderr": false,
            "Tty": false,
            "OpenStdin": false,
            "StdinOnce": false,
            "Env": [
                "PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin"
            ],
            "Cmd": [
                "/bin/bash",
                "-c",
                "while true;do echo yby;sleep 1;done"
            ],
            "Image": "centos",
            "Volumes": null,
            "WorkingDir": "",
            "Entrypoint": null,
            "OnBuild": null,
            "Labels": {
                "org.label-schema.build-date": "20201204",
                "org.label-schema.license": "GPLv2",
                "org.label-schema.name": "CentOS Base Image",
                "org.label-schema.schema-version": "1.0",
                "org.label-schema.vendor": "CentOS"
            }
        },
        "NetworkSettings": {
            "Bridge": "",
            "SandboxID": "c3f60843c72627cad9943908ca807e45079de7e62075a29592c1c98fb1eb0cf2",
            "HairpinMode": false,
            "LinkLocalIPv6Address": "",
            "LinkLocalIPv6PrefixLen": 0,
            "Ports": {},
            "SandboxKey": "/var/run/docker/netns/c3f60843c726",
            "SecondaryIPAddresses": null,
            "SecondaryIPv6Addresses": null,
            "EndpointID": "1eb5b9a8d0f2e7e36ec54fdc4d00dc6adef9b6b9bdf3caf36e165eb6902c7aed",
            "Gateway": "172.17.0.1",
            "GlobalIPv6Address": "",
            "GlobalIPv6PrefixLen": 0,
            "IPAddress": "172.17.0.2",
            "IPPrefixLen": 16,
            "IPv6Gateway": "",
            "MacAddress": "02:42:ac:11:00:02",
            "Networks": {
                "bridge": {
                    "IPAMConfig": null,
                    "Links": null,
                    "Aliases": null,
                    "NetworkID": "65cd8a5c21209090ade742fd62eef3d96d152446cea544d7001ee71d653e8668",
                    "EndpointID": "1eb5b9a8d0f2e7e36ec54fdc4d00dc6adef9b6b9bdf3caf36e165eb6902c7aed",
                    "Gateway": "172.17.0.1",
                    "IPAddress": "172.17.0.2",
                    "IPPrefixLen": 16,
                    "IPv6Gateway": "",
                    "GlobalIPv6Address": "",
                    "GlobalIPv6PrefixLen": 0,
                    "MacAddress": "02:42:ac:11:00:02",
                    "DriverOpts": null
                }
            }
        }
    }
]

```

**进入当前运行的容器**

```shell
# 我们通常容器 都是使用后台方式运行的，需要进入容器，修改一些配置

# 命令
docker exec -it 容器id baskshell
 
# 测试
[root@localhost ~]# docker ps
CONTAINER ID   IMAGE     COMMAND                  CREATED          STATUS          PORTS     NAMES
b395791b8b60   centos    "/bin/bash -c 'while…"   33 minutes ago   Up 33 minutes             pensive_einstein
[root@localhost ~]# docker exec -it b395791b8b60 /bin/bash
[root@b395791b8b60 /]# ls
bin  dev  etc  home  lib  lib64  lost+found  media  mnt  opt  proc  root  run  sbin  srv  sys  tmp  usr  var
[root@b395791b8b60 /]# ps -ef
UID          PID    PPID  C STIME TTY          TIME CMD
root           1       0  0 07:02 ?        00:00:01 /bin/bash -c while true;do echo yby;sleep 1;done
root        2022       0  0 07:36 pts/0    00:00:00 /bin/bash
root        2091       1  0 07:37 ?        00:00:00 /usr/bin/coreutils --coreutils-prog-shebang=sleep /usr/bin/sleep 1
root        2092    2022  0 07:37 pts/0    00:00:00 ps -ef

 # 方式二
 docker attach 容器id
 # 测试
 [root@localhost ~]# docker attach b395791b8b60
 正在执行当前的代码
 
 # docker exec 		# 进入容器后开启一个新的终端，可以在里面操作（常用）
 # docker attach 	# 进入容器正在执行的终端，不会启动新的进程

```

**从容器内拷贝到主机上面**

```shell
docker cp 容器id:容器内路径 目的的主机路径

# 进入当前容器内部
[root@localhost home]# docker ps
CONTAINER ID   IMAGE     COMMAND       CREATED          STATUS         PORTS     NAMES
4861017630f5   centos    "/bin/bash"   21 minutes ago   Up 4 seconds             zen_blackwell
[root@localhost home]# docker attach 4861017630f5
[root@4861017630f5 /]# ls
bin  dev  etc  home  lib  lib64  lost+found  media  mnt  opt  proc  root  run  sbin  srv  sys  tmp  usr  var
[root@4861017630f5 /]# cd home
# 在容器内新建一个文件
[root@4861017630f5 home]# touch test.js
[root@4861017630f5 home]# ls
test.js
[root@4861017630f5 home]# exit
exit
[root@localhost home]# ls
www  yby  yby2  yby.py

# 将这个文件拷贝到主机上
[root@localhost home]# docker cp 4861017630f5:/home/test.js /home
[root@localhost home]# ls
test.js  www  yby  yby2  yby.py

# 拷贝是一个手动过程 未来我们是用-v 卷的技术可以实现
```

## 小结

```shell
attach 			# 当前shell 下attach 链接指定运行镜像
build			# 通过Dockerfile定制镜像
commit 			# 提交当前容器为新镜像
cp				# 从容器中拷贝指定文件或目录到宿主机中
create			# 创建一个新容器，同run但不启动容器
diff			# 查看docker 容器变化
events			# 从docker服务器获取容器实时事件
exec			# 在已存在的容器上运行命令
export			# 导出容器的内容流作为一个tar归档文件[对应import]
history 		# 展示一个镜像形成历史
images 			# 列出系统当前镜像
import 			# 从tar包中的内容创建一个新的文件系统映像[对应export]
info 			# 显示系统相关信息
inspect			# 查看容器详情信息
kill			# kill指定Docker容器
load			# 从一个tar包中加载一个镜像[对应save]
login			# 注册或登录一个Docker源服务器
logout			# 从当前Docker	 reshistry 退出
logs			# 输出当前容器日志信息
port 			# 查看映射端口对应的容器内部源端口
pause			# 暂停容器
ps				# 列出容器列表
pull			# 从Docker镜像源服务器拉取指定镜像或者镜像库
push			# 推送指定镜像或者库镜像 至docker源服务器
restart			# 重启运行的容器
rm				# 移除一个或多个容器
rmi				# 移除一个或多个镜像[无容器使用该镜像才可删除，否则需删除相关容器才可继续 -f 强制删除]
run				# 创建一个新容器	并运行一个命令
save			# 保存一个镜像为一个tar包[对应 load]
search			# 在docker hub 中搜索镜像
start			# 启动容器
stop			# 停止容器
tag				# 给源中镜像打标签
top				# 查看容器中运行的进程信息
unpause			# 取消暂停容器
version			# 查看docker版本号
wait			# 截取容器停止时的退出状态值
tag				# 修改镜像名
```

## 作业

**Docker 安装Nginx**

```shell
docker search nginx
docker pull nginx
docker images
docker run -d --name nginx01 -p 8080:80 nginx
# 测试
[root@localhost /]# docker pull nginx
Using default tag: latest
latest: Pulling from library/nginx
a076a628af6f: Pull complete 
0732ab25fa22: Pull complete 
d7f36f6fe38f: Pull complete 
f72584a26f32: Pull complete 
7125e4df9063: Pull complete 
Digest: sha256:10b8cc432d56da8b61b070f4c7d2543a9ed17c2b23010b43af434fd40e2ca4aa
Status: Downloaded newer image for nginx:latest
docker.io/library/nginx:latest
[root@localhost /]# docker images
REPOSITORY   TAG       IMAGE ID       CREATED       SIZE
nginx        latest    f6d0b4767a6c   8 days ago    133MB
centos       latest    300e315adb2f   6 weeks ago   209MB
-d 后台运行
--name 给容器命名
-p 宿主机端口:容器端口
[root@localhost /]# docker run -d --name nginx01 -p 8080:80 nginx
bbf0681d37d27163453e0ac3da62fbd49595d13bfda74965c90fa856e2b8c59b

# 进入容器
docker exec -it nginx01 /bin/bash

exit

# 停止容器
docker stop nginx01
```

**思考问题：我们每次改动nginx配置文件，都需要进入容器内部？十分的麻烦，我要是在容器外部提供一个映射路径，达到在容器外部 修改文件，容器内部就可以自动修改？ -v 数据卷！**

```shell
# 其他用法
docker run -it --rm tomcat:9.0 
# 用完即删 一般用于测试	


docker run -d -p 3355:8080 --name tomcat01 tomcat

docker exec -it tomcat01 /bin/bash
```

**思考问题：我们以后要部署项目，如每次都要进入容器是不是十分麻烦? 我们要是在容器外部提供一个映射路径，webapps，我们在外部防止项目，就自动同步到内部就好了！**

**Docker 安装ES(elasticsearch) + kibana**

```shell
# es 暴露的端口很多
# es 十分的耗内存
# es 的数据一般放置到安全目录！挂载
# --net somenetwork 网络配置
# -e "discovery.type=single-node" 集群

# 启动
docker run -d --name elasticsearch -p 9200:9200 -p 9300:9300  elasticsearch:7.6.2

# 启动了linux 服务器就卡了 docker stats 查看 cpu 的状态

# es 是十分耗内存的
docker stats
# CPU 占用 %80 内存占用率100% 1.75 内存

# 赶紧关闭，增加内存限制，修改配置文件 -e 环境配置修改
docker run -d --name elasticsearch02 -p 9200:9200 -p 9300:9300 -e "discovery.type=single-node" -e ES_JAVA_OPTS="-Xms64m -Xms512m" elasticsearch:7.6.2

# vim /config/elasticsearch.yml 可以加一个容器数据卷
cluster.name: "docker-cluster"
network.host: 0.0.0.0 # 外部能访问的关键

# Always bind data volumes
# You should use a volume bound on /usr/share/elasticsearch/data for the following reasons:

# The data of your Elasticsearch node won’t be lost if the container is killed
# Elasticsearch is I/O sensitive and the Docker storage driver is not ideal for fast I/O
# It allows the use of advanced Docker volume plugins

# 查看内存
docker stats 容器id
```

```json
{
"name": "87a4b6000cec",
"cluster_name": "docker-cluster",
"cluster_uuid": "O5qoNL2fQX6eKYNahZhG-Q",
"version": {
"number": "7.6.2",
"build_flavor": "default",
"build_type": "docker",
"build_hash": "ef48eb35cf30adf4db14086e8aabd07ef6fb113f",
"build_date": "2020-03-26T06:34:37.794943Z",
"build_snapshot": false,
"lucene_version": "8.4.0",
"minimum_wire_compatibility_version": "6.8.0",
"minimum_index_compatibility_version": "6.0.0-beta1"
},
"tagline": "You Know, for Search"
}
```

**思考：如何通过linux内网实现Docker 容器之间通信**

# 可视化

## portainer (先用这个)

```shell
docker run -d -p 8080:9000 --restart=always -v /var/run/docker.sock:/var/run/docker.sock --privileged=true portainer/portainer
```

什么是portainer

Docker图形化界面管理工具！提供一个后台面板供我们操作

## Rancher(CI/CD再用)

# Docker镜像

## 镜像是什么

镜像是一种轻量级，可执行独立软件包，用来打包软件运行环境和基于环境开发的软件，它包含运行某个软件所需的所有内容，包括代码，运行时，库，环境变量和配置文件。

如何得到镜像

- 从远程仓库下载
- 朋友拷贝给你
- 自己制作一个镜像 DockerFile

## Docker 镜像加载原理

> **UnionFS（联合文件系统）**

 UnionFS（联合文件系统）：Union文件系统（ UnionFs）是一种分层，轻量级并且高性能的文件系统，它支持对文件系统的修改作为一次提交来一层层的叠加，同时可以将不同目录挂载到同一个虚拟文件系统下（nuite several directories into a single virtual filesystem ）Union 文件系统是Docker镜像的基础，镜像可以通过分层来进行继承，基于基础镜像（没有父镜像），可以制作各种具体的应用镜像。

特性：一次同时加载多个文件系统，但从外面看起来，只能看见一个文件系统，联合加载会把各层文件系统叠加起来，这样最终的文件系统会包含所有的底层和目录。

> **Docker镜像加载原理**

docker 镜像实际上有一层一层文件系统组成，这种层级的文件系统 UnionFS。

bootfs(boot file system) 主要包含bootloader和kernal,bootloader主要是引导加载kernel,Linux刚启动时会加载bootfs文件系统，在Docker镜像的最底层是bootfs,这一层与我们典型的Linux/Unix系统是一样的，包含boot加载器的内核，当boot加载完成之后整个内核都在内存中了，此时内存的使用权已由bootfs转交给内核，此时系统也会卸载bootfs。

rootfs（root file system）在bootfs 之上。包含的就是典型Linux系统中的 /dev /proc /bin /etc 等标准目录和文件。rootfs 就是各种不同操作系统发行版，比如 Ubuntu,CentOS等等。

对于一个精简的OS，rootfs可以很小，只需要包括最基本的命令、工具和程序就可以了，因为底层直接用宿主机的内核，自己只需要提供rootfs就可以了，因此可见，对于不用的Linux发行版，bootfs基本是一致的，而rootfs会有差别，因此不同的发行版可以公用bootfs。

![](https://gimg2.baidu.com/image_search/src=http%3A%2F%2Fimg.vnfan.com%2Fpictures%2Fblogs%2F2018_12%2F12180844322018196a29c55c8de4a2.png&refer=http%3A%2F%2Fimg.vnfan.com&app=2002&size=f9999,10000&q=a80&n=0&g=0n&fmt=jpeg?sec=1613797361&t=ddf525afd444f1dd85b83c53947bd87a)

## base 镜像

#### base 镜像有两层含义：

```
1. 不依赖其他镜像，从 scratch 构建。
2. 其他镜像可以之为基础进行扩展。
```

base 镜像的通常都是各种 Linux 发行版的 Docker 镜像，比如 Ubuntu, Debian, CentOS 等，以 CentOS 为例学习 base 镜像包含哪些内容。

###### 下载镜像：

```
[root@docker ~]# docker pull centos
Using default tag: latest
latest: Pulling from library/centos
af4b0a2388c6: Pull complete
Digest: sha256:2671f7a3eea36ce43609e9fe7435ade83094291055f1c96d9d1d1d7c0b986a5d
Status: Downloaded newer image for centos:latest ##下载centos最新镜像
```

###### 查看镜像信息：

```
[root@docker ~]# docker images centos
REPOSITORY          TAG                 IMAGE ID            CREATED             SIZE
centos              latest              ff426288ea90        4 weeks ago         207MB
```

使用docker pull centos下载最新版本的Centos镜像也就207M左右，而我们平时下载一个原生的centos镜像都是4G，对于 Docker 初学者都会有这个疑问。

下面来了解下Linux 操作系统由内核空间和用户空间组成，如下图所示：
![第八篇：Docker镜像结构原理](https://s4.51cto.com/images/blog/201802/09/dd5cf83799311a7b50f874205ff9de7a.png?x-oss-process=image/watermark,size_16,text_QDUxQ1RP5Y2a5a6i,color_FFFFFF,t_100,g_se,x_10,y_10,shadow_90,type_ZmFuZ3poZW5naGVpdGk=)

#### rootfs

内核空间是 kernel，Linux 刚启动时会加载 bootfs 文件系统，之后 bootfs 会被卸载掉。
用户空间的文件系统是 rootfs，包含我们熟悉的 /dev, /proc, /bin 等目录。
对于 base 镜像来说，底层直接用 Host 的 kernel，自己只需要提供 rootfs 就行了。
而对于一个精简的 OS，rootfs 可以很小，只需要包括最基本的命令、工具和程序库就可以了。相比其他 Linux 发行版，CentOS 的 rootfs 已经算臃肿的了，alpine 还不到 10MB。
我们平时安装的 CentOS 除了 rootfs 还会选装很多软件、服务、图形桌面等，需要好几个 GB 就不足为奇了。

#### base 镜像提供的是最小安装的 Linux 发行版。

下面是 CentOS 镜像的 Dockerfile 的内容：
![第八篇：Docker镜像结构原理](https://s4.51cto.com/images/blog/201802/09/8d9e3dc01c8689e3fdcb84bca0a9e4ec.png?x-oss-process=image/watermark,size_16,text_QDUxQ1RP5Y2a5a6i,color_FFFFFF,t_100,g_se,x_10,y_10,shadow_90,type_ZmFuZ3poZW5naGVpdGk=)
第二行 ADD 指令添加到镜像的 tar 包就是 CentOS 7 的 rootfs。在制作镜像时，这个 tar 包会自动解压到 / 目录下，生成 /dev, /porc, /bin 等目录。

注：可在 Docker Hub 的镜像描述页面中查看 Dockerfile 。

#### 支持运行多种 Linux OS

#### 不同 Linux 发行版的区别主要就是 rootfs。

比如 Ubuntu 14.04 使用 upstart 管理服务，apt 管理软件包；而 CentOS 7 使用 systemd 和 yum。这些都是用户空间上的区别，Linux kernel 差别不大。
所以 Docker 可以同时支持多种 Linux 镜像，模拟出多种操作系统环境。
![第八篇：Docker镜像结构原理](https://s4.51cto.com/images/blog/201802/09/84049ad18efec6d9ca147038c0131f9b.png?x-oss-process=image/watermark,size_16,text_QDUxQ1RP5Y2a5a6i,color_FFFFFF,t_100,g_se,x_10,y_10,shadow_90,type_ZmFuZ3poZW5naGVpdGk=)
上图 Debian 和 BusyBox上层提供各自的 rootfs，底层共用 Docker Host 的 kernel。

注意：base 镜像只是在用户空间与发行版一致，kernel 版本与发型版是不同的。

```
[root@docker ~]# uname -r
3.10.0-514.el7.x86_64                 ##Host kernel 为 3.10.0-514
[root@docker ~]# docker run -ti centos    ##启动并进入 CentOS 容器
[root@263132669aa3 /]# cat /etc/redhat-release   ##验证容器是 CentOS 7
CentOS Linux release 7.4.1708 (Core)
[root@263132669aa3 /]# uname -r      ##容器的 kernel 版本与 Host 一致
3.10.0-514.el7.x86_64
```

说明：

**容器只能使用 Host 的 kernel，并且不能修改。所有容器都共用 host 的 kernel，在容器中没办法对 kernel 升级。如果容器对 kernel 版本有要求（比如应用只能在某个 kernel 版本下运行），则不建议用容器，这种场景虚拟机可能更合适。**

> **Docker为什么采用分层结构呢？**

- 共享资源

　　多个镜像从相同的父镜像构建而来，那么宿主机只需在磁盘上保存一份父镜像，同时内存中也只需加载一份父镜像就可以为所有容器服务了，并且镜像的每一层都可以被共享。

> **Docker镜像特点**

- Docker镜像只读

- 当镜像实例为容器后，只有最外层是可写的。
- 当容器启动时，一个新的可写成加到镜像顶部！这一层就是我们通常说的容器层，容器之下就叫镜像层

## commit 镜像

> **如何提交自己的镜像**

```shell
docker commit 提交容器成为一个新的副本
# 其实就是把镜像添加自己的东西形成基础版本，发布出去
# 命令和git 原理类似
docker commit -m="提交的描述信息" -a="作者" 容器id 目标镜像名:[tag]
```

### 实战测试

```shell
docker commit -m="add webapps" -a="yby" tomcat01 tomcat02:1.0
# 如果你想保存当前容器的状态，就可通过commit来提交，获得一个镜像，就好比我们以前学习虚拟机的 时候，快照
```



# 容器数据卷

## 什么事容器数据卷

 容器之间有一个数据共享技术！Docker 容器中产生的数据，同步到本地！

这就是卷技术！目录的挂载，将我们容器内的目录，挂在到Linux 上

**总结一句话：容器的持久化和同步操作！容器间也是可以数据共享的**

## 使用数据卷

> 方式一：直接使用命令来挂载  -v (Volume)

 ```shell
docker run -it -v 主机内的目录:容器内的目录

# 测试
[root@localhost ~]# docker run -it -v /home/ceshi:/home centos /bin/bash
# 启动之后我们可以通过docker inspect 容器名 查看详细信息 Mounts（挂载）

 ```

**实战：安装mysql**

```shell
# 获取镜像
[root@localhost ceshi]# docker pull mysql:5.7

# 运行容器 ，需要数据挂载，需要密码
docker run --name mysql01 -p 3310:3306 -v /home/mysql/conf:/etc/mysql/conf.d -v /home/mysql/data:/var/lib/mysql -e MYSQL_ROOT_PASSWORD=970829 -d mysql:5.7 
-d 后台运行
-p 端口映射
-v 数据卷挂载
-e 环境配置
--name 容器名字

```

## 具名和匿名挂载

```shell
# 匿名挂载
-v 容器内路径
docker run -d -P --name nginx01 -v /etc/nginx nginx
-P 随机一个 49000 ~ 49900的端口 映射到容器开放的内部端口

# 查看所有卷的情况
[root@localhost data]# docker volume ls
# 这里发现
DRIVER    VOLUME NAME
local     41cffef89ea42e02e79cbdda9e77ff434232ddf5746e865b2e06462dfc61b72c

这种就是匿名挂载，我们在 -v 的时候只写了容器内的地址没写容器外的地址

# 具名挂载
[root@localhost data]#  docker run -d -P -v juming:/etc/nginx --name nginx02 nginx

[root@localhost data]# docker volume ls
DRIVER    VOLUME NAME
local     juming

# 通过 -v 卷名:容器内路径
# 查看一下这个卷
[root@localhost data]# docker volume inspect juming
[
    {
        "CreatedAt": "2021-01-21T06:51:30-05:00",
        "Driver": "local",
        "Labels": null,
        "Mountpoint": "/var/lib/docker/volumes/juming/_data",
        "Name": "juming",
        "Options": null,
        "Scope": "local"
    }
]
# 所有docker 容器内的卷，没有指定目录的情况下都是在 `/var/lib/docker/volumes/xxxx/_data`
# 我们他通过具名挂载可以方便的找到我们的一个卷，大多数情况下使用具名挂载
```

**如何确定是匿名挂载和具名挂载该是，指定路径挂载**

```shell
-v 容器内路径 	      # 匿名
-v 卷名:容器内路径		# 具名挂载
-v /宿主机路径:容器内路径 # 指定路径挂载
```



```shell
# 查看docker的 数据卷
docker volume --help 

Commands:
  create      Create a volume
  inspect     Display detailed information on one or more volumes
  ls          List volumes
  prune       Remove all unused local volumes
  rm          Remove one or more volumes
```

**拓展**

```shell
[root@localhost data]#  docker run -d -P -v juming:/etc/nginx:ro --name nginx02 nginx

readonly  ----> ro 只读
readwrite ----> rw 可读写

# 一旦设置了容器权限，容器对我们挂载出来的内容就有限定了
-v juming:/etc/nginx:ro
-v juming:/etc/nginx:rw

# ro 只要看到ro 就说明这个路径只能通过宿主机来操作，容器内部是不能操作的
# 默认rw

```





## 数据卷容器

多个mysql 同步数据

```shell
# 启动三个容器，通过我们刚才自己写的镜像启动

docker run -it --name docker01 9655ab7544fa

docker run -it --name docker02 --volumes-from docker01 9655ab7544fa

# 在docker01 volume 修改数据会自动同步 到docker02  只能同步数据卷中的数据

--volumes-from 容器id/容器名 # 实现容器间的数据共享  
```

```shell

[root@localhost docker-yby-volume]# docker run --name mysql01 -p 3310:3306  -v /etc/mysql/conf.d -v /var/lib/mysql -e MYSQL_ROOT_PASSWORD=970829 -d mysql:5.7
939769cc15a3f8d9f8298a6e2d4425ec4b7365442f86df8fb30b9ea59602c657
[root@localhost docker-yby-volume]# docker run --name mysql02 -p 3311:3306 --volumes-from mysql01  -v /etc/mysql/conf.d -v /var/lib/mysql -e MYSQL_ROOT_PASSWORD=970829 -d mysql:5.7
992734b091a8d8cca27e770154e48f23c97320683f82bfc805b822f7c587252a

# 两个mysql 数据同步了 
```

**容器之间配置信息的传递，数据卷容器的生命周期时一直持续到没有 容器使用为止**

**但是一旦你持久化到本地，这个时候，本地数据是不会删除的**

# DockerFile

## DockerFile介绍

构建步骤

1、编写一个dockerdile文件

2、docker buiild 构建成为一个镜像

3、docker run 运行镜像

4、docker push 发布镜像 （dockerHub，阿里云镜像仓库）

很多官方的镜像都是基础包，很多功能没有，我们会自己搭建自己的镜像！

官方既然可以制作镜像那我们也可以

 ## DockerFile 构建过程

**基础知识：**

1、每个保留关键字（指令） 都必须是大写

2、指令是从上到下顺序执行的

3、# 表示注释

4、没一个指令都会提交创建一个新的镜像层，并提交

![](https://ss2.bdstatic.com/70cFvnSh_Q1YnxGkpoWK1HF6hhy/it/u=1982640279,3003728739&fm=26&gp=0.jpg)

dockerfile是面向开发的，我们以后发部项目，作镜像，就需要编写dockerfile文件，这个文件十分简单！

Docker镜像逐渐成为企业交付的标准，必须掌握！

DockerFile：构建文件，定义了一切步骤

 DockerImages：通过DockerFile构建生成的镜像，最终发布和运行的产品。

Docker容器：容器就是镜像运行起来提供服务



## DockerFile的指令

```shell
FROM				# 基础镜像 一起从这里构建
MAINTAINER			# 镜像是谁写的，姓名+邮箱
RUN					# 镜像构建的时候需要运行的命令
ADD					# 步骤： tomcat镜像。这个tomcat的压缩包！添加内容
WORKDIR				# 镜像的工作目录
VOLUME 				# 挂载的目录
EXPOSE				# 指定暴露端口
CMD					# 指定这个容器启动的时候要运行命令,只有最后一个会生效，可被替代
ENTRYPOINT			# 指定这个容器启动的时候要运行命令，可以追加命令
ONBUILD				# 当构建一个被继承  DockerFile 这个时候就会运行ONBUILD 的指令，触发指令。
COPY				# 类似ADD，将我们文件拷贝到镜像中
ENV 				# 构建的时候设置环境变量
```



![](https://ss3.bdstatic.com/70cFv8Sh_Q1YnxGkpoWK1HF6hhy/it/u=3622110164,3202557425&fm=26&gp=0.jpg)

**实战测试**

Docker hub 中99% 的镜像都是从 FROM scratch 基础镜像过来的，然后配置需要的软件和配置来进行的构建

> 创建一个自己的 centos

```shell
# 自己的centOS
# 编写 DockerFile的文件
FROM centos
MAINTAINER yby<2694286031@qq.com>

ENV MYPATH /usr/local
WORKDIR $MYPATH

RUN yum -y install vim
RUN yum -y install net-tools

EXPOSE 80

CMD echo $MYPATH
CMD echo "----end----"

CMD /bin/bash 

# 通过文件构建镜像
docker build -f dockerfile文件路径 -t 镜像名:tag版本号 .

# 测试运行
docker run -it 镜像名:版本号

发现这个镜像里面有 vim net-tools 工具

# 查看docker 构建历史
docker history 镜像名:版本/镜像id

[root@localhost dockerfile]# docker history b8bdeb24942f
IMAGE          CREATED          CREATED BY                                      SIZE      COMMENT
b8bdeb24942f   30 minutes ago   /bin/sh -c #(nop)  CMD ["/bin/sh" "-c" "/bin…   0B        
ac1ea0c31a9d   30 minutes ago   /bin/sh -c #(nop)  CMD ["/bin/sh" "-c" "echo…   0B        
aa3390e86ebd   30 minutes ago   /bin/sh -c #(nop)  CMD ["/bin/sh" "-c" "echo…   0B        
d1e9cd371e5b   30 minutes ago   /bin/sh -c #(nop)  EXPOSE 80                    0B        
cf6f32931439   30 minutes ago   /bin/sh -c yum -y install net-tools             23.3MB    
ef3335dbb77a   30 minutes ago   /bin/sh -c yum -y install vim                   58.1MB    
2527bf6cb8ae   30 minutes ago   /bin/sh -c #(nop) WORKDIR /usr/local            0B        
ee42f2d3e7d0   30 minutes ago   /bin/sh -c #(nop)  ENV MYPATH=/usr/local        0B        
7fd4aea73e18   30 minutes ago   /bin/sh -c #(nop)  MAINTAINER yby<2694286031…   0B        
300e315adb2f   6 weeks ago      /bin/sh -c #(nop)  CMD ["/bin/bash"]            0B        
<missing>      6 weeks ago      /bin/sh -c #(nop)  LABEL org.label-schema.sc…   0B        
<missing>      6 weeks ago      /bin/sh -c #(nop) ADD file:bd7a2aed6ede423b7…   209MB     

```

> **CMD和ENTRYPOINT的区别**

```shell
CMD					# 指定这个容器启动的时候要运行命令,只有最后一个会生效，可被替代
ENTRYPOINT			# 指定这个容器启动的时候要运行命令，可以追加命令
```

```shell
# Dockerfile 文件
FROM centos
CMD ["ls","-a"]
# 构建之后执行发现我们的ls -a 命令生效

# 想追加一个命令
docker run 镜像id -l
发现报错
docker run 镜像id ls -al
发现可以
# 所以是CMD 命令是替换了
```

测试 ENTRYPOINT

```shell
# dockerfile 文件
FROM centos
ENTRYPOINT ["ls","-a"]
# 构建之后执行发现我们的ls -a 命令生效

# 想追加一个命令
docker run 镜像id -l
发现成功
# 所以是ENTRYPOINT 命令是追加
```

## 初始Dockerfile

Dockerfile 就是用来构建docker 镜像的 构建文件	

通过这个脚本可以生成镜像，镜像是一层一层的，每一个命令都是一层

```shell
# 创建一个dockerfile 文件，名字可以随机，建议Dockerfile
# 文件中的内容 指令（大写） 参数

FROM centos
VOLUME ["volume01","volume02"]

CMD echo "----end----"

CMD /bin/bash

# 这里的每个命令，就是镜像的一层 
# VOLUME 新建匿名
# 在VOLUME 不能使指定具名和指定主机路径,":"不好使
# 如果不指定VOLUME 也可以在新建容器的时候手动挂载
```

```shell
[root@localhost docker-yby-volume]# docker build -f dockerfile01 -t ybycentos:1.0 .
Sending build context to Docker daemon  2.048kB
Step 1/4 : FROM centos
 ---> 300e315adb2f
Step 2/4 : VOLUME ["volume01","volume02"]
 ---> Running in a656d92da24f
Removing intermediate container a656d92da24f
 ---> 16214c2e2dd0
Step 3/4 : CMD echo "----end----"
 ---> Running in 811c1a966272
Removing intermediate container 811c1a966272
 ---> 69e6c5bb2bc0
Step 4/4 : CMD /bin/bash
 ---> Running in f4795c8de1d1
Removing intermediate container f4795c8de1d1
 ---> 9655ab7544fa
Successfully built 9655ab7544fa
Successfully tagged ybycentos:1.0

# 参数
Options:
  -c, --cpu-shares int          CPU shares (relative weight)
  -f, --file string             指定dockerfile 文件路径 (Default is 'PATH/Dockerfile')
  -m, --memory bytes            Memory limit
  -t, --tag list                指定镜像名和版本 'name:tag' format

```

```shell
# 启动一下自己写的容器

docker run -it 镜像id
docker inspect 容器id 
"Mounts": [
            {
                "Type": "volume",
                "Name": "d048595dda4724c26ec73e5c06ef71f0f70194f7212fc4f118da272389412727",
                "Source": "/var/lib/docker/volumes/d048595dda4724c26ec73e5c06ef71f0f70194f7212fc4f118da272389412727/_data",
                "Destination": "volume01",
                "Driver": "local",
                "Mode": "",
                "RW": true,
                "Propagation": ""
            },
            {
                "Type": "volume",
                "Name": "85b2f017bff8a876cc2fd3d3748932dc0ea187fe9793015fa5b42c32ac4f32f7",
                "Source": "/var/lib/docker/volumes/85b2f017bff8a876cc2fd3d3748932dc0ea187fe9793015fa5b42c32ac4f32f7/_data",
                "Destination": "volume02",
                "Driver": "local",
                "Mode": "",
                "RW": true,
                "Propagation": ""
            }
        ],

```



## 实战：Nginx 镜像

1、准备镜像文件，Nginx压缩包 ，或网址

2、编写dockerfile文件，官方命名Dockerfile  build 会自动寻找这个文件，就不需要 -f

```shell
FROM centos:7
MAINTAINER shichao@scajy.cn
RUN rpm -ivh http://mirrors.ustc.edu.cn/epel/7/x86_64/Packages/e/epel-release-7-12.noarch.rpm 
RUN yum install -y gcc gcc-c++ make pcre pcre-devel openssl openssl-devel  pcre-davel gd-devel iproute net-tools telnet wget curl && yum clean  all && rm -rf /var/cache/yum/*
RUN useradd -M -s /sbin/nologin nginx
RUN  wget http://nginx.org/download/nginx-1.17.6.tar.gz && tar zxf  nginx-1.17.6.tar.gz && \
	cd nginx-1.17.6  && \
	./configure --prefix=/usr/local/nginx --user=nginx --group=nginx --with-http_stub_status_module --with-http_ssl_module --with-http_gzip_static_module  --with-http_flv_module --with-http_mp4_module --with-http_gunzip_module && \
	make && make install
ENV PATH /usr/local/nginx/sbin:$PATH 

EXPOSE 80

ENTRYPOINT ["nginx"]

CMD ["-g","daemon off;"]
```

## 爬虫Dockerfile

```python
# Dockerfile
FROM python:3.6
MAINTAINER yby xxxxxxx@qq.com
ADD . /usr/src
WORKDIR /usr/src
RUN pip install -r requirements.txt -i https://mirrors.aliyun.com/pypi/simple
RUN chmod +x run.sh
CMD /usr/src/run.sh
```

```shell
docker build -t spider:1.0 . # 构建爬虫镜像
```

## 1.CMD 和 RUN 的区别

两者都是用于执行命令，区别在于执行命令的时机不同，RUN命令适用于在 docker build 构建docker镜像时执行的命令，而CMD命令是在 docker run 执行docker镜像构建容器时使用，可以动态的覆盖CMD执行的命令。

## 2. CMD 和 ENTRYPOINT的区别

首先，CMD命令是用于默认执行的，且如果写了多条CMD命令，则只会执行最后一条，如果后续存在ENTRYPOINT命令，则CMD命令或被充当参数或者覆盖，而且Dockerfile中的CMD命令最终可以被在执行 docker run命令时添加的命令所覆盖。而ENTRYPOINT命令则是一定会执行的，一般用于执行脚本
根据写法分析，这里涉及到执行命令的两种写法，第一种使用 shell，第二种使用 exec，例如

```dockerfile
#shell写法
FROM centos
CMD echo 'hello'

#exec写法
FROM centos
CMD ["echo","hello"]
```

### 2.1 在 shell 写法环境下

在shell写法中，如果存在 ENTRYPOINT命令，则不管是在Dockerfile中存在CMD命令也好，还是在 docker run执行的后面添加的命令也好，都不会被执行。如果不存在 ENTRYPOINT命令，则可以被 docker run后面设置的命令覆盖，实现动态执行命令操作。

### 2.2 在 exec 写法环境下

在exec 写法中，如果存在 ENTRYPOINT命令，则在Dockerfile中如果存在CMD命令或者是在 docker run执行的后面添加的命令，会被当做 ENTRYPOINT命令的参数来使用。举例如下

```dockerfile
FROM centos
CMD ["hello"]
ENTRYPOINT ["echo"]
```

使用 docker run xxx 后，显示打印 hello，此时 CMD命令的内容会被充当ENTRYPOINT命令的参数，且这种情况，CMD命令的内容不会被ENTRYPOINT命令覆盖，还可以支持在docker run 后面的命令覆盖 Dockerfile中的CMD命令。
例如：执行 docker run xx helllo-docker , 会显示打印 hello-docker,可以得出 此时 docker run后面的内容将Dockerfile中的最后一条CMD命令的参数内容覆盖，搭配ENTRYPOINT命令使用。这种方法较常用，可以支持动态修改参数内容，保存执行命令一样。



## 发布自己的镜像

> Docker Hub

1、注册账号

2、确定这个账号可以使用

3、在我们的服务器上提交自己的镜像

```shell
[root@localhost dockerfile]# docker login --help

Usage:  docker login [OPTIONS] [SERVER]

Log in to a Docker registry.
If no server is specified, the default is defined by the daemon.

Options:
  -p, --password string   Password
      --password-stdin    Take the password from stdin
  -u, --username string   Username

# 登录
[root@localhost dockerfile]# docker login -u hljyby
Password: 
WARNING! Your password will be stored unencrypted in /root/.docker/config.json.
Configure a credential helper to remove this warning. See
https://docs.docker.com/engine/reference/commandline/login/#credentials-store

Login Succeeded

# push 自己的镜像到服务器上
[root@localhost dockerfile]# docker push yby/nginx
Using default tag: latest
The push refers to repository [docker.io/yby/nginx]
b9f709e8fab5: Preparing 
80b36ac9a523: Preparing 
3fdfae00f1d0: Preparing 
a92c9e397fe1: Preparing 
174f56854903: Preparing 

# docker tag 镜像id 新的镜像名:版本号
```

> 上传阿里云镜像服务器 
>
> 地址：https://cr.console.aliyun.com/repository/cn-hongkong/hljyby/yby-nginx/details

1、登录阿里云

2、容器镜像服务

3、创建命名空间

4、创建容器镜像

5，登录阿里云Docker

```shell
$ sudo docker login --username=webboyu registry.cn-hongkong.aliyuncs.com
```

6、生成镜像版本号

```shell
$ sudo docker tag [ImageId] registry.cn-hongkong.aliyuncs.com/hljyby/yby-test:[镜像版本号]
```

7、push 到阿里云上

```shell
$ sudo docker push registry.cn-hongkong.aliyuncs.com/hljyby/yby-test:[镜像版本号]
```

8、pull到本地

```shell
$ sudo docker pull registry.cn-hongkong.aliyuncs.com/hljyby/yby-nginx:[镜像版本号]
```

# Docker 搭建私有仓库

## Register

```shell
docker pull registry
```

## 配置文件

```shell
vim /etc/docker/daemon.json
# 添加
"insecure-registries": ["10.211.55.4:5000"] # 自己的docker IP地址
```

## 重启docker

```shell
systemctl restart docker
```

## 创建容器

``` shell
docker run -d -p 5000:5000 --name registry docker.io/registry
```

## 验证上传镜像到私有仓库

**我们使用`HelloWorld`镜像进行测试，首先先拉取一下：**

```shell
docker pull hello-world
```

**至此我们就有了一个 hello-world镜像，接下来我们使用 push 指令将镜像推送到刚刚搭建的registry中：**

```shell
# 标记hello-world该镜像需要推送到私有仓库
docker tag hello-world:latest 127.0.0.1:5000/hello-world:latest

# 通过push指令推送到私有仓库
docker push 127.0.0.1:5000/hello-world:latest
```

## 验证从私有仓库下载镜像

**验证完了上传，我们再来测试一下下载镜像：**

```shell
# 格式如下：
docker pull 127.0.0.1:5000/镜像名称:镜像版本号

# 以hello-world为例：
docker pull 127.0.0.1:5000/hello-world
```

## 报错

```shell
Trying to pull repository 10.211.55.4:5000/hello-world ...
Get https://10.211.55.4:5000/v1/_ping: http: server gave HTTP response to HTTPS client
```

## 处理

我们可以通过如下进行处理一下，xxx修改为自己的**ip**地址：

```shell
# 注1：下面的方法会覆盖源文件的内容，请谨慎使用，
# 注2：在那个机器上拉取镜像，就修改那个机器的docker配置文件，而不是在创建私有仓库的那台机器上。

echo '{ "insecure-registries":["xxx.xxx.xxx.xxx:5000"] }' > /etc/docker/daemon.json
```

# Docker网络 原理

## 理解Docker0

> 原理

1、没启动一个容器，docker就会给容器分配一个ip，我们只要安装了docker就会有一个网卡docker0，桥接模式，使用的技术是 evth-pair 技术！

```SHELL
[root@localhost dockerfile]# ip addr
1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN group default qlen 1000
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
    inet 127.0.0.1/8 scope host lo
       valid_lft forever preferred_lft forever
    inet6 ::1/128 scope host 
       valid_lft forever preferred_lft forever
2: ens160: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc fq_codel state UP group default qlen 1000
    link/ether 00:0c:29:4f:5e:f3 brd ff:ff:ff:ff:ff:ff
    inet 192.168.0.200/24 brd 192.168.0.255 scope global noprefixroute ens160
       valid_lft forever preferred_lft forever
    inet6 fe80::b70e:8001:e770:4aa5/64 scope link noprefixroute 
       valid_lft forever preferred_lft forever
3: docker0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc noqueue state UP group default 
    link/ether 02:42:8b:ad:10:63 brd ff:ff:ff:ff:ff:ff
    inet 172.17.0.1/16 brd 172.17.255.255 scope global docker0
       valid_lft forever preferred_lft forever
    inet6 fe80::42:8bff:fead:1063/64 scope link 
       valid_lft forever preferred_lft forever
53: vethcbc4eb9@if52: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc noqueue master docker0 state UP group default 
    link/ether da:aa:74:b8:04:2e brd ff:ff:ff:ff:ff:ff link-netnsid 1
    inet6 fe80::d8aa:74ff:feb8:42e/64 scope link 
       valid_lft forever preferred_lft forever

```



```shell
# 我们发现这个容器带来网卡，都是一对一对的
#  evth-pair 就是一对的 虚拟设备接口， 他们都是成对出现的，一端连着协议，一端彼此相连
# 正因为这个特性， evth-pair 充当桥梁，链接各种虚拟网络设备
# Docker 容器之间的连接， OVS的链接，都是使用evth-pair 技术

```

 2、我么来测试一下 容器容器之间能不能ping 通

```shell
# 可以ping通 因为是桥接的最后都到docker0 所以可以ping通
```

3、所有容器不指定网络的情况下，都是Docker0路由的，docker会给我们的容器分配一个默认可用 ip

```shell
容器a 和 docker0 是桥接模式
docker0 和 物理网卡是直连的（NAT）
docker 中的所有网络接口都是虚拟的，虚拟的转发效率高。
只要容器删除，对应网桥就没了
不能ping通容器名，我们想要通过容器名进行网络通信。
```

## --link

```shell
docker run -d -P --name nginx01 --link nginx02 nginx
# 发现 01 ping 02 可以ping通
# 发现 02 ping 01 不可以ping通

# 容器内，有/etc/hosts 文件 --link 的实现是在hosts 文件里加入指向

# 现在版本的Docker 不建议使用这种办法，这种办法太笨了。
```

## 自定义网络

> 查看所有Docker网络

```shell
docker network ls
```

**网络模式**

```shell
bridge 				# 桥接（默认）
none 				# 不配置网络
host				# 和linux服务器共享网络
container			# 容器内可以网络联通（不建议使用，局限很大）

```

**测试**

```shell
# 我们直接启动的命令 --net bridge,而这个就是我们的Docker0
[root@localhost ~]# docker run -d -P --name nginx01 --net bridge nginx

# docker0的特点：默认域名不能访问，--link可以打通链接

# 我们可以自定义网络
[root@localhost ~]# docker network create --driver bridge --subnet 192.168.0.0/16 --gateway 192.168.0.1 mynet

# 解释
--driver bridge # 桥接 默认桥接
--subnet 192.168.0.0/16 # 子网 16 代表子网掩码 255.255.0.0 25535 个IP地址可供分配
--gateway 192.168.0.1 # 网关 

# 好处
使用自己的网络所有网络里的容器可以相互ping 通，可以使用容器名ping通。
```

### 结论

我们自定义的网络 docker都已经维护好了对应关系，推荐我们平时都这样使用网络

**好处**

集群：

redis

mysql 

他们都有自己的专用网络，不互相影响

## 网络联通

两个不同网络的容器，之间互相联通，需要让容器和他想联通的容器的网络实现联通。

```shell
# docker network connect 网络名 容器名

# 联通之后，就是将我们的容器放到mynet 网络下

# 一个容器，两个ip
```

结论：假设要跨网络操作别人，就需要使用docker network connect 联通

# Docker 开机自动重启

```shell
systemctl enable docker.service
```

## docker 容器自动重启

```shell
docker run --restart=always
```

## 如果容器已经启动了

```shell
docker update --restart=always <CONTAINER ID>
```

# Docker compose

## 简介

`Compose` 项目是 Docker 官方的开源项目，负责实现对 Docker 容器集群的快速编排。从功能上看，跟 `OpenStack` 中的 `Heat` 十分类似。

其代码目前在 [https://github.com/docker/compose (opens new window)](https://github.com/docker/compose)上开源。

`Compose` 定位是 「定义和运行多个 Docker 容器的应用（Defining and running multi-container Docker applications）」，其前身是开源项目 Fig。

通过第一部分中的介绍，我们知道使用一个 `Dockerfile` 模板文件，可以让用户很方便的定义一个单独的应用容器。然而，在日常工作中，经常会碰到需要多个容器相互配合来完成某项任务的情况。例如要实现一个 Web 项目，除了 Web 服务容器本身，往往还需要再加上后端的数据库服务容器，甚至还包括负载均衡容器等。

`Compose` 恰好满足了这样的需求。它允许用户通过一个单独的 `docker-compose.yml` 模板文件（YAML 格式）来定义一组相关联的应用容器为一个项目（project）。

`Compose` 中有两个重要的概念：

- 服务 (`service`)：一个应用的容器，实际上可以包括若干运行相同镜像的容器实例。
- 项目 (`project`)：由一组关联的应用容器组成的一个完整业务单元，在 `docker-compose.yml` 文件中定义。

`Compose` 的默认管理对象是项目，通过子命令对项目中的一组容器进行便捷地生命周期管理。

`Compose` 项目由 Python 编写，实现上调用了 Docker 服务提供的 API 来对容器进行管理。因此，只要所操作的平台支持 Docker API，就可以在其上利用 `Compose` 来进行编排管理。

# Docker Compose 安装与卸载

`Compose` 支持 Linux、macOS、Windows 10 三大平台。

`Compose` 可以通过 Python 的包管理工具 `pip` 进行安装，也可以直接下载编译好的二进制文件使用，甚至能够直接在 Docker 容器中运行。

前两种方式是传统方式，适合本地环境下安装使用；最后一种方式则不破坏系统环境，更适合云计算场景。

`Docker for Mac` 、`Docker for Windows` 自带 `docker-compose` 二进制文件，安装 Docker 之后可以直接使用。

```shell
$ docker-compose --version

docker-compose version 1.17.1, build 6d101fb
```

 

Linux 系统请使用以下介绍的方法安装。

## 1、二进制包

在 Linux 上的也安装十分简单，从 [官方 GitHub Release (opens new window)](https://github.com/docker/compose/releases)处直接下载编译好的二进制文件即可。

例如，在 Linux 64 位系统上直接下载对应的二进制包。

```shell
sudo curl -L https://github.com/docker/compose/releases/download/1.28.2/docker-compose-`uname -s`-`uname -m` > /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose
```

 

## 2、PIP 安装

*注：* `x86_64` 架构的 Linux 建议按照上边的方法下载二进制包进行安装，如果您计算机的架构是 `ARM` (例如，树莓派)，再使用 `pip` 安装。

这种方式是将 Compose 当作一个 Python 应用来从 pip 源中安装。

执行安装命令：

```shell
$ sudo pip install -U docker-compose
```

 

可以看到类似如下输出，说明安装成功。

```shell
Collecting docker-compose
Downloading docker-compose-1.17.1.tar.gz (149kB): 149kB downloaded
...
Successfully installed docker-compose cached-property requests texttable websocket-client docker-py dockerpty six enum34 backports.ssl-match-hostname ipaddress
```

 

## 3、bash 补全命令

```shell
$ curl -L https://raw.githubusercontent.com/docker/compose/1.8.0/contrib/completion/bash/docker-compose > /etc/bash_completion.d/docker-compose
```

 

## 4、容器中执行

Compose 既然是一个 Python 应用，自然也可以直接用容器来执行它。

```shell
$ curl -L https://github.com/docker/compose/releases/download/1.8.0/run.sh > /usr/local/bin/docker-compose
$ chmod +x /usr/local/bin/docker-compose
```

 

实际上，查看下载的 `run.sh` 脚本内容，如下

```shell
set -e

VERSION="1.8.0"
IMAGE="docker/compose:$VERSION"


# Setup options for connecting to docker host
if [ -z "$DOCKER_HOST" ]; then
DOCKER_HOST="/var/run/docker.sock"
fi
if [ -S "$DOCKER_HOST" ]; then
DOCKER_ADDR="-v $DOCKER_HOST:$DOCKER_HOST -e DOCKER_HOST"
else
DOCKER_ADDR="-e DOCKER_HOST -e DOCKER_TLS_VERIFY -e DOCKER_CERT_PATH"
fi


# Setup volume mounts for compose config and context
if [ "$(pwd)" != '/' ]; then
VOLUMES="-v $(pwd):$(pwd)"
fi
if [ -n "$COMPOSE_FILE" ]; then
compose_dir=$(dirname $COMPOSE_FILE)
fi
# TODO: also check --file argument
if [ -n "$compose_dir" ]; then
VOLUMES="$VOLUMES -v $compose_dir:$compose_dir"
fi
if [ -n "$HOME" ]; then
VOLUMES="$VOLUMES -v $HOME:$HOME -v $HOME:/root" # mount $HOME in /root to share docker.config
fi

# Only allocate tty if we detect one
if [ -t 1 ]; then
DOCKER_RUN_OPTIONS="-t"
fi
if [ -t 0 ]; then
DOCKER_RUN_OPTIONS="$DOCKER_RUN_OPTIONS -i"
fi

exec docker run --rm $DOCKER_RUN_OPTIONS $DOCKER_ADDR $COMPOSE_OPTIONS $VOLUMES -w "$(pwd)" $IMAGE "$@"
```

 

可以看到，它其实是下载了 `docker/compose` 镜像并运行。

## 5、卸载

如果是二进制包方式安装的，删除二进制文件即可。

```shell
$ sudo rm /usr/local/bin/docker-compose
```

如果是通过 `pip` 安装的，则执行如下命令即可删除。

```shell
$ sudo pip uninstall docker-compose
```

# Docker Compose 使用

### 工程、服务、容器

- **Docker Compose 将所管理的容器分为三层，分别是工程（project）、服务（service）、容器（container）**
- **Docker Compose 运行目录下的所有文件（docker-compose.yml）组成一个工程,一个工程包含多个服务，每个服务中定义了容器运行的镜像、参数、依赖，一个服务可包括多个容器实例**

## Docker Compose 常用命令与配置

### 常见命令

- **ps**：列出所有运行容器

```shell
docker-compose ps
```

- **logs**：查看服务日志输出

```undefined
docker-compose logs
```

- **port**：打印绑定的公共端口，下面命令可以输出 eureka 服务 8761 端口所绑定的公共端口

```shell
docker-compose port eureka 8761
```

- **build**：构建或者重新构建服务

```shell
docker-compose build
```

- **start**：启动指定服务已存在的容器

```shell
docker-compose start eureka
```

- **stop**：停止已运行的服务的容器

```shell
docker-compose stop eureka
```

- **rm**：删除指定服务的容器

```shell
docker-compose rm eureka
```

- **up**：构建、启动容器

```shell
docker-compose up
```

- **kill**：通过发送 SIGKILL 信号来停止指定服务的容器

```bash
docker-compose kill eureka
```

- **pull**：下载服务镜像
- **scale**：设置指定服务运气容器的个数，以 service=num 形式指定

```shell
docker-compose scale user=3 movie=3
```

- **run**：在一个服务上执行一个命令

```shell
docker-compose run web bash
```

### docker-compose.yml 属性

- **version**：指定 docker-compose.yml 文件的写法格式
- **services**：多个容器集合
- **build**：配置构建时，Compose 会利用它自动构建镜像，该值可以是一个路径，也可以是一个对象，用于指定 Dockerfile 参数

```shell
build: ./dir
---------------
build:
    context: ./dir
    dockerfile: Dockerfile
    args:
        buildno: 1
```

- **command**：覆盖容器启动后默认执行的命令

```bash
command: bundle exec thin -p 3000
----------------------------------
command: [bundle,exec,thin,-p,3000]
```

- **dns**：配置 dns 服务器，可以是一个值或列表

```shell
dns: 8.8.8.8
------------
dns:
    - 8.8.8.8
    - 9.9.9.9
```

- **dns_search**：配置 DNS 搜索域，可以是一个值或列表

```shell
dns_search: example.com
------------------------
dns_search:
    - dc1.example.com
    - dc2.example.com
```

- **environment**：环境变量配置，可以用数组或字典两种方式

```bash
environment:
    RACK_ENV: development
    SHOW: 'ture'
-------------------------
environment:
    - RACK_ENV=development
    - SHOW=ture
```

- **env_file**：从文件中获取环境变量，可以指定一个文件路径或路径列表，其优先级低于 environment 指定的环境变量

```shell
env_file: .env
---------------
env_file:
    - ./common.env
```

- **expose**：暴露端口，只将端口暴露给连接的服务，而不暴露给主机

```bash
expose:
    - "3000"
    - "8000"
```

- **image**：指定服务所使用的镜像

```shell
image: java
```

- **network_mode**：设置网络模式

```bash
network_mode: "bridge"
network_mode: "host"
network_mode: "none"
network_mode: "service:[service name]"
network_mode: "container:[container name/id]"
```

- **ports**：对外暴露的端口定义，和 expose 对应

```shell
ports:   # 暴露端口信息  - "宿主机端口:容器暴露端口"
- "8763:8763"
- "8763:8763"
```

- **links**：将指定容器连接到当前连接，可以设置别名，避免ip方式导致的容器重启动态改变的无法连接情况

```bash
links:    # 指定服务名称:别名 
    - docker-compose-eureka-server:compose-eureka
```

- **volumes**：卷挂载路径

```shell
volumes:
  - /lib
  - /var
```

- **logs**：日志输出信息

```shell
--no-color          单色输出，不显示其他颜.
-f, --follow        跟踪日志输出，就是可以实时查看日志
-t, --timestamps    显示时间戳
--tail              从日志的结尾显示，--tail=200
```

## Docker Compose 其它

### 更新容器

- 当服务的配置发生更改时，可使用 docker-compose up 命令更新配置
- 此时，Compose 会删除旧容器并创建新容器，新容器会以不同的 IP 地址加入网络，名称保持不变，任何指向旧容起的连接都会被关闭，重新找到新容器并连接上去

### links

- 服务之间可以使用服务名称相互访问，links 允许定义一个别名，从而使用该别名访问其它服务

```bash
version: '2'
services:
    web:
        build: .
        links:
            - "db:database"
    db:
        image: postgres
```

- 这样 Web 服务就可以使用 db 或 database 作为 hostname 访问 db 服务了

## 创建一个简单的 docker-compose

```shell
touch docker-compose.yml

# docker-compose.yml
version: "3.0"

services:
	nginx01: # 服务名 随便取
		image: nginx # 镜像名
		ports: # 映射端口
			- 9002:80
	nginx02: # 服务名 随便取
		image: nginx # 镜像名
		ports: # 映射端口
			- 9003:80
# 直接复制过去不管用，得自己写，格式不对
# 冒号后面得有空格
# 缩进是必须的


redis:
	image: redis:5.0.10
	container_name: redis
	ports:
		- "6379:6379"
	volumes:
		- redisdata:/data
	command: "redis-server --appendonly yes" # 开启持久化 command 相当于覆盖内部的命令
mysql:
	image: mysql:5.7.32
	container_name: mysql
	ports:
		- 3307:3306
	volumes:
		- mysqldata:/var/lib/mysql
		- mysqlconf:/etc/mysql
	environment:
		- MYSQL_ROOT_PASSWORD=root
	network:
		- hellow
		
```

### 运行 dcoker-compose

```shell
docker-compose up # 启动这个项目的所有服务 必须保证运行命令的目录存在docker-compose.yml这个文件
```

# docker-compose模板常用命令

## 一、network创建

#### 1、docker-compose创建network

通过以下内容创建的network，名字为`up_darklight`

```yaml
version: '2'
networks:
  darklight:
    driver: bridge
    ipam:
      driver: default
      config:
        - subnet: 172.30.5.0/24
          ip_range: 172.30.5.0/24
          gateway: 172.30.5.1

services:
  web:
    name: xxx
    networks:
      darklight:
        ipv4_address: 172.30.5.10
```

#### 2、docker-compose使用已存在的network

`external: true`来指定使用已存在的network

```yaml
version: '2'
networks:
  darklight:
    external: true

services:
  web:
    name: xxx
    networks:
      darklight:
        ipv4_address: 172.30.5.10
```

## 二、模板常用的命令

**注意：在编写docker-compose.yml文件时，所有的冒号（:）、短横线（-）后面都需要加一个空格，不然会出错。**

### 1、build

指定Dockerfile所在文件夹的路径（可以是绝对路径，或者相对于docker-compose.yml文件的路径）。docker-compose将会利用它自动构建这个镜像，然后使用这个镜像。

使用 **context** 指定Dockerfile所在文件夹的路径。

使用 **dockerfile** 指定Dockerfile文件名

使用 **args** 指定构建镜像时的变量

```yaml
version: '3'
services: 
  web:
    build:
      context: ./dir
      dockerfile: Dockerfile
      args:
        timezone: 1
```

 

### 2、container_name

指定容器名称，相当于docker run中的`--name`。默认将会使用 `项目名称_服务名称_序号`

```yaml
version: '3'
services: 
  web:
    container_name: web-1
```

 

### 3、command

覆盖容器启动后默认执行的命令，覆盖DockerFile中的`CMD`或第三方镜像的启动命令

```yaml
version: '3'
services: 
  web:
    command: echo 'ok'
```

 

### 4、environment

设置环境变量，相当于docker run中的`-e`。

可以使用`数组`或`字典`两种格式。只给定名称的变量会自动获取运行Compose主机上对应变量的值，可以用来防止泄露不必要的数据。

**`-e`中值部分需要使用引号包裹， docker-compose.yml中不需要用引号**

```yaml
version: '3'
services: 
  mysql:
    environment:
      - MYSQL_ROOT_PASSWORD=12345678
      - MYSQL_DATABASE=my-db
      
    environment:
      MYSQL_ROOT_PASSWORD: 12345678
      
# 有杠 写等号
# 没有杠 写冒号
```

 

### 5、env_file

设置环境变量的文件路径，相当于docker run中的`--env-file`，文件必须是`.env`，内容中`key=value`

```yaml
version: '3'
services: 
  web:
    env_file:
      - envfile_path.env
# this is a environment file
NAME=kk yy

LENGHT=18.8

# 目的是记录敏感信息 如密码 公网ip 端口等等
```

 

### 6、image

指定为镜像名或镜像ID，如果镜像在本地不存在，Compose将会尝试拉取这个镜像。

```yaml
version: '3'
services: 
  mysql:
    image: mysql:5.7
```

 

### 7、network_mode

设置网络模式。使用和docker run的--network参数一样的值

```yaml
version: '3'
services: 
  mysql:
    network_mode: 'host'
    network_mode: 'none'
    network_mode: 'bridge'
```

### 8、networks

services中指定容器连接的网络，配置/创建network

```yaml
version: '3'
services:
  web:
    networks: 
      - network-demo
networks:
  network-demo:
  	external:
  		true # 代表使用外部已经创建的网络
  		
version: '3'
services:
  web:
    networks: 
      network-demo:
      		ipv4_address: 172.30.5.70
networks:
  network-demo
```

 

### 9、ports

暴露端口信息，使用宿主端口:容器端口（HOST:CONTAINER）格式，或者仅仅指定容器的端口（宿主将会随机选择端），相当与docker run中的`-p` 建议使用字符串格式，不适用会报错

```yaml
version: '3'
services:
  web:
    posrts: 
      - "8000:80"
      - "8080:8080"
      - "3000"	
```

 

### 10、volumes

数据卷所挂载路径设置，可以设置宿主机路径，同时支持相对路径，相当于docker run中的`-v`

`:ro`定义容器中的只读目录

```yaml
version: '3'
services:
  web:
    volumes:
      -v ./config:/root/config
      -v /home/xx/config:/root/config
      -v ./nginx.conf:/etc/nginx/nginx.conf:ro
      
version: '3'
services:
  web:
    volumes:
      -v webconfig:/root/config # 具名卷

volumes:
	webconfig: # 声明 自动创建该卷名，但他会在之前加入项目名
		external: # 使用外部卷名
			false # true确定使用指定卷名 注意：一旦使用自定义卷名启动服务之前必须创建该卷名
	# 必须在volumes 里面声明 才能在volumes 里面使用
```

 

### 11、entrypoint

指定服务容器启动后执行的入口文件

```yaml
version: '3'
services:
  web:
    entrypoint: /root/start.sh
```

 

### 12、working_dir

指定容器中工作目录, 也可在Dockerfile中指定

```yaml
version: '3'
services:
  web:
    working_dir: /root/proj
```

 

### 13、hostname

指定容器主机名，相当于docker run中的`-h`

```yaml
version: '3'
services:
  web:
    hostname: web-1
```

 

### 14、restart

指定重启策略，相当于docker run中的`--restart`

```yaml
version: '3'
services:
  web:
    restart: always
```

### 15、引用环境变量

Compose模板文件支持动态读取宿主机的系统环境变量和当前目录下 .env 文件中的变量。

例如，下面Compose文件将从运行它的环境中读取变量`${MONGO_VERSION}`的值，并写入执行的指令中

```yaml
version: '3'
services:
  db: 
    image: "mongo:${MONGO_VERSION}"
```

 

### 16、expose

暴露端口，但不映射到宿主机，只被连接的服务访问。仅可以指定内部端口为参数。

```yaml
version: '3'
services: 
  mysql:
    expose:
      - "3306"
```

 

### 17、extra_hosts

类似Docker中的--add-host参数，指定额外的host名称映射信息。会在启动后的服务容器中/etc/hosts文件中添加一个条目。如：8.8.8.8 googledns

```yaml
version: '3'
services: 
  mysql:
    extra_hosts:
      - "baidu:8000"
```

 

### 18、healthcheck

通过命令检查容器是否正常运行

```yaml
version: '3'
services: 
  mysql:
    healthcheck:
      test: ["CMD", "curl", "-f", "http://localhost"]
      interval: 1m30s
      timeout: 10s
      retries: 3
```

 

### 19、links

连接到其他容器。注意：不推荐使用该指令。

应该使用docker network，建立网络，而docker run --network来连接特定网络。

或者使用version: '2' 和更高版本的docker-compose.yml直接定义自定义网络并使用。

 

### 20、ulimits

指定容器的ulimits限制值。

例如，指定最大进程数为65535，指定文件句柄数为20000（软限制，应用可以随时修改，不能超过硬限制）和 40000（系统硬限制，只能root用户提高）

```yaml
version: '3'
services: 
  mysql:
    ulimits:
      nproc: 65535
      nofile:
        soft: 20000
        hard: 40000
```

 

### 21、user

指定容器中运行应用的用户名

```yaml
version: '3'
services: 
  mysql:
    user: ubuntu
```

 

### 22、links

链接到其它服务的中的容器，可以指定服务名称也可以指定链接别名（SERVICE：ALIAS)，与 Docker 客户端的 --link 有一样效果，会连接到其它服务中的容器。

```yaml
version: '3'
services: 
    web:
      links:
       - db
       - db:database
       - redis
```

 

### 23、depends_on

容器中服务之间的依赖关系，依赖关系会导致以下行为：

- docker-compose up以依赖顺序启动服务。在以下示例中，db并redis在之前启动web。
- docker-compose up SERVICE自动包含SERVICE依赖项。在以下示例中，docker-compose up web还创建并启动db和redis。
- docker-compose stop按依赖顺序停止服务。在以下示例中，web在db和之前停止redis

```yaml
version: "3.7"
services:
  web:
    build: .
    depends_on:
      - db # 服务名 依赖于db db启动后才可以启动web 服务
      - redis
  redis:
    image:redis
  db:
    image:postgres
    
    # web 服务会在db 和 redis服务完全启动后才会启动
```

 Compose 命令说明

## 命令对象与格式

对于 Compose 来说，大部分命令的对象既可以是项目本身，也可以指定为项目中的服务或者容器。如果没有特别的说明，命令对象将是项目，这意味着项目中所有的服务都会受到命令影响。

执行 `docker-compose [COMMAND] --help` 或者 `docker-compose help [COMMAND]` 可以查看具体某个命令的使用格式。

`docker-compose` 命令的基本的使用格式是

```bash
docker-compose [-f=<arg>...] [options] [COMMAND] [ARGS...]
```

## 命令选项

- `-f, --file FILE` 指定使用的 Compose 模板文件，默认为 `docker-compose.yml`，可以多次指定。
- `-p, --project-name NAME` 指定项目名称，默认将使用所在目录名称作为项目名。
- `--x-networking` 使用 Docker 的可拔插网络后端特性
- `--x-network-driver DRIVER` 指定网络后端的驱动，默认为 `bridge`
- `--verbose` 输出更多调试信息。
- `-v, --version` 打印版本并退出。

## 命令使用说明

### `build`

格式为 `docker-compose build [options] [SERVICE...]`。

构建（重新构建）项目中的服务容器。

服务容器一旦构建后，将会带上一个标记名，例如对于 web 项目中的一个 db 容器，可能是 web_db。

可以随时在项目目录下运行 `docker-compose build` 来重新构建服务。

选项包括：

- `--force-rm` 删除构建过程中的临时容器。
- `--no-cache` 构建镜像过程中不使用 cache（这将加长构建过程）。
- `--pull` 始终尝试通过 pull 来获取更新版本的镜像。

### `config`

验证 Compose 文件格式是否正确，若正确则显示配置，若格式错误显示错误原因。

### `down`

此命令将会停止 `up` 命令所启动的容器，并移除网络

### `exec`

进入指定的容器。

### `help`

获得一个命令的帮助。

### `images`

列出 Compose 文件中包含的镜像。

### `kill`

格式为 `docker-compose kill [options] [SERVICE...]`。

通过发送 `SIGKILL` 信号来强制停止服务容器。

支持通过 `-s` 参数来指定发送的信号，例如通过如下指令发送 `SIGINT` 信号。

```bash
$ docker-compose kill -s SIGINT
```

### `logs`

格式为 `docker-compose logs [options] [SERVICE...]`。

查看服务容器的输出。默认情况下，docker-compose 将对不同的服务输出使用不同的颜色来区分。可以通过 `--no-color` 来关闭颜色。

该命令在调试问题的时候十分有用。

### `pause`

格式为 `docker-compose pause [SERVICE...]`。

暂停一个服务容器。

### `port`

格式为 `docker-compose port [options] SERVICE PRIVATE_PORT`。

打印某个容器端口所映射的公共端口。

选项：

- `--protocol=proto` 指定端口协议，tcp（默认值）或者 udp。
- `--index=index` 如果同一服务存在多个容器，指定命令对象容器的序号（默认为 1）。

### `ps`

格式为 `docker-compose ps [options] [SERVICE...]`。

列出项目中目前的所有容器。

选项：

- `-q` 只打印容器的 ID 信息。

### `pull`

格式为 `docker-compose pull [options] [SERVICE...]`。

拉取服务依赖的镜像。

选项：

- `--ignore-pull-failures` 忽略拉取镜像过程中的错误。

### `push`

推送服务依赖的镜像到 Docker 镜像仓库。

### `restart`

格式为 `docker-compose restart [options] [SERVICE...]`。

重启项目中的服务。

选项：

- `-t, --timeout TIMEOUT` 指定重启前停止容器的超时（默认为 10 秒）。

### `rm`

格式为 `docker-compose rm [options] [SERVICE...]`。

删除所有（停止状态的）服务容器。推荐先执行 `docker-compose stop` 命令来停止容器。

选项：

- `-f, --force` 强制直接删除，包括非停止状态的容器。一般尽量不要使用该选项。
- `-v` 删除容器所挂载的数据卷。

### `run`

格式为 `docker-compose run [options] [-p PORT...] [-e KEY=VAL...] SERVICE [COMMAND] [ARGS...]`。

在指定服务上执行一个命令。

例如：

```bash
$ docker-compose run ubuntu ping docker.com
```

将会启动一个 ubuntu 服务容器，并执行 `ping docker.com` 命令。

默认情况下，如果存在关联，则所有关联的服务将会自动被启动，除非这些服务已经在运行中。

该命令类似启动容器后运行指定的命令，相关卷、链接等等都将会按照配置自动创建。

两个不同点：

- 给定命令将会覆盖原有的自动运行命令；
- 不会自动创建端口，以避免冲突。

如果不希望自动启动关联的容器，可以使用 `--no-deps` 选项，例如

```bash
$ docker-compose run --no-deps web python manage.py shell
```

将不会启动 web 容器所关联的其它容器。

选项：

- `-d` 后台运行容器。
- `--name NAME` 为容器指定一个名字。
- `--entrypoint CMD` 覆盖默认的容器启动指令。
- `-e KEY=VAL` 设置环境变量值，可多次使用选项来设置多个环境变量。
- `-u, --user=""` 指定运行容器的用户名或者 uid。
- `--no-deps` 不自动启动关联的服务容器。
- `--rm` 运行命令后自动删除容器，`d` 模式下将忽略。
- `-p, --publish=[]` 映射容器端口到本地主机。
- `--service-ports` 配置服务端口并映射到本地主机。
- `-T` 不分配伪 tty，意味着依赖 tty 的指令将无法运行。

### `scale`

格式为 `docker-compose scale [options] [SERVICE=NUM...]`。

设置指定服务运行的容器个数。

通过 `service=num` 的参数来设置数量。例如：

```bash
$ docker-compose scale web=3 db=2
```

将启动 3 个容器运行 web 服务，2 个容器运行 db 服务。

一般的，当指定数目多于该服务当前实际运行容器，将新创建并启动容器；反之，将停止容器。

选项：

- `-t, --timeout TIMEOUT` 停止容器时候的超时（默认为 10 秒）。

### `start`

格式为 `docker-compose start [SERVICE...]`。

启动已经存在的服务容器。

### `stop`

格式为 `docker-compose stop [options] [SERVICE...]`。

停止已经处于运行状态的容器，但不删除它。通过 `docker-compose start` 可以再次启动这些容器。

选项：

- `-t, --timeout TIMEOUT` 停止容器时候的超时（默认为 10 秒）。

### `top`

查看各个服务容器内运行的进程。

### `unpause`

格式为 `docker-compose unpause [SERVICE...]`。

恢复处于暂停状态中的服务。

### `up`

格式为 `docker-compose up [options] [SERVICE...]`。

该命令十分强大，它将尝试自动完成包括构建镜像，（重新）创建服务，启动服务，并关联服务相关容器的一系列操作。

链接的服务都将会被自动启动，除非已经处于运行状态。

可以说，大部分时候都可以直接通过该命令来启动一个项目。

默认情况，`docker-compose up` 启动的容器都在前台，控制台将会同时打印所有容器的输出信息，可以很方便进行调试。

当通过 `Ctrl-C` 停止命令时，所有容器将会停止。

如果使用 `docker-compose up -d`，将会在后台启动并运行所有的容器。一般推荐生产环境下使用该选项。

默认情况，如果服务容器已经存在，`docker-compose up` 将会尝试停止容器，然后重新创建（保持使用 `volumes-from` 挂载的卷），以保证新启动的服务匹配 `docker-compose.yml` 文件的最新内容。如果用户不希望容器被停止并重新创建，可以使用 `docker-compose up --no-recreate`。这样将只会启动处于停止状态的容器，而忽略已经运行的服务。如果用户只想重新部署某个服务，可以使用 `docker-compose up --no-deps -d ` 来重新创建服务并后台停止旧服务，启动新服务，并不会影响到其所依赖的服务。

选项：

- `-d` 在后台运行服务容器。
- `--no-color` 不使用颜色来区分不同的服务的控制台输出。
- `--no-deps` 不启动服务所链接的容器。
- `--force-recreate` 强制重新创建容器，不能与 `--no-recreate` 同时使用。
- `--no-recreate` 如果容器已经存在了，则不重新创建，不能与 `--force-recreate` 同时使用。
- `--no-build` 不自动构建缺失的服务镜像。
- `-t, --timeout TIMEOUT` 停止容器时候的超时（默认为 10 秒）。

### `version`

格式为 `docker-compose version`。

打印版本信息。

#Docker Swarm