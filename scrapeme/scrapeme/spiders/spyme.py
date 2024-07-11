import scrapy
from scrapeme.items import Product

class SpymeSpider(scrapy.Spider):
    name = "spyme"
    
    def start_requests(self):
        main_url = "https://scrapeme.live/shop/"
        
        yield scrapy.Request(url=main_url, callback=self.parse_main)

    def parse_main(self, response):
        
        all_p = response.xpath('//ul[contains(@class, "products columns")]//li')
        
        for i in range(1, len(all_p)+1):
            url = response.xpath(f'//ul[contains(@class, "products columns")]/li[{i}]/a[1]/@href').get()
            
            yield scrapy.Request(url=url, callback=self.parse_product)


    def parse_product(self, response):
        product = Product()
        
        product["name"] = response.xpath('//h1/text()').get()
        product["price"] = response.xpath('//p[@class = "price"]/span/span/text()').get() + response.xpath('//p[@class = "price"]/span/text()').get()
        product["description"] = response.xpath('//div[contains(@class, "short-description")]/p/text()').get()
        product["stock"] = response.xpath('//p[contains(@class, "stock")]/text()').get()


        yield (product)
