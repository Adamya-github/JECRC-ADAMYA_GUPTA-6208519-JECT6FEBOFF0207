'''
lambda(Anonymous Function):
    1. Lambda is a keyword. Which is used to create anonymous function
    2. For calling the lambda function, we can store the address of lambda inside a variable. By invoking the var_name, we can call the function
'''
'''
var_name = lambda args: <exp>
var_name(args) ## Calling the lambda function
'''

## lambda args: <exp>
# result = lambda a,b: a+b
# print(result)
# print(result(10,20))

## (lambda a,b: print(a+b))(int(input("First num: ")),int(input("Second num: "))) ## avoid using this at starting phase, go step by step

'''
lambda args: <exp 1> if consition else <exp 2>
'''
## WAP to find th square of a number if it is even
# num = int(input("Enter the number: "))
# if num % 2 == 0:
#   print(num**2) ## num*num
# result = lambda num: print(num**2) if num % 2 == 0 else None
# result(10)
# (lambda num: print(num**2) if num % 2 == 0 else None)(int(input("Enter the number: ")))

## WAP to find the square of number if it is even else cube 
# (lambda num: print(num**2) if num % 2 == 0 else print(num**3))(int(input("Enter the number: ")))


## Check whether a num is positive or, negative or zero
(lambda num: print('Positve') if num > 0 else print('Negative') if num < 0 else print('Zero'))(int(input("Enter the number: ")))