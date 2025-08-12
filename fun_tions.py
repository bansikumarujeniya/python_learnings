#1
def my_function():
    print("Hello from a function")

#2
def my_function():
    print("Hello from a function")

my_function()

#3
def my_function(fname):
    print(fname + " Refsnes")

my_function("Emil")
my_function("Tobias")
my_function("Linus")

#4
def my_function(fname, lname):
    print(fname + " " + lname)

my_function("Emil", "Refsnes")

#5
def my_function(*kids):
    print("The youngest child is " + kids[2])

my_function("Emil", "Tobias", "Linus")

#6
def my_function(child3, child2, child1):
    print("The youngest child is " + child2)

my_function(child1="Emil", child2="Tobias", child3="Linus")

#7
def my_function(**kid):
    print("His last name is " + kid["lname"])

my_function(fname="Tobias", lname="Refsnes")

#8
def my_function(country="Norway"):
    print("I am from " + country)

my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")

#7
def my_function(food):
    for x in food:
        print(x)

fruits = ["apple", "banana", "cherry"]
my_function(fruits)

#8
def my_function(x):
    return 5 * x

print(my_function(3))
print(my_function(5))
print(my_function(9))

#8
def my_function(x, /):
    print(x)

my_function(3)

#9
def my_function(x):
    print(x)

my_function(x=3)

#10
def my_function(*, x):
    print(x)

my_function(x=3)

#11
def my_function(a, b, /, *, c, d):
    print(a + b + c + d)

my_function(5, 6, c=7, d=8)

#12
def tri_recursion(k):
    if (k > 0):
        result = k + tri_recursion(k - 1)
        print(result)
    else:
        result = 0
    return result

print("Recursion Example Results:")
tri_recursion(6)

#13
def subNumbers(x,y):
    return (x-y)

a = 90
b = 50

res = subNumbers(a,b)

print("subtraction of", a , "and" , b, "is" , res)


#14 first 10 prime numbers

def fun(n):
    x = 2
    count = 0
    while count < n:
        for d in range(2,int(x ** 0.5) + 1):
            if x%d == 0:
                break
        else:
            print(x)
            count += 1
        x += 1

n = 10
fun(n)
