# 单引号，双引号，三引号（支持换行）（还可以是注释没有变量接收）
from bs4 import BeautifulSoup
from urllib.parse import urljoin


class HtmlParse():
    def __init__(self):
        self.url_set = set()
        self.img_set = set()

    def __url_parse(self, soup: BeautifulSoup, base: str):
        a_list = soup.find_all('a')
        for a in a_list:
            self.url_set.add(urljoin(base, a['href']))
        return self.url_set

    def __img_parse(self, soup: BeautifulSoup, base: str):
        img_list = soup.find_all('img')
        for img in img_list:
            self.img_set.add(urljoin(base, img['src']))
        return self.img_set

    def html_parse(self, html: str, base: str):
        soup = BeautifulSoup(html, 'html.parser')
        url_set = self.__url_parse(soup,base)
        img_set = self.__img_parse(soup,base)
        return url_set, img_set


if __name__ == "__main__":
    html_doc = """
            <html><head><title>The Dormouse's story</title></head>
            <body>
            <p class="title"><b>The Dormouse's story</b></p>

            <p class="story">Once upon a time there were three little sisters; and their names were
            <a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
            <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
            <a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
            and they lived at the bottom of a well.</p>
            <img src="/image/abc.png" />
            <p class="story">...</p>
            """
    hp = HtmlParse()
    url_set, img_set = hp.html_parse(html_doc,"http://www.163.com")
    print(url_set, img_set)
    print(urljoin("http://www.163.com", "/image/abc.png"))
    print(urljoin("http://www.163.com", "http://www.163.com/image/abc.png"))
    print(urljoin("http://www.163.com", "http://www.baidu.com/image/abc.png"))
