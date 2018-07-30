#!/usr/bin/env python
# filename : pickling.py
# 环境python3.5.2，序列化 反序列化

import pickle as p

shoplistfile = 'shoplist.data'

shoplist = ['apple', 'mango', 'carrot']

# 写文件
f = open(shoplistfile,'wb')
p.dump(shoplist, f) # 序列化
f.close()

del shoplist

# 读文件
f = open(shoplistfile, 'rb')
storedlist = p.load(f)  # 反序列化
print(storedlist)


# 输出
'''
['apple', 'mango', 'carrot']
'''
