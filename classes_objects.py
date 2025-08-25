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


#18
class A:
    def show_name(self):
        print("A")

class B:
    def show_name(self):
        print("B")

class C:
    def show_name(self):
        print("C")

instance_b = B()
instance_a = A()
instance_c = C()

instance_b.show_name()
instance_a.show_name()
instance_c.show_name()


#19
class A:
    def show_name(self):
        print("A")

class B:
    def show_name(self):
        print("B")

class C:
    def show_name(self):
        print("C")

instance_b = B()
instance_c = C()
instance_a = A()

instance_b.show_name()
instance_c.show_name()
instance_a.show_name()

#20
class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)


class Student(Person):
    def __init__(self, fname, lname):
        super().__init__(fname, lname)


x = Student("Mike", "Olsen")
x.printname()

#21
class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)


class Student(Person):
    def __init__(self, fname, lname, year):
        super().__init__(fname, lname)
        self.graduationyear = year

    def welcome(self):
        print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)


x = Student("Mike", "Olsen", 2024)
x.welcome()
