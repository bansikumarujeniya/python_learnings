#1
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)

#2
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)
    if x == "banana":
        break

#3
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    if x == "banana":
        continue
    print(x)

#4
for x in range(6):
    print(x)

#5
for x in range(2, 6):
    print(x)

#6
for x in range(2, 30, 3):
    print(x)

#7
for x in range(6):
    print(x)
else:
    print("Finally finished!")

#8
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
    for y in fruits:
        print(x, y)

#9
for x in [0, 1, 2]:
    pass
print(x)

#10
s = "Bansikumar Ujeniya"
vowels = "aeiouAEIOU"
counts = {}

for char in s:
    if char in vowels:
        counts[char] = counts.get(char,0) + 1
print(counts)

#11
