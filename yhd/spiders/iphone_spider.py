#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# @Time : 2019/5/17 9:38
# @Author : ActStrady@tom.com
# @FileName : iphone_spider.py
# @GitHub : https://github.com/ActStrady/yhd
import time

from scrapy import Spider, Request
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from yhd.items import YhdItem


class IphoneSpider(Spider):
    name = 'iphone'

    # 初始化，定义selenium driver
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        chrome_options = Options()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--disable-gpu')
        # 上面三行代码就是为了将Chrome不弹出界面，实现无界面爬取
        self.driver = webdriver.Chrome(chrome_options=chrome_options)

    def start_requests(self):
        # selenium 请求首页
        self.driver.get('https://www.yhd.com/')
        # 获取输入框
        input_ = self.driver.find_element_by_id('keyword')
        # 清空输入框，输入数据
        input_.clear()
        input_.send_keys('iphone')
        # 输入enter键
        input_.send_keys(Keys.ENTER)
        # 下拉页面
        url = self.driver.current_url
        yield Request(url)

    def parse(self, response):
        item = YhdItem()
        iphone_list = response.xpath("//div[@class='mod_search_pro']")
        for iphone in iphone_list:
            # 名称
            name = iphone.xpath(".//p[@class='proName clearfix']/a/text()").extract()[1].strip()
            item['name'] = name
            # 价格
            price = iphone.xpath(".//em[@class='num']/text()").extract()[1].strip()
            item['price'] = price
            # 好评率
            praise = iphone.xpath(".//span[@class='positiveRatio']/text()").extract_first()
            item['praise'] = praise
            # 店铺名
            store_name = iphone.xpath(".//span[@class='shop_text']/text()").extract_first()
            item['store_name'] = store_name
            # 图片url
            image_url = iphone.xpath(".//div[@class='proImg']/a/img/@src").extract_first()
            if image_url:
                image_url = 'http:' + image_url
            item['image_url'] = image_url
            yield item
        image_urls = iphone_list.xpath(".//div[@class='proImg']/a/img/@src").extract()
        item['image_urls'] = image_urls
        yield item
        # 处理下一页
        next_url = response.xpath("//a[@class='page_next']/@href").extract()
        if next_url:
            # 当前url加上参数url
            next_url = response.urljoin(next_url[0])
            # 关掉过滤
            yield Request(next_url, dont_filter=True)
