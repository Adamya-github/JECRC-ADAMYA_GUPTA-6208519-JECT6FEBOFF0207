'''
Encapsulation:
  1. It is used to provide security to the data(data means variables/prop & methods present inside a class)

  How to provide security to the data ?
    To provide security, we have to use access specifiers.
      1. public
      2. protected(Soft Barrier '_')
      3. private

Access specifier:
  It describe who can access the class members(properties & methods).      
'''

# ## Example for public access specifier.
# class Temp:
#   a,b,*c,d ='HELLO'

#   def greeting(self):
#     print('Good afternoon user : )')
# print(Temp.a)  

## packing
'''
a,b,c,d = '0123456789' show error
a,b,*c,d = '0123456789' it will execute
a -> 0
b -> 1
c -> [2.3,4,5,6,7,8]
d -> 9
'''

# ## Protected Access specifier
# class Temp:
#   ## Soft Barrier
#   _a = 10
#   _b = 'I LOVE PYTHON !'
# print(Temp._a)  

## Private Access specifier
# class Temp:
#   __a = 100

#   def __status(self):
#     print('Class name is Temp!')

# ## can't access it like this as 'a' is private
# obj = Temp()
# print(obj.__a)
# obj.__status()
## To avoid it
'''
1. By using Syntax
2. get & set method
3. By using @property decorater(setter)
'''
# ## By using Syntax
# '''
# obj_name/class_name._ClassName__prop_name/__method_name (Accessing)
# obj_name/class_name._ClassName_MemberName = NewValue (Modifing)
# '''
# print(Temp._Temp__a)

# print(obj._Temp__a)
# obj._Temp__status()

# obj._Temp__a = '0123456789'
# print(obj._Temp__a)

# def new_method():
#   print("Method is Changed")
# obj._Temp__status = new_method
# obj._Temp__status()

# ## By using get & set method
# class Temp:
#   __a = 100
#   def get(self):
#     print(self.__a)

#   def set(self,new_val):
#     self.__a = new_val
# obj = Temp()
# obj.get()
# obj.set(20)
# obj.get()

## By using @property decorater(setter)
class Temp:
  __a = 100

  @property
  def get(self):
    print(self.__a)

  @get.setter
  def  set(self, new_val):
    self.__a = new_val

obj = Temp()  
obj.get ## here the method can't be called it can be accessed
obj.set = 30
obj.get