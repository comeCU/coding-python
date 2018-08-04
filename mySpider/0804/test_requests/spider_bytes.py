#!/usr/bin/env python
# -*- coding:utf-8 -*-

# @File    : spider_bytes.py
# @Time    : 2018/8/4 22:30
# @Author  : dong

'''
抓取二进制文件
获取GitHub图标
'''

import requests

url = 'https://github.com/favicon.ico'
r = requests.get(url)

with open('favicon.ico', 'wb') as f:
    f.write(r.content)  # 写入文件

# print(r.text)
# print(r.content)
