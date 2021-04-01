###ls [选项] [目录名 | 列出相关目录下的所有目录和文件

```shell
-a  列出包括.a开头的隐藏文件的所有文件
-A  通-a，但不列出"."和".."
-l  列出文件的详细信息
-c  根据ctime排序显示
-t  根据文件修改时间排序
---color[=WHEN] 用色彩辨别文件类型 WHEN 可以是'never'、'always'或'auto'其中之一
    白色：表示普通文件
    蓝色：表示目录
    绿色：表示可执行文件
    红色：表示压缩文件
    浅蓝色：链接文件
    红色闪烁：表示链接的文件有问题
    黄色：表示设备文件
    灰色：表示其它文件   

```

###mv [选项] 源文件或目录 目录或多个源文件 | 移动或重命名文件

``````shell
-b  覆盖前做备份
-f  如存在不询问而强制覆盖
-i  如存在则询问是否覆盖
-u  较新才覆盖
-t  将多个源文件移动到统一目录下，目录参数在前，文件参数在后
eg:
    mv a /tmp/ 将文件a移动到 /tmp目录下
    mv a b 将a命名为b
    mv /home/zenghao test1.txt test2.txt test3.txt

```

###cp [选项] 源文件或目录 目录或多个源文件 | 将源文件复制至目标文件，或将多个源文件复制至目标目录。

``````shell
-r -R 递归复制该目录及其子目录内容
-p  连同档案属性一起复制过去
-f  不询问而强制复制
-s  生成快捷方式
-a  将档案的所有特性都一起复制

```

###scp [参数] [原路径] [目标路径] | 在Linux服务器之间复制文件和目录

```shell
-v  详细显示输出的具体情况
-r  递归复制整个目录
(1) 复制文件：  
命令格式：  
scp local_file remote_username@remote_ip:remote_folder  
或者  
scp local_file remote_username@remote_ip:remote_file  
或者  
scp local_file remote_ip:remote_folder  
或者  
scp local_file remote_ip:remote_file  
第1,2个指定了用户名，命令执行后需要输入用户密码，第1个仅指定了远程的目录，文件名字不变，第2个指定了文件名  
第3,4个没有指定用户名，命令执行后需要输入用户名和密码，第3个仅指定了远程的目录，文件名字不变，第4个指定了文件名   
(2) 复制目录：  
命令格式：  
scp -r local_folder remote_username@remote_ip:remote_folder  
或者  
scp -r local_folder remote_ip:remote_folder  
第1个指定了用户名，命令执行后需要输入用户密码；  
第2个没有指定用户名，命令执行后需要输入用户名和密码；
eg:
    从 本地 复制到 远程
    scp /home/daisy/full.tar.gz root@172.19.2.75:/home/root 
    从 远程 复制到 本地
    scp root@/172.19.2.75:/home/root/full.tar.gz /home/daisy/full.tar.gz

```

###rm [选项] 文件 | 删除文件

```shell
-r  删除文件夹
-f  删除不提示
-i  删除提示
-v  详细显示进行步骤

```

###touch [选项] 文件 | 创建空文件或更新文件时间

```shell
-a  只修改存取时间
-m  值修改变动时间
-r  eg:touch -r a b ,使b的时间和a相同
-t  指定特定的时间 eg:touch -t 201211142234.50 log.log 
    -t time [[CC]YY]MMDDhhmm[.SS],C:年前两位

```

###pwd 查看当前所在路径

###cd 改变当前目录

```shell
- ：返回上层目录
.. :返回上层目录
回车  ：返回主目录
/   :根目录

```

###mkdir [选项] 目录… | 创建新目录

```shell
-p  递归创建目录，若父目录不存在则依次创建
-m  自定义创建目录的权限  eg:mkdir -m 777 hehe
-v  显示创建目录的详细信息

```

###rmdir 删除空目录

```shell
-v  显示执行过程
-p  若自父母删除后父目录为空则一并删除

```

###rm [选项] 文件… | 一个或多个文件或目录

```shell
-f  忽略不存在的文件，不给出提示
-i  交互式删除
-r  将列出的目录及其子目录递归删除
-v  列出详细信息

```

###echo：显示内容

```shell
-n  输出后不换行
-e  遇到转义字符特殊处理  
    eg:
        echo "he\nhe"   显示he\nhe
        ehco -e "he\nhe"    显示he(换行了)he

```

###cat [选项] [文件]..| 一次显示整个文件或从键盘创建一个文件或将几个文件合并成一个文件

```shell
-n  编号文件内容再输出
-E  在结束行提示$

```

###tac | 反向显示

###more | 按页查看文章内容，从前向后读取文件，因此在启动时就加载整个文件

```shell
+n  从第n行开始显示
-n  每次查看n行数据
+/String    搜寻String字符串位置，从其前两行开始查看
-c  清屏再显示
-p  换页时清屏

```

###less | 可前后移动地逐屏查看文章内容，在查看前不会加载整个文件

```shell
-m  显示类似于more命令的百分比
-N  显示行号
/   字符串：向下搜索“字符串”的功能
?   字符串：向上搜索“字符串”的功能
n   重复前一个搜索（与 / 或 ? 有关）
N   反向重复前一个搜索（与 / 或 ? 有关）
b   向后翻一页
d   向后翻半页

```

###nl [选项]… [文件]… | 将输出内容自动加上行号

```shell
-b
-b a 不论是否有空行，都列出行号（类似 cat -n)
-b t 空行则不列行号（默认）
-n 有ln rn rz三个参数，分别为再最左方显示，最右方显示不加0，最右方显示加0
```

###head [参数]… [文件]… | 显示档案开头，默认开头10行

```shell
-v  显示文件名
-c number   显示前number个字符,若number为负数,则显示除最后number个字符的所有内容
-number/n (+)number     显示前number行内容，
-n number   若number为负数，则显示除最后number行数据的所有内容

```

###tail [必要参数] [选择参数] [文件] | 显示文件结尾内容

```shell
-v  显示详细的处理信息
-q  不显示处理信息
-num/-n (-)num      显示最后num行内容
-n +num 从第num行开始显示后面的数据
-c  显示最后c个字符
-f  循环读取

```

###vi 编辑文件

```shell
:w filename 将文章以指定的文件名保存起来  
:wq 保存并退出
:q! 不保存而强制退出
命令行模式功能键
1）插入模式
    按「i」切换进入插入模式「insert mode」，按"i"进入插入模式后是从光标当前位置开始输入文件；
    按「a」进入插入模式后，是从目前光标所在位置的下一个位置开始输入文字；
    按「o」进入插入模式后，是插入新的一行，从行首开始输入文字。

2）从插入模式切换为命令行模式
  按「ESC」键。
3）移动光标
　　vi可以直接用键盘上的光标来上下左右移动，但正规的vi是用小写英文字母「h」、「j」、「k」、「l」，分别控制光标左、下、上、右移一格。
　　按「ctrl」+「b」：屏幕往"后"移动一页。
　　按「ctrl」+「f」：屏幕往"前"移动一页。
　　按「ctrl」+「u」：屏幕往"后"移动半页。
　　按「ctrl」+「d」：屏幕往"前"移动半页。
　　按数字「0」：移到文章的开头。
　　按「G」：移动到文章的最后。
　　按「$」：移动到光标所在行的"行尾"。
　　按「^」：移动到光标所在行的"行首"
　　按「w」：光标跳到下个字的开头
　　按「e」：光标跳到下个字的字尾
　　按「b」：光标回到上个字的开头
　　按「#l」：光标移到该行的第#个位置，如：5l,56l。

4）删除文字
　　「x」：每按一次，删除光标所在位置的"后面"一个字符。
　　「#x」：例如，「6x」表示删除光标所在位置的"后面"6个字符。
　　「X」：大写的X，每按一次，删除光标所在位置的"前面"一个字符。
　　「#X」：例如，「20X」表示删除光标所在位置的"前面"20个字符。
　　「dd」：删除光标所在行。
　　「#dd」：从光标所在行开始删除#行

5）复制
　　「yw」：将光标所在之处到字尾的字符复制到缓冲区中。
　　「#yw」：复制#个字到缓冲区
　　「yy」：复制光标所在行到缓冲区。
　　「#yy」：例如，「6yy」表示拷贝从光标所在的该行"往下数"6行文字。
　　「p」：将缓冲区内的字符贴到光标所在位置。注意：所有与"y"有关的复制命令都必须与"p"配合才能完成复制与粘贴功能。

6）替换
　　「r」：替换光标所在处的字符。
　　「R」：替换光标所到之处的字符，直到按下「ESC」键为止。

7）回复上一次操作
　　「u」：如果您误执行一个命令，可以马上按下「u」，回到上一个操作。按多次"u"可以执行多次回复。

8）更改
　　「cw」：更改光标所在处的字到字尾处
　　「c#w」：例如，「c3w」表示更改3个字

9）跳至指定的行
　　「ctrl」+「g」列出光标所在行的行号。
　　「#G」：例如，「15G」，表示移动光标至文章的第15行行首。

```

###which 可执行文件名称 | 查看可执行文件的位置，在PATH变量指定的路径中查看系统命令是否存在及其位置

### whereis [-bmsu] [BMS 目录名 -f ] 文件名| 定位可执行文件、源代码文件、帮助文件在文件系统中的位置

```shell
-b   定位可执行文件。
-m   定位帮助文件。
-s   定位源代码文件。
-u   搜索默认路径下除可执行文件、源代码文件、帮助文件以外的其它文件。
-B   指定搜索可执行文件的路径。
-M   指定搜索帮助文件的路径。
-S   指定搜索源代码文件的路径。

```

###locate | 通过搜寻数据库快速搜寻档案

```shell
-r  使用正规运算式做寻找的条件

```

### find find [PATH] [option] [action] | 在文件树种查找文件，并作出相应的处理

```shell
选项与参数：
1. 与时间有关的选项：共有 -atime, -ctime 与 -mtime 和-amin,-cmin与-mmin，以 -mtime 说明
    -mtime n ：n 为数字，意义为在 n 天之前的『一天之内』被更动过内容的档案；
    -mtime +n ：列出在 n 天之前(不含 n 天本身)被更动过内容的档案档名；
    -mtime -n ：列出在 n 天之内(含 n 天本身)被更动过内容的档案档名。
    -newer file ：file 为一个存在的档案，列出比 file 还要新的档案档名

2. 与使用者或组名有关的参数：
    -uid n ：n 为数字，这个数字是用户的账号 ID，亦即 UID
    -gid n ：n 为数字，这个数字是组名的 ID，亦即 GID
    -user name ：name 为使用者账号名称！例如 dmtsai
    -group name：name 为组名，例如 users ；
    -nouser ：寻找档案的拥有者不存在 /etc/passwd 的人！
    -nogroup ：寻找档案的拥有群组不存在于 /etc/group 的档案！

3. 与档案权限及名称有关的参数：
    -name filename：搜寻文件名为 filename 的档案（可使用通配符）
    -size [+-]SIZE：搜寻比 SIZE 还要大(+)或小(-)的档案。这个 SIZE 的规格有：
        c: 代表 byte
        k: 代表 1024bytes。所以，要找比 50KB还要大的档案，就是『 -size +50k 』
    -type TYPE ：搜寻档案的类型为 TYPE 的，类型主要有：
        一般正规档案 (f)
        装置档案 (b, c)
        目录 (d)
        连结档 (l)
        socket (s)
        FIFO (p)
    -perm mode ：搜寻档案权限『刚好等于』 mode的档案，这个mode为类似chmod的属性值，举例来说，-rwsr-xr-x 的属性为4755！
    -perm -mode ：搜寻档案权限『必须要全部囊括 mode 的权限』的档案，举例来说，
        我们要搜寻-rwxr--r-- 亦即 0744 的档案，使用-perm -0744，当一个档案的权限为 -rwsr-xr-x ，亦即 4755 时，也会被列出来，因为 -rwsr-xr-x 的属性已经囊括了 -rwxr--r-- 的属性了。
    -perm +mode ：搜寻档案权限『包含任一 mode 的权限』的档案，举例来
        说，我们搜寻-rwxr-xr-x ，亦即 -perm +755 时，但一个文件属性为 -rw-------也会被列出来，因为他有 -rw.... 的属性存在！
4. 额外可进行的动作：
    -exec command ：command 为其他指令，-exec 后面可再接额外的指令来处理搜寻到的结果。
    -print ：将结果打印到屏幕上，这个动作是预设动作！
    eg:
        find / -perm +7000 -exec ls -l {} \; ,额外指令以-exec开头，以\;结尾{}代替前面找到的内容
    | xargs 
        -i  默认的前面输出用{}代替 
        eg:
            find . -name "*.log" | xargs -i mv {} test4

```

### grep ‘正则表达式’ 文件名 | 用正则表达式搜索文本，并把匹配的行打印出来

```shell
-c  只输出匹配行的计数。
-I  不区分大小写(只适用于单字符)。
-l  只显示文件名
-v  显示不包含匹配文本的所有行。
-n  显示匹配行数据及其行号

```

### file | 判断文件类型

### gzip [-cdtv#] 檔名 | 压缩、解压缩，源文件都不再存在

```shell
-d  进行解压缩
-c  将压缩的数据输出到屏幕上
-v  :显示原档案/压缩文件案的压缩比等信息
-#  ：压缩等级，-1最快，但压缩比最差，=9最慢，但压缩比最好

```

### gunzip | 解压缩

### bzip2 | 压缩、解压缩

```shell
-d  :解压
-z  :压缩
-k  :保留源文件
-c ：将压缩的过程产生的数据输出到屏幕上！
-v ：可以显示出原档案/压缩文件案的压缩比等信息；
-# ：与 gzip 同样的，都是在计算压缩比的参数， -9 最佳， -1 最快！

```

### bzcat 读取数据而无需解压

### tar [主选项+辅选项] 文件或者目录 | 多个目录或档案打包、压缩成一个大档案

```shell
主选项：
    -c  建立打包档案，可搭配 -v 来察看过程中被打包的档名(filename)
    -t  察看打包档案的内容含有哪些档名，重点在察看『档名』就是了；
    -x  解打包或解压缩的功能，可以搭配 -C (大写) 在特定目录解开
辅选项：
    -j  透过 bzip2 的支持进行压缩/解压缩：此时档名最好为 *.tar.bz2
    -z  透过 gzip 的支持进行压缩/解压缩：此时档名最好为 *.tar.gz
    -v  在压缩/解压缩的过程中，将正在处理的文件名显示出来！
    -f filename -f 后面要立刻接要被处理的档名！
    -C 目录   这个选项用在解压缩，若要在特定目录解压缩，可以使用这个选项。
    --exclude FILE：在压缩打包过程中忽略某文件 eg: tar --exclude /home/zenghao -zcvf myfile.tar.gz /home/* /etc
    -p  保留备份数据的原本权限与属性，常用于备份(-c)重要的配置文件
    -P(大写）  保留绝对路径，亦即允许备份数据中含有根目录存在之意；
eg:
    压 缩：tar -jcvf filename.tar.bz2 要被压缩的档案或目录名称
    查 询：tar -jtvf filename.tar.bz2
    解压缩：tar -jxvf filename.tar.bz2 -C 欲解压缩的目录

```

### exit 退出当前shell

### logout 退出登录shell

### shutdown -h now

### users 显示当前登录系统地用户

### who 登录在本机的用户与来源

```shell
-H或--heading 　显示各栏位的标题信息列。

```

### w 登录在本机的用户及其运行的程序

```shell
-s 　使用简洁格式列表，不显示用户登入时间，终端机阶段作业和程序所耗费的CPU时间。
-h 　不显示各栏位的标题信息列。

```

### write 给当前联机的用户发消息

### wall 给所有登录再本机的用户发消息

### last 查看用户的登陆日志

### lastlog 查看每个用户最后的登陆时间

### finger [选项] [使用者] [用户@主机] | 查看用户信息

```shell
-s 显示用户的注册名、实际姓名、终端名称、写状态、停滞时间、登录时间等信息
-l 除了用-s选项显示的信息外，还显示用户主目录、登录shell、邮件状态等信息，以及用户主目录下的.plan、.project和.forward文件的内容。
-p 除了不显示.plan文件和.project文件以外，与-l选项相同

```

### hostname 查看主机名

### alias ii = “ls -l” | 添加别名

### unalias ii | 清除别名

### useradd [-u UID] [-g 初始群组] [-G 次要群组] [-c 说明栏] [-d 家目录绝对路径] [-s shell] 使用者账号名 | 新增用户

```shell
-M  不建立用户家目录！(系统账号默认值)
-m  建立用户家目录！(一般账号默认值)
-r  建立一个系统的账号，这个账号的 UID 会有限制 
-e  账号失效日期，格式为『YYYY-MM-DD』
-D  查看useradd的各项默认值

```

### passwd | 修改密码

```shell
-l  使密码失效
-u  与-l相对，用户解锁
-S  列出登陆用户passwd文件内的相关参数
-n  后面接天数，shadow 的第 4 字段，多久不可修改密码天数
-x  后面接天数，shadow 的第 5 字段，多久内必须要更动密码
-w  后面接天数，shadow 的第 6 字段，密码过期前的警告天数
-i  后面接『日期』，shadow 的第 7 字段，密码失效日期
使用管道刘设置密码：echo "zeng" | passwd --stdin zenghao

```

### userdel 删除用户

```shell
-r  用户文件一并删除

```

### chage [-ldEImMW] 账号名 | 修改用户密码的相关属性

```shell
-l  列出该账号的详细密码参数；
-d  后面接日期，修改 shadow 第三字段(最近一次更改密码的日期)，格式YYYY-MM-DD
-E  后面接日期，修改 shadow 第八字段(账号失效日)，格式 YYYY-MM-DD
-I  后面接天数，修改 shadow 第七字段(密码失效日期)
-m  后面接天数，修改 shadow 第四字段(密码最短保留天数)
-M  后面接天数，修改 shadow 第五字段(密码多久需要进行变更)
-W  后面接天数，修改 shadow 第六字段(密码过期前警告日期)

```

### usermod [-cdegGlsuLU] username | 修改用户的相关属性

```shell
-c  后面接账号的说明，即 /etc/passwd 第五栏的说明栏，可以加入一些账号的说明。
-d  后面接账号的家目录，即修改 /etc/passwd 的第六栏；
-e  后面接日期，格式是 YYYY-MM-DD 也就是在 /etc/shadow 内的第八个字段数据啦！
-f  后面接天数为 shadow 的第七字段。
-g  后面接初始群组，修改 /etc/passwd 的第四个字段，亦即是GID的字段！
-G  后面接次要群组，修改这个使用者能够支持的群组
-l  后面接账号名称。亦即是修改账号名称， /etc/passwd 的第一栏！
-s  后面接 Shell 的实际档案，例如 /bin/bash 或 /bin/csh 等等。
-u  后面接 UID 数字啦！即 /etc/passwd 第三栏的资料；
-L  冻结密码
-U  解冻密码

```

### id [username] | 查看用户相关的id信息，还可以用来判断用户是否存在

### groups 查看登陆用户支持的群组， 第一个输出的群组为有效群组

### newgrp 切换有效群组

### groupadd [-g gid] 组名 | 添加组

```shell
-g  设定添加组的特定组id

```

### groupmod [-g gid] [-n group_name] 群组名 | 修改组信息

```shell
-g  修改既有的 GID 数字
-n  修改既有的组名

```

### groupdel [groupname] | 删除群组

### gpasswd | 群组管理员功能

```shell
root管理员动作：
    -gpasswd groupname 设定密码
    -gpasswd [-A user1,...] [-M user3,...] groupname
        -A  将 groupname 的主控权交由后面的使用者管理(该群组的管理员)
        -M  将某些账号加入这个群组当中
    -gpasswd [-r] groupname
        -r  将 groupname 的密码移除
群组管理员动作：
    - gpasswd [-ad] user groupname 
        -a  将某位使用者加入到 groupname 这个群组当中
        -d  将某位使用者移除出 groupname 这个群组当中

```

### chfn修改个人信息

### mount [-t vfstype] [-o options] device dir

```shell
-ro 采用只读方式挂接设备
-rw 采用读写方式挂接设备
eg:mount /home/mydisk.iso /tmp/mnt 通过mnt访问mydisk内的内容

```

### mount 取消挂载

### cut

```shell
-b ：以字节为单位进行分割。这些字节位置将忽略多字节字符边界，除非也指定了 -n 标志。
-c ：以字符为单位进行分割。
-d ：自定义分隔符，默认为制表符。
-f  ：与-d一起使用，指定显示哪个区域。

```

### sort

```shell
-n   依照数值的大小排序。
-o<输出文件>   将排序后的结果存入指定的文件。
-r   以相反的顺序来排序。
-t<分隔字符>   指定排序时所用的栏位分隔字符。
-k  选择以哪个区间进行排序。

```

### wc 统计指定文件中的字节数、字数、行数, 并将统计结果显示输出

```shell
-l filename 报告行数
-c filename 报告字节数
-m filename 报告字符数
-w filename 报告单词数

```

### uniq 去除文件中相邻的重复行

```shell
清空/新建文件，将内容重定向输入进去
&> 正确、错误都重定向过去
```

### set 显示环境变量和普通变量

### env 显示环境变量

### export 把普通变量变成环境变量

### unset 删除一个环境变量

```shell
aaa(){} 定义函数
```

### read

```shell
-p  接提示字符
-t  接等待的秒数
```

### declare、typeset

```shell
-i 声明为整数
-a 声明为数组
-f 声明为函数
-r 声明为只读

```

### ulimit 限制使用者的某些系统资源

```shell
-f  此 shell 可以建立的最大档案容量 (一般可能设定为 2GB)单位为 Kbytes eg: ulimit -f 1024 限制使用者仅能建立 1MBytes 以下的容量的档案
```

### df [选项] [文件] | 显示指定磁盘文件的可用空间,如果没有文件名被指定，则所有当前被挂载的文件系统的可用空间将被显示

```shell
-a  显示全部文件系统
-h  文件大小友好显示
-l  只显示本地文件系统
-i  显示inode信息
-T  显示文件系统类型
```

### du [选项] [文件] | 显示每个文件和目录的磁盘使用空间

```shell
-h  方便阅读的方式
-s  只显示总和的大小
```

### ln [参数] [源文件或目录] [目标文件或目录] | 某一个文件在另外一个位置建立一个同步的链接

```shell
-s  建立软连接   
-v  显示详细的处理过程
```

### diff [参数] [文件1或目录1] [文件2或目录2] | 比较单个文件或者目录内容

```shell
-b 　不检查空格字符的不同。
-B 　不检查空白行。
-i  不检查大小写
-q  仅显示差异而不显示详细信息
eg: diff a b > parch.log 比较两个文件的不同并产生补丁
```

### date [参数]… [+格式] | 显示或设定系统的日期与时间

```shell
%H 小时(以00-23来表示)。 
%M 分钟(以00-59来表示)。 
%P AM或PM。
%D 日期(含年月日)
%U 该年中的周数。
date -s “2015-10-17 01:01:01″ //时间设定
date +%Y%m%d         //显示前天年月日
date +%Y%m%d --date="+1 day/month/year"  //显示前一天/月/年的日期
date +%Y%m%d --date="-1 day/month/year"  //显示后一天/月/年的日期
date -d '2 weeks' 2周后的日期

```

### cal [参数] 月份] [年份] | 查看日历

```shell
-1  显示当月的月历
-3  显示前、当、后一个月的日历
-m  显示星期一为一个星期的第一天
-s  （默认）星期天为第一天
-j  显示当月是一年中的第几天的日历
-y  显示当前年份的日历

```

### ps | 列出当前进程的快照

```shell
a   显示所有的进程
-a  显示同一终端下的所有程序
e   显示环境变量
f   显示进程间的关系
-H  显示树状结构
r   显示当前终端的程序
T   显示当前终端的所有程序
-au 显示更详细的信息
-aux    显示所有包含其他使用者的行程 
-u  指定用户的所有进程

```

### top [参数] | 显示当前系统正在执行的进程的相关信息，包括进程ID、内存占用率、CPU占用率等

### kill [参数] [进程号] | 杀死进程

### free [参数] | 显示Linux系统中空闲的、已用的物理内存及swap内存,及被内核使用的buffer

### vmstat | 对操作系统的虚拟内存、进程、CPU活动进行监控

### iostat [参数] [时间t] [次数n](每隔t时间刷新一次，最多刷新n次）| 对系统的磁盘操作活动进行监视,汇报磁盘活动统计情况，同时也会汇报出CPU使用情况

```shell
-p[磁盘] 显示磁盘和分区的情况
```

### watch [参数] [命令] |重复执行某一命令以观察变化

```shell
-n  时隔多少秒刷新
-d  高亮显示动态变化
```

### at [参数] [时间] | 在一个指定的时间执行一个指定任务，只能执行一次

```shell
HH:MM[am|pm] + number [minutes|hours|days|weeks] 强制在某年某月某日的某时刻进行该项任务
atq 查看系统未执行的任务
atrm n 删除编号为n的任务
at -c n 显示编号为n的任务的内容
```

### crontab | 定时任务调度

```shell
file    载入crontab
-e  编辑某个用户的crontab文件内容
-l  显示某个用户的crontab文件内容
-r  删除某个用户的crontab文件

```

### ifconfig [网络设备] [参数] | 查看和配置网络设备

### route | 显示和操作IP路由表

### ping [参数] [主机名或IP地址] | 测试与目标主机的连通性

```shell
-q  只显示最后的结果
```

### netstat | 显示与IP、TCP、UDP和ICMP协议相关的统计数据

### telnet [参数] [主机] | 用于远程登录，采用明文传送报文，安全性不好

### rcp [参数] [源文件] [目标文件] | 远程文件拷贝

```shell
-r  递归复制
-p  保留源文件的属性
usage: rcp –r remote_hostname:remote_dir local_dir
```

### wget [参数] [URL地址] | 直接从网络上下载文件

```shell
-o FILE 把记录写到FILE文件中    eg : wget -O a.txt URL
wget --limit-rate=300k URL  限速下载

```

### awk

```shell
-F 分隔符  以分隔符分隔内容
{}  要执行的脚本内容 eg:cat /etc/passwd |awk  -F ':'  '{print $1"\t"$7}'

```

### sed 对数据行进行替换、删除、新增、选取等操作

```shell
a   新增，在新的下一行出现
c   取代，取代 n1,n2 之间的行 eg: sed '1,2c Hi' ab
d   删除
i   插入，在新的上一行出现

```

### paste 合并文件，需确保合并的两文件行数相同

```shell
-d  指定不同于空格或tab键的域分隔符
-s  按行合并，单独一个文件为一行

```

### su [参数] user | 切换登陆

```shell
-l  切换时连同环境变量、工作目录一起改变
-c command  执行command变回原来的使用者

```

### sudo | 以特定用户的权限执行特定命令

```shell
-l  列出当前用户可执行的命令
-u username#uid 以指定用户执行命令
```

## **系统信息**

arch 显示机器的处理器架构(1)

uname -m 显示机器的处理器架构(2)

uname -r 显示正在使用的内核版本

dmidecode -q 显示硬件系统部件 - (SMBIOS / DMI)

hdparm -i /dev/hda 罗列一个磁盘的架构特性

hdparm -tT /dev/sda 在磁盘上执行测试性读取操作

cat /proc/cpuinfo 显示CPU info的信息

cat /proc/interrupts 显示中断

cat /proc/meminfo 校验内存使用

cat /proc/swaps 显示哪些swap被使用

cat /proc/version 显示内核的版本

cat /proc/net/dev 显示网络适配器及统计

cat /proc/mounts 显示已加载的文件系统

lspci -tv 罗列 PCI 设备

lsusb -tv 显示 USB 设备

date 显示系统日期

cal 2007 显示2007年的日历表

date 041217002007.00 设置日期和时间 - 月日时分年.秒

clock -w 将时间修改保存到 BIOS

## **关机 (系统的关机、重启以及登出 )**

shutdown -h now 关闭系统(1)

init 0 关闭系统(2)

telinit 0 关闭系统(3)

shutdown -h hours:minutes & 按预定时间关闭系统

shutdown -c 取消按预定时间关闭系统

shutdown -r now 重启(1)

reboot 重启(2)

logout 注销

## **文件和目录**

cd /home 进入 '/ home' 目录'

cd .. 返回上一级目录

cd ../.. 返回上两级目录

cd 进入个人的主目录

cd ~user1 进入个人的主目录

cd - 返回上次所在的目录

pwd 显示工作路径

ls 查看目录中的文件

ls -F 查看目录中的文件

ls -l 显示文件和目录的详细资料

ls -a 显示隐藏文件

ls *[0-9]* 显示包含数字的文件名和目录名

tree 显示文件和目录由根目录开始的树形结构(1)

lstree 显示文件和目录由根目录开始的树形结构(2)

mkdir dir1 创建一个叫做 'dir1' 的目录'

mkdir dir1 dir2 同时创建两个目录

mkdir -p /tmp/dir1/dir2 创建一个目录树

rm -f file1 删除一个叫做 'file1' 的文件'

rmdir dir1 删除一个叫做 'dir1' 的目录'

rm -rf dir1 删除一个叫做 'dir1' 的目录并同时删除其内容

rm -rf dir1 dir2 同时删除两个目录及它们的内容

mv dir1 new_dir 重命名/移动 一个目录

cp file1 file2 复制一个文件

cp dir/* . 复制一个目录下的所有文件到当前工作目录

cp -a /tmp/dir1 . 复制一个目录到当前工作目录

cp -a dir1 dir2 复制一个目录

ln -s file1 lnk1 创建一个指向文件或目录的软链接

ln file1 lnk1 创建一个指向文件或目录的物理链接

touch -t 0712250000 file1 修改一个文件或目录的时间戳 - (YYMMDDhhmm)

file file1 outputs the mime type of the file as text

iconv -l 列出已知的编码

iconv -f fromEncoding -t toEncoding inputFile > outputFile creates a new from the given input file by assuming it is encoded in fromEncoding and converting it to toEncoding.

find . -maxdepth 1 -name *.jpg -print -exec convert "{}" -resize 80x60 "thumbs/{}" \; batch resize files in the current directory and send them to a thumbnails directory (requires convert from Imagemagick)

## **文件搜索**

find / -name file1 从 '/' 开始进入根文件系统搜索文件和目录

find / -user user1 搜索属于用户 'user1' 的文件和目录

find /home/user1 -name \*.bin 在目录 '/ home/user1' 中搜索带有'.bin' 结尾的文件

find /usr/bin -type f -atime +100 搜索在过去100天内未被使用过的执行文件

find /usr/bin -type f -mtime -10 搜索在10天内被创建或者修改过的文件

find / -name \*.rpm -exec chmod 755 '{}' \; 搜索以 '.rpm' 结尾的文件并定义其权限

find / -xdev -name \*.rpm 搜索以 '.rpm' 结尾的文件，忽略光驱、捷盘等可移动设备

locate \*.ps 寻找以 '.ps' 结尾的文件 - 先运行 'updatedb' 命令

whereis halt 显示一个二进制文件、源码或man的位置

which halt 显示一个二进制文件或可执行文件的完整路径

## **挂载一个文件系统**

mount /dev/hda2 /mnt/hda2 挂载一个叫做hda2的盘 - 确定目录 '/ mnt/hda2' 已经存在

umount /dev/hda2 卸载一个叫做hda2的盘 - 先从挂载点 '/ mnt/hda2' 退出

fuser -km /mnt/hda2 当设备繁忙时强制卸载

umount -n /mnt/hda2 运行卸载操作而不写入 /etc/mtab 文件- 当文件为只读或当磁盘写满时非常有用

mount /dev/fd0 /mnt/floppy 挂载一个软盘

mount /dev/cdrom /mnt/cdrom 挂载一个cdrom或dvdrom

mount /dev/hdc /mnt/cdrecorder 挂载一个cdrw或dvdrom

mount /dev/hdb /mnt/cdrecorder 挂载一个cdrw或dvdrom

mount -o loop file.iso /mnt/cdrom 挂载一个文件或ISO镜像文件

mount -t vfat /dev/hda5 /mnt/hda5 挂载一个Windows FAT32文件系统

mount /dev/sda1 /mnt/usbdisk 挂载一个usb 捷盘或闪存设备

mount -t smbfs -o username=user,password=pass //WinClient/share /mnt/share 挂载一个windows网络共享

## **磁盘空间**

df -h 显示已经挂载的分区列表

ls -lSr |more 以尺寸大小排列文件和目录

du -sh dir1 估算目录 'dir1' 已经使用的磁盘空间'

du -sk * | sort -rn 以容量大小为依据依次显示文件和目录的大小

rpm -q -a --qf '%10{SIZE}t%{NAME}n' | sort -k1,1n 以大小为依据依次显示已安装的rpm包所使用的空间 (fedora, redhat类系统)

dpkg-query -W -f='${Installed-Size;10}t${Package}n' | sort -k1,1n 以大小为依据显示已安装的deb包所使用的空间 (ubuntu, debian类系统)

## **用户和群组**

groupadd group_name 创建一个新用户组

groupdel group_name 删除一个用户组

groupmod -n new_group_name old_group_name 重命名一个用户组

useradd -c "Name Surname " -g admin -d /home/user1 -s /bin/bash user1 创建一个属于 "admin" 用户组的用户

useradd user1 创建一个新用户

userdel -r user1 删除一个用户 ( '-r' 排除主目录)

usermod -c "User FTP" -g system -d /ftp/user1 -s /bin/nologin user1 修改用户属性

passwd 修改口令

passwd user1 修改一个用户的口令 (只允许root执行)

chage -E 2005-12-31 user1 设置用户口令的失效期限

pwck 检查 '/etc/passwd' 的文件格式和语法修正以及存在的用户

grpck 检查 '/etc/passwd' 的文件格式和语法修正以及存在的群组

newgrp group_name 登陆进一个新的群组以改变新创建文件的预设群组

## **文件的权限 - 使用 "+" 设置权限，使用 "-" 用于取消**

ls -lh 显示权限

ls /tmp | pr -T5 -W$COLUMNS 将终端划分成5栏显示

chmod ugo+rwx directory1 设置目录的所有人(u)、群组(g)以及其他人(o)以读（r ）、写(w)和执行(x)的权限

chmod go-rwx directory1 删除群组(g)与其他人(o)对目录的读写执行权限

chown user1 file1 改变一个文件的所有人属性

chown -R user1 directory1 改变一个目录的所有人属性并同时改变改目录下所有文件的属性

chgrp group1 file1 改变文件的群组

chown user1:group1 file1 改变一个文件的所有人和群组属性

find / -perm -u+s 罗列一个系统中所有使用了SUID控制的文件

chmod u+s /bin/file1 设置一个二进制文件的 SUID 位 - 运行该文件的用户也被赋予和所有者同样的权限

chmod u-s /bin/file1 禁用一个二进制文件的 SUID位

chmod g+s /home/public 设置一个目录的SGID 位 - 类似SUID ，不过这是针对目录的

chmod g-s /home/public 禁用一个目录的 SGID 位

chmod o+t /home/public 设置一个文件的 STIKY 位 - 只允许合法所有人删除文件

chmod o-t /home/public 禁用一个目录的 STIKY 位

## **文件的特殊属性 - 使用 "+" 设置权限，使用 "-" 用于取消**

chattr +a file1 只允许以追加方式读写文件

chattr +c file1 允许这个文件能被内核自动压缩/解压

chattr +d file1 在进行文件系统备份时，dump程序将忽略这个文件

chattr +i file1 设置成不可变的文件，不能被删除、修改、重命名或者链接

chattr +s file1 允许一个文件被安全地删除

chattr +S file1 一旦应用程序对这个文件执行了写操作，使系统立刻把修改的结果写到磁盘

chattr +u file1 若文件被删除，系统会允许你在以后恢复这个被删除的文件

lsattr 显示特殊的属性

## **打包和压缩文件**

bunzip2 file1.bz2 解压一个叫做 'file1.bz2'的文件

bzip2 file1 压缩一个叫做 'file1' 的文件

gunzip file1.gz 解压一个叫做 'file1.gz'的文件

gzip file1 压缩一个叫做 'file1'的文件

gzip -9 file1 最大程度压缩

rar a file1.rar test_file 创建一个叫做 'file1.rar' 的包

rar a file1.rar file1 file2 dir1 同时压缩 'file1', 'file2' 以及目录 'dir1'

rar x file1.rar 解压rar包

unrar x file1.rar 解压rar包

tar -cvf archive.tar file1 创建一个非压缩的 tarball

tar -cvf archive.tar file1 file2 dir1 创建一个包含了 'file1', 'file2' 以及 'dir1'的档案文件

tar -tf archive.tar 显示一个包中的内容

tar -xvf archive.tar 释放一个包

tar -xvf archive.tar -C /tmp 将压缩包释放到 /tmp目录下

tar -cvfj archive.tar.bz2 dir1 创建一个bzip2格式的压缩包

tar -xvfj archive.tar.bz2 解压一个bzip2格式的压缩包

tar -cvfz archive.tar.gz dir1 创建一个gzip格式的压缩包

tar -xvfz archive.tar.gz 解压一个gzip格式的压缩包

zip file1.zip file1 创建一个zip格式的压缩包

zip -r file1.zip file1 file2 dir1 将几个文件和目录同时压缩成一个zip格式的压缩包

unzip file1.zip 解压一个zip格式压缩包

## **RPM 包 - （Fedora, Redhat及类似系统）**

rpm -ivh package.rpm 安装一个rpm包

rpm -ivh --nodeeps package.rpm 安装一个rpm包而忽略依赖关系警告

rpm -U package.rpm 更新一个rpm包但不改变其配置文件

rpm -F package.rpm 更新一个确定已经安装的rpm包

rpm -e package_name.rpm 删除一个rpm包

rpm -qa 显示系统中所有已经安装的rpm包

rpm -qa | grep httpd 显示所有名称中包含 "httpd" 字样的rpm包

rpm -qi package_name 获取一个已安装包的特殊信息

rpm -qg "System Environment/Daemons" 显示一个组件的rpm包

rpm -ql package_name 显示一个已经安装的rpm包提供的文件列表

rpm -qc package_name 显示一个已经安装的rpm包提供的配置文件列表

rpm -q package_name --whatrequires 显示与一个rpm包存在依赖关系的列表

rpm -q package_name --whatprovides 显示一个rpm包所占的体积

rpm -q package_name --scripts 显示在安装/删除期间所执行的脚本l

rpm -q package_name --changelog 显示一个rpm包的修改历史

rpm -qf /etc/httpd/conf/httpd.conf 确认所给的文件由哪个rpm包所提供

rpm -qp package.rpm -l 显示由一个尚未安装的rpm包提供的文件列表

rpm --import /media/cdrom/RPM-GPG-KEY 导入公钥数字证书

rpm --checksig package.rpm 确认一个rpm包的完整性

rpm -qa gpg-pubkey 确认已安装的所有rpm包的完整性

rpm -V package_name 检查文件尺寸、 许可、类型、所有者、群组、MD5检查以及最后修改时间

rpm -Va 检查系统中所有已安装的rpm包- 小心使用

rpm -Vp package.rpm 确认一个rpm包还未安装

rpm2cpio package.rpm | cpio --extract --make-directories *bin* 从一个rpm包运行可执行文件

rpm -ivh /usr/src/redhat/RPMS/`arch`/package.rpm 从一个rpm源码安装一个构建好的包

rpmbuild --rebuild package_name.src.rpm 从一个rpm源码构建一个 rpm 包

## **YUM 软件包升级器 - （Fedora, RedHat及类似系统）**

yum install package_name 下载并安装一个rpm包

yum localinstall package_name.rpm 将安装一个rpm包，使用你自己的软件仓库为你解决所有依赖关系

yum update package_name.rpm 更新当前系统中所有安装的rpm包

yum update package_name 更新一个rpm包

yum remove package_name 删除一个rpm包

yum list 列出当前系统中安装的所有包

yum search package_name 在rpm仓库中搜寻软件包

yum clean packages 清理rpm缓存删除下载的包

yum clean headers 删除所有头文件

yum clean all 删除所有缓存的包和头文件

DEB 包 (Debian, Ubuntu 以及类似系统)

dpkg -i package.deb 安装/更新一个 deb 包

dpkg -r package_name 从系统删除一个 deb 包

dpkg -l 显示系统中所有已经安装的 deb 包

dpkg -l | grep httpd 显示所有名称中包含 "httpd" 字样的deb包

dpkg -s package_name 获得已经安装在系统中一个特殊包的信息

dpkg -L package_name 显示系统中已经安装的一个deb包所提供的文件列表

dpkg --contents package.deb 显示尚未安装的一个包所提供的文件列表

dpkg -S /bin/ping 确认所给的文件由哪个deb包提供

APT 软件工具 (Debian, Ubuntu 以及类似系统)

apt-get install package_name 安装/更新一个 deb 包

apt-cdrom install package_name 从光盘安装/更新一个 deb 包

apt-get update 升级列表中的软件包

apt-get upgrade 升级所有已安装的软件

apt-get remove package_name 从系统删除一个deb包

apt-get check 确认依赖的软件仓库正确

apt-get clean 从下载的软件包中清理缓存

apt-cache search searched-package 返回包含所要搜索字符串的软件包名称

## 查看文件内容

cat file1 从第一个字节开始正向查看文件的内容

tac file1 从最后一行开始反向查看一个文件的内容

more file1 查看一个长文件的内容

less file1 类似于 'more' 命令，但是它允许在文件中和正向操作一样的反向操作

head -2 file1 查看一个文件的前两行

tail -2 file1 查看一个文件的最后两行

tail -f /var/log/messages 实时查看被添加到一个文件中的内容

## **文本处理**

cat file1 file2 ... | command <> file1_in.txt_or_file1_out.txt general syntax for text manipulation using PIPE, STDIN and STDOUT

cat file1 | command( sed, grep, awk, grep, etc...) > result.txt 合并一个文件的详细说明文本，并将简介写入一个新文件中

cat file1 | command( sed, grep, awk, grep, etc...) >> result.txt 合并一个文件的详细说明文本，并将简介写入一个已有的文件中

grep Aug /var/log/messages 在文件 '/var/log/messages'中查找关键词"Aug"

grep ^Aug /var/log/messages 在文件 '/var/log/messages'中查找以"Aug"开始的词汇

grep [0-9] /var/log/messages 选择 '/var/log/messages' 文件中所有包含数字的行

grep Aug -R /var/log/* 在目录 '/var/log' 及随后的目录中搜索字符串"Aug"

sed 's/stringa1/stringa2/g' example.txt 将example.txt文件中的 "string1" 替换成 "string2"

sed '/^$/d' example.txt 从example.txt文件中删除所有空白行

sed '/ *#/d; /^$/d' example.txt 从example.txt文件中删除所有注释和空白行

echo 'esempio' | tr '[:lower:]' '[:upper:]' 合并上下单元格内容

sed -e '1d' result.txt 从文件example.txt 中排除第一行

sed -n '/stringa1/p' 查看只包含词汇 "string1"的行

sed -e 's/ *$//' example.txt 删除每一行最后的空白字符

sed -e 's/stringa1//g' example.txt 从文档中只删除词汇 "string1" 并保留剩余全部

sed -n '1,5p;5q' example.txt 查看从第一行到第5行内容

sed -n '5p;5q' example.txt 查看第5行

sed -e 's/00*/0/g' example.txt 用单个零替换多个零

cat -n file1 标示文件的行数

cat example.txt | awk 'NR%2==1' 删除example.txt文件中的所有偶数行

echo a b c | awk '{print $1}' 查看一行第一栏

echo a b c | awk '{print $1,$3}' 查看一行的第一和第三栏

paste file1 file2 合并两个文件或两栏的内容

paste -d '+' file1 file2 合并两个文件或两栏的内容，中间用"+"区分

sort file1 file2 排序两个文件的内容

sort file1 file2 | uniq 取出两个文件的并集(重复的行只保留一份)

sort file1 file2 | uniq -u 删除交集，留下其他的行

sort file1 file2 | uniq -d 取出两个文件的交集(只留下同时存在于两个文件中的文件)

comm -1 file1 file2 比较两个文件的内容只删除 'file1' 所包含的内容

comm -2 file1 file2 比较两个文件的内容只删除 'file2' 所包含的内容

comm -3 file1 file2 比较两个文件的内容只删除两个文件共有的部分

## **字符设置和文件格式转换**

dos2unix filedos.txt fileunix.txt 将一个文本文件的格式从MSDOS转换成UNIX

unix2dos fileunix.txt filedos.txt 将一个文本文件的格式从UNIX转换成MSDOS

recode ..HTML < page.txt > page.html 将一个文本文件转换成html

recode -l | more 显示所有允许的转换格式

## **文件系统分析**

badblocks -v /dev/hda1 检查磁盘hda1上的坏磁块

fsck /dev/hda1 修复/检查hda1磁盘上linux文件系统的完整性

fsck.ext2 /dev/hda1 修复/检查hda1磁盘上ext2文件系统的完整性

e2fsck /dev/hda1 修复/检查hda1磁盘上ext2文件系统的完整性

e2fsck -j /dev/hda1 修复/检查hda1磁盘上ext3文件系统的完整性

fsck.ext3 /dev/hda1 修复/检查hda1磁盘上ext3文件系统的完整性

fsck.vfat /dev/hda1 修复/检查hda1磁盘上fat文件系统的完整性

fsck.msdos /dev/hda1 修复/检查hda1磁盘上dos文件系统的完整性

dosfsck /dev/hda1 修复/检查hda1磁盘上dos文件系统的完整性

## **初始化一个文件系统**

mkfs /dev/hda1 在hda1分区创建一个文件系统

mke2fs /dev/hda1 在hda1分区创建一个linux ext2的文件系统

mke2fs -j /dev/hda1 在hda1分区创建一个linux ext3(日志型)的文件系统

mkfs -t vfat 32 -F /dev/hda1 创建一个 FAT32 文件系统

fdformat -n /dev/fd0 格式化一个软盘

mkswap /dev/hda3 创建一个swap文件系统

## **SWAP文件系统**

mkswap /dev/hda3 创建一个swap文件系统

swapon /dev/hda3 启用一个新的swap文件系统

swapon /dev/hda2 /dev/hdb3 启用两个swap分区

## **备份**

dump -0aj -f /tmp/home0.bak /home 制作一个 '/home' 目录的完整备份

dump -1aj -f /tmp/home0.bak /home 制作一个 '/home' 目录的交互式备份

restore -if /tmp/home0.bak 还原一个交互式备份

rsync -rogpav --delete /home /tmp 同步两边的目录

rsync -rogpav -e ssh --delete /home ip_address:/tmp 通过SSH通道rsync

rsync -az -e ssh --delete ip_addr:/home/public /home/local 通过ssh和压缩将一个远程目录同步到本地目录

rsync -az -e ssh --delete /home/local ip_addr:/home/public 通过ssh和压缩将本地目录同步到远程目录

dd bs=1M if=/dev/hda | gzip | ssh user@ip_addr 'dd of=hda.gz' 通过ssh在远程主机上执行一次备份本地磁盘的操作

dd if=/dev/sda of=/tmp/file1 备份磁盘内容到一个文件

tar -Puf backup.tar /home/user 执行一次对 '/home/user' 目录的交互式备份操作

( cd /tmp/local/ && tar c . ) | ssh -C user@ip_addr 'cd /home/share/ && tar x -p' 通过ssh在远程目录中复制一个目录内容

( tar c /home ) | ssh -C user@ip_addr 'cd /home/backup-home && tar x -p' 通过ssh在远程目录中复制一个本地目录

tar cf - . | (cd /tmp/backup ; tar xf - ) 本地将一个目录复制到另一个地方，保留原有权限及链接

find /home/user1 -name '*.txt' | xargs cp -av --target-directory=/home/backup/ --parents 从一个目录查找并复制所有以 '.txt' 结尾的文件到另一个目录

find /var/log -name '*.log' | tar cv --files-from=- | bzip2 > log.tar.bz2 查找所有以 '.log' 结尾的文件并做成一个bzip包

dd if=/dev/hda of=/dev/fd0 bs=512 count=1 做一个将 MBR (Master Boot Record)内容复制到软盘的动作

dd if=/dev/fd0 of=/dev/hda bs=512 count=1 从已经保存到软盘的备份中恢复MBR内容

## **光盘**

cdrecord -v gracetime=2 dev=/dev/cdrom -eject blank=fast -force 清空一个可复写的光盘内容

mkisofs /dev/cdrom > cd.iso 在磁盘上创建一个光盘的iso镜像文件

mkisofs /dev/cdrom | gzip > cd_iso.gz 在磁盘上创建一个压缩了的光盘iso镜像文件

mkisofs -J -allow-leading-dots -R -V "Label CD" -iso-level 4 -o ./cd.iso data_cd 创建一个目录的iso镜像文件

cdrecord -v dev=/dev/cdrom cd.iso 刻录一个ISO镜像文件

gzip -dc cd_iso.gz | cdrecord dev=/dev/cdrom - 刻录一个压缩了的ISO镜像文件

mount -o loop cd.iso /mnt/iso 挂载一个ISO镜像文件

cd-paranoia -B 从一个CD光盘转录音轨到 wav 文件中

cd-paranoia -- "-3" 从一个CD光盘转录音轨到 wav 文件中（参数-3）

cdrecord --scanbus 扫描总线以识别scsi通道

dd if=/dev/hdc | md5sum 校验一个设备的md5sum编码，例如一张 CD



