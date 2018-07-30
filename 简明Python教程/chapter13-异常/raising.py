#!/usr/bin/env python
# filename: raising.py
# 触发异常

class ShortInputException(Exception):
    '''A usr-defined exception class.'''
    def __init__(self, length, atleast):
        Exception.__init__(self)
        self.length = length
        self.atleast = atleast


try:
    s = input('Enter something -->')
    if len(s) < 3:
        raise ShortInputException(len(s), 3)

except EOFError:
    print('\nWhy did you do an EOF on me?')
except ShortInputException as x:    # as 将异常赋于变量x
    print('ShortInputException:The input was of length %d,\
was excepting at least %d' %(x.length, x.atleast))
else:
    print('No exception was raised')
