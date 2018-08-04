#!/usr/bin/env python
# -*- coding:utf-8 -*-

# @File    : test_pymysql.py
# @Time    : 2018/8/3 23:28
# @Author  : dong

'''
测试数据库连接pymysql
数据库：toutiao
表：data
建表语句：
CREATE TABLE `data` (
    `title` varchar(200) DEFAULT NULL,
    `img_url` varchar(100) DEFAULT NULL,
    `url` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8'
'''

import requests
import json
import pymysql

# 建立一个MySQL连接
conn = pymysql.connect(host='localhost', port=3306, user='root', password='***',
                       db='toutiao', charset='utf8')
print('连接成功')
# 创建一个游标
cursor = conn.cursor()

# 从网页响应中找到 JS 脚本返回的 JSON 数据：Network --> XHR --> Preview 查看ajax返回的数据
url = "https://www.toutiao.com/api/pc/focus/"
wbdata = requests.get(url).text

# 对响应的数据json化
data = json.loads(wbdata)
# 索引到新闻数据的位置
news = data['data']['pc_feed_focus']

# 遍历和提取
for n in news:
    title = n['title']
    url = "https://www.toutiao.com" + n['display_url']
    image_url = "https:" + n['image_url']
    print("标题：%s URL:%s 图片url：%s" % (title, url, image_url))
    cursor.execute("INSERT INTO data(title,img_url,url)VALUES('{0}','{1}','{2}');".format(title, image_url, url))
    conn.commit()  # 提交执行

# 关闭连接
cursor.close()
conn.close()
