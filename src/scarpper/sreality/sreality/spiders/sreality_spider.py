import scrapy
from scrapy_selenium import SeleniumRequest
import json
import datetime
import time

from ..items import PropertyItem

class SrealitySpider(scrapy.Spider):
    name = 'sreality_spider'
    allowed_domains = ['sreality.cz']

    tms = int(time.time())

    
    num_items = 500
   
    start_urls = [f"https://www.sreality.cz/api/cs/v2/estates?category_main_cb=1&category_type_cb=1&per_page={num_items}&tms={tms}"]
   
    def parse(self, response):
        jsonresponse = json.loads(response.text)
        properties_list = jsonresponse["_embedded"]["estates"]
        image_filter = "?fl=res,749,562,3|wrm,/watermark/sreality.png,10|shr,,20|jpg,90"
        for property in properties_list:
            property_item = PropertyItem()
            property_item["title"] = property["name"]
            property_item["locality"] = property["locality"]    
            images_response = property["_links"]["images"]
            images = []
            for image in images_response:
                image_url = image["href"]
                image_url = image_url.split("?")
                
                image_url = image_url[0] + image_filter
                images.append(image_url)

            property_item["images_url"] = images
            yield property_item


# image_filter = "?fl=res,749,562,3|wrm,/watermark/sreality.png,10|shr,,20|jpg,90"

# image_filter_big = "?fl=res,1920,1080,1|wrm,/watermark/sreality.png,10|shr,,20|jpg,90"

