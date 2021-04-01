# 深究Python中的asyncio库-线程同步

前面的代码都是异步的，就如sleep，需要用asyncio.sleep而不是阻塞的time.sleep，如果有同步逻辑，怎么利用asyncio实现并发呢？答案是用run_in_executor。在一开始我说过开发者创建 Future 对象情况很少，主要是用run_in_executor，就是让同步函数在一个执行器( executor)里面运行。

同步代码

```python
def a():

    time.sleep(1)

    return 'A'

async def b():

    await asyncio.sleep(1)

    return 'B'

def show_perf(func):

    print('*' * 20)

    start = time.perf_counter()

    asyncio.run(func())

    print(f'{func.__name__} Cost: {time.perf_counter() - start}')

async def c1():

    loop = asyncio.get_running_loop()

    await asyncio.gather(

        loop.run_in_executor(None, a),

        b()

    )

In : show_perf(c1)

********************

c1 Cost: 1.0027242230000866

```

可以看到用run_into_executor可以把同步函数逻辑转化成一个协程，且实现了并发。这里要注意细节，就是函数a是普通函数，不能写成协程，下面的定义是错误的，不能实现并发：

```python
async def a():

    time.sleep(1)

    return 'A'

```

因为 a 里面没有异步代码，就不要用async def来定义。需要把这种逻辑用loop.run_in_executor封装到协程：

~~~python
```python
async def c():

    loop = asyncio.get_running_loop()

    return await loop.run_in_executor(None, a)
大家理解了吧？

```python
loop.run_in_executor(None, a)这里面第一个参数是要传递concurrent.futures.Executor实例的，传递None会选择默认的executor：

In : loop._default_executor

Out: <concurrent.futures.thread.ThreadPoolExecutor at 0x112b60e80>
~~~

当然我们还可以用进程池，这次换个常用的文件读写例子，并且用:

```python
async def c3():

    loop = asyncio.get_running_loop()

    with concurrent.futures.ProcessPoolExecutor() as e:

        print(await asyncio.gather(

            loop.run_in_executor(e, a),

            b()

        ))

In : show_perf(c3)

********************

['A', 'B']

c3 Cost: 1.0218078890000015
```