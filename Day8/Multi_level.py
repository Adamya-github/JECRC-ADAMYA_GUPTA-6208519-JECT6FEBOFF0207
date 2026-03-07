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
