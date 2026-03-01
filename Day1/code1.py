a = 10
print(type(a))

a = input()
b = input()
c = a + b
print(c)
print(type(c))

a = 20
print(id(a))

class Temp:
    pass

obj = Temp()
print(obj)

a = 30
b = a
a = a + b
print(a, b)
print(id(a))
print(id(b))
print(id(30))
# id of b and 60 may or may not be same (depends on memory optimization)
print(id(60))

n1 = int(input())
n2 = int(input())

class Add:
    @staticmethod
    def result(n1, n2):
        return (n1 + n2)

print(Add.result(n1, n2))

# mvc - multiple variable creation
a, b, c = 10, 20, 30
print(a, b, c)
result = a, b, c
print(type(result))

# number of variable less than number of values (fixed using *)
x, y, *z = 1, 2, 3, 4
print(x, y, z)

num = 20
_n = 2

# checking keywords
import keyword
print(keyword.kwlist)
print(len(keyword.kwlist))

print(type(None))

a = None
print(type(None))
print(type([1, 2, 3]))

var = 1000
var2 = 'HELLO'

print(type(888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888))
print(type(65656616.0000646))

print(type(20 + 9j))
print(type(-1.1 - 7878j))
num = 45j + 7
print(type(num))

print(type(7 + 8j))

a = 6.7
b = 23 + 67676j
print(a + b)

print(id(True))
print(id(False))

print(True + True + False)
print(20 * False)
print(20 * True)
print(20 * 1)
print(20 * 0)

print('HELLO')
print("HELLO")
print('''HELLO''')

name = "Harsh"
print(id(name))
print(id(name[0:1]))
print(id(name[1:2]))

paragraph = """
hrkhhafk
jjgjgjfg
lhlafafblb
"""
print(paragraph)

name = "Python"
print(name[-6] + name[-4] + name[-1])
print(name[-len(name) + 1])

print(int())
print(float())
print(bool())
print(str())
print(complex())
print(list())
print(tuple())
print(set())
print(dict())

print(bool(''))