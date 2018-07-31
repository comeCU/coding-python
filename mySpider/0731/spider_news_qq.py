#!/usr/bin/env python
# -*- coding:utf-8 -*-

# @File    : spider_news_qq.py
# @Time    : 2018/7/31 10:53
# @Author  : dong

'''
爬取腾讯新闻标题和链接，并存入txt文件
'''

import requests
from bs4 import BeautifulSoup

# 请求腾讯新闻的URL 获取其文本
url = "http://news.qq.com/"
wbdata = requests.get(url).text

# 对获取到的文本解析
soup = BeautifulSoup(wbdata, 'lxml')    # lxml库需要安装 https://www.lfd.uci.edu/~gohlke/pythonlibs/#lxml

# 从解析文件中通过select选择器定位指定的元素，返回一个列表
news_titles = soup.select("div.text > em.f14 > a.linkto")

# 对返回的链表进行遍历
i = 1   # 标记序号
for n in news_titles:
    # 提取出标题和链接信息
    title = n.get_text()
    link = n.get("href")
    data = {
        '序号': i,
        '标题': title,
        '链接': link
    }
    i = i + 1   # 序号+1

    f = open('save.txt', 'a', encoding='utf-8')   # 以追加模式写入
    toStr = str(data)   # 将字典转换为字符串
    f.write(toStr+"\n")

f.close()
print('获得%d条数据' % (i-1))
    # print(data)
