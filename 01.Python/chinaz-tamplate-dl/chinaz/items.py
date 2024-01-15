# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TemplateListItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    url = scrapy.Field()
    title = scrapy.Field()
    link = scrapy.Field()
    pass


class TemplateItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()
    img = scrapy.Field()
    download_link = scrapy.Field()
    pass


class PageItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    current_page = scrapy.Field()
    next_page_link = scrapy.Field()
    pass


class MyFileItem(scrapy.Item):
    image_urls = scrapy.Field()
    images = scrapy.Field()
    image_name = scrapy.Field()
    file_urls = scrapy.Field()
    files = scrapy.Field()
    file_name = scrapy.Field()
    pass

