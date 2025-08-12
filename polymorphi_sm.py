#1
x = "Hello World!"

print(len(x))

#2
mytuple = ("apple", "banana", "cherry")
print(len(mytuple))

#3
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

print(len(thisdict))

#4
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def move(self):
        print("Drive!")

class Boat:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def move(self):
        print("Sail!")

class Plane:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def move(self):
        print("Fly!")

car1 = Car("Ford", "Mustang")
boat1 = Boat("Ibiza", "Touring 20")
plane1 = Plane("Boeing", "747")

for x in (car1, boat1, plane1):
    x.move()

#5
class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def move(self):
        print("Move!")

class Car(Vehicle):
    pass

class Boat(Vehicle):
    def move(self):
        print("Sail!")

class Plane(Vehicle):
    def move(self):
        print("Fly!")

car1 = Car("Ford", "Mustang")
boat1 = Boat("Ibiza", "Touring 20")
plane1 = Plane("Boeing", "747")

for x in (car1, boat1, plane1):
    print(x.brand)
    print(x.model)
    x.move()

#6
class Vehicle:
    def __init__(self, brand , model):
        self.brand = brand
        self.model = model

    def move(self):
        print("Move!")

class Car(Vehicle):
    pass

class Boat(Vehicle):
    def move(self):
        print("Fly!")

car2 = Car("Ford", "Mustang")
boat2 = Boat("Ibiza","Touring 45")
plane2 = Plane("Boenig","850")

for x in (car2,boat2,plane2):
    print(x.brand)
    print(x.model)
    x.move()