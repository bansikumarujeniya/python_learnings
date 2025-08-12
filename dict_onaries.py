#1
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
print(thisdict)

#2
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
print(thisdict["brand"])

#3
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
x = thisdict["model"]
print(x)
x = thisdict.get("model")
print(x)
x = thisdict.keys()
print(x)
x = thisdict.values()
print(x)

#4
car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
x = car.items()
print(x)
car["year"] = 2020
print(x)

#5
car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

x = car.items()
print(x)
car["color"] = "red"
print(x)

#6
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
thisdict["year"] = 2018
print(thisdict)

thisdict.update({"year": 2020})
print(thisdict)

#7
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
mydict = thisdict.copy()
print(mydict)

#8
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
mydict = dict(thisdict)
print(mydict)

#9
newdict = {x: x**3 for x in range(10) if x**3 % 4 == 0}
print(newdict)

#10
l = "GFG"

dic = {
    x: {y: x+y for y in l} for x in l
}

print(dic)

