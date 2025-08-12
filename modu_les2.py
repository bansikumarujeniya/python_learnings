#1
import modu_les

modu_les.greeting("Jonathan")

#2
import modu_les

a1 = modu_les.person1["name"]
a2 = modu_les.person1["age"]
a3 = modu_les.person1["country"]

print(a1)
print(a2)
print(a3)

#3
import modu_les as mx

a = mx.person1["age"]
print(a)


#4
import platform

x = platform.system()
print(x)

#5 There is a built-in function to list all the function names (or variable names) in a module. The dir() function:
import platform

x = dir(platform)
print(x)

#6
from modu_les import person1

print(person1["age"])