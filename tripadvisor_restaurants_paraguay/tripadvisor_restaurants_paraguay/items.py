# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader.processors import TakeFirst


class Restaurant(scrapy.Item):
    url = scrapy.Field()
    name = scrapy.Field()
    cuisines = scrapy.Field()
    phone = scrapy.Field()
    locality = scrapy.Field()


class RestaurantItemLoader(scrapy.ItemLoader):
    default_item_class = Restaurant
    default_output_processor = TakeFirst()
