#!/usr/bin/env python
# -*- coding:utf-8 -*-

# @File    : http_request.py
# @Time    : 2018/7/31 10:40
# @Author  : dong

import requests
url = "https://zmister.com/"
data = requests.get(url)
# 输出请求的状态码
print(data.status_code)
# 输出响应的主体内容，未经解码和解析
print(data.content)