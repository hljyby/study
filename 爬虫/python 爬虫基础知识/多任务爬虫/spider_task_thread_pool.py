"""
    基于进程加线程实现多任务的爬虫程序
"""

from multiprocessing import Process, Queue
from threading import Thread
import threading
from queue import Queue as TQueue

import requests
from requests import Response

from lxml import etree

headers = {
    "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1"
}


class DownLoadThread(Thread):
    # 下载线程
    def __init__(self, task_queue, result_queue):
        super(DownLoadThread, self).__init__()
        self.task_queue = task_queue
        self.result_queue = result_queue

    def run(self):
        while True:
            try:
                url = self.task_queue.get(timeout=10)
                content = self.get(url)
                self.result_queue.put(content)
            except:
                break

    def get(self, url):
        print("开始下载", url, threading.current_thread().ident)
        resp: Response = requests.get(url, headers=headers)

        if resp.status_code == 200:
            resp.encoding = "utf-8"
            return resp.text
        print("下载完成", url)


class DownLoadProcess(Process):
    """
        下载进程
    """

    def __init__(self, url_q, html_q):
        super().__init__()
        self.url_q = url_q
        self.html_q = html_q

        # self.task_queue = TQueue()

    def run(self):
        ts = [DownLoadThread(self.url_q, self.html_q) for i in range(2)]

        # 将数据压入到解析队列中

        for i in ts:
            i.start()

        for i in ts:
            i.join()

        print("----下载进程 over ----")


class ParseThread(Thread):
    def __init__(self, html_q, url_q):
        super().__init__()
        self.html_q = html_q
        self.url_q = url_q

    def run(self):
        while True:
            try:
                html = self.html_q.get(timeout=10)
                next_page = self.parse(html)
                # next 下一页链接
                print(next_page)
                if next_page:
                    self.url_q.put(next_page[-1])  # 将新的下载任务加入到队列里
            except:
                break

    def parse(self, html):
        print("开始解析", threading.current_thread().ident)
        root = etree.HTML(html)
        imgs = root.xpath('//img[contains(@class,"lazy")]')

        item = {}
        for img in imgs:
            try:
                item['title'] = img.xpath('./@alt')[0]
            except:
                item['title'] = "没有"
            item['src'] = img.xpath('./@data-original')[0]
            print(item)
        
        next_element = root.xpath('//a[contains(@class,"button") and contains(@class,"radius")]/text()')
        bool_next = next_element and next_element[-1] == "下一页 »"
        print(next_element[-1])
        if bool_next:
            next_page = root.xpath('//a[contains(@class,"button") and contains(@class,"radius")]/@href')
            return next_page
        return []


class ParseProcess(Process):
    # 解析进程

    def __init__(self, url_q, html_q):
        super().__init__()
        self.url_q = url_q
        self.html_q = html_q

    def run(self):

        ts = [ParseThread(self.html_q, self.url_q) for i in range(3)]

        for i in ts:
            i.start()

        for i in ts:
            i.join()

        print("-----解析进程结束----")


if __name__ == "__main__":
    task1 = Queue()  # 下载任务队列
    task2 = Queue()  # 解析任务队列

    # 起始爬虫任务
    task1.put("https://www.mzitu.com/")

    p1 = DownLoadProcess(task1, task2)
    p2 = ParseProcess(task1, task2)

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print("------over-------")
