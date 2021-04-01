# scrapy-splash 简单使用

## 一.创建scrapy 应用

```python
scrapy startproject jingdong
```

## 二.穿件爬虫(爬虫名字不能scrapy名相

```python
scrapy genspider jd jd.com
```

## 三.开启scrapy-splash 服务

```python
sudo docker run -p 8050:8050 scrapinghub/splash
```

## 四.安装scrapy-splash 框架

```python
pip install scrapy-splash
```

## 五.配置setting文件

```python
ROBOTSTXT_OBEY = False


SPIDER_MIDDLEWARES = {
    'scrapy_splash.SplashDeduplicateArgsMiddleware': 100,
}


DOWNLOADER_MIDDLEWARES = {
    'scrapy_splash.SplashCookiesMiddleware': 723,
    'scrapy_splash.SplashMiddleware': 725,
    'scrapy.downloadermiddlewares.httpcompression.HttpCompressionMiddleware': 810
}


SPLASH_URL = 'http://localhost:8050'


DUPEFILTER_CLASS = 'scrapy_splash.SplashAwareDupeFilter'
HTTPCACHE_STORAGE = 'scrapy_splash.SplashAwareFSCacheStorage'
```

## 六.重写scrapy 的 start_requests方法调用请求

```python
def start_requests(self):
        for url in self.start_urls:
            yield SplashRequest(url,
                                self.parse,
                                args={'wait': '0.5'})
```

## 完整例子:

```python
import scrapy
from scrapy_splash import SplashRequest

class JdSpider(scrapy.Spider):
    name = 'jd'
    # allowed_domains = ['jd.com', 'book.jd.com']
    start_urls = ['https://book.jd.com/']


    def start_requests(self):
        for url in self.start_urls:
            yield SplashRequest(url,
                                self.parse,
                                args={'wait': '0.5'})


    def parse(self, response):
        div_list = response.xpath('//div[@class="book_nav_body"]/div')
        for div in div_list:
            title = div.xpath('./div//h3[@class="item_header_title"]/a/text()')
            print(title)
```