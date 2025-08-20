'''

#1 Write a program to print the following number pattern using a loop.
	1
	1 2
	1 2 3
	1 2 3 4
	1 2 3 4 5

'''

for i in range(1,6):
    for j in range(1, i+1):
        print(j,end = " ")
    print()

'''

#2 Write a program to print the following number pattern using a loop.
	2 
	2 4 
	2 4 6 
	2 4 6 8 
	2 4 6 8 10
	
'''

for i in range(1,6):
    for j in range(1, i+1):
        print(j*2,end = " ")
    print()

'''

#3 Write a program to print the following number pattern using a loop.
	2 4 6 8 10
	  2 4 6 8 
	    2 4 6 
	      2 4 
		    2

'''

for i in range(5,0,-1):
    print("  " * (5 - i),end = "")
    for j in range(1, i+1):
        print(j*2,end = " ")
    print()


'''

#4 Write a program to print the following number pattern using a loop.

	1                  2
	1 3              4 2
	1 3 5 	       6 4 2
	1 3 5 7      8 6 4 2
	1 3 5 7 9 10 8 6 4 2
	1 3 5 7      8 6 4 2
	1 3 5 	       6 4 2
	1 3 		     4 2
	1 		           2


'''
left = [1,3,5,7,9]
right = [10,8,6,4,2]

for i in range(5):
    for j in range(i+1):
        print(left[j],end=" ")

    if i != 4 :
        space = (4 - i) * 2
        print("  " * space,  end = " ")

    for j in range(5 - i - 1 , 5):
        print(right[j], end = " ")
    print()

for i in range(3,-1,-1):
    for j in range(i + 1):
        print(left[j], end = " ")

    space = (4 - i) * 2
    print("  " * space, end = " ")

    for j in range(5 - i - 1, 5):
        print(right[j], end=" ")
    print()
