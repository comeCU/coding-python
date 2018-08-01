#!/usr/bin/env python
# -*- coding:utf-8 -*-

# @File    : spider_cookie_zhihu.py
# @Time    : 2018/7/31 17:59
# @Author  : dong

'''
比较登录状态和未登录状态爬取知乎主页question标题和链接
Issues：
    1.未实现翻页功能，所以只能获取到几条信息
'''

import requests
from bs4 import BeautifulSoup
# 未登录状态cookie
cookie = '''_zap=ce740454-216b-4eb6-9bd7-a2fef706cfaf; d_c0="ALAvZvA-jA2PTpemhJp0aJpamXT2a01JAN0=|1525530039"; q_c1=f6083d98be554d859a9cf0415030e1ce|1530694849000|1517637965000; _xsrf=LEUU226iZ8ollNKJaiQpnmKiRm4FlUWr; l_n_c=1; l_cap_id="MWU2NzVkNmExNGZhNGIxZTk1ODk3Y2Q3NjM2YmFhZGU=|1533029270|d86e00a3dde76f1305e81256c65a48cc0060e043"; r_cap_id="ZjdjNDhhODRiNTk2NDJjNzhlYTQ0ZDU3ZmY0NjhmOWE=|1533029270|b0e1155953fc02487acf434356f5cefba6c43359"; cap_id="NjgxYjE5ODM1NGE5NDA1YzllNTFkYmZkYzdjNGVkMzY=|1533029270|f188fe908efc57122f082816773a260445530f82"; __utma=51854390.1916852744.1532530658.1533027374.1533029612.8; __utmc=51854390; __utmz=51854390.1533029612.8.8.utmcsr=zhihu.com|utmccn=(referral)|utmcmd=referral|utmcct=/collection/209648090; __utmv=51854390.000--|2=registration_date=20170201=1^3=entry_date=20180203=1; n_c=1; capsion_ticket="2|1:0|10:1533030003|14:capsion_ticket|44:ODFiZDZlMDBiZDI0NDU5MjliNmJiOTMzZTQyYzhhOTI=|32d5f5923e2e2ce81093e98435c2203ee9f5d5cd22663c34017c464372fe4014"; tgw_l7_route=53d8274aa4a304c1aeff9b999b2aaa0a'''

# 登录状态下的cookie，需要换成自己登录后的cookie
# cookie = ''' '''

# 模拟浏览器登录
header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36',
    'Connection': 'keep-alive',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Cookie': cookie
}

url = "https://www.zhihu.com/"
wbdata1 = requests.get(url, headers=header).text

soup = BeautifulSoup(wbdata1, 'lxml')
print(soup)

# 从解析文件中通过select选择器定位指定的元素，返回一个列表
question_titles = soup.select("h2 > div > a")   # 可在network右键copy中selector确定位置

for n in question_titles:
    title = n.get_text()
    link = "https://www.zhihu.com" + n.get("href")
    data = {
        '标题': title,
        '链接': link
    }
    print(data)
