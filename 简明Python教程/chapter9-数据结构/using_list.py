# filename: using_list.py
# 使用列表

#this is my shopping list
shoplist = ['apple', 'mango', 'carrot', 'banana']

print('I have', len(shoplist), 'item to purchase.')

print('These items are:')
for item in shoplist:
      print(item, end=' ')  #消除print自动换行

print('\nI alse have to buy rice.')
shoplist.append('rice')
print('My shopping list is now', shoplist)

print('I will sort my list mow')
shoplist.sort() #根据字母排序
print('Sorted shopping lsit is', shoplist)

print('The first item I will buy is', shoplist[0])
olditem = shoplist[0]
del shoplist[0] #删除第一个元素
print('I bought the', olditem)
print('My shopping list is now', shoplist)
