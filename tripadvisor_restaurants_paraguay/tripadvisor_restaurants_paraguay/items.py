# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from urlparse import urljoin

import scrapy
from scrapy.loader import ItemLoader
from scrapy.loader.processors import TakeFirst, Identity, MapCompose


class Restaurant(scrapy.Item):
    url = scrapy.Field(
        input_processor=MapCompose(
            lambda url: urljoin('https://www.tripadvisor.com', url)
        )
    )
    name = scrapy.Field(
        input_processor=MapCompose(
            unicode.strip
        )
    )
    cuisines = scrapy.Field(output_processor=Identity())
    phone = scrapy.Field()
    locality = scrapy.Field()


class RestaurantItemLoader(ItemLoader):
    default_item_class = Restaurant
    default_output_processor = TakeFirst()
