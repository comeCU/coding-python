#!/usr/bin/env python
# -*- coding:utf-8 -*-

# @File    : test_urllib_request_get.py
# @Time    : 2018/8/4 17:40
# @Author  : dong

'''
发送请求
1.利用urlopen方法，完成简单网页的GET请求抓取

'''

import urllib.request
# urlopen方法
response = urllib.request.urlopen('https://www.python.org')
# 输出网页源代码
print(response.read().decode('utf-8'))

# 获取response类型
print(type(response))

print(response.status)  # 返回状态码
print(response.getheaders())    # 返回头信息
print(response.getheader('Server'))  # 调用 getheader() 方法并传递一个参数 Server 获取了 headers 中的 Server 值


