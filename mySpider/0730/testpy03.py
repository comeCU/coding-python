#!/usr/bin/env python
# -*- coding:utf-8 -*-

# @File    : testpy03.py
# @Time    : 2018/7/30 15:42
# @Author  : dong

'''
我的第一个python爬虫
'''

import urllib.request
response = urllib.request.urlopen("http://www.baidu.com")
html = response.read()
html = html.decode('utf-8')
print(html)