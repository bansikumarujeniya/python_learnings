#lambda arguments: expression

#1
x = lambda a: a + 10
print(x(5))

#2
x = lambda a, b: a * b
print(x(5, 6))

#3
x = lambda a, b, c: a + b + c
print(x(5, 6, 2))

#4
'''
def myfunc(n):
    return lambda a: a * n
'''

#5
def myfunc(n):
    return lambda a: a * n

mydoubler = myfunc(2)
print(mydoubler(11))

#6
def myfunc(n):
    return lambda a: a * n

mytripler = myfunc(3)
print(mytripler(11))

#7
def myfunc(n):
    return lambda a: a * n

mydoubler = myfunc(2)
mytripler = myfunc(3)

print(mydoubler(11))
print(mytripler(11))

#8
sq = lambda x: x**2
print(sq(3))

def sqdef(x):
    return x**2
print(sqdef(3))

#9
li = [lambda arg = x: arg * 10 for x in range(1,5)]
for i in li:
    print(i())

#10
check = lambda x: "Even" if x % 2 == 0 else "odd"

print(check(7))

#11
calc = lambda x,y: (x+y,x*y)
res = calc(3,4)
print(res)

#12
from functools import reduce

a = [1,2,3,99]
b = reduce(lambda x,y: x * y, a)
print(b)

#13
li = [lambda arg = x: arg * 10 for x in range(1,5)]
for i  in li:
    print(i())

#14
check = lambda x: "Even" if x%2 == 0 else "odd"

print(check(7))
print(check(4))

#15
n =[1,2,3,4,5,6]
even = filter(lambda x : x%2 == 0,n)
print(list(even))

#!6
import functools
import operator

a = [1,3,5,6,2]

print(functools.reduce(operator.add,a))

print(functools.reduce(operator.mul,a))

print(functools.reduce(operator.add, ["geeks","for","geeks"]))

