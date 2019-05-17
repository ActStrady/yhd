#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# @Time : 2019/5/16 17:20
# @Author : ActStrady@tom.com
# @FileName : start.py
# @GitHub : https://github.com/ActStrady/scrapy_learn
from scrapy import cmdline

cmdline.execute("scrapy crawl iphone -o iphone.csv".split())
