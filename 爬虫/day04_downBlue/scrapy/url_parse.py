# 单引号，双引号，三引号（支持换行）（还可以是注释没有变量接收）
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import re


class HtmlParse():
    def __init__(self):
        self.url_set = set()
        self.img_set = list()
        self.num = 2

    def __url_parse(self):
        self.url_set = {"http://38.103.161.16/forum/forum-25-{}.html".format(str(self.num))}
        self.num = self.num + 1
        return self.url_set

    def __img_parse(self, soup: BeautifulSoup, base: str):

        a_list = soup.find_all('li', class_="Item")

        # a_list = soup.select('li a')
        # print(a_list)
        for a in a_list:
            isShow = a.find('a', string=re.compile(r'狗|推特|FSS|冯珊珊|奴|调教|SM'))

            if isShow:
                Bluedate = a.find('div', class_="Meta").find('em')
                BlueType = a.find('div', class_="Title").find('em').find('a')
                s = {'url': urljoin(base, isShow['href']),
                     'title': isShow.string,
                     'parentsUrl': "http://38.103.161.16/forum/forum-25-{}.html".format(str(self.num - 1)),
                     'page': str(self.num - 1),
                     'date': Bluedate.string,
                     'type': BlueType.string,
                     'company':'第一会所'
                     }
                self.img_set.append(s)
        return self.img_set

    def html_parse(self, html: str, base: str):
        soup = BeautifulSoup(html, 'html.parser')
        url_set = self.__url_parse()
        img_set = self.__img_parse(soup, base)
        # print(img_set)
        return url_set, img_set


if __name__ == "__main__":
    html_doc = """
            <html><head><title>The Dormouse's story</title></head>
            <body>
            <p class="title"><b>The Dormouse's story</b></p>

            <p class="story">Once upon a time there were three little sisters; and their names were
            <li href="http://example.com/elsie" class="Item sub" id="link1"><a href="http://example.com/tillie" class="b" id="link3">酒店</a><a href="http://example.com/tillie" class="b" id="link3">酒店</a></li>,
            <a href="http://example.com/lacie" class="b" id="link2">2</a> and
            <a href="http://example.com/tillie" class="b" id="link3">3</a>;
            and they lived at the bottom of a well.</p>
            <img src="/image/abc.png" />
            <p class="story">...</p>
            """
    hp = HtmlParse()
    url_set, img_set = hp.html_parse(html_doc, "http://www.163.com")

    print(img_set)
    print(url_set)
