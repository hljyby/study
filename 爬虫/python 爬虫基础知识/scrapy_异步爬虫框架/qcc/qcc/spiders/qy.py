import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class QySpider(CrawlSpider):
    name = 'qy'
    allowed_domains = ['qcc.com']
    start_urls = ['https://www.qcc.com/web/search?key=aa']

    rules = (
        Rule(LinkExtractor(restrict_css=(".maininfo")), callback='parse_item', follow=True),
        # Rule(LinkExtractor(restrict_css=()), callback='parse_item', follow=True)
    )

    def parse_item(self, response):
        item = {}
        #item['domain_id'] = response.xpath('//input[@id="sid"]/@value').get()
        #item['name'] = response.xpath('//div[@id="name"]').get()
        #item['description'] = response.xpath('//div[@id="description"]').get()
        return item
