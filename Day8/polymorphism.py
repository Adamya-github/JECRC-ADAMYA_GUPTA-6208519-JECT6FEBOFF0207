## Polymorphism
'''
using the same method or operator to perform two or more different operations


class Temp:
     def sum(self,a,b):
        print(a+b)

    def sum(self,a,b,c):
    print(a+b+c)
'''

'''
in python, if we want to perform method overloading then it will act as method overrriding.

In other programming languages,based upon no. of arguments, the respective method block wil get executed \.But in python, it never happens

Method Overrriding is a phenomenon of overriding the prev methods address with the latest one.'''


class Temp:
    def sum(self,a,b):
        print(a+b)
##Monkey Patching
##It is aprocess of storing the prv method's address inside a variable before overring the method area's address.Using that var, we can access the prev method's method area
    add_two_nums=sum

    def sum(self,a,b,c):
        print(a+b+c)

obj=Temp()
obj.sum(10,20,30)
obj.add_two_nums(10,20)