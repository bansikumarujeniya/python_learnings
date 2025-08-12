# JSON is a syntax for storing and exchanging data.
# JSON is text, written with JavaScript object notation.

#1  If you have a JSON string, you can parse it by using the json.loads() method.

import json

x = '{ "name":"John", "age":30, "city":"New York"}'

y = json.loads(x)

print(y["age"])

#2 If you have a Python object, you can convert it into a JSON string by using the json.dumps() method.

import json

x = {
    "name": "John",
    "age": 30,
    "city": "New York"
}

y = json.dumps(x)

print(y)

#3
import json

print(json.dumps({"name": "John", "age": 30}))
print(json.dumps(["apple", "bananas"]))
print(json.dumps(("apple", "bananas")))
print(json.dumps("hello"))
print(json.dumps(42))
print(json.dumps(31.76))
print(json.dumps(True))
print(json.dumps(False))
print(json.dumps(None))

#4
import json

x = {
    "name": "John",
    "age": 30,
    "married": True,
    "divorced": False,
    "children": ("Ann", "Billy"),
    "pets": None,
    "cars": [
        {"model": "BMW 230", "mpg": 27.5},
        {"model": "Ford Edge", "mpg": 24.1}
    ]
}

print(json.dumps(x))

#5
import json

x = {
    "name": "John",
    "age": 30,
    "married": True,
    "divorced": False,
    "children": ("Ann", "Billy"),
    "pets": None,
    "cars": [
        {"model": "BMW 230", "mpg": 27.5},
        {"model": "Ford Edge", "mpg": 24.1}
    ]
}

print(json.dumps(x, indent=4))

#6
import json

x = {
    "name": "John",
    "age": 30,
    "married": True,
    "divorced": False,
    "children": ("Ann", "Billy"),
    "pets": None,
    "cars": [
        {"model": "BMW 230", "mpg": 27.5},
        {"model": "Ford Edge", "mpg": 24.1}
    ]
}

print(json.dumps(x, indent=4, separators=(". ", " = ")))


#7
import json

x = {
    "name": "John",
    "age": 30,
    "married": True,
    "divorced": False,
    "children": ("Ann", "Billy"),
    "pets": None,
    "cars": [
        {"model": "BMW 230", "mpg": 27.5},
        {"model": "Ford Edge", "mpg": 24.1}
    ]
}

print(json.dumps(x, indent=4, sort_keys=True))

#8
import json

x = {
    "name" : "Bansi",
    "age": 32,
    "married": False,
    "divorced": False,
    "children": ("bbbb","cccc"),
    "pets": None,
    "cars": [
        {"model": "BMW 230", "mpg": 56.5},
        {"model": "BMW 230", "mpg": 14.5}
    ]
}

print(json.dumps(x, indent=5, sort_keys=True))