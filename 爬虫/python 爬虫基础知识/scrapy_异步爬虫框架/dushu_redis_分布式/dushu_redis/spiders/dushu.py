import uuid

from scrapy_redis.spiders import RedisSpider
from scrapy.http import Request

class DushuSpider(RedisSpider):
    name = 'dushu'
    allowed_domains = ['dushu.com']

    redis_key = 'gx_start_urls'

    # def start_requests(self,):

    def parse(self, response):
        for i in response.css('.sub-catalog a::attr(href)').getall():
            yield Request(response.urljoin(i),callback=self.parse_item)

    def parse_item(self,response):
        divs = response.css('.book-info')
        for div in divs:
            item ={}
            item["id"] = uuid.uuid4().hex
            item['name'] = div.css('div a img::attr(alt)').get()
            item['cover'] = div.css('div a img::attr(data-original)').get()
            item['detail_url'] = div.css('div a::attr(href)').get()

            yield item

        next_page = response.css('.pages a:last-child::attr(href)').get()
        yield Request(response.urljoin(next_page),callback=self.parse_item)