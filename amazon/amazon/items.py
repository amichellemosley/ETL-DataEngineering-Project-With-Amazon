# -*- coding: utf-8 -*-
import scrapy


class AmazonItem(scrapy.Item):
    item = scrapy.Field()
    price = scrapy.Field()
    pass
