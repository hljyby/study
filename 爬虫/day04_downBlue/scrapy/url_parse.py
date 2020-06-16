# 单引号，双引号，三引号（支持换行）（还可以是注释没有变量接收）
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import re


class HtmlParse():
    def __init__(self):
        self.url_set = set()
        self.img_set = set()
        self.num = 2

    def __url_parse(self):
        self.url_set.add("https://w13.wme6aqx1.club/2048/thread.php?fid-15-page-{}.html".format(str(self.num)))
        self.num = self.num + 1
        return self.url_set

    def __img_parse(self, soup: BeautifulSoup, base: str):
        a_list = soup.find_all('a', class_="subject", string=re.compile(r'狗'))
        b_list = soup.find_all('a', class_="subject", string=re.compile(r'推特'))
        c_list = soup.find_all('a', class_="subject", string=re.compile(r'FSS'))

        for a in a_list:
            self.img_set.add(urljoin(base, a['href']))
        for a in b_list:
            self.img_set.add(urljoin(base, a['href']))
        for a in c_list:
            self.img_set.add(urljoin(base, a['href']))
        return self.img_set

    def html_parse(self, html: str, base: str):
        soup = BeautifulSoup(html, 'html.parser')
        url_set = self.__url_parse()
        img_set = self.__img_parse(soup, base)
        return url_set, img_set


if __name__ == "__main__":
    html_doc = """
            <html><head><title>The Dormouse's story</title></head>
            <body>
            <p class="title"><b>The Dormouse's story</b></p>

            <p class="story">Once upon a time there were three little sisters; and their names were
            <a href="http://example.com/elsie" class="b" id="link1">1</a>,
            <a href="http://example.com/lacie" class="b" id="link2">2</a> and
            <a href="http://example.com/tillie" class="b" id="link3">3</a>;
            and they lived at the bottom of a well.</p>
            <img src="/image/abc.png" />
            <p class="story">...</p>
            """
    hp = HtmlParse()
    url_set, img_set = hp.html_parse(html_doc, "http://www.163.com")

    print(url_set)
