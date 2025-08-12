# The map() function is used to apply a given function to every item of an iterable, such as a list or tuple, and returns a map object (which is an iterator).
# map(function, iterable)

#1
s = ['1','2','3','4','5']
res = map(int,s)
print(list(res))

#2
a = [1,2,3,4]

def double(val):
    return val*2

res = list(map(double,a))
print(res)

#3
a = [1,2,3,4]

res = list(map(lambda x:x*2,a))
print(res)

#4
a = [1,2,3]
b = [4,5,6]

res = map(lambda x,y:x+y,a,b)
print(list(res))

#5
s = [' hello ',' world ',' python ']
res = map(str.strip,s)

print(list(res))

#6
celsius = [0,20,37,100]
fahrenhit = map(lambda c: (c * 9/5)  + 32, celsius)

print(list(fahrenhit))

#7
s = ['hello','world','python']
res = map(str.strip,s)

print(list(res))

#8
a = [7,8,9]
b = [10,11,12]

res = map(lambda x:x*2,a)
print(list(b))

#9
s = ['hello','pubg','BGMI']
res = map(str.strip,s)

print(list(res))
