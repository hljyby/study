# python open 函数

- 总结

## buffering 参数

- open 函数的buffering 参数是建立一个缓冲区，缓冲区就是缓冲内存与硬盘之间存储的一个东西
- 内存想要取得硬盘里的文件信息，会经常读写硬盘，有了缓冲区，可以减少硬盘读写次数。内存也不许要等待硬盘的io因为内存和硬盘之间读写速度不一样
- open 函数的缓冲区不同型号的电脑不一样，可以使用方法测出内存的缓冲区大小

```python
import time
import os
from string import ascii_letters
from random import choice

# f_content = []
# with open('abc.txt', 'w', buffering=-1) as f:
#     for i in range(10000):
#         if os.path.getsize('abc.txt') > 0:
#             break
#         else:
#             word = choice(ascii_letters)
#             f.write(word)
#             f_content.append(word)
#     print('系统缓冲区默认大小为，{}'.format(len(f_content)+1))

f = open('abc.txt', 'w', buffering=100)
f_content = []
for i in range(10000):
    if os.path.getsize('abc.txt') > 0:
        break
    else:
        word = choice(ascii_letters)
        f.write(word)
        f_content.append(word)
print(len(f_content)+1)

```

- 当buffer取0时，代表不适用缓冲区，内存想要取得文件内容只能直接读取硬盘。
- 当buffer取1时，代表行缓冲区，只要碰到/n 换行符就会把缓冲区的内容存到硬盘中去，如果超出了缓冲区的大小，会自动存到硬盘中去
- 当buffer为大于一的int 类型时，代表设置缓冲区，为buffer大小，（不过我设置后发现不好使，不知道为什么），查过韩冲去内容会存储到硬盘中去
- 当buffer 为-1 时，代表缓冲区大小为默认大小，超出缓冲区的内容会存到硬盘中
- open函数的flush 方法可以刷新缓冲区，没刷新一次，缓冲区的内容都会存到硬盘中去

## 流

- 流文件是啥我也不太清楚
- 看一个人的文章说是有字符流和字节流什么的
- 我对字节流就是经过utf8编码后的二进制流
- 而对字符流的理解就是unicode 编码的二进制流

## 首先，流是什么？

流是个抽象的概念，是对输入输出设备的抽象，Java程序中，对于数据的输入/输出操作都是以“流”的方式进行。设备可以是文件，网络，内存等。

![img](http://pic002.cnblogs.com/images/2012/79891/2012121818014532.png)

流具有方向性，至于是输入流还是输出流则是一个相对的概念，一般以程序为参考，如果数据的流向是程序至设备，我们成为输出流，反之我们称为输入流。

可以将流想象成一个“水流管道”，水流就在这管道中形成了，自然就出现了方向的概念。

![img](http://pic002.cnblogs.com/images/2012/79891/2012121719220226.jpg)

当程序需要从某个数据源读入数据的时候，就会开启一个输入流，数据源可以是文件、内存或网络等等。相反地，需要写出数据到某个数据源目的地的时候，也会开启一个输出流，这个数据源目的地也可以是文件、内存或网络等等。

## 流有哪些分类？

可以从不同的角度对流进行分类：

\1. 处理的数据单位不同，可分为：字符流，字节流

2.数据流方向不同，可分为：输入流，输出流

3.功能不同，可分为：节点流，处理流

\1. 和 2. 都比较好理解，对于根据功能分类的，可以这么理解：

**节点流**：节点流从一个特定的数据源读写数据。即节点流是直接操作文件，网络等的流，例如FileInputStream和FileOutputStream，他们直接从文件中读取或往文件中写入字节流。

![img](http://pic002.cnblogs.com/images/2012/79891/2012121818051872.png)

**处理流**：“连接”在已存在的流（节点流或处理流）之上通过对数据的处理为程序提供更为强大的读写功能。过滤流是使用一个已经存在的输入流或输出流连接创建的，过滤流就是对节点流进行一系列的包装。例如BufferedInputStream和BufferedOutputStream，使用已经存在的节点流来构造，提供带缓冲的读写，提高了读写的效率，以及DataInputStream和DataOutputStream，使用已经存在的节点流来构造，提供了读写Java中的基本数据类型的功能。他们都属于过滤流。

举个简单的例子：

![复制代码](http://common.cnblogs.com/images/copycode.gif)

```
public static void main(String[] args) throws IOException {
        // 节点流FileOutputStream直接以A.txt作为数据源操作
        FileOutputStream fileOutputStream = new FileOutputStream("A.txt");
        // 过滤流BufferedOutputStream进一步装饰节点流，提供缓冲写
        BufferedOutputStream bufferedOutputStream = new BufferedOutputStream(
                fileOutputStream);
        // 过滤流DataOutputStream进一步装饰过滤流，使其提供基本数据类型的写
        DataOutputStream out = new DataOutputStream(bufferedOutputStream);
        out.writeInt(3);
        out.writeBoolean(true);
        out.flush();
        out.close();
        // 此处输入节点流，过滤流正好跟上边输出对应，读者可举一反三
        DataInputStream in = new DataInputStream(new BufferedInputStream(
                new FileInputStream("A.txt")));
        System.out.println(in.readInt());
        System.out.println(in.readBoolean());
        in.close();
}
```

![复制代码](http://common.cnblogs.com/images/copycode.gif)

## **流结构介绍**：

Java所有的流类位于java.io包中，都分别继承字以下四种抽象流类型。

|        | 字节流       | 字符流 |
| ------ | ------------ | ------ |
| 输入流 | InputStream  | Reader |
| 输出流 | OutputStream | Writer |

1.继承自InputStream/OutputStream的流都是用于向程序中输入/输出数据，且数据的单位都是字节(byte=8bit)，如图，深色的为节点流，浅色的为处理流。

![img](http://pic002.cnblogs.com/images/2012/79891/2012121818562293.png) ![img](http://pic002.cnblogs.com/images/2012/79891/2012121819001442.png)

2.继承自Reader/Writer的流都是用于向程序中输入/输出数据，且数据的单位都是字符(2byte=16bit)，如图，深色的为节点流，浅色的为处理流。

![img](http://pic002.cnblogs.com/images/2012/79891/2012121819033620.png)![img](http://pic002.cnblogs.com/images/2012/79891/2012121819042121.png)

## 常见流类介绍：

**节点流类型常见的有：**

对文件操作的字符流有FileReader/FileWriter，字节流有FileInputStream/FileOutputStream。

**处理流类型常见的有：**

缓冲流：缓冲流要“套接”在相应的节点流之上，对读写的数据提供了缓冲的功能，提高了读写效率，同事增加了一些新的方法。

　　字节缓冲流有BufferedInputStream/BufferedOutputStream，字符缓冲流有BufferedReader/BufferedWriter，字符缓冲流分别提供了读取和写入一行的方法ReadLine和NewLine方法。

　　对于输出地缓冲流，写出的数据，会先写入到内存中，再使用flush方法将内存中的数据刷到硬盘。所以，在使用字符缓冲流的时候，一定要先flush，然后再close，避免数据丢失。

转换流：用于字节数据到字符数据之间的转换。

　　仅有字符流InputStreamReader/OutputStreamWriter。其中，InputStreamReader需要与InputStream“套接”，OutputStreamWriter需要与OutputStream“套接”。

数据流：提供了读写Java中的基本数据类型的功能。

　　DataInputStream和DataOutputStream分别继承自InputStream和OutputStream，需要“套接”在InputStream和OutputStream类型的节点流之上。

对象流：用于直接将对象写入写出。

　　流类有ObjectInputStream和ObjectOutputStream，本身这两个方法没什么，但是其要写出的对象有要求，该对象必须实现Serializable接口，来声明其是可以序列化的。否则，不能用对象流读写。

　　还有一个关键字比较重要，transient，由于修饰实现了Serializable接口的类内的属性，被该修饰符修饰的属性，在以对象流的方式输出的时候，该字段会被忽略。

# 网络请求

- 对于前端通过XMLHttpResquest 对象发来的请求后daunt的web框架一般经过疯长所以不会是流文件格式
- 所以会很占内存，只能使用分块上传的方式实现大文件上传（我搜了很多没有能一边接收数据一边写入数据的前端上传写法）
- 对于都端和后端语言来说python有个requests.get(url,stream=True) 方法可以实现流文件存储数据，其他的我就不知道了
- 我查了好多东西，没有能解释我想的，不知道是不是在浪费时间。

# node

```javascript
// process.stdin.pipe(process.stdout);
// process.stdin.setEncoding('UTF8')
process.stdin.on('data',(chunk)=>{
    console.log(chunk.toString())
})

buffer可以通过toString()方法转化为utf8编码的形式：
var str = buf.toString();
当然你也可以指定其他的编码形式：
var b64Str = buf.toString("base64");
像下面这样，你可以将utf-8编码的字符串转换为base64编码的字符串：
var utf8String = 'my string';
var buf = new Buffer(utf8String);
var base64String = buf.toString('base64');

运行这块命令 可以获取命令行输入的命令
stdin 是一个可读流
stdout 是一个可写流

buffer类型的string()可以吧buffer类型转化为utf8类型。还可以占华为别的类型
```

