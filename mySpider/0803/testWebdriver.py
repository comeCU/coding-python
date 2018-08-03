#!/usr/bin/env python
# -*- coding:utf-8 -*-

# @File    : testWebdriver.py
# @Time    : 2018/8/2 21:19
# @Author  : dong

'''
测试浏览器驱动
'''

from selenium import webdriver
from bs4 import BeautifulSoup

brower = webdriver.Firefox()

brower.get("https://www.baidu.com")
pages = brower.page_source
soup = BeautifulSoup(pages, 'lxml')

print(soup)

brower.close()
brower.quit()