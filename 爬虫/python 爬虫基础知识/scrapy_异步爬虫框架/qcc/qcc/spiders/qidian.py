import scrapy


class QidianSpider(scrapy.Spider):
    name = 'qidian'
    allowed_domains = ['qidian.com','bookcover.yuewen.com','facepic.qidian.com','qidian.gtimg.com']
    start_urls = ['https://www.qidian.com/xuanhuan']

    def parse(self, response):
        item={}
        if response.status == 200:
            imgs_lazy = response.css('img[data-original]::attr(data-original)').getall()
            imgs_src = response.xpath('//img[not(@data-original)]/@src').getall()
            
            item["image_urls"] = ["https:" + i for i in imgs_lazy] + ["https:" + i for i in imgs_src] 
            item['images'] =[]
            yield item