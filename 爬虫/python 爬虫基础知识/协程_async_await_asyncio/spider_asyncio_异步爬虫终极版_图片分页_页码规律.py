import time
import os
import json

import asyncio
import aiohttp
from bs4 import BeautifulSoup
from urllib.parse import urljoin    


async def getImg(session,name,url):
    try:
        img_name = url.split("/")[-1]
        all_name = os.path.join(name, img_name)
        if os.path.exists(all_name):
            return
        async with session.get(url, headers=headers) as resp:
            content = await resp.read()
            with open(all_name,'wb') as f:
                f.write(content)
            print(all_name,"-------success------")
    except:
        print(url,"-------error------")
# def saveImg(content,name,url):
    


async def waitSemaphore(session,semaphore,name,url,func):
     async with semaphore:
         return await func(session,name,url)

async def getDetail(session, name, url):
    async with session.get(url, headers=headers) as resp:
        html = await resp.text()
        item = await parseDetail(html, name)
        print(name)
        return item
        


async def getPage(session, url):
    async with session.get(url, headers=headers) as resp:
        html = await resp.text()
        item = await parsePage(html)
        return item


async def parseDetail(html, name):
    root = BeautifulSoup(html, 'lxml')
    urllist = []
    img_num = root.select(".wrapper .photo .big-pic #big-pic p a") # 一页的图片数量
    total_num = root.select(".wrapper .photo #photos #picnum .totalpage")[0].text
    # base_img_url[base_img_url.rfind("."):]
    # base_img_url[:base_img_url.rfind("/")+1]
    try:
        base_img_url = img_num[0].img.get("src")
        base_img_url = base_img_url[:base_img_url.rfind("/")+1] + "%s" + base_img_url[base_img_url.rfind("."):]
        for i in range(1,int(int(len(img_num))*int(total_num))+1):
            # https://img.aitaotu.cc:8089/Pics/2021/0113/07/01.jpg
            urllist.append(base_img_url % str(i).zfill(2))
        return [{"name": name, "url": i} for i in urllist]
    except:
        with open(name+".html","w",encoding="utf8") as f:
            f.write(html)
        print("出错",name)
        return []

async def parsePage(html):
    root = BeautifulSoup(html, 'lxml')
    return [{"name": i.img.get("alt"), "url": urljoin(base_url, i.get("href"))} for i in root.select("#infinite_scroll .item .img>a")]
    # return {"name": '', "url": ''}


async def main(url, page_size):

    async with aiohttp.ClientSession() as session:
        if os.path.exists("img.json"):
            with open("img.json","r",encoding="utf8") as f:
                all_img = json.loads(f.read())
                semaphore = asyncio.Semaphore(300)
                img_tasks = []
                for i in all_img:
                    char_list = ['*', '|', ':', '?','/', '<', '>', '"', '\\']
                    for iii in char_list:
                        if iii in i["name"]:
                            i["name"] = i["name"].replace(iii, "_")
                    full_path = os.path.join(base_path, i["name"].strip())
                    if not os.path.exists(full_path):
                        os.makedirs(full_path)
                    
                    img_tasks.append(asyncio.create_task(waitSemaphore(session,semaphore,full_path,i["url"],getImg)))
                await asyncio.wait(img_tasks)   
                return
        
        page_tasks = []
        for i in range(1, page_size):
            page_tasks.append(asyncio.create_task(getPage(session, url % i)))

        done, pending = await asyncio.wait(page_tasks)
        print("------------页面下载完成---------------")
        all_detail = []
        for i in done:
            all_detail = all_detail + i.result()
        detail_tasks = []

        for i in all_detail:
            detail_tasks.append(asyncio.create_task(
                getDetail(session, i["name"], i["url"])))

        done, pending = await asyncio.wait(detail_tasks)
        print("------------详情页下载完成---------------")
        all_img = []
        for i in done:
            all_img = all_img + i.result()
        
        data = json.dumps(all_img, ensure_ascii=False)

        with open('img.json', "w", encoding="utf-8") as f:
            f.write(data)
        img_tasks = []
        print("------------图片地址保存完成---------------")

        semaphore = asyncio.Semaphore(150)
        for i in all_img:
            char_list = ['*', '|', ':', '?','/', '<', '>', '"', '\\']
            for iii in char_list:
                if iii in i["name"]:
                    i["name"] = i["name"].replace(iii, "_")
            full_path = os.path.join(base_path, i["name"].strip())
            if not os.path.exists(full_path):
                os.makedirs(full_path)
            
            img_tasks.append(asyncio.create_task(waitSemaphore(session,semaphore,full_path,i["url"],getImg)))
        await asyncio.wait(img_tasks)   


if __name__ == "__main__":
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36",
        "Referer": "https://www.aitaotu.com/"
    }
    base_path = "F:\\爱套图"
    base_url = "https://www.aitaotu.com/"
    start_time = time.time()
    asyncio.run(main("https://www.aitaotu.com/meinv/list_%s.html", 284))
    end_time = time.time()
    print("耗时", end_time-start_time)
