# filename : func_global.py
# 全局变量

def func():
    global x #global语句，表明变量是在外面的块定义的

    print('x is', x)
    x = 2
    print('Change local x to', x)

x = 50
func()
print('Value of x is', x)


#输出
'''
x is 50
Change local x to 2
Value of x is 2

'''
