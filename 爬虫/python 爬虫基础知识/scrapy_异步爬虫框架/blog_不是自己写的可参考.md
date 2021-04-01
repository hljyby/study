# [day100 scrapy请求传参 中间件 去重规则 分布式爬虫](https://www.cnblogs.com/zqfzqf/p/12392317.html)

## 全站爬取cnblogs数据

深度优先 和 广度优先

```python
#重点：区分yield item 和request
1 yield Request对象，scrapy就会再去爬取这个地址
Request(url,callback=xx) 回调函数，加载的解析函数
2 深度爬取和广度爬取
	--深度优先：https://www.cnblogs.com/qing-gee/p/12365143.html
    --广度优先：https://www.cnblogs.com/sitehome/p/6
```

### cnblogs.py

```python
# -*- coding: utf-8 -*-
import scrapy
from xuexi.items import ArticleItem
# from scrapy import Request#通过这个也可以，提到这里了
from scrapy.http import Request  # 这是真正的位置


# 了解：究竟真正的起始爬取的方法在哪里 start_requests
class CnblogsSpider(scrapy.Spider):
    name = 'cnblogs'
    allowed_domains = ['www.cnblogs.com']  # 这个可以不写
    start_urls = ['https://www.cnblogs.com/']

    # def start_requests(self):
    #     yield Request(url='http://www.baidu.com')这个是真正的开始

    def parse(self, response):
        # print(response)<200 https://www.baidu.com/>
        div_list = response.css('div.post_item')
        for div in div_list:
            title = div.xpath('./div[2]/h3/a/text()').extract_first()
            # print(title)
            author = div.xpath('./div[2]/div/a/text()').extract_first()
            # print(author)
            desc = div.xpath('./div[2]/p/text()').extract()[-1]
            # print(desc)
            url = div.xpath('./div[2]/div/span[2]/a/@href').extract_first()
            # print(url)
            item=ArticleItem()
            item['title']=title
            item['author']=author
            item['desc']=desc
            item['url']=url
            ##########接下来做两件事
            #第一 深度爬取下一页
            # 第二 广度爬取
            # yield item对象回去保存 Request对象获取爬取
            # callback 回调 数据爬完回来 去哪里解析，默认是parse
            # meta  传参给回调函数的 以字典的形式
            yield Request(url=url,callback=self.parse_detail,meta={'item':item})

        #css选择器取属性  ::attr(属性名） 文本 ::text
        next_url='https://www.cnblogs.com'+response.css('div.pager>a:last-child::attr(href)').extract_first()
        # print(next_url)
        # 两种方式都可以
        # yield Request(url=next_url,callback=self.parse)
        yield Request(url=next_url)

    def parse_detail(self,response):
        print('------------',response)
        item=response.meta.get('item')
        # print(item)
        content=response.css('#post_detail').extract_first()
        # print(str(content))
        item['content']=str(content)
        yield item
```

### items.py

```python
class ArticleItem(scrapy.Item):
    title = scrapy.Field()
    author = scrapy.Field()
    desc = scrapy.Field()
    content = scrapy.Field()
    url = scrapy.Field()
```

### pipelines.py

```python
import pymysql
class MysqlArticlePipeline(object):
    def open_spider(self,spider):
        self.conn=pymysql.connect(host='127.0.0.1', user='root', password="",
                                    database='chouti', port=3306)

    def process_item(self, item, spider):
        cursor=self.conn.cursor()
        sql="insert into article (title,author,url,`desc`,content) values ('%s','%s','%s','%s','%s')"%(item['title'],item['author'],item['url'],item['desc'],item['content'])
        cursor.execute(sql)
        self.conn.commit()
        return item

    def close_spider(self, spider):
        self.conn.close()
```

## scrapy的请求传参

```python
1 yield Request(url=url,callback=self.parse_detail,meta={'item':item})  # meta=字典
2 解析方法中  response.meta.get('item')   上面传过来的
```

## 提升scrapy爬取数据的效率

```python
- 在配置文件中进行相关的配置即可:(默认还有一套setting)
#1 增加并发：
默认scrapy开启的并发线程为32个，可以适当进行增加。在settings配置文件中修改CONCURRENT_REQUESTS = 100值为100,并发设置成了为100。
#2 降低日志级别：
在运行scrapy时，会有大量日志信息的输出，为了减少CPU的使用率。可以设置log输出信息为INFO或者ERROR即可。在配置文件中编写：LOG_LEVEL = ‘INFO’
# 3 禁止cookie：
如果不是真的需要cookie，则在scrapy爬取数据时可以禁止cookie从而减少CPU的使用率，提升爬取效率。在配置文件中编写：COOKIES_ENABLED = False
# 4 禁止重试：
对失败的HTTP进行重新请求（重试）会减慢爬取速度，因此可以禁止重试。在配置文件中编写：RETRY_ENABLED = False
# 5 减少下载超时：
如果对一个非常慢的链接进行爬取，减少下载超时可以能让卡住的链接快速被放弃，从而提升效率。在配置文件中进行编写：DOWNLOAD_TIMEOUT = 10 超时时间为10s
```

## scrapy的中间件（下载中间件）

```python
-DownloaderMiddleware
	-process_request
  	-retrun None/Respnose/Request/raise
    -None：表示继续处理
    -Respnose：会被引擎调度，进入爬虫
    -Request：会被引擎调度，放到调度器，等待下一次爬取
    -raise：process_exception触发执行
  -process_response
  	-Response：继续处理，会被引擎调度，放到爬虫中解析
  	-Request：会被引擎调度，放到调度器，等待下一次爬取
    -raise：process_exception触发执行
  -process_exception
  	-None：表示继续处理
    -Respnose：会被引擎调度，进入爬虫
    -Request：会被引擎调度，放到调度器，等待下一次爬取
```

### process_exception的使用

```python
    def process_exception(self, request, exception, spider):
        from scrapy.http import Request
        print('xxx')
        request=Request(url='https://www.baidu.com/')
        return request
```

### process_response的使用

```python
   def process_request(self, request, spider):
        # 请求头
        # print(request.headers)
        request.headers['User-Agent']=random.choice(self.user_agent_list)

        # 设置cookie（并不是所有的请求，都需要带cookie，加一个判断即可）
        #可以使用cookie池
        print(request.cookies)
        # import requests #如果自己搭建cookie池 这么写
        # ret=requests.get('127.0.0.1/get').json()['cookie']
        # request.cookies=ret
        # request.cookies={'name':'lqz','age':18}

        # 使用代理池
        print(request.meta)
        request.meta['proxy']='http://117.27.152.236:1080'

        return None
```

### process_response在下面写

## selenium在scrapy中的使用流程

```python
1 在爬虫中启动和关闭selenium
-启动
def spider_closed(self,spider):
	self.bro = webdriver.Chrome('./chromedriver')
-关闭
def spider_closed(self,spider):
    print("爬虫结束，会走我关了")
    self.bro.quit()

@classmethod
def from_crawler(cls, crawler):
    # This method is used by Scrapy to create your spiders.
    s = cls()
    crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)        					     crawler.signals.connect(s.spider_closed, signal=signals.spider_closed)

    return s        
    2.在下载中间件中写
def process_response(self, request, response, spider):
    from scrapy.http import Request,HtmlResponse
    # 因为向该地址发请求，不能执行js，现在用selenium执行js，获取执行完的结果，再返回response对象
    url=request.url
    spider.bro.get(url)
    page_source=spider.bro.page_source
    import time
    time.sleep(2)
    new_response=HtmlResponse(url=url,body=page_source,encoding='utf-8',request=request)
    return new_response
```

## 去重规则源码分析

```python
from scrapy.dupefilter import RFPDupeFilter
from scrapy.core.scheduler import Scheduler

# 整个去重规则是通过RFPDupeFilter中的request_seen控制
# 在调度器Scheduler中的enqueue_request调用，如果dont_filter=True就不过滤了

# scrapy中如下两个地址，是同一个地址，通过request_fingerprint处理了
# http://www.baidu.com/?name=lqz&age=18
# http://www.baidu.com/?age=18&name=lqz
res1=Request(url='http://www.baidu.com/?name=lqz&age=18')
res2=Request(url='http://www.baidu.com/?age=18&name=lqz')
print(request_fingerprint(res1))
print(request_fingerprint(res2))


# 有更省空间的方式
bitmap方式：比特位：计算机的存储单位  1bit    byte=8个比特位    1kb=1024b   
布隆过滤器：BloomFilter：原理


# 自己重写去重规则
# 1 在setting中配置
DUPEFILTER_CLASS = 'scrapy.dupefilter.RFPDupeFilter' #默认的去重规则帮我们去重，去重规则在内存中
# 写一个类，继承BaseDupeFilter，重写方法，主要重写request_seen，如果返回True表示有了，False表示没有
```

## 分布式爬虫

```python
# scrapy-redis
# 概念：整站爬取，假设有9w条连接地址，一台机器一天只能爬3w条，爬3天
#			现在想用3台机器爬一天
# scrapy项目部署在3台机器上，三台机器重复的爬9w条，3台机器共享爬取的地址，
# 3台机器都去一个队列中取地址爬取

#scrapy-redis 重写了Scheduler和pipline
pip3 install scrapy-redis
#https://github.com/rmax/scrapy-redis ：整个源码总共不超过1000行


# 使用
1 在setting中配置
# 分布式爬虫的配置
SCHEDULER = "scrapy_redis.scheduler.Scheduler"
# Ensure all spiders share same duplicates filter through redis.
DUPEFILTER_CLASS = "scrapy_redis.dupefilter.RFPDupeFilter"

ITEM_PIPELINES = {
    'scrapy_redis.pipelines.RedisPipeline': 300
}
2 修改爬虫类
from scrapy_redis.spiders import RedisSpider
	class CnblogsSpider(RedisSpider): # 继承RedisSpider
    name = 'cnblogs'
    allowed_domains = ['www.cnblogs.com']

    redis_key = 'myspider:start_urls'  # 原来的start_ulr去掉，携写成这个
3 可以吧项目部署在不同的机器上了

4 任意一台机器，向redis中写入下面
redis-cli
lpush myspider:start_urls https://www.cnblogs.com/
```