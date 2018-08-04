#!/usr/bin/env python
# -*- coding:utf-8 -*-

# @File    : test_urllib_ProxyHandler.py
# @Time    : 2018/8/4 19:13
# @Author  : dong

'''
使用代理
Issue:
    1.[WinError 10061] 由于目标计算机积极拒绝，无法连接。
'''

from urllib.error import URLError
from urllib.request import ProxyHandler, build_opener

# 在此本地搭建了一个代理，运行在 9743 端口上
proxy_handler = ProxyHandler({
    'http': 'http://127.0.0.1:9744',
    'https': 'https://127.0.0.1:9744'
})

opener = build_opener(proxy_handler)

try:
    response = opener.open("https://www.baidu.com")
    print(response.read().decode('utf-8'))
except URLError as e:
    print(e.reason)
