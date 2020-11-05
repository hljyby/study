# Debian平台

- dpkg 命令
  - 用来安装离线安装包，不会自动安装依赖
- apt 命令
  - 可以离线，或者在线安装软件，并自动安装依赖
- 安装包都是.deb
- 代表作  Ubuntu

# Fedora 平台

- rpm  
  - 用来安装离线安装包，不会自动安装依赖
  - rpm -qa 遍历所有
  - rpm -e 删除
  - rpm -ivh 查看详细信息
- yum
  - 可以离线，或者在线安装软件，并自动安装依赖
  - yum install <安装包名>
  - yum list install 遍历安装列表 
  - yum remove vim 移除
  - yum check-update 检查更新 
  - yum update
- 安装包 都是.rpm
- 代表作是CentOs

# 安装软件的三种方式

- 下载离线安装包—————— dpkg/rpm
- 直接在线安装    —————— apt/yum
- 把代码的源代码下载下来，然后编译安装   —————— tgz 源代码 （类似window的zip / rar 压缩包）

# Linux 文件系统

- linux 就一个盘符，只有根路径

- bin 简写 （binary 二进制） 里面存的都是命令 二进制可执行文件

- etc 配置文件 

- Home 表示用户的家目录,新建一个用户就会在home里新建一个文件夹

- Boot 系统启动相关时所需要的文件

- lib（64）用来存放系统最基本的动态链接共享库

-  lost+found 这个目录一般情况下是空的，当系统非法关机后，这里会存储那些没有来的 急保存的文件

- media Linux系统自动识别一些设备，如光驱，U盘

- opt 如果你打算装一些第三方软件的话，你可以考虑把这些软件，装到这里面来、

- root root用户的家目录

- sbin 命令 用这个里面的命令要加sudo 才可以调用

  ## linux下的文件结构，看看每个文件夹都是干吗用的

- /bin 二进制可执行命令 

- /dev 设备特殊文件 

- /etc 系统管理和配置文件 

- /etc/rc.d 启动的配置文件和脚本 

- /home 用户主目录的基点，比如用户user的主目录就是/home/user，可以用~user表示 

- /lib 标准程序设计库，又叫动态链接共享库，作用类似windows里的.dll文件 

- /sbin 系统管理命令，这里存放的是系统管理员使用的管理程序 

- /tmp 公用的临时文件存储点 

- /root 系统管理员的主目录（呵呵，特权阶级） 

- /mnt 系统提供这个目录是让用户临时挂载其他的文件系统。 

- /lost+found 这个目录平时是空的，系统非正常关机而留下“无家可归”的文件（windows下叫什么.chk）就在这里 

- /proc 虚拟的目录，是系统内存的映射。可直接访问这个目录来获取系统信息。 

- /var 某些大文件的溢出区，比方说各种服务的日志文件 

- /usr 最庞大的目录，要用到的应用程序和文件几乎都在这个目录。其中包含： 

  - /usr/x11r6 存放x window的目录 

  - /usr/bin 众多的应用程序 

  - /usr/sbin 超级用户的一些管理程序 

  - /usr/doc linux文档 

  - /usr/include linux下开发和编译应用程序所需要的头文件 

  - /usr/lib 常用的动态链接库和软件包的配置文件 

  - /usr/man 帮助文档 

  - /usr/src 源代码，linux内核的源代码就放在/usr/src/linux里 

  - /usr/local/bin 本地增加的命令 

  - /usr/local/lib 本地增加的库根文件系统

- \1. /bin目录 

  / b i n目录包含了引导启动所需的命令或普通用户可能用的命令(可能在引导启动后)。这些 

  命令都是二进制文件的可执行程序( b i n是b i n a r y - -二进制的简称)，多是系统中重要的系统文件。 

  \2. /sbin目录 

  / s b i n目录类似/bin ，也用于存储二进制文件。因为其中的大部分文件多是系统管理员使 

  用的基本的系统程序，所以虽然普通用户必要且允许时可以使用，但一般不给普通用户使用。 

  \3. /etc目录 

  / e t c目录存放着各种系统配置文件，其中包括了用户信息文件/ e t c / p a s s w d，系统初始化文 

  件/ e t c / r c等。l i n u x正是*这些文件才得以正常地运行。 

  \4. /root目录 

  /root 目录是超级用户的目录。 

  \5. /lib目录 

  / l i b目录是根文件系统上的程序所需的共享库，存放了根文件系统程序运行所需的共享文 

  件。这些文件包含了可被许多程序共享的代码，以避免每个程序都包含有相同的子程序的副 

  本，故可以使得可执行文件变得更小，节省空间。 

  \6. /lib/modules 目录 

  /lib/modules 目录包含系统核心可加载各种模块，尤其是那些在恢复损坏的系统时重新引 

  导系统所需的模块(例如网络和文件系统驱动)。 

  \7. /dev目录 

  / d e v目录存放了设备文件，即设备驱动程序，用户通过这些文件访问外部设备。比如，用 

  户可以通过访问/ d e v / m o u s e来访问鼠标的输入，就像访问其他文件一样。 

  \8. /tmp目录 

  /tmp 目录存放程序在运行时产生的信息和数据。但在引导启动后，运行的程序最好使用 

  / v a r / t m p来代替/tmp ，因为前者可能拥有一个更大的磁盘空间。 

  \9. /boot目录 

  / b o o t目录存放引导加载器(bootstrap loader)使用的文件，如l i l o，核心映像也经常放在这里， 

  而不是放在根目录中。但是如果有许多核心映像，这个目录就可能变得很大，这时使用单独的 

  文件系统会更好一些。还有一点要注意的是，要确保核心映像必须在i d e硬盘的前1 0 2 4柱面内。 

  \10. /mnt目录 

  / m n t目录是系统管理员临时安装( m o u n t )文件系统的安装点。程序并不自动支持安装到 

  /mnt 。/mnt 下面可以分为许多子目录，例如/mnt/dosa 可能是使用m s d o s文件系统的软驱， 

  而/mnt/exta 可能是使用e x t 2文件系统的软驱，/mnt/cdrom 光驱等等。 

  \11. /proc, /usr,/var,/home目录 

  其他文件系统的安装点。 

  下面详细介绍； 

  /etc文件系统 

  /etc 目录包含各种系统配置文件，下面说明其中的一些。其他的你应该知道它们属于哪个 

  程序，并阅读该程序的m a n页。许多网络配置文件也在/etc 中。 

  \1. /etc/rc或/etc/rc.d或/etc/rc?.d 

  启动、或改变运行级时运行的脚本或脚本的目录。 

  \2. /etc/passwd 

  用户数据库，其中的域给出了用户名、真实姓名、用户起始目录、加密口令和用户的其 

  他信息。 

  \3. /etc/fdprm 

  软盘参数表，用以说明不同的软盘格式。可用setfdprm 进行设置。更多的信息见s e t f d p r m 

  的帮助页。 

  \4. /etc/fstab 

  指定启动时需要自动安装的文件系统列表。也包括用swapon -a启用的s w a p区的信息。 

  \5. /etc/group 

  类似/etc/passwd ，但说明的不是用户信息而是组的信息。包括组的各种数据。 

  \6. /etc/inittab 

  init 的配置文件。 

  \7. /etc/issue 

  包括用户在登录提示符前的输出信息。通常包括系统的一段短说明或欢迎信息。具体内 

  容由系统管理员确定。 

  \8. /etc/magic 

  “f i l e”的配置文件。包含不同文件格式的说明，“f i l e”基于它猜测文件类型。 

  \9. /etc/motd 

  m o t d是message of the day的缩写，用户成功登录后自动输出。内容由系统管理员确定。 

  常用于通告信息，如计划关机时间的警告等。 

  \10. /etc/mtab 

  当前安装的文件系统列表。由脚本( s c r i t p )初始化，并由mount 命令自动更新。当需要一 

  个当前安装的文件系统的列表时使用(例如df 命令)。 

  \11. /etc/shadow 

  在安装了影子( s h a d o w )口令软件的系统上的影子口令文件。影子口令文件将/ e t c / p a s s w d 

  文件中的加密口令移动到/ e t c / s h a d o w中，而后者只对超级用户( r o o t )可读。这使破译口令更困 

  难，以此增加系统的安全性。 

  \12. /etc/login.defs 

  l o g i n命令的配置文件。 

  \13. /etc/printcap 

  类似/etc/termcap ，但针对打印机。语法不同。 

  \14. /etc/profile 、/ e t c / c s h . l o g i n、/etc/csh.cshrc 

  登录或启动时b o u r n e或c shells执行的文件。这允许系统管理员为所有用户建立全局缺省环境。 

  \15. /etc/securetty 

  确认安全终端，即哪个终端允许超级用户( r o o t )登录。一般只列出虚拟控制台，这样就不 

  可能(至少很困难)通过调制解调器( m o d e m )或网络闯入系统并得到超级用户特权。 

  \16. /etc/shells 

  列出可以使用的s h e l l。chsh 命令允许用户在本文件指定范围内改变登录的s h e l l。提供一 

  台机器f t p服务的服务进程ftpd 检查用户s h e l l是否列在/etc/shells 文件中，如果不是，将不允 

  许该用户登录。 

  \17. /etc/termcap 

  终端性能数据库。说明不同的终端用什么“转义序列”控制。写程序时不直接输出转义 

  序列(这样只能工作于特定品牌的终端)，而是从/etc/termcap 中查找要做的工作的正确序列。 

  这样，多数的程序可以在多数终端上运行。 

  /dev文件系统 

  /dev 目录包括所有设备的设备文件。设备文件用特定的约定命名，这在设备列表中说明。 

  设备文件在安装时由系统产生，以后可以用/dev/makedev 描述。/ d e v / m a k e d e v.local 是 

  系统管理员为本地设备文件(或连接)写的描述文稿(即如一些非标准设备驱动不是标准 

  makedev 的一部分)。下面简要介绍/ d e v下一些常用文件。 

  \1. /dev/console 

  系统控制台，也就是直接和系统连接的监视器。 

  \2. /dev/hd 

  i d e硬盘驱动程序接口。如： / d e v / h d a指的是第一个硬盘， h a d 1则是指/ d e v / h d a的第一个 

  分区。如系统中有其他的硬盘，则依次为/ d e v / h d b、/ d e v / h d c、. . . . . .；如有多个分区则依次为 

  h d a 1、h d a 2 . . . . . . 

  \3. /dev/sd 

  s c s i磁盘驱动程序接口。如有系统有s c s i硬盘，就不会访问/ d e v / h a d，而会访问/ d e v / s d a。 

  \4. /dev/fd 

  软驱设备驱动程序。如： / d e v / f d 0指系统的第一个软盘，也就是通常所说的a：盘， 

  / d e v / f d 1指第二个软盘，. . . . . .而/ d e v / f d 1 h 1 4 4 0则表示访问驱动器1中的4 . 5高密盘。 

  \5. /dev/st 

  s c s i磁带驱动器驱动程序。 

  \6. /dev/tty 

  提供虚拟控制台支持。如： / d e v / t t y 1指的是系统的第一个虚拟控制台， / d e v / t t y 2则是系统 

  的第二个虚拟控制台。 

  \7. /dev/pty 

  提供远程登陆伪终端支持。在进行te l n e t登录时就要用到/ d e v / p t y设备。 

  \8. /dev/ttys 

  计算机串行接口，对于d o s来说就是“ c o m 1”口。 

  \9. /dev/cua 

  计算机串行接口，与调制解调器一起使用的设备。 

  \10. /dev/null 

  “黑洞”，所有写入该设备的信息都将消失。例如：当想要将屏幕上的输出信息隐藏起来 

  时，只要将输出信息输入到/ d e v / n u l l中即可。 

  /usr文件系统 

  /usr 是个很重要的目录，通常这一文件系统很大，因为所有程序安装在这里。/usr 里的 

  所有文件一般来自l i n u x发行版( d i s t r i b u t i o n )；本地安装的程序和其他东西在/usr/local 下，因为这样可以在升级新版系统或新发行版时无须重新安装全部程序。/usr 目录下的许多内容是 

  可选的，但这些功能会使用户使用系统更加有效。/ u s r可容纳许多大型的软件包和它们的配置 

  文件。下面列出一些重要的目录(一些不太重要的目录被省略了)。 

  \1. /usr/x11r6 

  包含x wi n d o w系统的所有可执行程序、配置文件和支持文件。为简化x的开发和安装， 

  x的文件没有集成到系统中。x wi n d o w系统是一个功能强大的图形环境，提供了大量的图形 

  工具程序。用户如果对microsoft wi n d o w s或m a c h i n t o s h比较熟悉的话，就不会对x wi n d o w系统感到束手无策了。 

  \2. /usr/x386 

  类似/ u s r / x 11r6 ，但是是专门给x 11 release 5的。 

  \3. /usr/bin 

  集中了几乎所有用户命令，是系统的软件库。另有些命令在/bin 或/usr/local/bin 中。 

  \4. /usr/sbin 

  包括了根文件系统不必要的系统管理命令，例如多数服务程序。 

  \5. /usr/man、/ u s r / i n f o、/ u s r / d o c 

  这些目录包含所有手册页、g n u信息文档和各种其他文档文件。每个联机手册的“节” 

  都有两个子目录。例如： / u s r / m a n / m a n 1中包含联机手册第一节的源码(没有格式化的原始文 

  件)，/ u s r / m a n / c a t 1包含第一节已格式化的内容。l联机手册分为以下九节：内部命令、系统调 

  用、库函数、设备、文件格式、游戏、宏软件包、系统管理和核心程序。 

  \6. /usr/include 

  包含了c语言的头文件，这些文件多以. h结尾，用来描述c语言程序中用到的数据结构、 

  子过程和常量。为了保持一致性，这实际上应该放在/usr/lib 下，但习惯上一直沿用了这个名 

  字。 

  \7. /usr/lib 

  包含了程序或子系统的不变的数据文件，包括一些s i t e - w i d e配置文件。名字l i b来源于库 

  (library); 编程的原始库也存在/usr/lib 里。当编译程序时，程序便会和其中的库进行连接。也 

  有许多程序把配置文件存入其中。 

  \8. /usr/local 

  本地安装的软件和其他文件放在这里。这与/ u s r很相似。用户可能会在这发现一些比较大 

  的软件包，如t e x、e m a c s等。 

  /var文件系统 

  /var 包含系统一般运行时要改变的数据。通常这些数据所在的目录的大小是要经常变化 

  或扩充的。原来/ v a r目录中有些内容是在/ u s r中的，但为了保持/ u s r目录的相对稳定，就把那 

  些需要经常改变的目录放到/ v a r中了。每个系统是特定的，即不通过网络与其他计算机共享。 

  下面列出一些重要的目录(一些不太重要的目录省略了)。 

  \1. /var/catman 

  包括了格式化过的帮助( m a n )页。帮助页的源文件一般存在/ u s r / m a n / m a n中；有些m a n页 

  可能有预格式化的版本，存在/ u s r / m a n / c a t中。而其他的m a n页在第一次看时都需要格式化， 

  格式化完的版本存在/var/man 中，这样其他人再看相同的页时就无须等待格式化了。 

  (/var/catman 经常被清除，就像清除临时目录一样。) 

  \2. /var/lib 

  存放系统正常运行时要改变的文件。 

  \3. /var/local 

  存放/usr/local 中安装的程序的可变数据(即系统管理员安装的程序)。注意，如果必要， 

  即使本地安装的程序也会使用其他/var 目录，例如/var/lock 。 

  \4. /var/lock 

  锁定文件。许多程序遵循在/var/lock 中产生一个锁定文件的约定，以用来支持他们正在 

  使用某个特定的设备或文件。其他程序注意到这个锁定文件时，就不会再使用这个设备或文 

  件。 

  \5. /var/log 

  各种程序的日志( l o g )文件，尤其是login (/var/log/wtmp log纪录所有到系统的登录和注 

  销) 和syslog (/var/log/messages 纪录存储所有核心和系统程序信息)。/var/log 里的文件经常不 

  确定地增长，应该定期清除。 

  \6. /var/run 

  保存在下一次系统引导前有效的关于系统的信息文件。例如， /var/run/utmp 包含当前登 

  录的用户的信息。 

  \7. /var/spool 

  放置“假脱机( s p o o l )”程序的目录，如m a i l、n e w s、打印队列和其他队列工作的目录。每 

  个不同的s p o o l在/var/spool 下有自己的子目录，例如，用户的邮箱就存放在/var/spool/mail 中。 

  \8. /var/tmp 

  比/tmp 允许更大的或需要存在较长时间的临时文件。 

  注意系统管理员可能不允许/var/tmp 有很旧的文件。 

  /proc文件系统 

  /proc 文件系统是一个伪的文件系统，就是说它是一个实际上不存在的目录，因而这是一 

  个非常特殊的目录。它并不存在于某个磁盘上，而是由核心在内存中产生。这个目录用于提 

  供关于系统的信息。下面说明一些最重要的文件和目录(/proc 文件系统在proc man页中有更详 

  细的说明)。 

  \1. /proc/x 

  关于进程x的信息目录，这一x是这一进程的标识号。每个进程在/proc 下有一个名为自 

  己进程号的目录。 

  \2. /proc/cpuinfo 

  存放处理器( c p u )的信息，如c p u的类型、制造商、型号和性能等。 

  \3. /proc/devices 

  当前运行的核心配置的设备驱动的列表。 

  \4. /proc/dma 

  显示当前使用的d m a通道。 

  \5. /proc/filesystems 

  核心配置的文件系统信息。 

  \6. /proc/interrupts 

  显示被占用的中断信息和占用者的信息，以及被占用的数量。 

  \7. /proc/ioports 

  当前使用的i / o端口。 

  \8. /proc/kcore 

  系统物理内存映像。与物理内存大小完全一样，然而实际上没有占用这么多内存；它仅 

  仅是在程序访问它时才被创建。(注意：除非你把它拷贝到什么地方，否则/proc 下没有任何 

  东西占用任何磁盘空间。) 

  \9. /proc/kmsg 

  核心输出的消息。也会被送到s y s l o g。 

  \10. /proc/ksyms 

  核心符号表。 

  \11. /proc/loadavg 

  系统“平均负载”； 3个没有意义的指示器指出系统当前的工作量。 

  \12. /proc/meminfo 

  各种存储器使用信息，包括物理内存和交换分区( s w a p )。 

  \13. /proc/modules 

  存放当前加载了哪些核心模块信息。 

  \14. /proc/net 

  网络协议状态信息。 

  \15. /proc/self 

  存放到查看/proc 的程序的进程目录的符号连接。当2个进程查看/proc 时，这将会是不同 

  的连接。这主要便于程序得到它自己的进程目录。 

  \16. /proc/stat 

  系统的不同状态，例如，系统启动后页面发生错误的次数。 

  \17. /proc/uptime 

  系统启动的时间长度。 

  \18. /proc/version 

  核心版本。

# Linux 命令 

- ls | grep ip

- ls <path> 列出指定路径下的 文件和文件夹 不能查看隐藏目录  

- ls -a 查看全部文件和文件夹（包括隐藏文件和文件夹）

- ls 命令 -a 选项  /home/yby 参数 

- ls -l 列出文件的详细信息  ====  ll

- ls -lh 更人性化 以 **KMGT**显示文件大小

- su <用户名>  切换用户

- cat <文件名> 从上到下查看文件内容

- tac <文件名> 从下到上查看文件内容

- head -n <文件名> 前n行，默认查看前10行数据

- tail  -n <文件名> 后n行，默认查看后10行数据

- nl 和 cat类似但是它显示行号

- wc 统计显示内容单词数，行数，字符数，文件名

- more 默认显示一屏 空格翻页 ，enter换行 q退出

- less 用来显示一屏 查看完毕以后不会退出 需要输入q

- mv  text.txt ~/Document

  - 剪切 / 移动

- cp text.txt ~/Document app.txt

  - 复制 到Document 文件夹
  - cp 源文件 目标文件夹 <重命名>

- drwxrwxr-x  2 yby  yby      6 10月  8 23:22 test

  - 由yby创建，自动归为yby 组，如果别的人加入yby组也有操作该文件的权限
  - yby 表示所有者
  - yby 表示所有组
  - 10月  8 23:22 表示文件最后一次修改时间
  - test 文件夹的名字
  - 6
    - 如果你是文件夹，就是文件夹的大小（大小不改变）
    - 如果你是文件 就是文件的大小

  - 2 
    - 如果是个文件夹 表示这个文件夹里有几个**子文件夹**
    - 如果是个文件，表示**文件硬链接的个数** (文件的名字)

  - drwxrwxr-x

    - rwxrwxr-x
      - 9个字母表示权限 
      - 三个一组，分别表示所有者，所属组和其它权限
      - r 表示读权限
      - w 表示写权限
      - x 表示执行权限

    - 第一个字母 表示文件的类型 
      - d 表示文件夹
      - \- 表示普通文件
      - l 表示一个链接（快捷方式）
      - c 表示字符设备文件 ， 即串行端口的接口设备，如鼠标键盘等
      -  b 表示块设备文件，就是存储数据以供系统存取的接口设备，简而言之就是硬盘
      - s 套接字文件 这类文件通常用在网络数据连接，最常在/var/run中看到这种文件类型
      - p 表示管道文件，他主要目的是解决多个文件存取一个文件所造成的错误

- 以点开头的文件或者文件夹为隐藏文件/文件夹

- pwd 
  - 打印工作目录
- rm -rf 
  - 删除
  - r 代表递归
  - f 代表强制
- useradd <用户名> -m -s /bin/bash 
  - 创建用户
- passwd <用户名> 
  - 设置密码 
- sudo gpasswd -a <用户名>  root  
  - 把用户添加到root组中
- ~ 
  - 代表当前用户的家目录
- cd - ; cd ~; cd 等价于 cd ~;
- mkdir aaa/bbb/ccc -p 创建多级目录 
- rmdir 移除一个空文件夹
- touch <文件名> 创建一个空文件
- rm -rf *.txt 把所有以.txt结尾的文件全都删掉
- cat /etc/group 查看所有组
- groups <用户名> 查看当前用户所在的组
- cat /etc/passwd 查看所有用户
- alias 可以给命令起别名
  - alias la='ls -a'
  - alias 查看全部别名
  - 别名是临时 如果在控制台里输入
  - unalias la 删除别名

# vim 的使用

- /etc/vimrc vim的配置文件，可以修改里面的命令配置文件 
  - ~/vimrc  没有可以创建

- vim 三种模式
  - 插入模式
    - i 进入到插入模式在光标的后面插入
    - I 在第一个非空字符前面插入数据
    - a 在光标后面插入
    - A 在这一行的最后面插入
    - s 删除光标所在位置的文字并插入内容
    - S 删除光标所在行的文字并插入内容
    - o 在光标所在行的下一行插入数据
    - O 在光标所在行的上一行插入数据
    - 想要退出必须进入到命令模式
    - esc 退出插入模式 进入命令模式
  - 命令模式
    - 默认命令模式
      - shift + z + z （保存并退出）退出ctrl + z  
      - dd 删除一行数据
      - ndd 用来删除n行数据
      - u 撤销
      - yy 复制
      - nyy 复制n行
      - p 粘贴
      - G 定位到最后一行
      - gg 定位到第一行
      - ngg 定位到第n行
      - $ 定位到这一行的最后面
      - 0/^ 定位到行首
      - ctrl ＋ｆ　下翻一页
      - ctrl ＋ｂ　上翻一页
      - ctrl ＋ｄ　下翻半页
      - ctrl ＋ｕ　上翻半页
      - ｘ     删光标右边的数据
      - ｎｘ 删光标右边n个数据
      - Ｘ     删光标走遍的数据
      - ｎＸ  删光标左边n个数据
      - ctrl + r  反撤销
  - 底线命令模式
    - ： 进入编辑（底线命令模式）模式
    - ESC 退出到命令模式
    - w 保存
    - q 退出 
    - q! 不保存强制退出
    - wq 保存并退出
    - e! 放弃修改
    - w <文件名> 另存
    - set nu 行号
    - set nonu 隐藏行号
    - set tabstop=4 设置一个tab缩进四个字符
    - set mouse=a 启动鼠标的点击功能
    - n 可以直接跳转到n行
    - /<要搜索的词> 按n键上翻 N 键下翻
    - ？ <要搜索的词> 按n键上翻 N 键下翻 查找指定内容
    - %s/原内容/新内容/g ---所有行内容替换,只会匹配每一行匹配到的第一个数据，g表示全局
    - m,ns/原内容/新内容/g----- m到n内容替换，g表示全局

# Linux 里的配置文件

- /etc/bashrc 文件 **全局环境**

- ~/.bashrc 文件 **局部环境**

- 打开终端都会执行配置文件里的代码

- Bash的名字是一系列缩写：Bourne-Again SHell — 这是关于Bourne shell（sh）的一个双关语（Bourne again / born again）

- bashrc rc表示 run command

  #  用户管理

- useradd <用户名> 
  - -m 在home 里创建一个家目录
  - -d 指定用户的家目录 一般情况下不改
  - -M 不创建家目录
  - -s 指定用户登录时的shell解析脚本，一般指定/etc/bash

- su <用户名> 切换用户 su - /su 切换到root用户

- passwd <用户名> / <空> 设置密码，空就是给当前用户设置密码

- sudo 用root权限执行命令

- userdel <用户名> -r  删除用户 -r删除用户家目录 

- kill 杀死进程

- sudo 不是所有用户都可以使用，必须是加入 /etc/sudoers 文件的用户才可以（还可以添加到有权限的组里面），用vim /etc/sudoers 把用户名加进去（在root 下面）

- Linux 有专门的命令添加sudoers 文件  visudo  和上面的一样的效果，只不过打开方式不是vim

- sudo update-alternatives --config editor 更改默认的编辑器

- groupadd 添加组  当我们创建一个用户的时候会自动创建一个和他同名的分组

- groupdel 删除组

- gpasswd 向指定组添加或删除制定的用户 gpasswd -a/-d user group 看/etc/sudoers文件可以看到加入什么组有权限

-  groups 查看指定用户的组信息

- 修改指定用户的shell 解析器 如  sudo chsh test -s /usr/sbin/nologin (禁止登录)

- yby2:\$6\$Xs7.Gu66GElksdgg$4UVUmTpPPHiP3d.xJuRRfs1dSuTiWw16rS78I4elrIW139tZuBmLqSx/bxpbfi4CO9M97sdK4.HSDgGazkBtZ.:18545:0:99999:7:::

  - 这是shandow 里面的数据

  - yby2 账户名

  - \$6\$Xs7.Gu66GElksdgg$4UVUmTpPPHiP3d.xJuRRfs1dSuTiWw16rS78I4elrIW139tZuBmLqSx/bxpbfi4CO9M97sdK4.HSDgGazkBtZ.  密码

    - 空表示密码为空
    - *标识账号被锁定
    - 但叹号表示未设置密码
    - 双叹号表示密码已过期
    - \$1\$表示用MD5加密
    - \$2\$表示用Blowfish加密
    - \$5\$表示用SHA-256加密
    - \$6\$表示用SHA-512加密

  - 18545 上次修改密码的时间 与1970-1-1 相聚的天数

  - 0 密码不可改的天数

  - 99999 密码需要修改的期限。如果为99999则永远不需要修改

  - 7 修改期限前天发出警告

  - 密码过期的宽限，假设这个数字被设定为M，那过期后M天内修改密码是可以修改的

  - 账号失效日期  ，假设这个数字被设定为N 表示日期与1970-1-1 相聚的天数

    

-   yby:x:1000:1000:yby:/home/yby:/bin/bash

  - yby 用户名
  - x 密码  密码在  /etc/shadow 里
  - 1000 用户id  （UID）
  - 1000 组的id   （GID）
  - yby 电脑名
  - /home/yby  用户的家目录
  - /bin/bash 用户登录的脚本

- /etc/group

- chmod 修改权限　chmod o+w text.txt 给其他人添加写权限
- - o 其他 o+w
  - u 所有者 u+x
  - g 所属组 g-w
  - ａ全部

- 权限的值
- - w ：2
  - r ： 4
  - x： 1
  - 加起来 为 7

- u = rwx 可以这么赋值
- chmod 777 text.txt ，第一个7所有者的权限，第二个7所属组的权限，第三个7代表其他人权限，权限全开
- chmod 644 text.txt 设置权限
- 文件夹默认775
- 普通文件默认664
- umask  查看文件（夹）的默认权限，默认值为 0002 
  - 第一个0不用管
  - 后三个全部分别变成2进制数，取反就是他的权限
  -   0      0       2
  - 000  000  010
  - 111  111  101  取反
  -    7      7       5

- umask 0022 设置权限 在新建文件（夹）权限就会改变 (反码) 最好别动
- chgrp yby yby.txt  把yby.txt 的所属组 修改成 yby组
- chown yby ybytxt 把yby.txt 的所有者 修改成 yby人

# 压缩解压命令

- zip / unzip

  - 压缩 zip a.zip 1.txt

  -  解压缩 unzip a.zip
  - 可以对文件夹压缩

- gzip / gunzip
  - gzip 1.txt 会把原来的文件替换为1.txt.gz
  - gunzip 1.txt.gz  
  - 加-k 不替换原来的文件
  - -r 可以把文件夹里的文件进行递归压缩 

- bzip2 
  - 用法和gzip 基本一致
  - 不能压缩文件夹

- linux 里常用的压缩方式.zip ,.tgz ,.tbz
- tar 打包命令 三种模式 专门打包文件夹的 不会对内容进行压缩，还会变大
  - -c 打包
  - -x 拆包
  - -t 不拆包查看内容
  - 最多只能出现一个参数
  - tar -cf test.tar test
  - tar -tvf test.tar test
  - tar -xvf test.tar test
  - -v是查看过程
  - -f 指定文件 -f 后要立即加文件想要归档的名称
  - -z 使用gzip压缩成tgz 文件
  - -j 使用bzip2压缩成tbz 文件
  - 最常用的压缩命令
    - tar -zcvf test.tgz test ===>将test 压缩成 test.tgz 文件 
    - tar -zxvf test.tgz
    - tar -jcvf test.tgz test ===>将test 压缩成 test.tbz 文件 
    - tar -jxvf test.tgz

# Nginx 安装

- sudo yum install nginx
- whereis nginx 查找nginx所在地
- systemctl start(stop) nginx (.server)                      ------ systemctl (systemcontrol)
- ps aux|grep nginx 查看后台运行的程序
- 先运行 然后读取配置文件一般是在/etc/nginx/nginx.conf 
- 安装包编译安装
  - wget <下载链接> 命令下载安装包
  - 把安装包解压
  - 执行./configure --prefix=url进行配置
    - --prefix 指定安装目录
    - 目的是用来查看当前系统的环境能否安装软件，在此过程中可能会提示你安装第三方依赖包
    - 在此过程中会提示需要安装第三方依赖包需要手动运行命令安装
    - 依赖安装完成以后在执行一边命令

- - 生成MakeFIle
  - 执行命令进行编译安装 sudo make && sudo make install
  - 启动nginx  
  - - cd /usr/local/nginx/sbin 进入安装目录启动它
    - 执行nginx文件 或者 执行 systemctl start(stop) nginx (.server) （不一定好使，好像服务没有注册）

# 安装python3

- 标准的centOS yum 装不了python3 因为标准库不确定
- 但是阿里云，腾讯云可以，因为它使用了镜像。
- 标准的centOS 在安装一个库 就可以安装python3了
  - sudo yum install epel-release
  - sudo yum install python3 -y
    - -y代表着中间不提示是否继续安装提示

# python 虚拟环境

- sys.path 可以找到python包的site-packages 里面有各种安装的包插件

- pychrome 新进一个工程可以选择新建一个虚拟环境或者在大环境下写代码，最好用虚拟环境，并且虚拟环境和代码别放在一起，这么做找插件好找，不同项目不同虚拟环境。

- pip freeze > requirement.txt 把安装的插件写入这个文件，给别人发送

- 在Linux环境里site-packages 一般在/usr/local/bin/python/下

- Linux 1:安装虚拟环境 可以使用virtualenv
  
- pip3 install virualenv
  
- 2: virtualenvwrapper
  
- sudo pip3 install virtualenvwapper
  
- 3:编辑~/.bashrc 在文件的最后面添加下面三行
  - export VIRTUALENVWRAPPER_PYTsoucHON=/usr/bin/python3.6 指定新虚拟环境使用的解释器
  - export WORKON_HOME=~/.env 指定新的虚拟环境保存在那个文件夹里
  - source /usr/local/bin/virtualenvwrapper.sh 指定virtualenvwrapper.sh 脚本

- 执行mkvirtualenv test 新建虚拟环境目录放在~/.env里

- 在虚拟环境里安装时不要用sudo 命令，会穿透虚拟环境

- 切换虚拟环境 **workon pa** 切换虚拟环境 

- 退出虚拟环境 **deactivate**

- 删除虚拟环境 **rmvirtualenv**

- ln -s python3.6 python  创建一个链接，把python指向python3.6

  # anaconda

- conda info -e 

- ```python
  conda create --name python34 python=3.4
  
  activate python34 # for Windows
  source activate python34 # for Linux & Mac
  
  
  # 此时，再次输入
  python --version
  
  # 如果想返回默认的python 2.7环境，运行
  deactivate python34 # for Windows
  source deactivate python34 # for Linux & Mac
  
  # 删除一个已有的环境
  conda remove --name python34 --all
  ```

# Linux 监听服务

- ps -aux
- pstree
- KILL -9 PID 强制杀死 最好不要用
- netstat  网络连接状态 -anop 
  - -a 显示所有socket
  - -n 以网络IP地址代替名称
  - -o 显示与网络计时器相关的信息
  - -t 显示tcp链接的情况
  - -u 显示与udp链接情况
  - -p 显示建立相关连接的程序名和PID

# 管道与重定向，多个命令的连接

- yum list installed | less
  - 把|前面查到的东西当做后面内容处理

- find 路径（可写可不写） -name 文件名
- find . -name demo.txt | xargs rm -rf
  - xargs 把字符串转化为文件名

- \> 重定向

  - ps -aux > ps.txt
    - \> 把结果转化为文件存储，如果文件已经存在，会覆盖

  - \>> 不会覆盖，会追加

  - 分类

    - 标准输出
      - 默认就是重定向标准输出，还可写作1> === >，如果命令出错，不会把结果写到文件里

    - 错误输出
      - 错误的是 2> 命令如果执行失败他会把错误写到文件里，如果命令对了他不会输出到文件里

    - 全部输出
      - &> 把所有输出都重定向到文件（无论错误还是正确的命令）

- 多个命令的连接

  - ：

    - ls;ps -aux

      - 先列出文件后列出ps 查到的列表

      - 完成第一个命令后，紧接着进行下面的命令

    - ||
      - ls || mkdir
      - 如果前面的命令执行成功，后面的命令就不在执行了

    - &&
      - ls && mkdir
      - 只有前面的命令执行成功，后面的才可以执行