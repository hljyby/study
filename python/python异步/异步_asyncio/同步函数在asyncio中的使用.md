# 在python中如何以异步的方式调用第三方库提供的同步API



在[关于asyncio的基本用法](https://zhuanlan.zhihu.com/p/47104217)中提到，asyncio并不是多线程。在协程中调用同步（阻塞函数），都占用同一线程的CPU时间，即当前线程会被阻塞（即协程只会在等待一个协程时可能出让CPU，如果是普通函数，它是不会出让CPU的，会一直执行直到完成，或者被其它线程中断）。

如果我们依赖的某个第三方库并不是异步的，那么对其API的调用也会阻塞住。如果这个第三方库是网络IO请求密集型的，那么是可以通过多线程甚至多进程封装，从而将其改造成异步库的。

本文提供了通过concurrent.futures库来实现多线程异步封装的思路和实现。

------

concurrent.futures

这个包提供了线程池和进程池的实现。从Python 3.5以后，asyncio提供了loop.run_in_executor的实现，将asyncio的协程与concurrent.futures的future连接起来的方法。这样我们自己就不用去实现线程池，信号机制、返回值的传递机制了。

我们这里不仔细分析两者的连接及内部机制，只通过一个例子来展示如何使用：

```python
from concurrent.futures import ThreadPoolExecutor
import time
import asyncio

def work():
    time.sleep(5)
    return 'done'

async def main(loop):
  executor = ThreadPoolExecutor()
  result = await loop.run_in_executor(executor, work)
  print(result)

loop = asyncio.get_event_loop()
loop.run_until_complete(main(loop))
loop.close()
```

上面的代码已经很清楚了。代码定义了一个线程池executor，通过loop.run_in_executor，将同步调用work转化成异步调用，并且work的返回值也一并传递出来。

整个代码段都是异步函数风格的。如果你多调用几次await loop.run_in_executor(executor, work)，就会发现代码的执行也确实是异步行为。

## 通过代理机制封装

明白了通过concurrent.futures来实现同步转异步的原理，理论上我们就可以依照上面的方式，将任何一个同步调用（比如上面的work），转化成异步调用了。

但如果第三方库提供了非常多的API，我们就得考虑更优美的实现方式，以减少重复代码量。这里我们使用代理机制。

首先我们来看一个特别的函数， **getattr**(self, name)。如果我们有一个类对象foo，通过foo来引用其属性bar时，如果bar不存在，python就会调用**getattr**来继续查找这个bar，如果**getattr**没有被我们改写，则结果仍然会是找不到，此时就会抛出熟悉的AttributeError:

```python
AttributeError: 'Foo' object has no attribute 'bar'
```

我们可以利用这个特性来实现Python的对象代理。假设被代理的库名为somelib，其中提供了一个同步的网络函数send，则我们可以通过代理技术来实现一个mylib，当调用mylib.send时，最终仍然通过somelib.send来完成功能，但它是异步的。

```python
import asyncio
from concurrent.futures import ThreadPoolExecutor


class AsyncWrapper:
    def __init__(self, subject, loop=None, max_workers=None):
        self.subject = subject
        self.loop = loop or asyncio.get_event_loop()
        self.executor = ThreadPoolExecutor(max_workers=max_workers)

    def __getattr__(self, name):
        origin = getattr(self.subject, name)
        if callable(origin):
            def foo(*args, **kwargs):
                return self.run(origin, *args, **kwargs)

            # cache the function we built right now, to avoid later lookup
            self.__dict__[name] = foo
            return foo
        else:
            return origin

    async def run(self, origin_func, *args, **kwargs):
        def wrapper():
            return origin_func(*args, **kwargs)

        return await self.loop.run_in_executor(self.executor, wrapper)
```

这里我实现了一个非常简单的异步封装器AsynWrapper。构造函数接受三个参数，第一个为要代理的对象主体，在我们的例子中即为somelib。第二个是event loop对象，如果不提供，则会自动生成。第三个是初始化线程池所需要的。

这里要注意event loop对象尽管是可选的，但如果你的程序是多线程的，则必须在主线程中获取event loop对象并将其传递过来。因为每个线程都有自己的event loop，它们之间无法同步。

改写的**getattr**是我们实现魔法的地方。假设我们通过AsyncWrapper生成了一个对象foo，则在foo上调用send函数时：

```python
await foo.send(...)
```

当foo.send()被调用时，究竟发生了什么？可以认为这里发生了两件事，第一件事是要找到foo.send这个函数对象，其次是要对它进行调用。看起来比较啰嗦，但却是理解我们封装的关键。

我们先看查找。

由于foo本身是没有send这个属性的，因此**getattr**被调用，并且传入了name = 'send'。我们先检查这个send是否是原来lib中的一个函数，因为我们没有必要也不应该拦截属性：

```python
origin = getattr(self.subject, name)

if callable(origin):
     #替换
else:
    return origin
```

因此如果send是somelib中的一个属性（比如常量），我们直接返回其值。但如果它是一个可执行对象，那么我们将其封装成一个异步函数。

如果send是一个函数呢？我们当然不能直接返回它，而应该返回另一个函数，在这个函数里，它将在executor中执行origin，从而实现异步化。这个函数就是self.run：

```python
async def run(self, origin_func, *args, **kwargs):
    def wrapper():
        return origin_func(*args, **kwargs)

    return await self.loop.run_in_executor(self.executor, wrapper)
```

这里的内联函数wrapper只是为了将参数封装，因为run_in_executor只接受位置参数(*args)，而不接受可选参考(**kwargs)。

现在问题来了，如何在**getattr**中返回run对象，并且这个run对象知道应该执行哪一个origin函数呢？这就是内联函数foo的作用。它将origin原本应该有的参数，以及origin本身一起打包：

```python
def foo(*args, **kwargs):
    return self.run(origin, *args, **kwargs)
```

最后要提到的就是这一行：

```python
self.__dict__[name] = foo
```

这是一种优化。如此以来，下一次我们再调用foo.send时，**getattr**就不会再调用了，因为send已经成为foo的一个方法。

## Demo

```python
import somelib
async main():
    foo = AsyncWrapper(somelib)
    await foo.send("hello world!")
```

## 其它

除了**getattr**外，python还提供了**getattribute**函数。两者的区别是，后者无论如何（即在foo中有send属性时）都会被调用。考虑到我们的目的，这里当然使用**getattr**。