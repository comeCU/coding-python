#!/usr/bin/env python
# -*- coding:utf-8 -*-

# @File    : test_search.py
# @Time    : 2018/8/5 15:33
# @Author  : dong

'''
search方法，扫描整个字符串，返回 第一个 成功匹配的结果
'''

import re

content = 'Extra stings Hello 1234567 World_This is a Regex Demo Extra stings'
# result = re.match('Hello.*(\d+).*?Demo', content)
# print(result.group())

result = re.search('Hello.*(\d+).*?Demo', content)
print(result.group())

# 测试提取歌手和歌名
html = '''<div id="songs-list">
    <h2 class="title">经典老歌</h2>
    <p class="introduction">
        经典老歌列表
    </p>
    <ul id="list" class="list-group">
        <li data-view="2">一路上有你</li>
        <li data-view="7">
            <a href="/2.mp3" singer="任贤齐">沧海一声笑</a>
        </li>
        <li data-view="4" class="active">
            <a href="/3.mp3" singer="齐秦">往事随风</a>
        </li>
        <li data-view="6"><a href="/4.mp3" singer="beyond">光辉岁月</a></li>
        <li data-view="5"><a href="/5.mp3" singer="陈慧琳">记事本</a></li>
        <li data-view="5">
            <a href="/6.mp3" singer="邓丽君"><i class="fa fa-user"></i>但愿人长久</a>
        </li>
    </ul>
</div>'''

result2 = re.search('<li.*?active.*?singer="(.*?)">(.*?)</a>', html, re.S)  # re.S 匹配换行符
if result2:     # 返回一个匹配对象
    print(result2.group(1), result2.group(2))
# 去掉class中的active
result3 = re.search('<li.*?singer="(.*?)">(.*?)</a>', html, re.S)
if result3:
    print(result3.group(1), result3.group(2))   # 返回第一个匹配正确的结果

# 语法 if 对象 返回True
if 'ddd':
    print(True)

# 去掉re.S
result4 = re.search('<li.*?singer="(.*?)">(.*?)</a>', html)
if result4:
    print(result4.group(1), result4.group(2))


