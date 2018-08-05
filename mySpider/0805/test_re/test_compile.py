#!/usr/bin/env python
# -*- coding:utf-8 -*-

# @File    : test_compile.py
# @Time    : 2018/8/5 17:17
# @Author  : dong

'''
compile() 方法将正则表达式编译成一个正则表达式对象，以便复用
'''

import re

content1 = '2016-12-15 12:00'
content2 = '2016-12-17 12:55'
content3 = '2016-12-22 13:21'

# 编译成一个对象
pattern = re.compile('\d{2}:\d{2}')

result1 = re.sub(pattern, '', content1)
result2 = re.sub(pattern, '', content2)
result3 = re.sub(pattern, '', content3)

print(result1, result2, result3)