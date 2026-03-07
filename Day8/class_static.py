'''
Staic Method:
 1.It is neither related to object nor class.
 2.For static method,there is no need to use self or, cls.
 3."@staticmethod" decorator is used to create one static method.
   
    class ClassName:
    @staticmethod
    def method_name
        statement
        block
'''

class Car:
    ## Below variables are known as "Properties/States/Members"
    wheelers=4
    engine='Petrol'
    base_speed='40Kmph'
    max_speed='120Kmph'
    gears=4

    @staticmethod
    def greeting(name):
        print(f'Good Morning {name}')

TATA=Car
TATA.greeting('Harsh')