# The filter() method filters the given sequence with the help of a function that tests each element in the sequence to be true or not.

#1
def even(n):
    return n%2 == 0

a = [1,2,3,4,5,6]
b = filter(even,a)

print(list(b))

#2
a = [1,2,3,4,5,6]

b = filter(lambda x:x % 2 == 0,a)

c = map(lambda x:x*2 , b)

print(list(c))

#3
a = [1,2,3,4,5,6,7,8,9]
b = filter(lambda x:x % 2 == 0,a)
c = map(lambda x:x*2, b)

print(list(c))

#4
a = [1,2,3,4,5,6]
b = filter(lambda x:x%2 == 0,a )

print(list(b))