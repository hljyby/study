from scrapy.url_manager import UrlManager
from scrapy.url_downloader import down_html
from scrapy.url_parse import HtmlParse
import time


class Scrapy():
    def __init__(self):
        self.um = UrlManager()
        self.hp = HtmlParse()
        self.all_url = set()

    def scrapy_html(self, root_url):
        self.um.add_url(root_url)
        current = 1
        while self.um.has_url():
            try:
                url = self.um.get_url()
                html_str = down_html(url)
                if not html_str:
                    self.save_data(img_set,"app")
                    break
                url_set, img_set = self.hp.html_parse(html_str, "https://w13.wme6aqx1.club/2048/")
                print(img_set)
                print(url_set)

                self.um.add_urls(url_set)
                self.addUrls(img_set)
                current += 1
            except:
                print(f'在下载{current}出现错误')

    def addUrls(self,url):
        self.all_url = self.all_url | url

    def save_data(data, name):
        file_name = name + '_' + time.strftime('%Y_%m_%d', time.localtime(time.time())) + '.csv'
        data.to_csv(file_name, index=None, encoding='utf_8_sig')
        print(file_name + '保存成功！')

if __name__ == "__main__":
    scrapy = Scrapy()
    scrapy.scrapy_html("https://w13.wme6aqx1.club/2048/thread.php?fid-15-page-1.html")
