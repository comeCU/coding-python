#!/usr/bin/env python
# -*- coding:utf-8 -*-

# @File    : spider_test_selenium.py
# @Time    : 2018/8/2 23:03
# @Author  : dong

'''
测试火狐浏览器驱动geckodriver
selenium切换和定位iframe
模拟登陆QQ空间
'''

from selenium import webdriver
from bs4 import BeautifulSoup
import time

driver = webdriver.Firefox()

# 登录QQ空间
def login_qzone():
    driver.get("https://qzone.qq.com/")
    time.sleep(5)
    try:
        driver.find_element_by_id('login_div')
        a = True
    except:
        a = False
    if a == True:
        driver.switch_to.frame('login_frame')  # 切换到iframe

        pages = driver.page_source  # 获取iframe中的内容
        soup = BeautifulSoup(pages, 'lxml')
        print(soup)

        # title = driver.find_element_by_id('title_0')
        # print(title.text)

        driver.find_element_by_id('switcher_plogin').click()    # 点击账号密码登录
        driver.find_element_by_id('u').click()  # 选择用户名框
        driver.find_element_by_id('u').send_keys("***")  # 本人QQ号
        driver.find_element_by_id('p').click()  # 选择密码框
        driver.find_element_by_id('p').send_keys("***")     # 本人QQ登录密码

        driver.find_element_by_id('login_button').click()   # 点击登录
        time.sleep(3)

    driver.implicitly_wait(3)   # 隐式地等待一个无素被发现或一个命令完成

    print("=============OK============")

    # driver.switch_to.default_content()  # 切到主文档
    # driver.switch_to.frame(driver.find_element_by_id('login_frame'))   # 通过id切到iframe
    # driver.switch_to.frame(driver.find_elements_by_tag_name("iframe")[0]) # 通过iframe的index切换

    # driver.close()    # 关闭浏览器窗口
    driver.quit()   # 关掉驱动和相应窗口


if __name__ == '__main__':
    login_qzone()