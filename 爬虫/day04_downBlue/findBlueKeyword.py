from scrapy.url_manager import UrlManager
from scrapy.url_downloader import down_html
from scrapy.url_parse import HtmlParse
import time
import json


class Scrapy():
    def __init__(self):
        self.um = UrlManager()
        self.hp = HtmlParse()
        self.all_url = list()

    def scrapy_html(self, root_url):
        self.um.add_url(root_url)
        current = 1
        while self.um.has_url() and current <= 600:
            try:
                url = self.um.get_url()
                html_str = down_html(url)
                # if not html_str:
                #     self.save_data()
                #     break
                # print(html_str)
                url_set, img_set = self.hp.html_parse(html_str, "http://38.103.161.16/forum/")
                # print(img_set)
                print(url_set)

                self.um.add_urls(url_set)
                self.addUrls(img_set)
                current += 1
            except Exception as e:
                print(e)
                print(f'在下载{current}出现错误')

    def addUrls(self,url):
        self.all_url = url

    def save_data(self):
        with open('./blueData.json', 'w', encoding='utf-8') as f:
            f.write(json.dumps(self.all_url, ensure_ascii=False))
        print('保存成功！')

if __name__ == "__main__":
    scrapy = Scrapy()
    scrapy.scrapy_html("http://38.103.161.16/forum/forum-25-1.html")
    # print(json.dumps(scrapy.all_url,ensure_ascii=False))
    with open('./blueData.json', 'w', encoding='utf-8') as f:
        f.write(json.dumps(scrapy.all_url, ensure_ascii=False))
    print('保存成功！')
