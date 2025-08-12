#1
x = 5
y = "John"
print(x)
print(y)

#2
x = 4
x = "Sally"
print(x)

#3
x = str(3)
y = int(3)
z = float(3)

#4
print(z)
print(x)
print(y)

#5
x = "John"
# is the same as
x = 'John'

#6
myvar = "John"
my_var = "John"

print(myvar,my_var)

#7
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)


#8
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)

#9
x = "Python"
y = "is"
z = "awesome"
print(x, y, z)

#10
x = "Python "
y = "is "
z = "awesome"
print(x + y + z)

#11
x = 5
y = "John"
print(x, y)

#12
print('Hello', 'World')


#Global Varibles :-   Variables that are created outside of a function are known as global variables.

#1
x = "ujeniya"

def myfunc():
    print("bansikumar" + x)
    print("bansikumar" , x)
myfunc()

#2
x = "awesome"

def myfunc():
    x = "fantastic"
    print("Python is " + x)


myfunc()

print("Python is " + x)


#Global Keyword :- Normally, when you create a variable inside a function, that variable is local, and can only be used inside that function.

#1
def myfunc():
    global x
    x = "fantastic"
myfunc()

print("Python is " + x)

#2
x = "awesome"

def myfunc():
    global x
    x = "fantastic"

myfunc()

print("Python is " + x)

#3
x = "Superbbb!"

def myfunc():
    global x
    x = "fantastic"

myfunc()
print("Python is " + x)


