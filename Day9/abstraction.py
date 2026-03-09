'''
Abstraction:
    Hiding the internal implementation and showing only functionality to the end user.

Abstract Method:
    If a method/function consists of only declaration not definition then it will be called as "Abstract Mathod".
    def def_name():
      pass

Abstract Class:
    If a class consists of at least one abstract method, it will be called as "Abstract class"

Concret Class:
    It consists of zero(0) abstract method

abc: Module
ABC: Abstract Base Class
'''

from abc import ABC, abstractmethod

class ATM(ABC): ## HERE ATM is said as Abstract class and methods here are called generate_pin
  @abstractmethod
  def generate_pin(self):
    pass

  @abstractmethod
  def forget_pin(self):
    pass

  @abstractmethod
  def check_bal(self):
    pass

  @abstractmethod
  def withdraw(self):
    pass

  @abstractmethod
  def deposite(self):
    pass

# obj = ATM() ## Can't instantiate abstract class ATM without an implementation for abstract methods 'check_bal', 'deposite', 'forget_pin', 'generate_pin', 'withdraw'

# class SBI_ATM(ATM):
#   def generate_pin(self):
#     print("It is used to generate the ATM pin")

#   def forget_pin(self):
#     print('Not able to remember the pin! Then forget Now!')

#   def check_bal(self):
#     print('No balance is there in your account')

#   def deposite(self):
#     print('Save your money by giving it to me!')

# obj = SBI_ATM() ## Need all the method's present in abstract class needs to be added
## Can't instantiate abstract class SBI_ATM without an implementation for abstract method 'withdraw'

class SBI_ATM(ATM):
  def generate_pin(self):
    print("It is used to generate the ATM pin")

  def forget_pin(self):
    print('Not able to remember the pin! Then forget Now!')

  def check_bal(self):
    print('No balance is there in your account')

  def deposite(self):
    print('Save your money by giving it to me!')

  def withdraw(self):
    print('Do not withdraw the money! Please!')  

obj = SBI_ATM()
obj.generate_pin()
obj.forget_pin()
obj.check_bal()
obj.deposite()
obj.withdraw()


