#!/usr/bin/env python
# -*- coding:utf-8 -*-

# @File    : test_urllib_request_post.py
# @Time    : 2018/8/4 17:58
# @Author  : dong

'''
1.POST请求
2.请求超时，抛出异常
'''

import urllib.parse
import urllib.request
import socket
import urllib.error

data = bytes(urllib.parse.urlencode({'word': 'hello'}), encoding='utf8')
response = urllib.request.urlopen("http://httpbin.org/post", data=data)  # data在form字段中
print(response.read().decode('utf-8'))

# response = urllib.request.urlopen("http://httpbin.org/get", timeout=0.1)
# # 返回urllib.error模块信息：urllib.error.URLError: <urlopen error timed out>
# print(response.read())

try:
    response = urllib.request.urlopen("http://httpbin.org/get", timeout=0.1)
except urllib.error.URLError as e:
    if isinstance(e.reason, socket.timeout):
        print('TIME OUT')

