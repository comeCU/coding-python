# filename : func_local.py
# 局部变量

def func(x):
    print('x is', x)
    x = 2
    print('Change local x to', x)

x = 50
func(x)
print('x is still', x)

# 输出
'''
x is 50
Change local x to 2
x is still 50

'''
