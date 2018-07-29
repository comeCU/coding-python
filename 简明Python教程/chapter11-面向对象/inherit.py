#!/usr/bin/env python
# filename: inherit.py
# 继承

# 父类
class SchoolMenber:
    '''Represents any school member.'''
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print('(Initialized SchoolMenber: %s)' % self.name)


    def tell(self):
        '''Tell my details.'''
        print('Name:"%s" Age:"%s"' %(self.name, self.age), end="")

# Teacher子类
class Teacher(SchoolMenber):
    '''Represents a teacher.'''
    def __init__(self, name, age, salary):
        SchoolMenber.__init__(self, name, age)
        self.salary = salary
        print('(Initialized Teacher: %s)' % self.name)


    def tell(self):
        SchoolMenber.tell(self)
        print('Salary: "%d"' % self.salary)

# Student子类
class Student(SchoolMenber):
    '''Represents a student.'''
    def __init__(self, name, age, marks):
        SchoolMenber.__init__(self, name, age)
        self.marks = marks
        print('(Initalized Student: %s)' % self.name)


    def tell(self):
        SchoolMenber.tell(self)
        print('Marks: %d' % self.marks)


t = Teacher('Tom', 40, 30000)
s = Student('Jack', 20, 90)

print()

members = [t, s]
for member in members:
    member.tell()



