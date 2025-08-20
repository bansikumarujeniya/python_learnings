'''
#1 Write a Python program to calculate the length of a string.

str = "w3school"

print(len(str))

#2 Write a Python program to get a string made of the first 2 and last 2 characters of a given string. If the string length is less than 2, return the empty string instead.

str = "w3school"

if len(str) < 2 :
    print("")
else:
    result = str[0:2] + str[-2:]
    print(result)


#3 Write a Python program to get a string from a given string where all occurrences of its first char have been changed to '$', except the first char itself.

str = "test"

fc = str[0]
rest = str[1:]
changed = rest.replace(fc, "$")
result = fc + changed

print(result)

#4  Write a Python program to change a given string to a newly string where the first and last chars have been exchanged.

str = "xyz"

first = str[0]
last  = str[-1]
middle = str[1:-1]

result = last + middle + first
print(result)

#5  Write a Python program to perform uppercase of the later part of the string.

str = "w3school"

half_index = len(str) // 2
fp = str[:half_index]
sp = str[half_index:]
result = fp +  sp.upper()
print(result)

'''

#6
s1 = "Test"
s2 = "TEST"
abc = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
       "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z",
       "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M",
       "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
f1 = [0] * 52
f2 = [0] * 52
l1 = l2 = 0
for a in s1:
    l1+=1
for b in s2:
    l2+=1
if l1 is not l2: print("The strings have different lengths.");exit()
for s, f in [(s1, f1), (s2, f2)]:
    i = 0
    while 1:
        try:
            c = s[i]
        except:
            break
        j = 0
        while 1:
            try:
                if c in abc[j]: f[j] += 1;break
                j += 1
            except:
                break
        i += 1
i = 0
while i is not 52:
    if f1[i] is not f2[i]:
        print("False");exit()
    i = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
         21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37,
         38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52][i]
print("True")


#7
set1 = {"apple", "banana", "cherry"}
set2 = {"cherry", "microsoft", "apple"}

set3 = set1 ^ set2

print(set3)
