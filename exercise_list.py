'''
#1
fruits = []
fruits_lower = []

while True:
    fruit = input("Enter Fruit Name:").strip()

    if fruit.lower() == "done":
        break

    if fruit.lower() in fruits_lower:
        print("duplicate!this fruit already in the list.")

    else:
        fruits.append(fruit)
        fruits_lower.append(fruit.lower())
        print(f"'{fruit}' added to the list.")

print("\nFinal unique fruit lists:")
print(fruits)
'''

#2
'''
[1] Write a Python program to count the occurrences of each word in a given sentence.

Input: "Complete Sentence Complete exercise"

Output: Complete - 2
		sentence - 1
		exercise - 1
'''
Sentence = "Complete Sentence Complete exercise"
words = Sentence.split()
counted = []

for word in words:
    if word not in counted:
        print(word,"-",words.count(word))
        counted.append(word)
#3
'''
[2] Write a Python program to sum all the items in a list.

Input: [10,12,20,22]
Output: 64
'''

numbers = [10,12,20,22]
total = 0

for num in numbers:
    total += num

print(total)

#4
'''
[3] Write a Python program to get the smallest number from a list.

Input: [10,12,20,22,2]
Output: 2
'''
numbers = [10,12,20,22,-1,0]
smallest = numbers[0]

for num in numbers:
    if num < smallest:
        smallest = num

print(smallest)

#5
'''
[4] Write a Python program to count the number of strings from a given list of strings. The string length is 2 or more and the first and last characters are the same.

Input : ['abc', 'xyz', 'aba', '1221']
Output : 2
'''

words = ['abc', 'xyz','aba','1221']
count = 0

for word in words:
    if len(word) >= 2 and word[0] == word[-1]:
        count += 1

print(count)


#6
'''
[5] Write a Python program to remove duplicate number from a list.

Input: [10,12,20,22,10]
Output: [10,12,20,22]
'''
numbers = [10,12,20,22,10,0,0,0,0,-1,-56]
unique = []

for num in numbers:
    if num not in unique:
        unique.append(num)

print(unique)