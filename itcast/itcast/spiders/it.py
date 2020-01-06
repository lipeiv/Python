# -*- coding: utf-8 -*-
import scrapy


class ItSpider(scrapy.Spider):
    name = 'it'
    allowed_domains = ['itcast.cn']
    start_urls = ['http://www.itcast.cn/channel/teacher.shtml#ajavaee']

    def parse(self, response):
        print(response.xpath('//div[@class="li_txt"]/h3/text()').extract())
        pass
