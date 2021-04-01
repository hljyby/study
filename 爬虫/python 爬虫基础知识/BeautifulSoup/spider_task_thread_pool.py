"""
    基于进程加线程实现多任务的爬虫程序
"""
import os

from multiprocessing import Process, Queue
from threading import Thread
import threading
from queue import Queue as TQueue

import requests
from requests import Response

from lxml import etree
from bs4 import BeautifulSoup
headers = {
    "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1"
}

download_type = {
    'img': 'img',
    'page': 'page',
    'content': 'content'
}

base_dir = "F:\嫩色艳图" # 本地地址
base_url = "http://www.fulimeitu.xyz" # 网站根目录

num = 1


class DownLoadPageThread(Thread):
    # 下载线程
    def __init__(self, url_q, html_q, img_url_q, content_q):
        super().__init__()
        self.url_q = url_q
        self.html_q = html_q
        self.img_url_q = img_url_q
        self.content_q = content_q

    def run(self):
        while True:
            try:
                taskType, url = self.url_q.get(timeout=10)
                content = self.get(taskType, url)
                self.html_q.put((taskType, content))
            except:
                break

    def get(self, taskType, url):
        print("---开始下载page---", url)
        resp: Response = requests.get(url, headers=headers)
        if resp.status_code == 200:
            resp.encoding = "utf-8"
            return resp.text
        print("---page下载失败---", url)


class DownLoadPageProcess(Process):
    """
        下载Page进程
        @ des:下载下一页 页面的进程
    """

    def __init__(self, url_q, html_q, img_url_q, content_q):
        super().__init__()
        self.url_q = url_q
        self.html_q = html_q
        self.img_url_q = img_url_q
        self.content_q = content_q

    def run(self):
        ts = [DownLoadPageThread(
            self.url_q, self.html_q, self.img_url_q, self.content_q) for i in range(2)]

        for i in ts:
            i.start()

        for i in ts:
            i.join()

        print("----下载Page进程 over ----")


class DownLoadContentThread(Thread):
    # 下载线程
    def __init__(self, url_q, html_q, img_url_q, content_q):
        super().__init__()
        self.url_q = url_q
        self.html_q = html_q
        self.img_url_q = img_url_q
        self.content_q = content_q

    def run(self):
        while True:
            try:
                taskType, url_list = self.content_q.get(timeout=10)
                self.get(taskType, url_list)

            except:
                break

    def get(self, taskType, url_list):
        print("---开始下载content---", len(url_list))
        # print(url_list)
        for url in url_list:
            resp: Response = requests.get(url, headers=headers)
            if resp.status_code == 200:
                resp.encoding = "utf-8"
                self.html_q.put((taskType, resp.text))
        print("---content下载结束---", len(url_list))

class DownLoadContentProcess(Process):
    """
        下载Content进程
        @ des:下载详情 页面的进程

    """

    def __init__(self, url_q, html_q, img_url_q, content_q):
        super().__init__()
        self.url_q = url_q
        self.html_q = html_q
        self.img_url_q = img_url_q
        self.content_q = content_q

    def run(self):
        ts2 = [DownLoadContentThread(
            self.url_q, self.html_q, self.img_url_q, self.content_q) for i in range(5)]

        for i in ts2:
            i.start()

        for i in ts2:
            i.join()

        print("----下载Content进程 over ----")


class ParseThread(Thread):
    def __init__(self, url_q, html_q, img_url_q, content_q):
        super().__init__()
        self.url_q = url_q
        self.html_q = html_q
        self.img_url_q = img_url_q
        self.content_q = content_q

    def run(self):
        while True:
            try:
                taskType, html = self.html_q.get(timeout=10)
                self.parse(taskType, html)
            except:
                break

    def parse(self, taskType, html):
        print("---开始解析---", taskType)
        if taskType == download_type.get("page"):
            root = BeautifulSoup(html, 'lxml')
            # print(html)
            url_list = [base_url + i.get("href")
                        for i in root.select("#portfolio-grid .item-wrap,.fancybox")]
            print(url_list)
            self.content_q.put(
                (download_type.get("content"), url_list))

            li_list = root.select('.pagelist li a')
            # for i in range(len(li_list)):
            #     # print(i.get_text())
            #     # print(int(i.get("href").split("/")[-1].split(".")[0].split("_")[-1]))
            #     # if i.get_text() == ">" :
            #     #     if int(i.get("href").split("/")[-1].split(".")[0].split("_")[-1]) <= 11:
            # print("-"*20,li_list)
            if int(li_list[-2].get("href").split("/")[-1].split(".")[0].split("_")[-1]) <= 11:
                self.url_q.put(
                    (taskType, base_url + li_list[-2].get("href"))
                )
            print(taskType, "---解析结束---")
        if taskType == download_type.get("content"):
            
            root = BeautifulSoup(html, 'lxml')
            name = root.select(".head h3")[0].get_text()
            url_list = [i.get("data-original")
                        for i in root.select(".container .art-content a .lazy")]

            self.img_url_q.put(
                (name, url_list)
            )
            print(taskType, "---解析结束---")
        return


class ParseProcess(Process):
    # 解析html进程

    def __init__(self, url_q, html_q, img_url_q, content_q):
        super().__init__()
        self.url_q = url_q
        self.html_q = html_q
        self.img_url_q = img_url_q
        self.content_q = content_q

    def run(self):

        ts = [ParseThread(self.url_q, self.html_q,
                          self.img_url_q, self.content_q) for i in range(10)]

        for i in ts:
            i.start()

        for i in ts:
            i.join()

        print("-----解析进程结束----")


class SaveImgThread(Thread):
    def __init__(self, url_q, html_q, img_url_q, content_q):
        super().__init__()
        self.url_q = url_q
        self.html_q = html_q
        self.img_url_q = img_url_q
        self.content_q = content_q

    def run(self):
        while True:
            try:
                name, url_list = self.img_url_q.get(timeout=10)
                self.save(name, url_list)
            except:
                break

    def save(self, name, url_list):
        print("---开始保存---", name ,len(url_list))
        # print(url_list)
        if not os.path.exists(base_dir + '/' + name):
            os.makedirs(base_dir + '/' + name)

        for i in url_list:
            img_name = i.split("/")[-1]

            if os.path.exists(base_dir + '/' + name + '/' + img_name):
                continue

            resp: Response = requests.get(i, headers=headers)

            with open(base_dir + '/' + name + '/' + img_name, "wb") as f:
                f.write(resp.content)
        print("---保存结束---", name)


class SaveImgProcess(Process):
    # 下载保存图片进程

    def __init__(self, url_q, html_q, img_url_q, content_q):
        super().__init__()
        self.url_q = url_q
        self.html_q = html_q
        self.img_url_q = img_url_q
        self.content_q = content_q

    def run(self):

        ts = [SaveImgThread(self.url_q, self.html_q,
                            self.img_url_q, self.content_q) for i in range(10)]

        for i in ts:
            i.start()

        for i in ts:
            i.join()

        print("-----保存图片进程结束----")


if __name__ == "__main__":
    task1 = Queue()  # 索引任务队列
    task2 = Queue()  # 解析任务队列
    task3 = Queue()  # 图片任务队列
    task4 = Queue()  # 具体页面任务队列

    # 起始爬虫任务
    task1.put((download_type.get("page"), "http://www.fulimeitu.xyz/xgpic/"))

    p1 = DownLoadPageProcess(task1, task2, task3, task4)
    p2 = ParseProcess(task1, task2, task3, task4)
    p3 = SaveImgProcess(task1, task2, task3, task4)
    p4 = DownLoadContentProcess(task1, task2, task3, task4)

    p1.start()
    p4.start()
    p2.start()
    p3.start()

    p1.join()
    p4.join()
    p2.join()
    p3.join()

    print("------over-------")
