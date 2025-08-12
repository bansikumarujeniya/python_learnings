# A RegEx, or Regular Expression, is a sequence of characters that forms a search pattern.
# RegEx can be used to check if a string contains the specified search pattern.

#1 Python has a built-in package called re, which can be used to work with Regular Expressions.

# import re

#2
import re

txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)

if x:
    print("YES! We have a match!")
else:
    print("No match")

#3 regex function :- The re module offers a set of functions that allows us to search a string for a match:

'''
#1 The findall() function returns a list containing all matches.

'''
import re

txt = "The rain in Spain"
x = re.findall("ai", txt)
print(x)

'''
#2 The search() function searches the string for a match, and returns a Match object if there is a match.
If there is more than one match, only the first occurrence of the match will be returned:

'''

import re

txt = "The rain in Spain"
x = re.search("\s", txt)

print("The first white-space character is located in position:", x.start())

'''
#3  The split() function returns a list where the string has been split at each match:
'''

import re

txt = "The rain in Spain"
x = re.split("\s", txt)
print(x)



