# filename: func_default.py
'''
使用默认参数值
 只有在形参表末尾的那些参数可以有默认参数值，
 即你不能在声明函数形参的时候，先声明有默认值的形参而后声明没有默认值的形参。
'''
def say(message, times = 1):   
    print(message * times)

say('hello')
say('world', 5)


#输出
'''
hello
worldworldworldworldworld
'''


