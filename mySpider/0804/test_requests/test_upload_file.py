#!/usr/bin/env python
# -*- coding:utf-8 -*-

# @File    : test_upload_file.py
# @Time    : 2018/8/4 22:57
# @Author  : dong

'''
测试上传文件
网站会返回一个Response,里面包含files字段
'''

import requests

url = 'http://httpbin.org/post'
files = {'file': open('favicon.ico', 'rb')}  # 读二进制数据
r = requests.post(url, files=files)
print(r.text)

