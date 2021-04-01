import asyncio
import requests
import aiohttp
import time
async def fun2(i):
    async with aiohttp.ClientSession() as session:
        async with session.get("https://www.baidu.com/") as resp:
            # print("内",i)
            await resp.read()
            # print("外",i)
            return i

async def fun1(i):
    async with aiohttp.ClientSession() as session:
        async with session.get("https://www.baidu.com/") as resp:
            await resp.read()
            tasks = []
            for ii in range(10):
                tasks.append(asyncio.ensure_future(fun2(ii)))
                # print(i,ii,a)
            iter_task = asyncio.as_completed(tasks)
            for task in iter_task:
                print("--------BBBBBB--------")
                await task
async def main():
    task = []
    for i in range(10):
        task.append(asyncio.ensure_future(fun1(i)))

    iter_task = asyncio.as_completed(task)
    for i in iter_task:
        print("hahahahah")
        await i

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    start_time = time.time()
    loop.run_until_complete(main())
    end_time = time.time()
    print(end_time-start_time)
    loop.close()