import os
import time

import asyncio
import aiohttp
import requests
import tqdm
# from concurrent.futures import ThreadPoolExecutor
from bs4 import BeautifulSoup


async def getNextPage(session, url, res):
    item = []
    async with session.get(url, headers=headers) as resp:
        # global item
        html = await resp.text()
        item = await parseNextPage(html)
        # print(item)
    for i in item:
        # print(i["url"])
        base_url = "/".join(i["url"].split("/")[:-1]) + "/" + \
            i["url"].split("/")[-1].split(".")[0] + '_%s' + ".html"
        for ii in range(1, 100):
            try:
                async with session.get(base_url % ii, headers=headers) as resp:
                    # print(base_url % ii)
                    if resp.status == 200:
                        html = await resp.text()
                        img_url = await parseDetailPage(html)
                        name = i["name"]
                        char_list = ['*', '|', ':', '?',
                                     '/', '<', '>', '"', '\\']
                        for iii in char_list:
                            if iii in name:
                                name = name.replace(iii, "_")
                        await getImg(session, name, img_url)
                    else:
                        break
            except:
                print(item, "-----", url, "-----", i["name"])
    return res


def itempipeline(f, content):

    # with open(name, "wb") as f:
    f.write(content)


async def getImg(session, name, img_url):
    # url = "https://imgpc.iimzt.com/2020/11/25a01.jpg"
    # code = img_url.split("/")[-1].split(".")[0][:3]
    # prefix = img_url.split("/")[-1].split(".")[-1]
    # img_base_url = img_url.split("/")[:-2]
    # img_base_url = "/".join(img_base_url) + "/" + code + '%s' + '.' + prefix

    full_path = os.path.join(base_path, name.strip())

    if not os.path.exists(full_path):
        os.makedirs(full_path)

    img_name = img_url.split("/")[-1][:21]
    all_name = os.path.join(full_path, img_name)

    if os.path.exists(all_name):
        return
    try:
        async with session.get(img_url, headers=headers) as resp:
            content = await resp.read()
            with open(all_name, "wb") as f:
                await lp.run_in_executor(None, itempipeline, f, content)
            print(all_name, "----图片保存完成----")
    except:
        print(all_name, "----图片保存出错----")
        return


async def parseDetailPage(html):
    # with open("aaa.html", "w", encoding="utf8") as f:
    #     f.write(html)
    root = BeautifulSoup(html, 'lxml')
    # img_url = root.select(
    #     ".main-wrapper .showcontw")[0].find("a", title="点击翻页").img.get("src")
    img_url = root.select(
        ".main-wrapper .showcontw")[0].find("a", title="点击翻页").img.get("src")
    return img_url


async def parseNextPage(html):
    # with open("aaa.html","w",encoding="utf8") as f:
    #     f.write(html)
    root = BeautifulSoup(html, 'lxml')
    a_list = root.select(
        ".main-wrapper .all-work-list .work-list-box .card-img>a")

    # print(a_list)
    return [{"name": i.get("title"), "url": i.get("href")} for i in a_list]
    # return [{"name": "", "url": ""}]


async def begin_download(sem, session: aiohttp.ClientSession, url: str, i):
    # 控制协程并发数量
    async with sem:
        return await getNextPage(session, url, i)


async def download(sem):

    tasks = []
    async with aiohttp.ClientSession() as session:
        for i in range(1, 46):
            # 创建url
            url = f"https://www.souutu.com/dmkt/index_{i}.html"
            if i == 1:
                url = f"https://www.souutu.com/dmkt/index.html"
            # 构造一个协程列表
            tasks.append(asyncio.ensure_future(
                begin_download(sem, session, url, i)))
        # 等待返回结果
        tasks_iter = asyncio.as_completed(tasks)
        # # 创建一个进度条
        # fk_task_iter = tqdm.tqdm(tasks_iter, total=len(tasks))

        for coroutine in tasks_iter:
            # 获取结果
            res = await coroutine
            print(res, '页面下载完成')


if __name__ == "__main__":
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36",
        "Referer": "https://www.souutu.com/"
    }

    base_path = "F:\动漫图片"
    base_img_url = "https://imgpc.iimzt.com/"

    # 获取事件循环
    lp = asyncio.get_event_loop()
    start = time.time()
    # 创建一个信号量以防止DDos
    sem = asyncio.Semaphore(300)
    lp.run_until_complete(download(sem))
    end = time.time()
    lp.close()
    print('耗时:', end-start)
