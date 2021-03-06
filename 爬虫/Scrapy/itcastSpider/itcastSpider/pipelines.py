# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

# class ItcastspiderPipeline(object):
#     def process_item(self, item, spider):
#         return item
import json


class ItcastPipeline(object):
    #可选初始化方法
    def __init__(self):
        self.filename = open('teacher.json', 'w')

    #必选 出来返回来的数据
    def process_item(self, item, spider):
        jsontext = json.dumps(dict(item), ensure_ascii=False) + '\n'
        self.filename.write(jsontext)
        return item

    #可选 结束时调用
    def close_spider(self, spider):
        self.filename.close()