# [Linux下swap到底有没有必要使用](https://www.cnblogs.com/coolops/p/12806595.html)

周五看到QQ群里在讨论Linux主机上到底需不需要开启swap空间，而且目前公有云主机默认都是把swap关了的，很多公司也是没有开启swap，那到底需不需要开启呢？


我之前在看《鸟哥的Linux私房菜》上他写了这么一段话：swap在目前的桌面计算机来讲，存在的意义已经不大了，这是因为目前的X86主机所含的内存实在都太大了，所以我们的系统大概率用不到swap，不过，如果针对服务器或者工作站这些常年上线的系统来说，swap还是需要的。


当然，这段话是《鸟哥的Linux私房菜》第三版里写的（在第四版不知道还是不是这么写的），那时候的内存还远远没有现在大，那现在到底需不需要呢？我们先来看看什么是swap，它的作用是什么。



## 什么是swap

swap是磁盘上的一个区域，可以是一个分区，也可以是一个文件，或者是它们的组合，简单点说，当系统物理内存不够时，Linux会将内存中不常访问的数据保存到swap上，这样系统就有更多的物理内存为各个进程服务，而当系统需要访问swap上存储的内容时，再将swap上的数据加载到内存中，这就是我们常说的swap out和swap in。



## swap的主要功能

其实上面基本已经将swap的主要功能说了，这里再来重述一下：
（1）、当物理内存不足的时候，将某些在内存中所占用的程序暂时移动到swap当中，让物理内存可以被需要的程序来使用；
（2）、Linux会将内存中不常访问的数据保存到swap中，当系统需要再次调用的时候，就把它从swap加载到内存；
（3）、如果你的主机支持电源管理模式，也就是说，你的Linux主机系统可以进入"休眠"模式的话，那么，运行当中的程序状态则会被记录到swap中去，以作为"唤醒"主机状态的依据；
（4）、在某些程序运行时，本来就会利用swap特性来存放一些数据，比如在装Oracle11g的时候会检查swap size；



## swap给我们带来什么好处

上面介绍了swap的主要功能，其实就是swap的优点。在说swap给我们带来好处之前先说说swap的缺点。由于swap是磁盘上的一个区域，要么是文件，要么是分区，甚至它们的组合，其实都逃不脱"在磁盘上"，那么很明显的一个缺点就是速度，磁盘的速度和内存的速度不是一个量级的，就算现在的SSD磁盘，还是跟不上内存的速度，所以说如果不停的读写swap，对磁盘的性能是有很大的影响的，尤其是在物理内存吃紧，swap读写频率又高的极端情况下，这时候除了加物理内存别无他法了。

有的小伙伴看到这里可能在想，哇，我还用它干啥，我直接把我内存加够不就行了。骚年莫急，我将慢慢道来。
来看看下面这些情况：
（1）、有些应用程序在启动的时候会需要大量内存，但是在启动完成后需要的内存很小，这时候swap就很是时候了，假如全部用物理内存，其实就有点浪费资源了，谁的钱不是钱呢？你说是吧。
（2）、现在很多小伙伴开发都用Ubuntu，Ubuntu有休眠的功能，如果需要用到休眠的话，也是需要swap的，它会把休眠之前内存中的数据保存到swap中，你下次用的时候，就直接从swap加载到内存中，省的麻烦。
（3）、有些小公司讲究节约成本，甚至有的把这个当成kpi了，所以就不能把内存搞得蛮大了，我们就需要在保证系统正常运行所需内存的情况下，配备swap，既可以保证业务运行，也可以防患于未然。
（4）、现在大部分物理内存都够用了，很多公司也完全放弃了swap。但是谁也不知道下一秒会发生什么问题，比如内存泄漏，比如某个进程需要内存超过预期，这时候如果只有物理内存，可能就会直接OOM了，等不到我们收到报警，进行处理。如果这时候有swap，我们收到物理内存不够报警的时候还会有swap顶一下，回滚或者加内存什么的也有足够的时间，避免手忙脚乱发生生产事故。

当然还有很多情况，这里就不例举了。从上面其实可以看出，swap有它的好处，也有它的缺点，具体用不用是根据每个公司具体情况来定的，不是说不用，也不是说一定要用（当然，有的软件是一定要用的）。就像今天上午在微信群里和一为小伙伴讨论要不要秒级报警一样，每个公司有每个公司的打法，在讨论问题的时候切莫以自己公司的就是标准，我一直认为互联网时代没有唯一的标准，只有不断探索，不断追求，当然，大部分公司基本都是采用"前车之鉴"这种模式，比如效仿BAT公司成熟方案，学习各大高科技公司的落地实施等。

说了这么多，其实也就几句话：swap空间到底用不用，取决于应用软件需不需要，取决于公司的规范标准，还却决于作为运维人员自己的考虑，更多情况下还却决于现实（你的公司舍不舍得花钱）。

# **Swap交换分区概念**

什么是Linux swap space呢？我们先来看看下面两段关于Linux swap space的英文介绍资料:

 

Linux divides its physical RAM (random access memory) into chucks of memory called pages. Swapping is the process whereby a page of memory is copied to the preconfigured space on the hard disk, called swap space, to free up that page of memory. The combined sizes of the physical memory and the swap space is the amount of virtual memory available.

Swap space in Linux is used when the amount of physical memory (RAM) is full. If the system needs more memory resources and the RAM is full, inactive pages in memory are moved to the swap space. While swap space can help machines with a small amount of RAM, it should not be considered a replacement for more RAM. Swap space is located on hard drives, which have a slower access time than physical memory.Swap space can be a dedicated swap partition (recommended), a swap file, or a combination of swap partitions and swap files.

 

Linux内核为了提高读写效率与速度，会将文件在内存中进行缓存，这部分内存就是Cache Memory(缓存内存)。即使你的程序运行结束后，Cache Memory也不会自动释放。这就会导致你在Linux系统中程序频繁读写文件后，你会发现可用物理内存变少。当系统的物理内存不够用的时候，就需要将物理内存中的一部分空间释放出来，以供当前运行的程序使用。那些被释放的空间可能来自一些很长时间没有什么操作的程序，这些被释放的空间被临时保存到Swap空间中，等到那些程序要运行时，再从Swap分区中恢复保存的数据到内存中。这样，系统总是在物理内存不够时，才进行Swap交换。

关于Swap分区，其实我们有很多疑问,如果能弄清楚这些疑问，那么你对Swap的了解掌握就差不多了。如何查看Swap分区大小？ Swap分区大小应该如何设置？系统在什么时候会使用Swap分区? 是否可以调整？ 如何调整Swap分区的大小？Swap分区有什么优劣和要注意的地方？ Swap分区是否必要？那么我一个一个来看看这些疑问吧！

 



# **查看Swap分区大小**

 

查看Swap分区的大小以及使用情况，一般使用free命令即可，如下所示，Swap大小为2015M，目前没有使用Swap分区

```
[root@DB-Server ~]# free -m
             total       used       free     shared    buffers     cached
Mem:          1000        855        145          0         28        296
-/+ buffers/cache:        530        470
Swap:         2015          0       2015
```

另外我们还可以使用swapon命令查看当前swap相关信息：例如swap空间是swap partition，Swap size，使用情况等详细信息

```
[root@DB-Server ~]# swapon -s
Filename                                Type            Size    Used    Priority
/dev/sda3                               partition       2064344 0       -1
[root@DB-Server ~]# cat /proc/swaps
Filename                                Type            Size    Used    Priority
/dev/sda3                               partition       2064344 0       -1
[root@DB-Server ~]# 
```

[![clip_image001](https://images2015.cnblogs.com/blog/73542/201603/73542-20160306002145690-21305302.png)](http://images2015.cnblogs.com/blog/73542/201603/73542-20160306002757409-997990791.png)

 

# **Swap分区大小设置**

 

系统的Swap分区大小设置多大才是最优呢？ 关于这个问题，应该说只能有一个统一的参考标准，具体还应该根据系统实际情况和内存的负荷综合考虑，像ORACLE的官方文档就推荐如下设置，这个是根据物理内存来做参考的。

| **RAM**                         | **Swap Space**             |
| ------------------------------- | -------------------------- |
| **Up to 512 MB**                | 2 times the size of RAM    |
| **Between 1024 MB and 2048 MB** | 1.5 times the size of RAM  |
| **Between 2049 MB and 8192 MB** | Equal to the size of RAM   |
| **More than 8192 MB**           | 0.75 times the size of RAM |

另外在其它博客中看到下面一个推荐设置，当然我不清楚其怎么得到这个标准的。是否合理也无从考证。可以作为一个参考。

4G以内的物理内存，SWAP 设置为内存的2倍。

4-8G的物理内存，SWAP 等于内存大小。

8-64G 的物理内存，SWAP 设置为8G。

64-256G物理内存，SWAP 设置为16G。

上下两个标准确实也很让人无所适从。我就有一次在一台ORACLE数据库服务器（64G的RAM），按照官方推荐设置了一个很大的Swap分区，但是我发现其实这个Swap几乎很少用到，其实是浪费了磁盘空间。所以如果根据系统实际情况和内存的负荷综合考虑，其实应该按照第二个参考标准设置为8G即可。当然这个只是个人的一些认知。

 

# **释放Swap分区空间**

 

```
[root@testlnx ~]# free -m
             total       used       free     shared    buffers     cached
Mem:         64556      55368       9188          0        926      51405
-/+ buffers/cache:       3036      61520
Swap:        65535         13      65522
[root@testlnx ~]# swapon -s
Filename                                Type            Size    Used    Priority
/dev/mapper/VolGroup00-LogVol01         partition       67108856        14204   -1
```

# **使用swapoff关闭交换分区**

[root@testlnx ~]# swapoff /dev/mapper/VolGroup00-LogVol01

# **使用swapon启用交换分区**，此时查看交换分区的使用情况，你会发现used为0了

```
[root@testlnx ~]# swapon /dev/mapper/VolGroup00-LogVol01
[root@testlnx ~]# free -m
             total       used       free     shared    buffers     cached
Mem:         64556      55385       9171          0        926      51406
-/+ buffers/cache:       3052      61504
Swap:        65535          0      65535
[root@testlnx ~]#
```

 

# **Swap分区空间什么时候使用**

 



系统在什么情况或条件下才会使用Swap分区的空间呢？ 其实是Linux通过一个参数swappiness来控制的。当然还涉及到复杂的算法。

这个参数值可为 0-100，控制系统 swap 的使用程度。高数值可优先系统性能，在进程不活跃时主动将其转换出物理内存。低数值可优先互动性并尽量避免将进程转换处物理内存，并降低反应延迟。默认值为 60。注意：这个只是一个权值，不是一个百分比值，涉及到系统内核复杂的算法。关于该参数请参考这篇文章[转载]调整虚拟内存，在此不做过多赘述。下面是关于swappiness的相关资料

 

The Linux 2.6 kernel added a new kernel parameter called swappiness to let administrators tweak the way Linux swaps. It is a number from 0 to 100. In essence, higher values lead to more pages being swapped, and lower values lead to more applications being kept in memory, even if they are idle. Kernel maintainer Andrew Morton has said that he runs his desktop machines with a swappiness of 100, stating that "My point is that decreasing the tendency of the kernel to swap stuff out is wrong. You really don't want hundreds of megabytes of BloatyApp's untouched memory floating about in the machine. Get it out on the disk, use the memory for something useful."

Swappiness is a property of the Linux kernel that changes the balance between swapping out runtime memory, as opposed to dropping pages from the system page cache. Swappiness can be set to values between 0 and 100 inclusive. A low value means the kernel will try to avoid swapping as much as possible where a higher value instead will make the kernel aggressively try to use swap space. The default value is 60, and for most desktop systems, setting it to 100 may affect the overall performance, whereas setting it lower (even 0) may improve interactivity (by decreasing response latency.

 

有两种临时修改swappiness参数的方法，系统重启后失效

```
方法1：
[root@DB-Server ~]# more /proc/sys/vm/swappiness
60
[root@DB-Server ~]# echo 10 > /proc/sys/vm/swappiness
[root@DB-Server ~]# more /proc/sys/vm/swappiness
10
 
方法2
[root@DB-Server ~]#sysctl vm.swappiness=10
```

永久修改swappiness参数的方法就是在配置文件/etc/sysctl.conf里面修改vm.swappiness的值，然后重启系统

```
echo 'vm.swappiness=10' >>/etc/sysctl.conf
```

如果有人会问是否物理内存使用到某个百分比后才会使用Swap交换空间，可以明确的告诉你不是这样一个算法，如下截图所示，及时物理内存只剩下8M了，但是依然没有使用Swap交换空间，而另外一个例子，物理内存还剩下19G，居然用了一点点Swap交换空间。

[![clip_image002](https://images2015.cnblogs.com/blog/73542/201603/73542-20160306002147330-695954439.png)](http://images2015.cnblogs.com/blog/73542/201603/73542-20160306002758487-1243796217.png)

[![clip_image003](https://images2015.cnblogs.com/blog/73542/201603/73542-20160306002157190-2143348506.png)](http://images2015.cnblogs.com/blog/73542/201603/73542-20160306002805127-979972529.png)

另外调整/proc/sys/vm/swappiness这个参数，如果你没有绝对把握，就不要随便调整这个内核参数，这个参数符合大多数情况下的一个最优值。

 

# **Swap交换分区对性能的影响**

 

我们知道Linux可以使用文件系统中的一个常规文件或独立分区作为Swap交换空间，相对而言，交换分区要快一些。但是和RAM比较而言，Swap交换分区的性能依然比不上物理内存，目前的服务器上RAM基本上都相当充足，那么是否可以考虑抛弃Swap交换分区，是否不需要保留Swap交换分区呢？这个其实是我的疑问之一。在这篇What Is a Linux SWAP Partition, And What Does It Do?博客中，作者给出了swap交换空间的优劣

**Advantages:**



1. Provides overflow space when your memory fills up completely
2. Can move rarely-needed items away from your high-speed memory
3. Allows you to hibernate

**Disadvantages:**



1. Takes up space on your hard drive as SWAP partitions do not resize dynamically
2. Can increase wear and tear to your hard drive
3. Does not necessarily improve performance (see below)

其实保留swap分区概括起来可以从下面来看：

首先，当物理内存不足以支撑系统和应用程序（进程）的运作时，这个Swap交换分区可以用作临时存放使用率不高的内存分页，把腾出的内存交给急需的应用程序（进程）使用。有点类似机房的UPS系统，虽然正常情况下不需要使用，但是异常情况下， Swap交换分区还是会发挥其关键作用。

其次，即使你的服务器拥有足够多的物理内存，也有一些程序会在它们初始化时残留的极少再用到的内存分页内容转移到 swap 空间，以此让出物理内存空间。对于有发生内存泄漏几率的应用程序（进程），Swap交换分区更是重要，因为谁也不想看到由于物理内存不足导致系统崩溃。

最后，现在很多个人用户在使用Linux，有些甚至是PC的虚拟机上跑Linux系统，此时可能常用到休眠（Hibernate），这种情况下也是推荐划分Swap交换分区的。

其实少量使用Swap交换空间是不会影响性能，只有当RAM资源出现瓶颈或者内存泄露，进程异常时导致频繁、大量使用交换分区才会导致严重性能问题。另外使用Swap交换分区频繁，还会引起kswapd0进程（虚拟内存管理中, 负责换页的）耗用大量CPU资源，导致CPU飙升。

关于Swap分区的优劣以及是否应该舍弃，我有点恶趣味的想到了这个事情：人身上的两个器官，阑尾和扁桃体。切除阑尾或扁桃体是否也是争论不休。另外，其实不要Swap交换分区，Linux也是可以正常运行的（有人提及过这个问题）

 

# **调整Swap分区的大小**

如下测试案例所示，Swap分区大小为65535M，我现在想将Swap分区调整为8G，那么我们来看看具体操作吧

1：查看Swap的使用情况以及相关信息

```
[root@getlnx14uat ~]# swapon -s
Filename                                Type            Size    Used    Priority
/dev/mapper/VolGroup00-LogVol01         partition       67108856        878880  -1
[root@getlnx14uat ~]# free -m
             total       used       free     shared    buffers     cached
Mem:          3957       3920         36          0         39       3055
-/+ buffers/cache:        825       3132
Swap:        65535        858      64677
```

2： 关闭Swap交换分区

```
[root@getlnx14uat ~]# swapoff /dev/mapper/VolGroup00-LogVol01
[root@getlnx14uat ~]# swapon -s
Filename                                Type            Size    Used    Priority
```

3： 这里是缩小Swap分区大小，如果是增大Swap分区大小，那么就需要扩展正在使用的swap分区的逻辑卷,此处使用lvreduce命令收缩逻辑卷。

```
[root@getlnx14uat ~]# lvreduce -L 8G /dev/mapper/VolGroup00-LogVol01
  WARNING: Reducing active logical volume to 8.00 GB
  THIS MAY DESTROY YOUR DATA (filesystem etc.)
Do you really want to reduce LogVol01? [y/n]: y
  Reducing logical volume LogVol01 to 8.00 GB
  Logical volume LogVol01 successfully resized
```

4：格式化swap分区

```
[root@getlnx14uat ~]# mkswap /dev/mapper/VolGroup00-LogVol01
Setting up swapspace version 1, size = 8589930 kB
```

5:启动swap分区,并增加到/etc/fstab自动挂载

```
[root@getlnx14uat ~]# swapon -s
Filename                                Type            Size    Used    Priority
[root@getlnx14uat ~]# swapon /dev/mapper/VolGroup00-LogVol01
[root@getlnx14uat ~]# swapon -s
Filename                                Type            Size    Used    Priority
/dev/mapper/VolGroup00-LogVol01         partition       8388600 0       -1
```

[![clip_image004](https://images2015.cnblogs.com/blog/73542/201603/73542-20160306002200862-139709144.png)](http://images2015.cnblogs.com/blog/73542/201603/73542-20160306002806987-799592866.png)