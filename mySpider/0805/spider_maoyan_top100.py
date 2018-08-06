#!/usr/bin/env python
# -*- coding:utf-8 -*-

# @File    : spider_maoyan_top100.py
# @Time    : 2018/8/6 8:59
# @Author  : dong

"""
用正则表达式作为解析工具，爬取猫眼电影top100
    猫眼电影：http://maoyan.com/board/4

注：添加文档字符串。三重双引号，回车
    函数说明写在前面三个引号后面
    参数隔行写在后面
    参考Google python风格指南：
    http://zh-google-styleguide.readthedocs.io/en/latest/google-python-styleguide/python_style_rules/#comments
"""

import requests
import re
import json
from requests.exceptions import RequestException
import time


def get_one_page(url):
    """获一个页面的源代码

    :param url: 爬取页面的url
    :return: 如果状态码为200，则返回页面源代码，否则，返回None
    """
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
        return None
    except RequestException:
        return None


def parse_one_page(html):
    """通过正则表达式匹配出信息

    :param html: 网页源代码
    :return:
    """
    # 编译成pattern对象
    pattern = re.compile('<dd>.*?board-index.*?>(.*?)</i>.*?data-src="(.*?)".*?name.*?a.*?>(.*?)</a>.*?\
star.*?>(.*?)</p>.*?releasetime.*?>(.*?)</p>.*?integer.*?>(.*?)</i>.*?fraction.*?>(.*?)</i>.*?</dd>', re.S)

    if pattern:
        items = re.findall(pattern, html)
        for item in items:
            yield {     # 生成器
                'top': item[0],
                'image': item[1],
                'title': item[2],
                'actor': item[3].strip()[3:] if len(item[3]) > 3 else '',
                'time': item[4].strip()[5:] if len(item[4]) > 5 else '',
                'score': item[5].strip() + item[6].strip()
            }


def write_to_file(content):
    """将爬取数据写入文件

    :param content: 提取结果
    :return:
    """
    with open('maoyan_top100.txt', 'a', encoding='utf-8') as f:
        # print(type(json.dumps(content)))    # str
        f.write(json.dumps(content, ensure_ascii=False) + '\n')     # json 库的 dumps() 方法实现字典的序列化


def main(offset):
    """main方法

    :param offset: 偏移量，更新下一页链接
    :return:
    """
    url = 'http://maoyan.com/board/4?offset={0}'.format(offset)
    html = get_one_page(url)
    for item in parse_one_page(html):
        print(item)
        write_to_file(item)


if __name__ == '__main__':
    for i in range(10):     # 分页爬取，共10页，格式0 10 20 30 ……
        main(i * 10)
        time.sleep(1)   # 延时等待，防止抓取过快被反爬虫机制识别
