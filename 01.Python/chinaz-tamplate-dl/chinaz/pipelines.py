# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import scrapy
import os
from scrapy.pipelines.images import ImagesPipeline
from scrapy.pipelines.files import FilesPipeline
import re
from scrapy.exceptions import DropItem


class MyFilesPipeline(FilesPipeline):
    def get_media_requests(self, item, info):
        for url in item["file_urls"]:
            yield scrapy.Request(url)

    def file_path(self, request, response=None, info=None):
        """
        重命名模块
        """
        path = os.path.join('D:\download',  ''.join( [request.url.replace('http://xmlt.sc.chinaz.com/Files/DownLoad/', '').replace('/', '_').replace(':', '_').replace('__', '_')]))
        return path
    pass


class MyImagesPipeline(ImagesPipeline):
    def get_media_requests(self, item, info):
        for url in item["image_urls"]:
            yield scrapy.Request(url)

    def file_path(self, request, response=None, info=None):
        """
        重命名模块
        """
        path = os.path.join('D:\download',  ''.join([request.url.replace('http://pic.sc.chinaz.com/files/pic/', '').replace('http://pic1.sc.chinaz.com/files/pic/', '').replace('http://pic2.sc.chinaz.com/files/pic/', '').replace('/', '_').replace(':', '_').replace('__', '_')]))
        return path
    pass
