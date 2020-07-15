# -*- coding: utf-8 -*-
import scrapy
from amazon.items import AmazonItem


class amazonproductinfoSpider(scrapy.Spider):
    name = 'amazonproductinfo'
    allowed_domains = ['amazon.com']
    start_urls = ['https://www.amazon.com/Best-Sellers-Electronics/zgbs/electronics/ref=zg_bs_nav_0']
  
        
    def parse(self, response):
        item = response.css("span.zg-item").css("a.a-link-normal::attr(href)").extract()
        price = response.css("span.p13n-sc-price::text").extract()
        
        yield {
            'item': item,
            'price': price,
            }
      
        
