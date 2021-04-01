import requests
import pymysql
from requests import Response
from lxml import etree
import uuid
from csv import DictWriter
import os

def itempipeline(item):
    conn = pymysql.connect(
        host="localhost",
        user="root",
        password="1234",
        database="gsw"
    )
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    sql = "insert into gsw(%s) values(%s)"
    fields = ",".join(item.keys())
    value_placeholds = ",".join(["%%(%s)s" % key for key in item])
    sql = sql % (fields, value_placeholds)

    cursor.execute(sql, item)
    conn.commit()

    cursor.close()
    conn.close()


has_header = os.path.exists('dushuwang.csv')  # 是否第一次操作csv
header_fields = ('id', 'title', 'author', 'content')


def itempipeline4csv(item):
    global has_header
    print(item)
    with open("dushuwang.csv", "a") as f:
        write = DictWriter(f, header_fields)
        if not has_header:
            write.writeheader()
            has_header = True
        write.writerow(item)

def parse(html):
    item = {}
    root = etree.HTML(html)
    divs = root.xpath('//div[@class="left"]/div[@class="sons"]')
    for div in divs:
        item['id'] = uuid.uuid4().hex
        item['title'] = div.xpath('./div[@class="cont"]/p/a/b/text()')[0]
        item['author'] = "-".join(div.xpath('./div[@class="cont"]/p/a/text()'))
        item['content'] = "<br>".join(
            div.xpath('./div[@class="cont"]/div[@class="contson"]//text()'))
        # itempipeline(item)
        itempipeline4csv(item)

def get(url):
    resp: Response = requests.get(url)
    if resp.status_code == 200:
        parse(resp.text)
    else:
        raise Exception("请求失败")


if __name__ == "__main__":
    url = 'https://so.gushiwen.cn/shiwens/default.aspx?xstr=%e8%af%97'
    get(url)
