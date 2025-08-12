# F-String was introduced in Python 3.6, and is now the preferred way of formatting strings.
# Before Python 3.6 we had to use the format() method.

# F-string allows you to format selected parts of a string.
# To specify a string as an f-string, simply put an f in front of the string literal, like this:

#1
txt = f"The price is 50 dollars"
print(txt)

#2
price = 50
txt = f"The price is {price} dollars"
print(txt)

#3 A placeholder can also include a modifier to format the value.
# A modifier is included by adding a colon : followed by a legal formatting type, like .2f which means fixed point number with 2 decimals:

price = 59
txt = f"The price is {price:.2f} dollars"
print(txt)

#4

txt = f"The Price is {20*59} dollars"
print(txt)

#5

price = 60
tax = 0.25
txt = f"The Price is {price + (price * tax)} dollars"
print(txt)

#6
fruit = "apples"
txt = f"i love {fruit.upper()}"
print(txt)

#7
price = 49
txt = "The price is {} dollars"
print(txt.format(price))

#8
price = 49
txt = "The price is {:.2f} dollars"
print(txt.format(price))


#9 Multiple Values :- print(txt.format(price , itemno , count))

quantity = 3
itemno = 567
price = 49
myorder = "I want {} pieces of item number {} for {:.2f} dollars."
print(myorder.format(quantity, itemno, price))

#10

quantity = 3
itemno = 567
price = 49
myorder = "I want {0} pieces of item number {1} for {2:.2f} dollars."
print(myorder.format(quantity, itemno, price))

#11 Named Indexes :- You can also use named indexes by entering a name inside the curly brackets {carname}, but then you must use names when you pass the parameter values txt.format(carname = "Ford"):

myorder = "I have a {carname}, it is a {model}."
print(myorder.format(carname="Ford", model="Mustang"))

