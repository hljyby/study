import uuid

import scrapy
from scrapy.http import Response, HtmlResponse, Request
from scrapy.selector import Selector, SelectorList

from qidian.items import *

class FinishSpider(scrapy.Spider):
    name = 'finish'
    allowed_domains = ['qidian.com',"book.qidian.com"]
    start_urls = ['https://www.qidian.com/finish']

    def parse(self, response: Response):
        if response.status == 200:
            liList = response.css(".all-img-list.cf li")
            for i in liList:
                item = BookItem()
                item["book_id"] = uuid.uuid4().hex
                item["url"] = i.css('.book-mid-info h4 a::attr("href")').get()
                item["cover"] = i.css('.book-img-box a img::attr("src")').get()
                item["name"] = i.css('.book-mid-info h4 a::text').get()
                item["summary"] = i.css(
                    '.book-mid-info .intro::text').get().replace(" ", "").replace("\r", "")
                item["author"], * \
                    item["tags"] = i.css(
                        '.book-mid-info .author a::text').getall()
                yield item
                yield Request(response.urljoin(item["url"]),callback=self.parse_info,priority=10,meta={'book_id':item['book_id']})

                # 请求小说详情页
            next_url = response.css(
                ".lbf-pagination li:last-child a::attr('href')").get()
            if next_url.find("javascript") == -1:
                yield Request(response.urljoin(next_url),callback=self.parse,priority=100)

    def parse_info(self,response:Response):
        if response.status == 200: 
            segs = response.css('.volume-wrap .volume ul li a')
            for seg in segs:
                item = SegItem()
                item['book_id'] = response.meta['book_id']
                item["seg_id"] = uuid.uuid4().hex
                item["title"] = seg.css("::text").get()
                item["seg_url"] = response.urljoin(seg.css("::attr(href)").get())
                yield item
                yield Request(item["seg_url"],callback=self.parse_seg,priority=1,meta={"seg_id":item["seg_id"]})
    
    def parse_seg(self,response:Response):
        if response.status == 200:
            item = SegDetail()
            seg_detail = response.css(".read-content p::text").getall()
            seg_detail = "<br>".join(seg_detail)
            seg_detail = seg_detail.replace("\u3000","").strip().replace("\n","")
            item["seg_id"] = response.meta["seg_id"]
            item["text"] = seg_detail