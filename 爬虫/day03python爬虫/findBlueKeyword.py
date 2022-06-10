from scrapy.url_manager import UrlManager
from scrapy.url_downloader import down_html
from scrapy.url_parse import HtmlParse


class Scrapy():
    def __init__(self):
        self.um = UrlManager()
        self.hp = HtmlParse()

    def scrapy_html(self, root_url):
        self.um.add_url(root_url)
        current = 1
        while self.um.has_url():
            try:
                url = self.um.get_url()
                html_str = down_html(url)
                url_set, img_set = self.hp.html_parse(html_str, "http://www.baidu.com")
                self.um.add_urls(url_set)
                for img in img_set:
                    print(f'第{current}下载的图片地址为:', img)
                current += 1
                if current > count:
                    break
            except:
                print(f'在下载{current}出现错误')
        print(f'待下载的url数量为:{len(self.um.new_url)}已下载的url数量为:{len(self.um.old_url)}')


if __name__ == "__main__":
    scrapy = Scrapy()
    scrapy.scrapy_html("http://www.baidu.com")
