# -*- coding: utf-8 -*-
import scrapy
from w3lib.url import add_or_replace_parameter
from scrapy.utils.response import open_in_browser

from tripadvisor_restaurants_paraguay.items import RestaurantItemLoader


class RestaurantsSpider(scrapy.Spider):
    name = "restaurants"
    allowed_domains = ["tripadvisor.com"]
    start_urls = (
        'https://www.tripadvisor.com/Restaurants-g294079-Paraguay.html',
    )

    def parse(self, response):
        # open_in_browser(response)
        for restaurant in response.css('.shortSellDetails'):
            il = RestaurantItemLoader(selector=restaurant)
            il.add_css('name', '.property_title::text')
            il.add_css('url', '.property_title::attr(href)')
            il.add_css('cuisines', '.cuisine::text')
            yield il.load_item()

        pagination_url = (
            'https://www.tripadvisor.com/RestaurantSearch?Action=PAGE'
            '&geo=294079&ajax=1&sortOrder=popularity&o=a0'
            '&availSearchEnabled=false'
        )
        if not response.css('.nav.next.disabled'):
            offset = response.meta.get('offset', 0) + 30
            pagination_url = add_or_replace_parameter(
                pagination_url, 'o', 'a{}'.format(offset))
            yield scrapy.Request(pagination_url, meta={'offset': offset})
