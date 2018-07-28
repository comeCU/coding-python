# filename : func_key.py
# 使用关键参数

def func(a, b=5, c=10):
    print('a is', a, 'and b is', b, 'and c is', c)

func(3, 7)
func(25, c=14)
func(c=199, a=353)


#输出
'''
a is 3 and b is 7 and c is 10
a is 25 and b is 5 and c is 14
a is 353 and b is 5 and c is 199
'''
