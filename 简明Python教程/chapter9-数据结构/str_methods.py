#!/usr/bin/env python
# filename: str_methods.py
# 字符串的方法

name = 'Swaroop'

if name.startswith('Swa'):
    print('Yes, the string starts with "Swa"')

if 'a' in name:
    print('Yes, it contains the string "a"')

if name.find('war') != -1:  # 没有找到返回-1
    print('Yes, it contains the string "war"')

delimiter = '_*_'
mylist = ['china', 'us', 'india', 'japain']
print(delimiter.join(mylist)) # 分隔符


# 输出
'''
Yes, the string starts with "Swa"
Yes, it contains the string "a"
Yes, it contains the string "war"
china_*_us_*_india_*_japain
'''
