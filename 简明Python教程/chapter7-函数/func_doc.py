# filename : func_doc.py
# 函数的文档字符串

def printMax(x, y):
    '''Prints the maximum of two numbers.

    The two values must be integers.'''
    x = int(x)  # conbert to integers, if possible
    y = int(y)

    if x > y:
        print(x, 'is maximum')
    else:
        print(y, 'is maximum')

printMax(3, 5)
print(printMax.__doc__)
