## INHERITANCE
'''
 1.Single Level,
 2.Multi-level,
 3.Multiple,
 4.Herarchical,
 5.Hybrid,

 '''

## Single Level,
## We will have a single parent & child class. Also the properties will be derived only one time.

# # Parent Class or,Super Class
# # The class from which we are going to derive the properties

# class parent:
#     bank_balance='54L'
#     def desc(self):
#         print('I am the parent class')

# # Child class or, sub classs
# #The class in which we are going to drive the properties

# class Child(parent):
#     pass

# obj=Child()
# print(Child.bank_balance)
# obj.desc()


## Constructor chaining:Calling parent class's constructor from inside child class 's constructor is known as constructor chaining

# class parent:
#     bank_balance='54L'
#     def __init__(self,*members):
#         self.members=members

    


#     def desc(self):
#         print('I am the parent class')

# class Child(parent):
#     def __init__(self,child_name,*args):
#         super().__init__(args)
#         self.child_name=child_name

#     def display(self):
#         super().desc()

# obj=Child('Harsh','MOM','DAD')
# print(obj.members)
# print(obj.child_name)
# obj.display()

## Multi-Level

'''
-- It is atype of inheritance in which the properties will be derived from one to another class by considering more than on level
'''

class Class_1:##Parent
    a='class1'
class Class_2(Class_1):##parent
    b='class2'
class Class_3(Class_2):##child
    c='class3'
class Class_4(Class_3):
    d='class4'
class Class_5(Class_4):
    e='class5'

obj=Class_5()
print(obj.a,obj.b,obj.c,obj.d,obj.e)

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

## Hierarchical Inheritance

'''
It is a type of inheritance in which the properties will be derived from single parent child to multiple child class
'''

class parent:
    gold='2Kg'
    silver='10kg'
    no_of_flats=12

class SmallerBrother(parent):
    name='G'

class ElderBrother(parent):
    my_name='rob'

class Sister(parent):
    sis_name='sansa'

print(SmallerBrother.gold)
print(ElderBrother.silver)
print(Sister.no_of_flats)

## Hybrid Inheritence

'''
It is a mixture of more than one type of inheritance
'''

