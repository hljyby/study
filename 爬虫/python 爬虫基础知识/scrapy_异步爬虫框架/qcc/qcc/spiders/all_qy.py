import scrapy


class AllQySpider(scrapy.Spider):
    name = 'all_qy'
    allowed_domains = ['qcc.com']
    start_urls = ['http://qcc.com/']

    def parse(self, response):
        pass
