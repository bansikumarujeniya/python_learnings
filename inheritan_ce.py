# Inheritance:- Inheritance allows us to define a class that inherits all the methods and properties from another class.
# Parent class is the class being inherited from, also called base class.
# Child class is the class that inherits from another class, also called derived class.

#1
class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)

x = Person("John", "Doe")
x.printname()

#2
class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)

class Student(Person):
    pass

x = Student("Mike", "Olsen")
x.printname()


#3
class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)

class Student(Person):
    def __init__(self, fname, lname):
        Person.__init__(self, fname, lname)

x = Student("Mike", "Olsen")
x.printname()

#4
class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)

class Student(Person):
    def __init__(self, fname, lname):
        super().__init__(fname, lname)
        self.graduationyear = 2019

x = Student("Mike", "Olsen")
print(x.graduationyear)

#5
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

x = Student("Mike", "Olsen", 2019)
print(x.graduationyear)

#6
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

#7
class Person:
    def __init__(self, fname , lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname , self.lastname)

x = Person("John","Doe")
x.printname()

#8
class Person:
    def __init__(self, fname , lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname , self.lastname)

class Student(Person):
    pass

x = Student("Mike","Olsen")
x.printname()

#9
class Person:
    def __init__(self,fname,lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname,self.lastname)

class Student(Person):
    def __init__(self,fname,lname):
        Person.__init__(self,fname, lname)

x = Student("Bansikumar","Ujeniya")
x.printname()

#10
class Person:
    def __init__(self,fname,lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname,self.lastname)

class Student(Person):
    def __init__(self,fname,lname):
        super().__init__(fname,lname)

x = Student("Harsh","Vadoliya")
x.printname()

#11
class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)


class Student(Person):
    def __init__(self, fname, lname):
        super().__init__(fname, lname)
        self.graduationyear = 2025

x = Student("Harsh", "Vadoliya")
print(x.graduationyear)

#12
class Person:
    def __init__(self,fname,lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firtsname,self.lastname)

class Student(Person):
    def __init__(self,fname,lname,year):
            super().__init__(fname, lname)
            self.graduationyear = year

    def welcome(self):
        print("Welcome",self.firstname,self.lastname,"to the class of",self.graduationyear)

x = Student("Bansikumar","Ujeniya",2025)
x.welcome()

#13
class Person:
    def __init__(self,fname,lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname,self.lastname)

class Student(Person):
    pass

x = Person("John","Doe")
x.printname()

#14
class Person:
    def __init__(self,fname,lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname,self.lastname)

class Student(Person):
    pass

x = Person("Bansikumar","Ujeniya")
x.printname()

#15
class Person:
    def __init__(self,fname,lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname,self.lastname)

class Student(Person):
    def __init__(self,fname,lname,year):
        super().__init__(fname,lname)
        self.graduationyear = year

    def welcome(self):
        print("Welcome",self.firstname,self.lastname,"to the class of",self.graduationyear)

x = Student("Bansikumar","Ujeniya",2025)
x.welcome()

#16
class Person:
    def __init__(self,fname,lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname,self.lastname)

class Student(Person):
    def __init__(self,fname,lname,year):
        super().__init__(fname, lname)
        self.graduationyear = year

    def welcome(self):
        print("Welcome",self.firstname,self.lastname,"to the class of",self.graduationyear)

x = Student("John","Doe",2025)
x.welcome()












