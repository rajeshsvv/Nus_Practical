print("Hello world")

'''
Match Function:

This method is used to test whether a regular expression matches a specific string in Python. 
The re.match(). 
The function returns 'none' of the pattern doesn't match or 
includes additional information about which part of the string the match was found.


syntax:
re.match (pattern, string, flags=0)
Here, all the parts are explained below:

match():    is a method
pattern:     this is the regular expression that uses meta-characters to describe what strings can be matched.
string:     is used to search & match the pattern at the string's initiation.
flags:      programmers can identify different flags using bitwise operator '|' (OR)


In the below example, the pattern uses meta-character to describe what strings it can match. 
Here '\w' means word-character & + (plus) symbol denotes one-or-more.


'''

# import re
# list=["mouse","cat","dog","no-match","peacock","insects"]
# for elements in list:
#     m=re.match("cat",elements)
#
# if m:
#     print(m)
# else:
#     print("nothing")


"""
Search Function:

It works in a different manner than that of a match. 
Though both of them uses pattern; but 'search' attempts this at all possible starting points in the string. 
It scans through the input string and tries to match at any location.

syntax:
re.search( pattern, strings, flags=0)
"""


# import re
# value="cyberdyne"
#
# g=re.search("(dy.*)",value)
#
# if g:
#     print("search:",g.group(0))
# s=re.match("(vi.*)",value)
#
# if s:
#     print("match:",m.group(1))


# Split function:
'''
The re.split() accepts a pattern that specifies the delimiter. 
Using this, we can match pattern & separate text data.
split()" is also available directly on a string & handles no regular expression.

Program to show how to use split():
'''

import re
value="two 2 four 4 six 6"
res=re.split("\D+",value)
print(dir(re))

for elements in res:
    print(elements)