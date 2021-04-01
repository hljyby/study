# python基础-BytesIO,StringIO

- - - StringIO
      - [常用方法](https://blog.csdn.net/u013210620/article/details/79276280#常用方法)
      - [示例代码](https://blog.csdn.net/u013210620/article/details/79276280#示例代码)
      - [strIO截取](https://blog.csdn.net/u013210620/article/details/79276280#strio截取)
      - [利用缓存写入文件](https://blog.csdn.net/u013210620/article/details/79276280#利用缓存写入文件)
    - BytesIO
      - [通过缓存存入文件](https://blog.csdn.net/u013210620/article/details/79276280#通过缓存存入文件)
      - [通过缓存读取文件](https://blog.csdn.net/u013210620/article/details/79276280#通过缓存读取文件)
      - [文件句柄赋值BytesIO](https://blog.csdn.net/u013210620/article/details/79276280#文件句柄赋值bytesio)



想要了解文件读取操作的，可以参考

[文件读取 文件读取 文件读取](http://blog.csdn.net/u013210620/article/details/78389913)

### **StringIO**

#### 常用方法

1、read
s.read([n])：参数n用于限定读取的长度，类型为int，默认为从当前位置读取对象s中所有的数据。读取结束后，位置被移动。

2、readline
s.readline([length])：length用于限定读取的结束位置，类型为int，缺省为None，即从当前位置读取至下一个以’\n’为结束符的当前行。读位置被移动。

3、readlines
s.readlines()：读取所有行

4、write
s.write(s)：从读写位置将参数s写入到对象s。参数为str或unicode类型，读写位置被移动。

5、writeline
s.writeline(s)：从读写位置将list写入给对象s。参数list为一个列表，列表的成员为str或unicode类型。读写位置被移动

6、getvalue
s.getvalue()：返回对象s中的所有数据

7、truncate
s.truncate([size])：从读写位置起切断数据，参数size限定裁剪长度，默认为None

8、tell
s.tell()　　#返回当前读写位置

9、seek
s.seek(pos[,mode])：移动当前读写位置至pos处，可选参数mode为0时将读写位置移动到pos处，为1时将读写位置从当前位置移动pos个长度，为2时读写位置置于末尾处再向后移动pos个长度。默认为0

10、close
s.close()：释放缓冲区，执行此函数后，数据将被释放，也不可再进行操作。

11、isatty
s.isatty()：此函数总是返回0。不论StringIO对象是否已被close。

12、flush
s.flush()：刷新缓冲区。

#### 示例代码

```python
from io import BytesIO,StringIO

"""
    read
    readline
    readlines
    write
    writeline
    getvalue
    truncate
    tell
    seek
    close
    isatty
    flush
"""


strIO = StringIO()
#0位置
print(strIO.tell())
strIO.write("www")

#3位置
print(strIO.tell())
#输出缓存内容
print(strIO.getvalue())
#移动到0位置
print(strIO.seek(0))
#读取全部内容
print(strIO.read())
#3位置
print(strIO.tell())
print("*"*10)

#移动到0位置
strIO.seek(0)
print(strIO.tell())
#覆盖读写
strIO.write(".baidu")
print(strIO.getvalue())

strIO.seek(1)
strIO.write(".com")
print(strIO.getvalue())

#末尾插入
strIO.seek(0,2)
strIO.write("AB")
print(strIO.getvalue())
#首部插入
strIO.seek(0,0)
strIO.write("CD")
print(strIO.getvalue())
#首部向后偏移一位覆盖插入
strIO.seek(1,0)
strIO.write("P")
print(strIO.getvalue())

#当前插入覆盖
strIO.seek(0,1)
strIO.write("EF")
print(strIO.getvalue())


strIO.write("我的")
print(strIO.getvalue())

```

输出如下：

```python
E:\python\python_sdk\python.exe E:/python/py_dev/python/bbs/safly.py
0
3
www
0
www
3
**********
0
.baidu
..comu
..comuAB
CDcomuAB
CPcomuAB
CPEFmuAB
CPEF我的AB

Process finished with exit code 0


```

#### **strIO截取**

```python
from io import BytesIO,StringIO

strIO  = StringIO()
strIO.write("abcdefgdsfdsfsdhij")
print(strIO.getvalue())

#从开头截取,会截取缓存种的部分片段
strIO.truncate(10)
print(strIO.getvalue())


#通过截取出来的10个字符，定位到第二个，然后截取2个
strIO.seek(2)
print(strIO.tell())
strIO.truncate()

print(strIO.getvalue())


```

输出如下：

```python
E:\python\python_sdk\python.exe E:/python/py_dev/python/bbs/safly.py
abcdefgdsfdsfsdhij
abcdefgdsf
2
ab

Process finished with exit code 0

```

#### **利用缓存写入文件**

```python
from io import BytesIO,StringIO

strIo = StringIO()

strIo.write("我的StringIO")

print(strIo.getvalue())


with open("file.txt",mode="w",encoding="utf-8") as file_w:
    strIo.truncate(4)
    file_w.write(strIo.getvalue())


```

然后文件写入后的结果如下：
![这里写图片描述](https://img-blog.csdn.net/20180207104427838?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvdTAxMzIxMDYyMA==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)

### **BytesIO**

BytesIO跟StringIo方法差不多，不过BytesIO操作的数据类型为bytes

#### 通过缓存，存入文件

```python
from io import BytesIO,StringIO

byIo = BytesIO()

#参数类型为bytes
byIo.write("我的byio".encode("utf-8"))

print(byIo.getvalue())

print(byIo.getvalue().decode("utf-8"))

#或者如下
print(byIo.getvalue().decode(encoding="utf-8"))
#或者如下
print(str(byIo.getvalue(),"utf8"))



#字节类型的，其实也可以进行seek，只不过一个汉字代表3个光标位置，如果移动5个就报错
byIo.seek(6)
print(byIo.tell())
print(byIo.read().decode("utf-8"))


#通过缓存写入文件
with open("file.txt",mode="wb") as file:
    file.write(byIo.getvalue())

```

我们看下写入文件的内容：
![这里写图片描述](https://img-blog.csdn.net/20180207110548261?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvdTAxMzIxMDYyMA==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)

#### 通过缓存，读取文件

```python
readIo = BytesIO()
with open("file.txt",mode="rb") as file:
        ret =file.read()
        print(ret,type(ret))

        #写入BytesIO缓存
        readIo.write(ret)

#从缓存种取出来

print(readIo.getvalue().decode("utf-8"))1234567891011
```

输出如下：

```python
E:\python\python_sdk\python.exe E:/python/py_dev/python/bbs/safly.py
b'\xe6\x88\x91\xe7\x9a\x84byio' <class 'bytes'>
我的byio

Process finished with exit code 0

```

#### 文件句柄赋值BytesIO

可以将文件句柄赋值为BytesIO

```python
readIo = BytesIO()
with open("file.txt",mode="rb") as readIo:
        rt = readIo.read()
        print(rt.decode("utf-8"))


#<_io.BufferedReader name='file.txt'>

print(readIo)

```

输出如下：

```
我的byio
<_io.BufferedReader name='file.txt'>
```

# Python3 Image图片webp格式转换，URL Image Byte字节流操作

前言

> 首先图片格式转换的方法有很多，但是转图片字节流的，我搜了一下午终于在 [stackoverflow](https://stackoverflow.com/questions/33101935/convert-pil-image-to-byte-array)上搜到了
> 说一下为什么要在线转这个图片格式
> 图片不需要下载到本地，爬取到图片url后，读取图片字节流数据，然后上传到自己七牛云上面，并且替换其格式(**这一点很坑**)

- 上传图片二进制数据到七牛云上面不难， 照着七牛云API文档基本就能行，有一点坑，七牛云官方文档[Python API](https://developer.qiniu.com/kodo/sdk/1242/python) 上面的Demo全是上传本地图片的put_file()方法，我要上传远程服务器上面的，没看到对应的方法。
- 准备修改qiniu SDK源码的，看到了一个put_data()方法能传字节流数据。

##### 好我写这篇博文重点来了

需求：由于我爬取的图片远程是google的 .webp格式的图片， 链接是https://xxxx.webp这种，而这个格式又不能直接修改后缀改。

于是我去网上搜Python3 图片格式转换的方法。
最多的就是这种方法

```python
 from PIL import Image   # 安装pillow 有些小坑  对了我的版本是Pillow==4.3.0
 im = Image.open("./demo1.jpg")
 im.save("./demo2.png")
```

但是我要上传的文件都不在本地，都是请求图片二进制流在线修改图片后缀。
二话不说直接亮代码吧，找了一下午，还在pillow的github issue上提问。终于在stackoverflow上搜到了。

```python
from io import BytesIO
from PIL import Image  # 注意我的Image版本是pip3 install Pillow==4.3.0
import requests

res = requests.get('http://p1.pstatp.com/list/300x196/pgc-image/152923179745640a81b1fdc.webp', stream=True)  # 获取字节流最好加stream这个参数,原因见requests官方文档

byte_stream = BytesIO(res.content)  
# 把请求到的数据转换为Bytes字节流(这样解释不知道对不对，可以参照[廖雪峰](https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/001431918785710e86a1a120ce04925bae155012c7fc71e000)的教程看一下)

roiImg = Image.open(byte_stream)   # Image打开Byte字节流数据
# roiImg.show()   #  弹出 显示图片
imgByteArr = io.BytesIO()     # 创建一个空的Bytes对象

roiImg.save(imgByteArr, format='PNG') # PNG就是图片格式，我试过换成JPG/jpg都不行 JPEG 可以

imgByteArr = imgByteArr.getvalue()   # 这个就是保存的图片字节流

# 下面这一步只是本地测试， 可以直接把imgByteArr，当成参数上传到七牛云
with open("./abc.png", "wb") as f:
    f.write(imgByteArr)
```

`我感觉我这个在线转换的绝对是CSDN第一篇， 搜了一下午，人都搜绝望了。`
还是 [stackoverflow](https://stackoverflow.com/questions/33101935/convert-pil-image-to-byte-array) 好用， 这个链接就是我搜到答案。

今天一上github ，作者回复我了的问题了，https://github.com/python-pillow/Pillow/issues/3192
虽然我自己查出来了，但还是感谢作者。

# Python学习之---open操作+buffering缓冲区+上下文管理+StringIO和BytesIO

## 文件操作

文件操作对编程语言的重要性不用多说，如果数据不能持久保存，信息技术也就失去了意义。

### 1.1 ,open 操作

```python
open(
    file,      # 文件名
    mode='r',  #默认为只读模式
    buffering=-1,# 缓冲区
    encoding=None,# 默认编码
    errors=None,#
    newline=None,
    closefd=True,
    opener=None,
)

```

| 操作 | 解释                                                         |
| ---- | ------------------------------------------------------------ |
| r    | 只读权限;默认是文本模式                                      |
| w    | **只写权限**,文件不存在则创建新的文件,如果存在则清空文件内容. |
| x    | 不存在则创建一个新的,存在则报错;**只写权限**                 |
| a    | **只写权限**,尾部追加写入,读也是从文件末尾开始读取,受文件指针影响 |
| b    | 只读二进制模式                                               |
| t    | 文本模式,相当于"rt ''只读模式,                               |
| +    | 为r,w,a,x提供缺失的读或者写功能,但是获取文件对象依旧按照r,w,a,x自己的特征 |

```python
# r模式
f = open('test') # 默认只读 
f.read() # 可以读取
f.write('abc')# 报错
f.close()#关闭文件
f = open('test', 'r') # 只读模式打开  
f.write('abc') 
f.close()
f = open('test1', 'r') # 只读，文件不存在 则创建一个新的文件
# w模式
f = open('test','w') # 只写打开
f.write('abc')
f.close()
f = open('test', mode='w') 
f.close()
>>> cat test # 看看内容
f = open('test1', mode='w')
f.write('123')
f.close()
>>> cat test1 # 看看内容

```

**wxa模式都可以产生新文件**

- w不管文件存在与否，都会生成全新内容的文件
- a不管文件是否存在，都能在打开的文件尾部追加
- x必须要求文件事先不存在，自己造一个新文件

### 文本模式打开

字符流，将文件的字节按照某种字符编码理解，按照字符操作。open的默认mode就是rt。

### 二进制模式

字节流，将文件就按照字节理解，与字符编码无关。二进制模式操作时，字节操作使用bytes类型.

```python
f = open("test3",'rb') # 二进制只读
s = f.read()
print(type(s)) # bytes
print(s)
f.close() # 关闭文件
f = open("test3",'wb') # IO对象
s = f.write("好好学习".encode())
print(s) ## 先会将汉字转化为进制模式,然后写进文件中
f.close()

```

**"+"补充缺省权限**

```python
f = open("test3",'rw') #
f = open("test3",'r+')
s = f.read()
f.write("好好学习")
print(f.read()) # 没有显示，为什么
f.close()
f = open("test3",'r+')  #文件不存在会报错
s = f.write("daydaystudy") #
print(f.read())
f.close()
>>> cat test3
f = open('test3', 'w+')	
f.read() #
f.close()
>>> cat test3
f = open('test3', 'a+')
f.write('test')
f.read()
f.close()
>>> cat test3
f = open('test3', 'a+')
f.write('edu')
f.close()
>>> cat test3
f = open('test3', 'x+') # 文件已存在,报错
f = open('test4', 'x+') #
f.write('python')
f.read()
f.close()
>>> cat test4

```

### 文件指针操作

文件指针,指向当前字节位置

mode = r -->指针在其实位置

moder =a -->指针在文件末尾开始

tell()显示当前指针位置

seek(offest [,whence])

**文本模式下:**

whence 0 缺省值，表示从头开始，offest只能正整数
whence 1 表示从当前位置，offest只接受0
whence 2 表示从EOF开始，offest只接受0

**f.seek(‘移动位置’, whence值)**

```python
# 文本模式
f = open('test4','r+')
f.tell() # 起始 返回当前的指针位置
f.read()
f.tell() # EOF  上面的read读取结束后,指针到结尾
f.seek(0) # 起始 回到起始位置
f.read()  #读取完毕,此时指针在末尾
f.seek(2,0) # 从开头开始,右移2个字符
f.read()
f.seek(2,0)  #  直接回到文件末尾 
f.seek(2,1) # offset必须为0
f.seek(2,2) # offset必须为0   
f.close()
# 中文
f = open('test4','w+')
f.write('好好学习')
f.tell()
f.close()
f = open('test4','r+')
f.read(2)
f.seek(1)
f.tell()
f.read() #
f.seek(2) # f.seek(3)
f.close()

```

**二进制模式下:**

与文本模式不同的是,二进制模式下可以任意跳转指针

whence 0 缺省值，表示从头开始，offest只能正整数
whence 1 表示从当前位置，offest可正可负
whence 2 表示从EOF开始，offest可正可负

f.seek(-2,2)–>>相对于末尾往回跳2 个字节

移动文件指针位置offest 只能是正整数

seek在跳时是已字节模式读取,若碰到汉字,但定义的指针位置处于汉子字节的中间,这样读取出来时就会报错,因此,尽量不要使用字节跳转.

无论二进制还是文本模式,在向左跳转指针时,向右可以随便跳转,但是左端不能超出界限.

```python
# 二进制模式
f = open('test4','rb+')
f.tell() # 起始
f.read()
f.tell() # EOF
f.write(b'abc')
f.seek(0) # 起始
f.seek(2,1) # 从当前指针开始，向后2
f.read()
f.seek(-2,1) # 从当前指针开始，向前2
f.seek(2,2) # 从EOF开始，向后2
f.seek(0)
f.seek(-2,2) # 从EOF开始，向前2
f.read()
f.seek(-20,2) # OSError
f.close()

```

### 1.2 buffering：缓冲区

-1 表示使用缺省大小的buffer。如果是二进制模式，使用`io.DEFAULT_BUFFER_SIZE`值默认是4096或者8192。

```python
import io 
print(io.DEFAULT_BUFFER_SIZE)  
>>>8192

```

如果是文本模式，如果是终端设备，是行缓存方式，如果不是，则使用二进制模式的策略。

- 0 ，只在二进制模式使用，表示关buffer

- 1 ，**只在文本模式使用**，表示使用行缓冲。**意思就是见到换行符就flush** # 按一个行进行缓冲,如果一行的缓冲内存被占满时,就会写入到磁盘,或者有换行符就会进行缓冲.

  用途:用户输入换行符后,将这一批数据存入磁盘.

- 大于1， 用于指定buffer的大小,# 对于文本模式,是无效的,仅针对二进制

```python
f= open('test02','rb+',buffering=0)
# 关闭缓冲区,有一个数据立即写入,不建议使用
f= open('test02','rb+',buffering=1)
# 是行缓冲,在缓存未被沾满时不写入,直到检测到换行符
# 如果这一批写入的数据中存在换行符,那么这一批数据都写进磁盘
f.flush#手动写入磁盘

```

| buffering     | 说明                                                         |
| ------------- | ------------------------------------------------------------ |
| buffering= -1 | t和b都是io.DEFAULT_BUFFER_SIZE                               |
| buffering=0   | 二进制模式 关闭缓冲区 文本模式不支持                         |
| buffering=1   | 文本模式行缓冲，遇到换行符才flush                            |
| buffering>1   | 二进制模式表示缓冲大小。缓冲区的值可以超过 io.DEFAULT_BUFFER_SIZE，直到设定的值超出后才把缓冲区flush 文本模式，是io.DEFAULT_BUFFER_SIZE字节，flush完后把当前字符串也写入磁盘 |

总结:

1. 文本模式，一般都用默认缓冲区大小
2. 二进制模式，是一个个字节的操作，可以指定buffer的大小
3. 一般来说，默认缓冲区大小是个比较好的选择，除非明确知道，否则不调整它
4. 一般编程中，明确知道需要写磁盘了，都会手动调用一次flush，而不是等到自动flush或者close的时候.

### 1.3 encoding：编码，仅文本模式使用

windows 下缺省GBK, code page 936 ,Linux编码采用utf-8

### 1.4 newline

文本模式中，换行的转换。可以为None、’’ 空串、’\r’、’\n’、’\r\n’
读时，None表示’\r’、’\n’、’\r\n’都被转换为’\n’；’‘表示不会自动转换通用换行符；其它合法字符表示换行符就是指
定字符，就会按照指定字符分行
写时，None表示’\n’都会被替换为系统缺省行分隔符os.linesep；’\n’或’‘表示’\n’不替换；其它合法字符表示’\n’会

```PYTHON
chars = (None,'','\n','\r')
for newline in chars:
    f = open ('test',newline = newline)   # 直接受换行符进行分割
#     print(f.read().encode())
    print(f.readlines())  #  按照行读取模式读出
    f.close() 
>>>
['a\n', 'b\n', 'c\n', 'd']
['a\n', 'b\r', 'c\n', 'd']
['a\n', 'b\rc\n', 'd']
['a\nb\r', 'c\nd']

```

**1.5 closefd**
关闭文件描述符，True表示关闭它。False会在文件关闭后保持这个描述符。fileobj.fileno()查看

```python
f= open('test','w+',closefd=True)  # 默认是True 每打开一个文件就会有一个文件描述符,若closed = False 系统不会释放该文件描述符,多次打开,知道系统资源被耗尽

```

**1.6 read**

行读取
readline(size=-1)
一行行读取文件内容。size设置一次能读取行内几个字符或字节。
readlines(hint=-1)
读取所有行的列表。指定hint则返回指定的行数。

```python
for line in f:
    print(line)  # 安行读取也可以用循环打印,这样就不会向readlines 生成一个列表
  
def a():
    for line in open('test'):
        yield line
# 或者:
def a():
    yield from  open('test')
#以上两种都可以生成一个惰性求值
for i in a():
    print(i)
 # 然后在用可迭代对象打印.  

```

**1.7 write**
write(s)，把字符串s写入到文件中并返回字符的个数
writelines(lines)，将字符串列表写入文件。 # 换行的话需要自己写入’\n"

**其他**

| 名称       | 说明         |
| ---------- | ------------ |
| seekable() | 是否可seek   |
| readable() | 是否可读     |
| writable() | 是否可写     |
| closed     | 是否已经关闭 |

### **2.1 上下文管理**

首先举一个例子:

```python
f= open('test')
print(1/0)
print('---------------')  # 如果发生错误,打开的文件还能关闭么?
f.closed# 文件没有关闭 
>>>False 

```

当打开一个文件操作后,中间发生异常,会直接报错,此时,文件就一直不会被关闭

既然有这样的情况,又该如何解决这个问题呢?

**方法一# 使用异常处理,关闭打开的文件**

```python
try:
    f.read()
    print(1/0)
finally:
    f.close()#不管上面是否出现异常,此行代买必会执行

```

**方法二:上下文管理**

with 语句块 ,不开辟作用域

```python
f= open('test')
with f:  # 必须是个可迭代对象支持上下文.
    print(f.read(),f.closed)
print('~~~~~~~')
print(f.closed)
>>> False
~~~~~~~
True  # 离开with语句块时,一定会关闭进入的对象  
with open('test','w+')as f:   #正成使用这种方法行上下文管理.
```

对于类似于文件对象的IO对象，一般来说都需要在不使用的时候关闭、注销，以释放资源。
IO被打开的时候，会获得一个文件描述符。计算机资源是有限的，所以操作系统都会做限制。就是为了保护计算机
的资源不要被完全耗尽，计算资源是共享的，不是独占的。
一般情况下，除非特别明确的知道资源情况，否则不要提高资源的限制值来解决问题。

## StringIO和BytesIO

## StringIO

io模块中的类
from io import StringIO
内存中，开辟的一个文本模式的buffer，可以像文件对象一样操作它
当close方法被调用的时候，这个buffer会被释放

```python
import io 
sio = io.StringIO()
sio.readable(),sio.seekable(),sio.writable()  
True, True, True  
sio.write('abc')  # 可以写,字符串对象
sio.read()# 可读,但此时指针在EOF位置,读取不到信息
sio.seek(0)#调整指针位置
sio.read()  # 重新读取便可以读取 
sio.read() # 指针又回到EOF,读取为空
sio.getvalue() # sio有getvalue操作,可以得到内容,不受指针影响 
sio.close()
```

类文件对象,这是一个基于内存的,提供的所谓的一个文件对象,操作该类文件对象如同操作文件对象一样,但是该类文件对象不落地,不写入磁盘.

因此,在使用时,若只是临时使用,在内存中仅操作,便可以使用该类文件对象,若想写入磁盘,可自行写入

### BytesIO

```python
import io 
sio = io.BytesIO()
sio = io.BytesIO(b'a+')  # 追加写时也需要加上'b'
sio.readable(),sio.seekable(),sio.writable()  
True, True, True 
sio.write(b'abc')  #  BytesIO写入时只能写入bytes类型,其他操作方法与StringIO一样.
```

既然是一个类文件对象,同样支持上下文管理:

```PythoN
import io
with io.StringIO()as if :
    pass
if.closed()
>>> True 
#使用完即关闭,不在需要手动关闭
```