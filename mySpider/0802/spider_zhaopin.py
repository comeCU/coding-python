#!/usr/bin/env python
# -*- coding:utf-8 -*-

# @File    : spider_zhaopin.py
# @Time    : 2018/8/1 17:46
# @Author  : dong

'''
爬取智联招聘信息
    1.网站：https://www.zhaopin.com/
    2.输入关键字：java
    3.从网页响应中找到 JS 脚本返回的 JSON 数据：Network --> XHR --> Preview 查看ajax返回的数据
Issues:
    0.同名文件第二遍运行写入会乱码
    1.大量数据重复
'''

import requests
import json
from multiprocessing import Pool
import codecs


def get_zhaopin(page):
    url = "https://fe-api.zhaopin.com/c/i/sou?pageSize=60&cityId=489&workExperience=-1&education=-1&companyType=-1&emp+\
    loymentType=-1&jobWelfareTag=-1&kw=java&kt=3&lastUrlQuery=%7B+\
    %22p%22:{0},%22jl%22:%22489%22,%22kw%22:%22java%22,%22kt%22:%223%22%7D".format(page)    # 翻页后更新链接
    print("第{0}页".format(page))     # 0 描述：占位符，如果可能，填充位

    wbdata = requests.get(url).text

    data = json.loads(wbdata)

    # 招聘信息总数
    global news_count
    news_count = data['data']['numFound']
    # 总页数
    global pages
    pages = (news_count // 62) + 1
    # print(news_count)
    # print(pages)

    news = data['data']['results']

    for n in news:
        job_name = n['jobName']
        job_salary = n['salary']
        job_company = n['company']['name']
        job_time = n['updateDate']

        # f = open('zhaopin.csv', 'a', encoding='utf-8')
        # 这里表示把intimate.txt文件从utf-8编码转换为unicode，就可以对其进行unicode读写了
        # 参考博客：https://www.cnblogs.com/shengulong/p/7097869.html
        f = codecs.open('zp.csv', 'a', encoding='utf-8')
        toStr = str(job_name + "\t" + job_salary + "\t" + job_company + "\t" + job_time)
        f.write(toStr+"\n")

    f.close()


'''
当.py文件被直接运行时，if __name__ == '__main__'之下的代码块将被运行；
当.py文件以模块形式被导入时，if __name__ == '__main__'之下的代码块不被运行
'''
if __name__ == '__main__':
    pool = Pool(processes=6)
    # 加载函数，让全局变量pages获得值
    # 参考：https://stackoverflow.com/questions/14751688/nameerror-global-name-name-is-not-defined
    get_zhaopin(0)
    pool.map_async(get_zhaopin, range(2, pages + 1))  # 爬取2~end页招聘信息，该网站招聘信息第一页链接格式与其他不一致（反爬虫）
    pool.close()
    pool.join()
    print("总数据%s条" % news_count)