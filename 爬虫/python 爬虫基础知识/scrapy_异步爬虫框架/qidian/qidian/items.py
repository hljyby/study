# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class BookItem(scrapy.Item):
    book_id = scrapy.Field() # 书的id
    url = scrapy.Field()     # 书的url
    cover = scrapy.Field()   # 书封面url
    name = scrapy.Field()    # 书名
    summary = scrapy.Field() # 简介
    author = scrapy.Field()  # 作者 
    tags = scrapy.Field()    # 标签

class SegItem(scrapy.Item):
    book_id = scrapy.Field() # 书id
    seg_id = scrapy.Field()  # 章节id
    title = scrapy.Field()   # 章节标题
    seg_url = scrapy.Field()   # 章节url

class SegDetail(scrapy.Item):
    seg_id = scrapy.Field() # 章节id
    text = scrapy.Field()   # 内容

# class QidianItem(scrapy.Item):
#     # define the fields for your item here like:
#     # name = scrapy.Field()
#     pass
