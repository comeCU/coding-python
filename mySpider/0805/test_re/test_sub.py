#!/usr/bin/env python
# -*- coding:utf-8 -*-

# @File    : test_sub.py
# @Time    : 2018/8/5 16:28
# @Author  : dong

'''
文本替换
'''

import re

content = '54aK54yr5oiR54ix5L2g'
new_content = re.sub('\d+', "", content)
print(new_content)

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

# 直接用正则表达式提取
results = re.findall('<li.*?>\s*?(<a.*?>)?(\w+)(</a>)?\s*?</li>', html, re.S)   # \s*? 匹配缩进多个空格
for result in results:
    # print(result[0], result[1], result[2])
    print(result[1])

# 先用sub去除a标签
new_html = re.sub('<a.*?>|</a>|<i.*?>|</i>', '', html)  # 只剩下li标签和歌名
print(new_html)
results2 = re.findall('<li.*?>(.*?)</li>', new_html, re.S)
for result2 in results2:
    # print(result2)
    print(result2.strip())  # strip方法：移除字符串头尾指定的字符（默认为空格或换行符）或字符序列

