#1
thislist = ["apple", "banana", "cherry"]
print(thislist)

#2
thislist = ["apple", "banana", "cherry"]
print(len(thislist))

#3
list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]

print(list1 ,list2 , list3)

#4
list1 = ["abc", 34, True, 40, "male"]
print(list1)

#5
mylist = ["apple", "banana", "cherry"]
print(type(mylist))

#6
thislist = list(("apple", "banana", "cherry"))
print(thislist)

#7
thislist = ["apple", "banana", "cherry"]
print(thislist[1])

#8
thislist = ["apple", "banana", "cherry"]
print(thislist[-1])

#9
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])
print(thislist[3:])

#10
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[-4:-1])

#11
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)

#12
thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")
print(thislist)

#13
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)

#14
thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist)

#15
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)

#16
thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)

#17
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)

#18
thislist = ["apple", "banana", "cherry"]
for x in thislist:
    print(x)

#19
thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
    print(thislist[i])

#20
thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
    print(thislist[i])
    i = i + 1

#21
thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist]

#22
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
    if "a" in x:
        newlist.append(x)

print(newlist)

#OR
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if "a" in x]

print(newlist)


#23
thislist = [100, 50, 65, 82, 23]
thislist.sort()
print(thislist)

#24
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse=True)
print(thislist)

#25
thislist = [100, 50, 65, 82, 23]
thislist.sort(reverse=True)
print(thislist)

#26
def myfunc(n):
    return abs(n - 50)

thislist = [100, 50, 65, 82, 23]
thislist.sort(key=myfunc)
print(thislist)

#27
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort()
print(thislist)

#28
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key=str.lower)
print(thislist)

#29
thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)

#30
thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)
print(mylist)

#31
thislist = ["apple", "banana", "cherry"]
mylist = thislist[:]
print(mylist)

#32
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

for x in list2:
    list1.append(x)

print(list1)

#33
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list1.extend(list2)
print(list1)

#34
m = []

for i in range(5):
    m.append( [] )
    for j in range(5):
        m[i].append(j)

print(m)

#35
m = [["apple","banana","cherry"],["date","fig","grape"],["kiwi","lemon","mango"]]

mod_m = []
for r in m:
    mod_r = []
    for f in r:
        mod_r.append(f.capitalize())
    mod_m.append(mod_r)

print(mod_m)

#36 column wise sum of nested list
def column_sum(lst):
    res = []
    for i in range(0,len(lst)):
        s = 0
        for j in range(0,len(lst[i])):
            s += lst[j] [i]
        res.append(s)
    return res

lst = [[1,5,3], [2,7,8], [4,6,9]]
print(column_sum(lst))

