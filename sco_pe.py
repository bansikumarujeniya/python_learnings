# scope :- A variable is only available from inside the region it is created. This is called scope.

#local scope :- A variable created inside a function belongs to the local scope of that function, and can only be used inside that function.

#1
def myfunc():
    x = 300
    print(x)

myfunc()

#2
def myfunc():
    x = 300

    def myinnerfunc():
        print(x)

    myinnerfunc()

myfunc()

#global scope :- A variable created in the main body of the Python code is a global variable and belongs to the global scope.

#3
x = 300

def myfunc():
    print(x)

myfunc()

print(x)

#4
x = 300

def myfunc():
    x = 200
    print(x)

myfunc()

print(x)

#global keyword :- If you need to create a global variable, but are stuck in the local scope, you can use the global keyword.
#1
def myfunc():
    global x
    x = 300

myfunc()

print(x)

#2
x = 300

def myfunc():
    global x
    x = 200

myfunc()

print(x)

#Nonlocal Keyword :- The nonlocal keyword is used to work with variables inside nested functions.
def myfunc1():
    x = "Jane"

    def myfunc2():
        nonlocal x
        x = "hello"
    myfunc2()
    return x

print(myfunc1())

