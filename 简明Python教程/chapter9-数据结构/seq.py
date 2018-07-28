#!/usr/bin/env python
# filename : seq.py
# 序列

shoplist = ['apple', 'mango', 'carrot', 'banana']

#Indexing or Subscription operation
print('Item 0 is', shoplist[0])
print('Item 1 is', shoplist[1])
print('Item -1 is', shoplist[-1])
print('Item -2 is', shoplist[-2])

# Slicing on a list
print('Item 1 to 3 is', shoplist[1:3])
print('Item 2 to end is', shoplist[2:]) # 输出 Item 2 to end is ['carrot', 'banana']
print('Item 1 to -1 is', shoplist[1:-1]) # 输出 Item 1 to -1 is ['mango', 'carrot']
print('Item start to end is', shoplist[:])

# Slicing on a string
name = 'swaroop'
print('characters 1 to 3 is', name[1:3])
print('characters 1 to -2 is', name[1:-2]) # 输出 characters 1 to -2 is waro
