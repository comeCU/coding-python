#!/usr/bin/env python
# -*- coding:utf-8 -*-

# @File    : spider_toutiao_js.py
# @Time    : 2018/8/1 13:14
# @Author  : dong

'''
爬取今日头条的“推荐”栏的URL、标题、图片url
'''

import requests
import json

url = "https://www.toutiao.com/api/pc/focus/"
wbdata = requests.get(url).text

# 对响应的数据json化
data = json.loads(wbdata)
# 索引到新闻数据的位置
news = data['data']['pc_feed_focus']

# 遍历和提取
for n in news:
    title = n['title']
    url = "https://www.toutiao.com" + n['display_url']
    image_url = "https:" + n['image_url']
    print("标题：%s URL:%s 图片url：%s" % (title, url, image_url))
