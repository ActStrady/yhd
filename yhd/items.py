# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class YhdItem(scrapy.Item):
    # 名称
    name = scrapy.Field()
    # 价格
    price = scrapy.Field()
    # 好评率
    praise = scrapy.Field()
    # 店铺名
    store_name = scrapy.Field()
    # 图片地址
    image_url = scrapy.Field()
    # 默认的图片键
    image_urls = scrapy.Field()
    # 默认的图片结果键
    images = scrapy.Field()
