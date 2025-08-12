#1
thisset = {"apple", "banana", "cherry"}
print(thisset)

#2
thisset = {"apple", "banana", "cherry", "apple"}
print(thisset)

#3
thisset = {"apple", "banana", "cherry", True, 1, 2}
print(thisset)

#4
thisset = {"apple", "banana", "cherry", False, True, 0}
print(thisset)

#5
thisset = {"apple", "banana", "cherry"}
thisset.add("orange")
print(thisset)

#6
thisset = {"apple", "banana", "cherry"}
thisset.discard("banana")
print(thisset)

#7
thisset = {"apple", "banana", "cherry"}
x = thisset.pop()
print(x)
print(thisset)

#8
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2)
print(set3)

#9
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

set3 = set1 | set2
print(set3)

#10
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"John", "Elena"}
set4 = {"apple", "bananas", "cherry"}

myset = set1.union(set2, set3, set4)
print(myset)

#12
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.intersection(set2)
print(set3)

#13
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1.symmetric_difference(set2)

print(set3)

#14
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1 ^ set2

#15
set1 = {1,2,3,4,5,6}
set1.remove(3)
print(set1)

try:
    set1.remove(10)
except KeyError as e :
    print("Error:", e)

set1.discard(4)
print(set1)

set1.discard(10)
print(set1)

#16
li = [1,2,2,3,3,4,5,5,6,2]
set1 = set(li)
print(set1)

s = "GeeksForGeeks"
set1 = set(s)
print(set1)

d = {1: "One", 2: "Two", 3: "Three"}
set1 = set(d)
print(set1)


<<<<<<< HEAD

tdbbektghoedbgblsdnlfgnsdngn

rgkejkrgkke g jkrf gjkasdgjkasklasngl

fd aj jker gjerhg re gjaeh gja sjd  
=======
jhydhjdsghdghtuerthdrthdsrur
>>>>>>> a79d9be134ef252e87f9167e22d2de03cfb4c180
