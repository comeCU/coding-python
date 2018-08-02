#!/usr/bin/env python
# -*- coding:utf-8 -*-

# @File    : testPage1.py
# @Time    : 2018/8/1 21:42
# @Author  : dong

'''
爬取智联招聘第一页招聘信息
'''

import requests
import json

# 从网页响应中找到 JS 脚本返回的 JSON 数据
url = "https://fe-api.zhaopin.com/c/i/sou?pageSize=60&cityId=765&workExperience=-1&education=-1&" \
      "companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=java&kt=3&lastUrlQuery=%7B%22jl%22:%22765%22," \
      "%22kw%22:%22java%22,%22kt%22:%223%22%7D"

wbdata = requests.get(url).text

data = json.loads(wbdata)

# 招聘信息总数
news_count = data['data']['numFound']

news = data['data']['results']
i = 0
for n in news:
    job_name = n['jobName']
    job_salary = n['salary']
    job_company = n['company']['name']
    job_time = n['updateDate']
    i = i + 1
    print(job_name, job_salary, job_company, job_time)

print("总招聘信息%s" %(news_count))
print("共爬取%s条数据" % (i))