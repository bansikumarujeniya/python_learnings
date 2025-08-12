#1
a = "Hello, World!"
print(a[1])

#2
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)

#3
a = "Hello"
print(a)


#4
for x in "banana":
    print(x)

#5
a = "Hello,World!"
print(len(a))

#6
txt = "The best things in life are free!"
print("free" in txt)


#7
b = "Hello, World!"
print(b[2:5])

#8
b = "Hello, World!"
print(b[:2])

#9
b = "Hello, World!"
print(b[-5:-2])

#10
a = "Hello, World!"
print(a.upper())

#11
a = "Hello, World!"
print(a.lower())

#12
a = " Hello, World! "
print(a.strip())

#13
a = "Hello,world"
print(a.replace("H","J"))
print(a.split(","))

#14
a = "Hello"
b = "World"
c = a + b
print(c)

#15
a = "Hello"
b = "World"
c = a + " " + b
print(c)

#16
age = 36
txt = f"My name is John, I am {age}"
print(txt)

#17
#1
price = 59
txt = f"The price is {price} dollars"
print(txt)

#2
txt = f"The price is {price:.2f} dollars"
print(txt)

#3
txt = f"The price is {20 * 59} dollars"
print(txt)

#4
txt = "We are the so-called \"Vikings\" from the north."
print(txt)

#5
def count(s,c) :
    res = 0

    for i in range(len(s)) :

        if (s[i] == c):
            res = res + 1
    return res

str = "geeksforgeeks"
c = 's'
print(count(str,c))

#6
def count_in_string(ch,idx,s):
    if idx == len(s):
        return 0

    count = 0

    if s[idx] == ch:
        count += 1

    count += count_in_string(ch,idx+1,s)

    return count

if __name__ == "__main__" :
    str = "geeksforgeeks"
    c = 'g'
    print(count_in_string(c,0,str))