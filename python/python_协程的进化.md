### Python中的协程大概经历了如下三个阶段：

\1. 最初的生成器变形yield/send
\2. 引入@asyncio.coroutine和yield from
\3. 在最近的Python3.5版本中引入async/await关键字

### 一、生成器变形yield/send

普通函数中如果出现了yield关键字，那么该函数就不再是普通函数，而是一个生成器。
 

```python

def mygen(alist):
    while len(alist) > 0:
        c = randint(0, len(alist)-1)
        yield alist.pop(c)
a = ["aa","bb","cc"]
c=mygen(a)
print(c)
 
输出：<generator object mygen at 0x02E5BF00>
```

像上面代码中的c就是一个生成器。生成器就是一种迭代器，可以使用for进行迭代。生成器函数最大的特点是可以接受外部传入的一个变量，并根据变量内容计算结果后返回。
这一切都是靠生成器内部的send()函数实现的。

```python
def gen():
    value=0
    while True:
        receive=yield value
        if receive=='e':
            break
        value = 'got: %s' % receive
 
g=gen()
print(g.send(None))     # 启动生成器，返回value的值，并暂停
print(g.send('hello'))  # 返回got: hello 并暂停
print(g.send(123456))
print(g.send('e'))
```

上面生成器函数中最关键也是最易理解错的，就是receive=yield value这句,如果对循环体的执行步骤理解错误，就会失之毫厘，差之千里。
其实receive=yield value包含了3个步骤：
1、向函数外抛出（返回）value
2、暂停(pause)，等待next()或send()恢复
3、赋值receive=MockGetValue() 。 这个MockGetValue()是假想函数，用来接收send()发送进来的值

执行流程：
1、通过g.send(None)或者next(g)启动生成器函数，并执行到第一个yield语句结束的位置。这里是关键，很多人就是在这里搞糊涂的。运行receive=yield value语句时，我们按照开始说的拆开来看，实际程序只执行了1，2两步，程序返回了value值，并暂停(pause)，并没有执行第3步给receive赋值。因此yield value会输出初始值0。这里要特别注意：在启动生成器函数时只能send(None),如果试图输入其它的值都会得到错误提示信息。

2、通过g.send('hello')，会传入hello，从上次暂停的位置继续执行，那么就是运行第3步，赋值给receive。然后计算出value的值，并回到while头部，遇到yield value，程序再次执行了1，2两步，程序返回了value值，并暂停(pause)。此时yield value会输出”got: hello”，并等待send()激活。

3、通过g.send(123456)，会重复第2步，最后输出结果为”got: 123456″。

4、当我们g.send(‘e’)时，程序会执行break然后推出循环，最后整个函数执行完毕，所以会得到StopIteration异常。

从上面可以看出， 在第一次send(None)启动生成器（执行1–>2，通常第一次返回的值没有什么用）之后，对于外部的每一次send()，生成器的实际在循环中的运行顺序是3–>1–>2，也就是先获取值，然后dosomething，然后返回一个值，再暂停等待。

### 二、yield from

看一段代码：

```python
def g1():     
     yield  range(5)
def g2():
     yield  from range(5)
 
it1 = g1()
it2 = g2()
for x in it1:
    print(x)
 
for x in it2:
    print(x)
```

输出：
range(0, 5)
0
1
2
3
4

这说明yield就是将range这个可迭代对象直接返回了。
而yield from解析了range对象，将其中每一个item返回了。
yield from iterable本质上等于for item in iterable: yield item的缩写版
来看一下例子，假设我们已经编写好一个斐波那契数列函数
 

```python
def fab(max):
     n,a,b = 0,0,1
     while n < max:
          yield b
          # print b
          a, b = b, a + b
          n = n + 1
f=fab(5)
```

fab不是一个普通函数，而是一个生成器。因此fab(5)并没有执行函数，而是返回一个生成器对象(生成器一定是迭代器iterator，迭代器一定是可迭代对象iterable)
现在我们来看一下，假设要在fab()的基础上实现一个函数，调用起始都要记录日志

```python
def f_wrapper(fun_iterable):
    print('start')
    for item  in fun_iterable:
        yield item
     print('end')
wrap = f_wrapper(fab(5))
for i in wrap:
    print(i,end=' ')
```

现在使用yield from代替for循环

```python
import logging
def f_wrapper2(fun_iterable):
    print('start')
    yield from fun_iterable  #注意此处必须是一个可生成对象
    print('end')
wrap = f_wrapper2(fab(5))
for i in wrap:
    print(i,end=' ')
```

再强调一遍：yield from后面必须跟iterable对象(可以是生成器，迭代器)

### 三、asyncio.coroutine和yield from

yield from在asyncio模块中得以发扬光大。之前都是我们手工切换协程，现在当声明函数为协程后，我们通过事件循环来调度协程。

先看示例代码：
 

```python
import asyncio,random
@asyncio.coroutine
def smart_fib(n):
    index = 0
    a = 0
    b = 1
    while index < n:
        sleep_secs = random.uniform(0, 0.2)
        yield from asyncio.sleep(sleep_secs) #通常yield from后都是接的耗时操作
        print('Smart one think {} secs to get {}'.format(sleep_secs, b))
        a, b = b, a + b
        index += 1
@asyncio.coroutine
def stupid_fib(n):
    index = 0
    a = 0
    b = 1
    while index < n:
        sleep_secs = random.uniform(0, 0.4)
        yield from asyncio.sleep(sleep_secs) #通常yield from后都是接的耗时操作
        print('Stupid one think {} secs to get {}'.format(sleep_secs, b))
        a, b = b, a + b
        index += 1
if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    tasks = [
        smart_fib(10),
        stupid_fib(10),
    ]
    loop.run_until_complete(asyncio.wait(tasks))
    print('All fib finished.')
    loop.close()
 
 
输出：
 
Smart one think 0.12342379986171913 secs to get 1
Smart one think 0.08258702029211769 secs to get 1
Stupid one think 0.2837443076840253 secs to get 1
Smart one think 0.10973309903065592 secs to get 2
Smart one think 0.11514146666964056 secs to get 3
Smart one think 0.12036801890549893 secs to get 5
Stupid one think 0.3456028326663949 secs to get 1
Smart one think 0.1135888075073404 secs to get 8
Smart one think 0.11467704003701512 secs to get 13
Stupid one think 0.32749036813321014 secs to get 2
Stupid one think 0.01895472179590443 secs to get 3
Smart one think 0.19058406683902024 secs to get 21
Stupid one think 0.0384250702808524 secs to get 5
Smart one think 0.11090975352016748 secs to get 34
Smart one think 0.12915936726213914 secs to get 55
Stupid one think 0.36674070201230735 secs to get 8
Stupid one think 0.272315540646428 secs to get 13
Stupid one think 0.37616966078358993 secs to get 21
Stupid one think 0.24273673910432106 secs to get 34
Stupid one think 0.39477427098873813 secs to get 55
All fib finished.
```

yield from语法可以让我们方便地调用另一个generator。
本例中yield from后面接的asyncio.sleep()是一个coroutine(里面也用了yield from)，所以线程不会等待asyncio.sleep()，而是直接中断并执行下一个消息循环。当asyncio.sleep()返回时，线程就可以从yield from拿到返回值（此处是None），然后接着执行下一行语句。
asyncio是一个基于事件循环的实现异步I/O的模块。通过yield from，我们可以将协程asyncio.sleep的控制权交给事件循环，然后挂起当前协程；之后，由事件循环决定何时唤醒asyncio.sleep,接着向后执行代码。
协程之间的调度都是由事件循环决定。
yield from asyncio.sleep(sleep_secs) 这里不能用time.sleep(1)因为time.sleep()返回的是None，它不是iterable，还记得前面说的yield from后面必须跟iterable对象(可以是生成器，迭代器)。
所以会报错：

```python
yield from time.sleep(sleep_secs)
TypeError: ‘NoneType’ object is not iterable
```

### 四、async和await

弄清楚了asyncio.coroutine和yield from之后，在Python3.5中引入的async和await就不难理解了：可以将他们理解成asyncio.coroutine/yield from的完美替身。当然，从Python设计的角度来说，async/await让协程表面上独立于生成器而存在，将细节都隐藏于asyncio模块之下，语法更清晰明了。
加入新的关键字 async ，可以将任何一个普通函数变成协程
 

```python
import time,asyncio,random
async def mygen(alist):
    while len(alist) > 0:
        c = randint(0, len(alist)-1)
        print(alist.pop(c))
a = ["aa","bb","cc"]
c=mygen(a)
print(c)
输出：
<coroutine object mygen at 0x02C6BED0>
```

在上面程序中，我们在前面加上async，该函数就变成一个协程了。

但是async对生成器是无效的。async无法将一个生成器转换成协程。
还是刚才那段代码，我们把print改成yield

```python
async def mygen(alist):
    while len(alist) > 0:
        c = randint(0, len(alist)-1)
        yield alist.pop(c)
a = ["ss","dd","gg"]
c=mygen(a)
print(c)
```

可以看到输出

```
<async_generator object mygen at 0x02AA7170>
```

并不是coroutine 协程对象

所以我们的协程代码应该是这样的

```python
import time,asyncio,random
async def mygen(alist):
    while len(alist) > 0:
        c = random.randint(0, len(alist)-1)
        print(alist.pop(c))
        await asyncio.sleep(1) 
strlist = ["ss","dd","gg"]
intlist=[1,2,5,6]
c1=mygen(strlist)
c2=mygen(intlist)
print(c1)
```

要运行协程，要用事件循环
在上面的代码下面加上：

```python

if __name__ == '__main__':
        loop = asyncio.get_event_loop()
        tasks = [
        c1,
        c2
        ]
        loop.run_until_complete(asyncio.wait(tasks))
        print('All fib finished.')
        loop.close()
```

就可以看到交替执行的效果。

以下是整理的使用 asyncio 封装的执行协程的函数，在使用的时候，将需要执行的协程添加进入coros ，作为列表 coros 中的元素，然后传入函数 start(*coros)，再调用 start(*coros) 即可批量执行协程

```python
import asyncio
 
def start(*coros):
    # 执行协程，如coro为多个，则全部并发执行。
    try:
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        if len(coros) == 1:
            loop.run_until_complete(coros[0])
        else:
            loop.run_until_complete(asyncio.wait(coros))
    finally:
        loop.close()
```