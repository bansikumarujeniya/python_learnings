#  Classes and Objects are the two core concepts in object-oriented programming.
#  A class defines what an object should look like, and an object is created based on that class.

#1
class MyClass:
    x = 5

print(MyClass)

#2
class MyClass:
    x = 5

p1 = MyClass()
print(p1.x)

#3
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = Person("John", 36)

print(p1.name)
print(p1.age)


#4
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = Person("John", 36)
print(p1)

#5
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name}({self.age})"

p1 = Person("John", 36)
print(p1)

#6
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def myfunc(self):
        print("Hello my name is " + self.name)

p1 = Person("John", 36)
p1.myfunc()

#7
class Person:
    def __init__(mysillyobject, name, age):
        mysillyobject.name = name
        mysillyobject.age = age

    def myfunc(abc):
        print("Hello my name is " + abc.name)

p1 = Person("John", 36)
p1.myfunc()

#8
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def myfunc(self):
        print("Hello my name is " + self.name)

p1 = Person("John", 36)
p1.age = 40
print(p1.age)

#9
'''
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def myfunc(self):
        print("Hello my name is " + self.name)

p1 = Person("John", 36)
del p1.age
print(p1.age)
'''

#10
'''

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def myfunc(self):
        print("Hello my name is " + self.name)

p1 = Person("John", 36)
del p1
print(p1.age)

'''

#11
class Person:
    pass


#12
class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def myfunc(self):
        print("Hello my name is " + self.name)


p1 = Person("John",36)
p1.myfunc()

#13
class MyClass:
    x = 5

p1 = MyClass()
print(p1.x)

#14
class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

p1 = Person("John",36)

print(p1.name)
print(p1.age)

#15
class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def myfunc(self):
        print("Hello my Name is " +  self.name)

p1 = Person("John",36)
p1.myfunc()

#16
class Person:
    def __init__(mysillyobject,name,age):
        mysillyobject.name = name
        mysillyobject.age = age

    def myfunc(abc):
        print("Hello my name is "+ abc.name)

p1 = Person("John",40)
p1.age = 44
print(p1.age)


#17
class Person:
    def __init__(mysillyobject,name,age):
        mysillyobject.name = name
        mysillyobject.age = age

    def myfunc(abc):
        print("Hello my name is "+ abc.name)

p1 = Person("John",78)
p1.age = 89
print(p1.age)
