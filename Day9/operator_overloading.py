'''
--Operator Overloading: It is a phenomemon of making the operators to work on user on user-defined data types by invoking respective magic methods

-- Magic Method/Dundar: It is a special type of methods in which double underscore will be there at the starting and ending of the method's name.

-- Example:
1. __add__
2. __sub__
3. __mul__
4. __floordiv__
5. __truediv__
6. __mod__

-- If we don't use operator overloading then what will happen ?
  For using the operators inside user-defined data types we have to use operator overloading

-- Syntax: 
class ClassName:
  def __init__(self, val):
      self.val = val
  def __add__(self,ano_obj):
    return self.val + ano_obj.value
obj1 = ClassName(val1)
obj2 = ClassName(val2)
print(obj1 + obj2 )   ## obj1.__add__(obj2)       
'''

class MyDT:
  def __init__(self, val):
      self.val = val

  def __str__(self):
    return str(self.val)    

  def __add__(self, ano_obj):
    return MyDT(self.val + ano_obj.val)
  
  def __sub__(self,ano_obj):
    return MyDT(self.val - ano_obj.val)
  
  def __mul__(self,ano_obj):
    return MyDT(self.val * ano_obj.val)
  
  def __floordiv__(self,ano_obj):
    return MyDT(self.val // ano_obj.val)
  
  def __truediv__(self,ano_obj):
    return MyDT(self.val / ano_obj.val)
  
  def __mod__(self,ano_obj):
    return MyDT(self.val % ano_obj.val)
# obj1 = ClassName(10)
# obj2 = ClassName(20)
# print(obj1 + obj2 )   ## obj1.__add__(obj2)     
## Also like below

## while using str 
print(MyDT(10) + MyDT(20))
print(MyDT(10) - MyDT(20))
print(MyDT(10) * MyDT(20))
print(MyDT(10) // MyDT(20))
print(MyDT(10) / MyDT(20))
print(MyDT(10) % MyDT(20))

## without using str
print()
print((MyDT(10) + MyDT(20) + MyDT(30) + MyDT(10)).val) 
print((MyDT(10) - MyDT(20) - MyDT(30) - MyDT(60)).val)
print((MyDT(10) * MyDT(20) * MyDT(30) * MyDT(60)).val)
# print((MyDT(10) // MyDT(20) // MyDT(30) // MyDT(60)).val)
# print((MyDT(10) / MyDT(20) / MyDT(30) / MyDT(60)).val)
# print((MyDT(10) % MyDT(20) % MyDT(30) % MyDT(60)).val)

