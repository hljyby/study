import os
import time

import asyncio
import aiohttp
import requests
import tqdm
# from concurrent.futures import ThreadPoolExecutor
from bs4 import BeautifulSoup


async def getNextPage(session, url, i):
    item = []
    async with session.get(url, headers=headers) as resp:
        # global item
        html = await resp.text()
        item = await parseNextPage(html)

    for i in item:
        async with session.get(i["url"], headers=headers) as resp:
            html = await resp.text()
            img_url = await parseDetailPage(html)
            name = i["name"]
        await getImg(session, name, img_url)
    return i


async def getImg(session, name, img_url):
    # url = "https://imgpc.iimzt.com/2020/11/25a01.jpg"
    code = img_url.split("/")[-1].split(".")[0][:3]
    prefix = img_url.split("/")[-1].split(".")[-1]
    img_base_url = img_url.split("/")[:-2]
    img_base_url = "/".join(img_base_url) + "/" + code + '%s' + '.' + prefix

    full_path = os.path.join(base_path, name)

    if not os.path.exists(full_path):
        os.makedirs(full_path)
    
    for i in range(1, 200):
        ii = str(i).zfill(2)
        url = img_base_url % ii
        img_name = url.split("/")[-1]

        all_name = os.path.join(full_path, img_name)

        if os.path.exists(all_name):
            continue
        async with session.get(url, headers=headers) as resp:
            content = await resp.read()
            with open(all_name, "wb") as f:
                await lp.run_in_executor(None, itempipeline, f, content)


async def parseDetailPage(html):
    root = BeautifulSoup(html, 'lxml')
    return root.select(".content .main-image>p>a>img")[0].get("src")
    # return  "name"


async def parseNextPage(html):
    root = BeautifulSoup(html, 'lxml')
    a_list = root.select(".main-content .postlist #pins li>a")
    return [{"name": i.img.get("alt"), "url": i.get("href")} for i in a_list]
    # return [{"name": "", "url": ""}]


def itempipeline(f, content):

    # with open(name, "wb") as f:
    f.write(content)


async def begin_download(sem, session: aiohttp.ClientSession, url: str, i):
    # 控制协程并发数量
    async with sem:
        return await getNextPage(session, url, i)


async def download(sem):

    tasks = []
    async with aiohttp.ClientSession() as session:
        for i in range(1, 3):
            # 创建url
            url = f"https://www.mzitu.com/page/{i}/"
            # 构造一个协程列表
            tasks.append(asyncio.ensure_future(
                begin_download(sem, session, url, i)))
        # 等待返回结果
        tasks_iter = asyncio.as_completed(tasks)
        # # 创建一个进度条
        fk_task_iter = tqdm.tqdm(tasks_iter, total=len(tasks))
        # tasks_detail = []
        for coroutine in fk_task_iter:
            # 获取结果
            res = await coroutine
            # tasks_detail = [tasks_detail + res]
            print(res, '页面下载完成')
        # print(tasks_detail)
        # for i in tasks_detail:


if __name__ == "__main__":
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36",
        "Referer": "https://www.mzitu.com/"
    }

    base_path = "F:\妹子图"
    base_img_url = "https://imgpc.iimzt.com/"

    # 获取事件循环
    lp = asyncio.get_event_loop()
    start = time.time()
    # 创建一个信号量以防止DDos
    sem = asyncio.Semaphore(500)
    lp.run_until_complete(download(sem))
    end = time.time()
    lp.close()
    print('耗时:', end-start)
