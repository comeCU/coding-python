#!/usr/bin/env python
# filename: class_init.py
# __init__方法,对象被建立时运行，类似于java中的构造方法

class Person:
    def __init__(self, nam):
        self.name = nam
    def sayHi(self):
        print('Hello, my name is', self.name)

p = Person('swaroop')
p.sayHi()
