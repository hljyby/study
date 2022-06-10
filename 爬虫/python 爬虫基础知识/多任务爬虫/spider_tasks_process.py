"""
    基于进程加线程实现多任务的爬虫程序
"""


from multiprocessing import Process, Queue
from threading import Thread
from queue import Queue as TQueue

import requests
from requests import Response

from lxml import etree
import pymysql
headers = {
    "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1"
}

conn = pymysql.connect(
    host="localhost",
    user="root",
    password="1234",
    database="meinvtu"
)

cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)


class DownLoadThread(Thread):
    def __init__(self, url):
        super(DownLoadThread, self).__init__()
        self.url = url
        self.content = None

    def run(self):
        print("开始下载", self.url)
        resp: Response = requests.get(self.url, headers=headers, verify=False)

        if resp.status_code == 200:
            resp.encoding = "utf-8"
            self.content = resp.text
        print("下载完成", self.url)

    def get_content(self):
        return self.content


class DownLoadProcess(Process):
    """
        下载进程
    """

    def __init__(self, url_q, html_q):
        self.url_q = url_q
        self.html_q = html_q
        super().__init__()

    def run(self):
        while True:
            try:
                url = self.url_q.get(timeout=5)
                t = DownLoadThread(url)
                t.start()
                t.join()

                # 获取下载的数据
                html = t.get_content()

                # 将数据压入到解析队列中
                self.html_q.put((url, html))

            except:
                break

        print("----下载进程 over ----")


class ParseThread(Thread):
    def __init__(self, html, url_q):
        super().__init__()
        self.html = html
        self.url_q = url_q

    def run(self):
        root = etree.HTML(self.html)
        imgs = root.xpath('//img[contains(@class,"lazy")]')

        item = {}
        for img in imgs:
            try:
                item['title'] = img.xpath('./@alt')[0]
            except:
                item['title'] = "没有"
            item['src'] = img.xpath('./@data-original')[0]
            print(item)

            # sql = "insert into main_img(%s) values(%s)"
            # fields = ",".join(item.keys())
            # value_placeholds = ",".join(["%%(%s)s" % key for key in item])
            # sql = sql % (fields, value_placeholds)
            # cursor.execute(sql, item)
            # conn.commit()

        # next 下一页链接
        next_page = root.xpath(
            '//a[contains(@class,"button") and contains(@class,"radius")]/@href')
        print(next_page)
        if next_page:
            self.url_q.put(next_page[-1])  # 将新的下载任务加入到队列里


class ParseProcess(Process):
    # 解析进程

    def __init__(self, url_q, html_q):
        super().__init__()
        self.url_q = url_q
        self.html_q = html_q

    def run(self):
        while True:
            try:
                # 读取解析任务
                url, html = self.html_q.get(timeout=5)
                print("开始解析")
                ParseThread(html, self.url_q).start()
            except:
                break
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

    cursor.close()
    conn.close()

    print("------over-------")
