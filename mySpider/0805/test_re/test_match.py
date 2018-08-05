#!/usr/bin/env python
# -*- coding:utf-8 -*-

# @File    : test_match.py
# @Time    : 2018/8/5 11:22
# @Author  : dong

'''
re库的match匹配方法
正则表达式学习：
    1.python3网络爬虫开发实战: https://germey.gitbooks.io/python3webspider/3.3-%E6%AD%A3%E5%88%99%E8%A1%A8%E8%BE%BE%E5%BC%8F.html
    2.廖雪峰的官方网站：https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/00143193331387014ccd1040c814dee8b2164bb4f064cff000
'''

import re

content = 'Hello 123 world_This is a Regex demo'
print(len(content))
result = re.match('^Hello\s(\d{3})\s(\w{10})', content)

print(result)
print(result.group())
print(result.group(1))  # 将数字部分的正则表达式用(), 调用group(index)输出匹配结果
print(result.group(2))
print(result.span())

# 通用匹配 .*(点星) 匹配所有字符
result2 = re.match('^Hello.*Regex', content)
print(result2.group())

# 贪婪匹配 .* 与 非贪婪匹配 .*?
result3 = re.match('He.*(\d+).*demo', content)  # 贪婪匹配
print(result3.group(1))

result4 = re.match('He.*?(\d+).*demo', content)
print(result4.group(1))  # 非贪婪匹配

# 修饰符
content2 = '''Hello 123 world_This 
is a Regex demo'''
result5 = re.match('He.*(\d+).*?demo', content2, re.S)  # re.S 它的作用是使 .(点)匹配包括换行符在内的所有字符
print(result5.group(1))

# 转义匹配
content3 = '(百度)www.baidu.com'
result6 = re.match('\(百度\)www\.baidu\.com', content3)
print(result6)


