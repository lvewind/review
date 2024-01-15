# -*- coding: UTF-8 -*-

import scrapy
from chinaz.items import TemplateListItem, TemplateItem, PageItem, MyFileItem


class ChinazSpider(scrapy.spiders.Spider):
    name = "chinaz"
    allowed_domains = ["chinaz.com"]

    start_urls = [
        "http://sc.chinaz.com/moban/"
    ]

    def parse(self, response):
        page_number_list = response.xpath("//div[@class='fenye']/a[@class='active']/b/text()").extract()
        page_number = int(page_number_list[0])
        if page_number == 1:
            url = ChinazSpider.start_urls[0]
            page_number += 1
            yield scrapy.Request(url, callback=self.parse_list)
        while page_number < 120:
                url = ChinazSpider.start_urls[0] + "index_" + str(page_number) + ".html"
                page_number += 1
                yield scrapy.Request(url, callback=self.parse_list)

    def parse_list(self, response):
        for href in response.xpath("//div[@id='container']/div/div/a/@href"):
            url = response.urljoin(href.extract())
            yield scrapy.Request(url, callback=self.parse_template)

    def parse_template(self, response):
        template = MyFileItem()
        template['image_name'] = response.xpath("//div[@class='imga']/a/@title").extract()
        template['image_urls'] = response.xpath("//div[@class='imga']/a/@href").extract()
        template['file_name'] = response.xpath("//div[@class='imga']/a/@title").extract()
        template['file_urls'] = response.xpath("//div[@class='dian'][a='广东联通下载']/a[3]/@href").extract()
#        print(template)
        yield template
    pass
