#!/usr/bin/env python
# filename: objvar.py
# 类与对象的变量

class Person:
    '''Represent a person.'''
    population = 0

    def __init__(self, name):
        '''Initializes the person's data '''
        self.name = name
        print('(Initializing %s)' % self.name)

        Person.population += 1
        

    def __del__(self):
        '''I an dying. '''
        print('%s says bye.' % self.name)

        Person.population -= 1

        if Person.population == 0:
            print('I an the last one.')
        else:
            print('There are still %d people left.' % Person.population)


    def sayHi(self):
        '''Greeting by the person.'''
        print('Hi, my name is %s.' % self.name)


    def howMany(self):
        '''Prints the current population.'''
        if Person.population == 1:
            print('I an the only person here.')
        else:
            print('We have %d persons here.' % Person.population)


swaroop = Person('Swaroop')
swaroop.sayHi()
swaroop.howMany()

kalam = Person('Abdul Kalam')
kalam.sayHi()
kalam.howMany()

swaroop.sayHi()
swaroop.howMany()

Person.__del__(kalam)
Person.__del__(swaroop)


# 输出
'''
(Initializing Swaroop)
Hi, my name is Swaroop.
I an the only person here.
(Initializing Abdul Kalam)
Hi, my name is Abdul Kalam.
We have 2 persons here.
Hi, my name is Swaroop.
We have 2 persons here.
Abdul Kalam says bye.
There are still 1 people left.
Swaroop says bye.
I an the last one.
'''
    
