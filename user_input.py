# Python allows for user input.that means we are able to ask for user input.

#1
print("Enter Your Name:")
name = input()
print(f"Hello, {name}!")

#2
name = input("Enter your name:")
print(f"Hello {name}")
fav1 = input("What is your favorite animal:")
fav2 = input("What is your favorite color:")
fav3 = input("What is your favorite number:")
print(f"Do you want a {fav2} {fav1} with {fav3} legs?")

#3 Input Number :- The input from the user is treated as a string. Even if, in the example above, you can input a number, the Python interpreter will still treat it as a string.
# You can convert the input into a number with the float() function:

import math

x = input("Enter a number:")
y = math.sqrt(float(x))

print(f"The square root of {x} is {y}")

#4 Validate Input :- It is a good practice to validate any input from the user. In the example above, an error will occur if the user inputs something other than a number.To avoid getting an error, we can test the input, and if it is not a number, the user could get a message like "Wrong input, please try again", and allowed to make a new input:

y = True
while y == True:
    x = input("Enter a number:")
    try:
        x = float(x);
        y = False
    except:
        print("Wrong input, please try again.")

print("Thank you!")
