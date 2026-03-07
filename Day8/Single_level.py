# Parent Class or,Super Class
# The class from which we are going to derive the properties

class parent:
    bank_balance='54L'
    def desc(self):
        print('I am the parent class')

# Child class or, sub classs
#The class in which we are going to drive the properties

class Child(parent):
    pass

obj=Child()
print(Child.bank_balance)
obj.desc()