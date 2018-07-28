#!/usr/bin/env python
# filename: reference.py
# 对象与参考

# 同一个对象的引用
shoplist = ['apple', 'mango', 'carrot', 'banana']
mylist = shoplist   # mylist is just another name pointing to the same object!

del shoplist[0]

print('Shoplist is', shoplist)
print('mylist is', mylist)

# 输出
'''
Shoplist is ['mango', 'carrot', 'banana']
mylist is ['mango', 'carrot', 'banana']
'''

# 使用切片操作符取得拷贝
mylist = shoplist[:]    # make a copy by doing a full slice
del mylist[0]

print('shoplist is', shoplist)
print('mylist is', mylist)

# 输出
'''
shoplist is ['mango', 'carrot', 'banana']
mylist is ['carrot', 'banana']
'''
