'''
raise --> It is a keyword, which helps us to throw an error in between a program.
Exception creation:
1. custom Exception (raise)
2. User-defined Exception (raise)
3. Assertion exception (assert)
'''

'''
Custom Exception:
We use pre-built Exception classess according to our requirement.
 
raise ErrorName('message')
Value Error : message
'''

# num = 10
# if num >= 18:
#   print('You are eligible for voting & driving')
# else:
#   raise KeyboardInterrupt('Age should be greater then or equals to 18')  ## their is not restiction in choosing and writing the error type , it totally depend on user whether to use ValueError or NameError and any other errors

'''
-- User-defined Exception

    1. It is a  type of exception in which we can create our own exception classes based upon our own requirement. We can also provide names to those classes according to the user case
'''
# class MyException(Exception):
#   pass

# # raise MyException('This is my exception class!')

# n1, n2 = 10,3
# if n2 == 0:
#   raise MyException("Second num cannot be zero!")
# else:
#   print(n1 / n2)

'''
Assertion Exception
-- It can be created using one keyword called 'assert'
assert <condition>, print(error)
print(output)
'''

s = input("Enter a string: ")
assert s == s[::-1], print('It is not a palindromic String!')
print('It is a palindromic string!')

