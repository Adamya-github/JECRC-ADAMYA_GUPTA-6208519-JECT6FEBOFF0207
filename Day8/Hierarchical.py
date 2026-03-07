## Hierarchical Inheritance

'''
It is a type of inheritance in which the properties will be derived from single parent child to multiple child class
'''

class parent:
    gold='2Kg'
    silver='10kg'
    no_of_flats=12

class SmallerBrother(parent):
    name='G'

class ElderBrother(parent):
    my_name='rob'

class Sister(parent):
    sis_name='sansa'

print(SmallerBrother.gold)
print(ElderBrother.silver)
print(Sister.no_of_flats)