# **1. nohup**



要实现守护进程，一种方法是按守护进程的规则去编程，比较麻烦；另一种方法是仍然用普通方法编程，然后用nohup命令启动程序： 
nohup <程序名> & 
则控制台logout后，进程仍然继续运行，起到守护进程的作用（虽然它不是严格意义上的守护进程）。
使用nohup命令后，原程序的的标准输出被自动改向到当前目录下的nohup.out文件，起到了log的作用，实现了完整的守护进程功能。



# **2.bg（background）和fg（foreground）**



我们都知道，在 Windows 上面，我们要么让一个程序作为服务在后台一直运行，要么停止这个服务。而不能让程序在前台后台之间切换。而 Linux 提供了 fg 和 bg 命令，让我们轻松调度正在运行的任务。

假设你发现前台运行的一个程序需要很长的时间，但是需要干其他的事情，你就可以用 Ctrl-Z ，挂起这个程序，然后可以看到系统提示（方括号中的是作业号）：
[1]+ Stopped /root/bin/rsync.sh
然后我们可以把程序调度到后台执行：（bg 后面的数字为作业号）

## 一 & 最经常被用到

这个用在一个命令的最后，可以把这个命令放到后台执行

## 二 ctrl + z

可以将一个正在前台执行的命令放到后台，并且暂停

## 三 jobs

查看当前有多少在后台运行的命令

## 四 fg

将后台中的命令调至前台继续运行
如果后台中有多个命令，可以用 fg %jobnumber将选中的命令调出，%jobnumber是通过jobs命令查到的后台正在执行的命令的序号(不是pid)

## 五 bg

将一个在后台暂停的命令，变成继续执行
如果后台中有多个命令，可以用bg %jobnumber将选中的命令调出，%jobnumber是通过jobs命令查到的后台正在执行的命令的序号(不是pid)



# Linux：“后台、安静运行命令”的bg、fg、&和nohup总结

参考链接：[Linux的bg和fg命令简单介绍](http://www.jb51.net/LINUXjishu/65800.html)

> 在工作中，往往需要连接远程服务器，这是一个连接只有一个窗口（当然可以用xshell开启多个窗口连接），那么如何在当前窗口同时运行多个程序呢？这就需要用到&,bg,fg和nohup了。

## 关于 &

在命令的最后加上`&`，则可以安静运行程序（如果程序没问题或者不会一下子就运行完的话，击打任意键后程序就在后台运行着）：
![关于 &](G:\新知识\linux\images\at.png)

## jobs查看后台运行的程序

用`jobs`命令查看后台运行的程序，可以看到后台程序和其编号`i`：
![job命令实例](G:\新知识\linux\images\jobs.png)

## fg命令将后台运行的命令调用到前台：foreground

用`fg i`命令将后台运行的程序调用到前面来，其中i为`jobs`命令查看到的编号：
![ fg命令将后台运行的命令调用到前台：foreground](G:\新知识\linux\images\fg.png)

当然，`fg`也可以将`ctrl+z`后挂起的程序（见下）唤醒到前台。

## ctrl + z 将正在运行着的程序暂停（挂起）

当程序在当前窗口运行着时，用`ctrl+z`将正在运行着的程序暂停，或者说挂起：
![ctrl+z将程序挂起](G:\新知识\linux\images\ctrlZ.png)

## bg命令将挂起的程序放到后台运行

当程序挂起时，可以用`bg i`命令，将挂起的命令放于后台背景运行，其中`i`是`jobs`的编号。
![bg命令将挂起的程序放到后台运行](G:\新知识\linux\images\bg.png)

## nohup命令

如果希望关掉ssh窗口后，程序依旧运行，并且可以重新登录新的ssh连接后还能看到程序的输出日志，那么就得用nohup命令。格式如下：
`nohup 命令 [2>&1 重定向文件名] &`
其中[]内的可选，如果没有，则将日志默认输出到当前目录下的**nohup.out**文件。

![nohup默认](G:\新知识\linux\images\nohup.png)

![nohup自定义文件输出](G:\新知识\linux\images\21nohup.png)

`nohup`之后似乎无法重新唤醒到前台，只能通过`tail -f 日志文件名`来查看运行日志。

## ps命令查看nohup的程序

使用`nohup`命令，并关闭当前ssh连接后，再重连，是不能通过`jobs`查看运行着的进程的。
这时可以通过`ps -f | grep 程序名` 来查找该进程的`pid`，方便查看是否运行和`kill`掉它。

![ps命令查看nohup的程序](G:\新知识\linux\images\psef.png)

## 问题

`screen`功能是什么，似乎也可以做到后台运行？
`nohup`中的`2>&1`是什么意思？
以后有时间再完善。





## nohup和&

> 在Linux执行任务时，如果键入Ctrl+C退出进行其他任务或者关闭当前session
> 当前任务就会终止 要想不让进程停止或者让进程在后台运行，就需要一些命令，nohup和&就是一种非常好的方式

首先以执行一个python脚本为例：

```
python test.py
```

### **nohup和&的区别**

- &：后台运行，但当用户退出(挂起)的时候，命令自动也跟着退出**

什么意思呢？ 意思是说， 当你在执行 `python test.py &` 的时候， 即使你用`ctrl C`, 那么`python test.py`照样运行（因为对SIGINT信号免疫）。 但是要注意， 如果你直接关掉shell后， 那么， 这个python进程同样消失。 可见， &的后台并不硬（因为对SIGHUP信号不免疫）。

- **nohup： 即no hang up，不挂断的运行**

nohup的意思是忽略SIGHUP信号， 所以当运行`nohup python test.py`的时候， 关闭shell, 那么这个python进程还是存在的（对SIGHUP信号免疫）。 但是， 要注意， 如果你直接在shell中用Ctrl C, 那么, 这个python进程也是会消失的（因为对SIGINT信号不免疫）

注意并没有后台运行的功能，就是指，用nohup运行命令可以使命令永久的执行下去，和用户终端没有关系，例如我们断开SSH连接都不会影响他的运行，注意了nohup没有后台运行的意思；&才是后台运行

- **综合使用**

如果想让进程在后台不挂断的运行，需要`nohup`和`&`结合起来使用

```
nohup nohup python test.py & > /var/log/python.log &
```

nohup语法：

```
nohup Command [ Arg ... ] [　& ]
```

> nohup 命令运行由 Command参数和任何相关的 Arg参数指定的命令，忽略所有挂断（SIGHUP）信号。在注销后使用 nohup 命令运行后台中的程序。要运行后台中的 nohup 命令，添加 & （ 表示“and”的符号）到命令的尾部。
> 如果不将 nohup 命令的输出重定向，输出将附加到当前目录的 `nohup.out` 文件中。如果当前目录的 nohup.out 文件不可写，输出重定向到 $HOME/nohup.out 文件中。如果没有文件能创建或打开以用于追加，那么 Command 参数指定的命令不可调用。如果标准错误是一个终端，那么把指定的命令写给标准错误的所有输出作为标准输出重定向到相同的文件描述符。

### **实战讲解**

首先准备一个python测试代码，是一个输出HelloWorld和数字的死循环脚本，每输出一行就等待1秒：

```
#!/usr/bin/python
# -*- coding: UTF-8 -*-
import time

var = 1
while var > 0 :  # 该条件永远为true，循环将无限执行下去

   print "HelloWorld: ", var
   var = var +1
   time.sleep(1)  #每输出一行就休眠1秒
```

- **1. 前台运行**

执行下列命令前台运行python脚本是什么情况呢？

```
python test.py
```

[![img](G:\新知识\linux\images\1549915-20190923150012423-1077146702.png)](https://img2018.cnblogs.com/blog/1549915/201909/1549915-20190923150012423-1077146702.png)

程序每隔一秒会在终端输出一个字符串。

此时如果键入Ctrl+C ，程序会收到一个SIGINT信号，如果不做特殊处理，程序的默认行为是终止（如上图）。

- **2. 后台运行**

执行下面的命令在后台运行这个python脚本：

```
python test.py &
```

[![img](G:\新知识\linux\images\1549915-20190924130230245-588825427.png)](https://img2018.cnblogs.com/blog/1549915/201909/1549915-20190924130230245-588825427.png)

如上图，首先会在终端显示进程号是8778

如果键入Ctrl + C，发出SIGINT信号，程序会继续运行吗？

下图所示，键入Ctrl + C程序仍然会继续运行：

[![img](G:\新知识\linux\images\1549915-20190924130254209-1205183582.png)](https://img2018.cnblogs.com/blog/1549915/201909/1549915-20190924130254209-1205183582.png)

执行`ps -ef|grep test.py`查询一下，程序进程确实存在，如下图所示：

[![img](G:\新知识\linux\images\1549915-20190924130402860-896520518.png)](https://img2018.cnblogs.com/blog/1549915/201909/1549915-20190924130402860-896520518.png)

此时如果关闭session即关闭xshell，程序会收到一个SIGHUP信号，此时会怎么样呢？

重新打开xshell的session，：

[![img](G:\新知识\linux\images\1549915-20190924130526103-401951805.png)](https://img2018.cnblogs.com/blog/1549915/201909/1549915-20190924130526103-401951805.png)

如上图，程序不会继续输出，而且执行`ps -ef|grep test.py`刚刚打开的进程以及被关闭了。

- **3. 使用nohup运行脚本**

如果使用nohup命令来运行python脚本的话，会是怎样的情况呢？

执行以下命令：

```
nohup python test.py
```

[![img](G:\新知识\linux\images\1549915-20190923151725157-1597598171.png)](https://img2018.cnblogs.com/blog/1549915/201909/1549915-20190923151725157-1597598171.png)

如上图，使用nohup 运行程序test.py，会发现：

- 前台没有出现进程号
- 有一个“忽略输入，输出至nohup.out”的提示
- hello的输出也没有出现在前台

[![img](G:\新知识\linux\images\1549915-20190923152016292-940146314.png)](https://img2018.cnblogs.com/blog/1549915/201909/1549915-20190923152016292-940146314.png)

如上图，在另一个xshell的session的窗口执行`ps -ef|grep test.py`，会发现脚本已经在运行了，进程号是20085

在前一个图中提示输出至nohup.out的提示，那么我们在新打开的窗口去看看这里面是啥。

```
vi nohup.out
```

[![img](G:\新知识\linux\images\1549915-20190923152622057-1212835983.png)](https://img2018.cnblogs.com/blog/1549915/201909/1549915-20190923152622057-1212835983.png)

如上图，脚本的日志会在这个文件输出。

此时，如果我们关闭原来执行脚本的xshell的session，程序会收到一个SIGHUP信号，程序会不会关闭呢？

[![img](G:\新知识\linux\images\1549915-20190923152848719-401756928.png)](https://img2018.cnblogs.com/blog/1549915/201909/1549915-20190923152848719-401756928.png)

如上图，我们在新打开的xshell创建执行`ps -ef | grep test.py`发现，这个PID为20085的python进程还存在

此时只能通过kill命令来杀死进程了：

```
kill -9 20085
```

然后，再次ps一下，如下图，进程已经被杀掉了

[![img](G:\新知识\linux\images\1549915-20190923153343370-911386903.png)](https://img2018.cnblogs.com/blog/1549915/201909/1549915-20190923153343370-911386903.png)

此时重新使用nohup执行一下这个python脚本：`nohup python test.py`

然后键入Ctrl+C，并且执行`ps -ef | grep test.py`查看一下进程：

[![img](G:\新知识\linux\images\1549915-20190923153618723-1749544364.png)](https://img2018.cnblogs.com/blog/1549915/201909/1549915-20190923153618723-1749544364.png)

如上图所示，键入Ctrl+C后，程序收到SIGINT信号后，进程直接关闭了

- **4. 后台不挂断运行**

`nohup`和`&`一起使用，我们来看看是什么情况：

使用以下指令运行程序：

```
nohup python test.py &
```

[![img](G:\新知识\linux\images\1549915-20190923154344289-1100542373.png)](https://img2018.cnblogs.com/blog/1549915/201909/1549915-20190923154344289-1100542373.png)

如上图，使用`nohup python test.py &`运行程序后，可以看到：

- 会在终端显示进程号是21503
- 也会有一个“忽略输入，输出至nohup.out”的提示
- 键入Ctrl + C，发送SIGINT信号，似乎没反应。

关闭session，发送SIGHUP信号，再打开一个session窗口ps一下：

[![img](G:\新知识\linux\images\1549915-20190923154436837-420073416.png)](https://img2018.cnblogs.com/blog/1549915/201909/1549915-20190923154436837-420073416.png)

如上图，ID为21503的进程依然存在，后续也只能用kill来关闭它。

- **5.结论**

### **使用&后台运行程序：**

- 结果会输出到终端
- 使用Ctrl + C发送SIGINT信号，程序免疫
- 关闭session发送SIGHUP信号，程序关闭

### **使用nohup运行程序：**

- 结果默认会输出到nohup.out
- 使用Ctrl + C发送SIGINT信号，程序关闭
- 关闭session发送SIGHUP信号，程序免疫

### **使用nohup和&配合来启动程序：**

- 同时免疫SIGINT和SIGHUP信号

### **最佳实践方案：**

不要将信息输出到终端标准输出，标准错误输出，而要用日志组件将信息记录到日志里

nohup命令可以将日志输入到文件中

- 如果不指定输出文件，默认输出到当前目录下的`nohup.out`文件
- 如果当前目录的 nohup.out 文件不可写，输出重定向到 $HOME/nohup.out 文件中。

举个例子：

```
nohup python test.py > test.log 2>&1 &
nohup ping www.baidu.com > ping.log 2>&1 &
```