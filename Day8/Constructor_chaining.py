## Constructor chaining:Calling parent class's constructor from inside child class 's constructor is known as constructor chaining

class parent:
    bank_balance='54L'
    def __init__(self,*members):
        self.members=members


    def desc(self):
        print('I am the parent class')

class Child(parent):
    def __init__(self,child_name,*args):
        super().__init__(args)
        self.child_name=child_name

obj=Child('Harsh','MOM','DAD')
print(obj.members)
print(obj.child_name)