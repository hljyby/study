import asyncio
import requests
import aiohttp
import time
import requests


async def fun1(i):
    print()
    await asyncio.sleep(11-i)
    # requests.get("http://www.baidu.com/")


async def main(i):
    tasks = [asyncio.create_task(fun1(i)) for i in range(10)]
    await asyncio.wait(tasks)
    # print("-----kaishi----", i)
    # end_time = time.time()
    # print(end_time-start_time)
    # requests.get("http://www.baidu.com/")
    # if i > 10:
    #     return
    # i += 1
    # await main(i)
    # print("-----kaishi----", i)

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    start_time = time.time()
    loop.run_until_complete(main(0))

    # for i in range(10):
    #     requests.get("http://www.baidu.com/")
    end_time = time.time()
    print(end_time-start_time)
    loop.close()
