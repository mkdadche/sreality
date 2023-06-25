import scrapy

class Sreality_spider(scrapy.Spider):
    name = 'sreality_spider'
    start_urls = ['https://www.sreality.cz/hledani/prodej/byty']

    def parse(self, response):
        property = response.css(".property")
        print(f"************{len(property)=}***************")
        # for title in response.css('.property'):
        #     yield {'title': title.css('::text').get() }
    