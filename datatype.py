"""
Text Type: str

Numeric Types: int, float, complex

Sequence Types: list, tuple, range

Mapping Type: dict

Set Types: set, frozenset

Boolean Type: bool

Binary Types: bytes, bytearray, memoryview

None Type: NoneType

"""



#1
x = 5
print(type(x))

#2
x = "Hello World"
print(type(x))

#3
x = 20.5
print(type(x))


#4
x = ["apple", "banana", "cherry"]
print(type(x))

#5
x = ("apple", "banana", "cherry")
print(type(x))

#6
x = {"name": "John", "age": 36}
print(type(x))


#7
x = {"apple", "banana", "cherry"}
print(type(x))

#8
x = frozenset({"apple", "banana", "cherry"})
print(type(x))