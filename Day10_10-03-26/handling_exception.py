'''
Exception Handling
--> Specific EH
--> Generic EH
--> Dafault EH

'''

'''
Specific EH
-- If we are aware of the error or, exception then we can go with "specific".

try:
  PROBLEM
  STATEMENT
except ErrorName:
  RESOLUTION/ 
  SOLUTION CODE  
'''

# n1, n2 = 21, 0
# # print(n1/n2)
# try:
#   ## Problem Statement
#   result = n1 / n2
#   print(result)
# except ZeroDivisionError:
#   ## Solution Code
#   print('Please do not choose 0 as the second number!')
# ## Despite having error , using these it will be handled and will not halt the rememaning the code the below of it
# print('Code After Try Except - 01')    
# print('Code After Try Except - 02')   
# print('Code After Try Except - 03') 
#


# try:
#   a , b , c = 1 , 2
# except ValueError:
#   print('For performing MVC, number of variables should be equals to number of value!')  

# try:
#   print(a,b,c)
# except NameError:
#   print("Identifiers are not there in the memory!") 
#

'''
Generic EH
-- It is a type of exception handling approach in which there is no need to pass any particular exception class name. Instead of we can use parent "exception" class called "Exception"

-- Using "generic exception handling", we can't handle keyword interruption
'''
# try:
#   a , b , c = 1 , 2
# except Exception:
#   print('For performing MVC, number of variables should be equals to number of value!')  

# try:
#   print(a,b,c)
# except Exception:
#   print("Identifiers are not there in the memory!")   

# import time
# try:
#   while True:
#     print(time.time())
# # except Exception: ### here you can see the generic exception work perfect for every execption using Exception but will not work in KeyboardInterrupt error
# #   print('Loop got stopped')        
# except KeyboardInterrupt:
#   print('Loop got stopped')    

'''
Default EH
-- It is a type of exception handling in which we can handle all types of errors of exception except "Syntax Error"
'''

import time
try:
  while True:
    print(time.time())
except:
  print("Loop got stopped")    