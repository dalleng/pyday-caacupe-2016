# -*- coding: utf-8 -*-
from urlparse import urljoin
import scrapy


class RestaurantsSpider(scrapy.Spider):
    name = "restaurants"
    allowed_domains = ["tripadvisor.com"]
    start_urls = (
        'https://www.tripadvisor.com/Restaurants-g294079-Paraguay.html',
    )

    def parse(self, response):
        # restaurants = soup.find_all('div', class_='shortSellDetails')
        for restaurant in response.css('.shortSellDetails'):
            yield {
                'name': restaurant.css('.property_title::text').extract_first(),
                'url': urljoin(
                    response.url,
                    restaurant.css('.property_title::attr(href)').extract_first()
                ),
                'cuisines': restaurant.css('.cuisine::text').extract()
            }
