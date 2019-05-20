# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from util import mysql_util
from scrapy import Request
from scrapy.pipelines.images import ImagesPipeline


class YhdPipeline(object):
    def open_spider(self, spider):
        # 获取mysql连接
        self.db_conn = mysql_util.get_mysql_connect()
        # 获取mysql游标
        self.db_cursor = self.db_conn.cursor()
        self.db_cursor.execute('truncate yhd.iphone')

    def process_item(self, item, spider):
        sql = '''
            insert into yhd.iphone(name, price, praise, store_name, image_url)
            values(%s,%s,%s,%s,%s)
        '''
        iphone = (item['name'], item['price'], item['praise'], item['store_name'], item['image_url'])
        self.db_cursor.execute(sql, iphone)
        return item

    # 爬虫全部完成后执行一次（收尾工作）
    def close_spider(self, spider):
        self.db_conn.commit()
        self.db_cursor.close()
        self.db_conn.close()


class YhdPipelineImage(ImagesPipeline):
    # 生成下载图片的request
    def get_media_requests(self, item, info):
        return [Request('http:' + x) for x in item.get(self.images_urls_field, [])]

    # 指定文件名和存的父目录
    def file_path(self, request, response=None, info=None):
        # 图片名
        image_name = request.url.split("/")[-1]
        # 组目录
        return '/%s' % image_name
