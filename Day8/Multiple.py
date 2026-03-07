##Multiple Inheritance
'''
It is a type of onheritance in which the properties will be derived from multiple parent class to as single child class
'''

class Parent_1:
    a=10
class Parent_2:
    b=100
class Parent_3:
    c=1000
class Parent_4:
    d=10000

class Child(Parent_1,Parent_2,Parent_3,Parent_4):
    pass

print(Child.a,Child.b,Child.c,Child.d)