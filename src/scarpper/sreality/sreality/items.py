import scrapy


class PropertyItem(scrapy.Item):
    title = scrapy.Field()
    locality = scrapy.Field()
    images_url = scrapy.Field()
