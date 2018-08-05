#!/usr/bin/env python
# -*- coding:utf-8 -*-

# @File    : test_session_getcookies.py
# @Time    : 2018/8/4 23:10
# @Author  : dong

'''
通过session获得cookies
'''

import requests

s = requests.Session()
s.get('http://httpbin.org/cookies/set/number/123456789')
r = s.get('http://httpbin.org/cookies')

print(r.text)