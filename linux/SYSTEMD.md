# 深入了解 Systemd 之概要介绍

[Linux](https://tlanyan.me/category/linux/) [网络转载](https://tlanyan.me/category/forward/)[tlanyan](https://tlanyan.me/author/tlanyan/)2020年11月8日

> 本文转载自：https://george.betterde.com/20190602.html，个人觉得是写得非常好的systemd介绍教程

Systemd 是 Linux 系统的一中 Init 用户程序和基础组件的集合，由 Lennart Poettering 带头开发并在 LGPL 2.1 及后续版本许可证下开源发布，目前 [Systemd](https://tlanyan.me/tag/systemd/) 已纳入众多 [Linux](https://tlanyan.me/category/linux/) 发行版的软件源中。

## Linux 引导原理

Linux 内核加载启动后，用户空间的第一个进程就是初始化进程，这个程序的物理文件约定位于 `/sbin/init`，当然也可以通过传递内核参数来让内核启动指定的程序。这个进程的特点是进程号为1，代表第一个运行的用户空间进程。不同发行版采用了不同的启动程序，主要有以下几种主流选择：

1. 以 Ubuntu 为代表的 Linux 发行版采用 Upstart。
2. 以7.0版本之前的 CentOS 为代表的 System V Init。
3. CentOS7.0 版本的 Systemd。

## Systemd

Systemd 是 Linux 系统的一中 Init 用户程序和基础组件的集合，由 Lennart Poettering 带头开发并在 LGPL 2.1 及后续版本许可证下开源发布。Systemd 提供了一个系统和服务管理器，运行为 PID 1 并负责启动其它程序。其开发目标是提供更优秀的框架以表示系统服务间的依赖关系，并以此实现系统初始化时服务的并行启动，同时达到降低Shell的系统开销的效果，最终代替现在常用的 System V 与 BSD 风格 Init 程序。

Systemd 使用 socket 和 D-Bus 来开启服务，提供基于守护进程的按需启动策略，保留了 Linux Cgroups 的进程追踪功能，支持快照和系统状态恢复，维护挂载和自挂载点，实现了各服务间基于从属关系的一个更为精细的逻辑控制，拥有前卫的并行性能。Systemd 无需经过任何修改便可以替代 System V Init。Systemd 已纳入众多 Linux 发行版的软件源中，Fedora 15及后续版本都采用的 Systemd 作为 Linux 下的默认 Init 程序。

功能包括：

- 支持并行化任务；
- 同时采用 socket 式与 D-Bus 总线式激活服务；
- 按需启动守护进程（daemon）；
- 利用 Linux 的 Cgroups 监视进程；
- 支持快照和系统恢复；
- 维护挂载点和自动挂载点；
- 各服务间基于依赖关系进行精密控制。

### 从 System V Init 到 Systemd

System V Init 守护进程是一个基于运行级别的系统，它使用运行级别（单用户、多用户以及其他更多级别）和链接（位于 `/etc/rc?.d` 目录中，分别链接到 `/etc/init.d` 中的 Init 脚本）来启动和关闭系统服务。Upstart Init 守护进程则是基于事件的系统，它使用事件来启动和关闭系统服务。

近年来，Linux 系统的 Init 进程经历了两次重大的演进，传统的 System V Init 已经淡出历史舞台，新的 Init 系统 UpStart 和 Systemd 各有特点，而越来越多的 Linux 发行版采纳了 Systemd。

### 设计理念

#### 尽可能启动更少的进程

当 SysV-init 程序初始化系统时，必须将所有可能用到的后台服务进程全部运行起来。而用户需要等待系统将所有的服务都启动完成之后，才能够登陆。这种做法会带来两个问题：系统的启动时间过长和系统的资源浪费。

Systemd 提供了服务按需启动的能力，使得特定的服务只有在被真正请求时才会启动。特别是与具体硬件相关的服务，比如蓝牙服务仅在蓝牙适配器被插入时才需要运行，打印服务仅在打印机链接或程序要打印时才需要运行，甚至 sshd 服务也只需要用户在使用 SSH 连接到服务器时才需要启动。这种能力建立在 Systemd 对 DBus 总线或特定 Socket 端口监听的特性上的，这种设计相比于传统启动程序具有颠覆性进步。

#### 尽可能将进程并行启动

在 SysV-init 时代，将每个服务项目编号依次执行启动脚本。后来 Ubuntu 的 UPstart 解决了没有直接依赖启动项之间的并行启动。而 Systemd 通过 Socket 缓存、DBus 缓存和建立临时挂载点等方法进一步解决了启动进程直接的依赖，做到了所有系统服务并发启动。这一设计同样是 Systemd 独具特色的创意。对于用户定义的服务，Systemd 允许配置其启动依赖的项目，从而保证服务必须按照必要的顺序运行。

#### 跟踪和管理进程的生命周期

在 Systemd 之前的主流应用管理服务都是使用 “进程树” 来跟踪应用的继承关系，而进程的父子关系很容易通过 `两次 fork` 的方法来脱离。

而 Systemd 则提出通过 CGroup 跟踪进程关系，弥补了这个缺漏。通过 CGroup 不仅能够实现服务之间的访问隔离，限制特定应用程序对系统资源的防伪配额，还能更精确的管理服务的生命周期。

#### 统一管理服务日志

Systemd 是一系列工具的集合，包括了一个专用的系统日志管理服务：Journald。这个服务的设计初衷是克服现有 Syslog 服务的日志内容易伪造和日志格式不统一等缺点，现在已经纳入了 Systemd 的标准姊妹服务中。Journald 用二进制格式保存所有日志信息，因而日志内容很难被手工伪造。Journald 还提供了一个 journalctl 命令来查看日志信息，这样使得不同服务输出的日志具有相同的排版格式，便于数据的二次处理。

### 使用 Systemd 的发行版本

Systemd 已纳入众多 Linux 发行版的软件源中，以下简表

默认init程序为systemd的发行版：

- Fedora 15及后续版本
- Mageia 2
- Mandriva 2011
- openSUSE 12.1及后续版本
- Arch Linux 在2012年10月13日将 systemd-sysvcompat 纳入 base 软件组，自此 Arch Linux 默认安装完即以 Systemd 为 Init 程序，同时也提供了与 Arch 自带启动脚本兼容用的 Systemd 启动脚本包以方便用户，使用户能“开箱即用”；
- Chakra GNU/Linux，在2012年10月的光碟映像档发布后默认使用 Systemd

可以使用systemd的发行版：

- Debian GNU/Linux，于“testing”分支源中提供
- Gentoo，同 Openrc 一起被 Gentoo 官方支持

除此以外，Systemd 已由 Lennart Poettering 提请纳入 GNOME 3.2 的外部依赖关系列表，而这意味着所有使用 GNOME 的发行版都应该使用 Systemd ，最低限度来说也必须将其作为配置选项之一。

### Systemd 的服务管理

#### Unit 和 Target

##### 单元类型

Unit 是 Systemd 管理服务的基本单元，可以认为每个服务就是一个 Unit，并使用一个 Unit 文件定义。在 Unit 文件中需要包含相应服务的描述、属性以及需要运行服务的命令。

Systemd主要有如下单元类型：

- 系统服务（.service）；
- 挂载点（.mount）；
- 自动挂载点（.automount）；
- 套接字（.socket）；
- 系统设备（.device）；
- 交换分区（.swap）；
- 文件路径（.path）；
- 启动目标（.target）；
- 计时器（.timer）；
- 不是由 Systemd 启动的外部进程（.scope）;
- 进程组（.slice）;
- Systemd 快照（.snapshot）;

##### Target

Target 是 Systemd 中用于指定服务组的启动方式，相当于 SysV-init 中的 `运行级别`。每次系统启动时都会运行与当前系统具有同级别 Target 关联的所有服务，如果服务不需要跟随系统自动启动，则完全可以忽略这个 Target 的内容。通常来说，大多数 Linux 用户平时使用的都是 `多用户模式` 这个级别，对应的 Target 值为 `multi-user.target`，它又一个等效的可用值是 `default.target`。

```
# 查看当前系统的所有 Target
$ systemctl list-unit-files --type=target

# 查看一个 Target 包含的所有 Unit
$ systemctl list-dependencies multi-user.target

# 查看启动时的默认 Target
$ systemctl get-default

# 设置启动时的默认 Target
$ sudo systemctl set-default multi-user.target

# 切换 Target 时，默认不关闭前一个 Target 启动的进程，
# systemctl isolate 命令改变这种行为，
# 关闭前一个 Target 里面所有不属于后一个 Target 的进程
$ sudo systemctl isolate multi-user.target
```

前面说过，Systemd 使用 Target 取代了 System V Init 的运行级的概念。

| 运行级别     | Systemd 目标                                          | 备注                                                      |
| ------------ | ----------------------------------------------------- | --------------------------------------------------------- |
| 0            | runlevel0.target, poweroff.target                     | 关闭系统                                                  |
| 1, s, single | runlevel1.target, rescue.target                       | 单用户模式                                                |
| 2, 4         | runlevel2.target, runlevel4.target, multi-user.target | 用户定义/域特定运行级别。默认等同于 3                     |
| 3            | runlevel3.target, multi-user.target                   | 多用户，非图形化。用户可以通过多个控制台或网络登录        |
| 5            | runlevel5.target, graphical.target                    | 多用户，图形化。通常为所有运行级别 3 的服务外加图形化登录 |
| 6            | runlevel6.target, reboot.target                       | 重启                                                      |
| emergency    | emergency.target                                      | 紧急 Shell                                                |

### 日志管理

Systemd 统一管理所有 Unit 的启动日志。带来的好处就是，可以只用 `journalctl` 一个命令，查看所有日志（内核日志和应用日志）。日志的配置文件是 `/etc/systemd/journald.conf`。

```
# 查看所有日志（默认情况下 ，只保存本次启动的日志）
$ sudo journalctl

# 查看内核日志（不显示应用日志）
$ sudo journalctl -k

# 查看系统本次启动的日志
$ sudo journalctl -b
$ sudo journalctl -b -0

# 查看上一次启动的日志（需更改设置）
$ sudo journalctl -b -1

# 查看指定时间的日志
$ sudo journalctl --since="2012-10-30 18:17:16"
$ sudo journalctl --since "20 min ago"
$ sudo journalctl --since yesterday
$ sudo journalctl --since "2015-01-10" --until "2015-01-11 03:00"
$ sudo journalctl --since 09:00 --until "1 hour ago"

# 显示尾部的最新10行日志
$ sudo journalctl -n

# 显示尾部指定行数的日志
$ sudo journalctl -n 20

# 实时滚动显示最新日志
$ sudo journalctl -f

# 查看指定服务的日志
$ sudo journalctl /usr/lib/systemd/systemd

# 查看指定进程的日志
$ sudo journalctl _PID=1

# 查看某个路径的脚本的日志
$ sudo journalctl /usr/bin/bash

# 查看指定用户的日志
$ sudo journalctl _UID=33 --since today

# 查看某个 Unit 的日志
$ sudo journalctl -u nginx.service
$ sudo journalctl -u nginx.service --since today

# 实时滚动显示某个 Unit 的最新日志
$ sudo journalctl -u nginx.service -f

# 合并显示多个 Unit 的日志
$ journalctl -u nginx.service -u php-fpm.service --since today

# 查看指定优先级（及其以上级别）的日志，共有8级
# 0: emerg
# 1: alert
# 2: crit
# 3: err
# 4: warning
# 5: notice
# 6: info
# 7: debug
$ sudo journalctl -p err -b

# 日志默认分页输出，--no-pager 改为正常的标准输出
$ sudo journalctl --no-pager

# 以 JSON 格式（单行）输出
$ sudo journalctl -b -u nginx.service -o json

# 以 JSON 格式（多行）输出，可读性更好
$ sudo journalctl -b -u nginx.serviceqq
 -o json-pretty

# 显示日志占据的硬盘空间
$ sudo journalctl --disk-usage

# 指定日志文件占据的最大空间
$ sudo journalctl --vacuum-size=1G

# 指定日志文件保存多久
$ sudo journalctl --vacuum-time=1years
```

### 配置和使用

如开头简介中所说，你打算开发一个新的系统服务，就必须了解如何让这个服务能够被 Systemd 管理。这需要您注意以下这些要点：

- 后台服务进程代码不需要执行两次派生来实现后台守护进程，只需要实现服务本身的主循环即可；
- 不要调用 setsid()，交给 Systemd 处理；
- 不再需要维护 PID 文件；
- Systemd 提供了日志功能，服务进程只需要输出到 stderr 即可，无需使用 syslog；
- 处理信号 SIGTERM，这个信号的唯一正确作用就是停止当前服务，不要做其他的事情；
- SIGHUP 信号的作用是重启服务；
- 需要套接字的服务，不要自己创建套接字，让 Systemd 传入套接字；
- 使用 sd_notify() 函数通知 Systemd 服务自己的状态改变。一般地，当服务初始化结束，进入服务就绪状态时，可以调用它。

### 单元文件存放路径

```
$ sudo systemctl show --property=UnitPath

# 按优先级从低到高显示加载目录
UnitPath=/etc/systemd/system /run/systemd/system /run/systemd/generator /usr/local/lib/systemd/system /usr/lib/systemd/system /run/systemd/generator.late
```

- /usr/lib/systemd/system/：软件包安装的单元
- /etc/systemd/system/：系统管理员安装的单元

### 命令汇总

```
#重载单元
$ sudo systemctl daemon-reload

#立即激活单元
$ sudo systemctl start UNIT

#立即停止单元
$ sudo systemctl stop UNIT

#立即重启单元
$ sudo systemctl restart UNIT

#重新加载配置
$ sudo systemctl reload UNIT

#输出单元运行状态
$ sudo systemctl status UNIT

#检查单元是否配置为自动启动
$ sudo systemctl is-enabled UNIT

#开机自动激活单元，根据[Install]设置的 WantedBy 会在 /etc/systemd/system/TARGET.wants/ 目录中创建软链
$ sudo systemctl enable UNIT

#设置单元为自动启动并立即启动这个单元
$ sudo systemctl enable --now UNIT

#取消开机自动激活单元
$ sudo systemctl disable UNIT

#禁用一个单元（禁用后，间接启动也是不可能的）
$ sudo systemctl mask UNIT

#取消禁用一个单元
$ sudo systemctl unmask UNIT

#显示单元的手册页（必须由单元文件提供）
$ sudo systemctl help UNIT

#列出一个 Unit 的所有依赖，默认不会展开显示。如果要展开 Target，就需要使用--all参数。
$ sudo systemctl list-dependencies [--all] UNIT

#列出所有配置文件
$ sudo systemctl list-unit-files

#列出指定类型的配置文件
$ sudo systemctl list-unit-files --type=service
```

## 电源管理命令

```
#重启
$ sudo systemctl reboot

#退出系统并关闭电源
$ sudo systemctl poweroff

#待机
$ sudo systemctl suspend

#休眠
$ sudo systemctl hibernate

#混合休眠模式（同时休眠到硬盘并待机）
$ sudo systemctl hybrid-sleep
```

Systemd 的强大之处，还需在实践中自行体会。后面的文章也会陆续记录一些实践中的心得……