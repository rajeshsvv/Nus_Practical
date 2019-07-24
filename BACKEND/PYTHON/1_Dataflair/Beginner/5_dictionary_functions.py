
"""create an empty dictionary here"""
# dict2={}
# print(dict2)
#
# print(type(dict2))

#                                   a. Python Dictionary Comprehension

# mydict={x:x*x for x in range(0,10) if x%2==0}
# print(mydict)
#
# dict3={1:'carrots','two':[1,2,3]}
# print(dict3)

#Using the dict() function, you can convert a compatible combination of constructs into a Python dictionary
# dict2=dict(([1,2],[2,4],[3,6]))
# print(dict2)
# dict=dict({1:2,3:4,5:6})
# print(dict)
# print(type(dict))

#
# mydict2={1:2,1:3,1:9,2:4}
# print(mydict2)
#
# print(mydict[8])
#
# print(mydict.get(64))





"""a. Updating the Value of an Existing Key"""

# dict4={1:1,2:2,3:3}
# dict4[2]="Sree"
# print(dict4)

"""b. Adding a new key"""

# dict4[4]="Edureka"
# print(dict4)


"""b. Deleting a single key-value pair"""

dict4={1:1,2:2,3:3,4:4}
del dict4
print(dict4)


#   7. In-Built Functions on a Python Dictionary

#       any()                           len()                    all()                              sorted()


# dict4={3:3,1:1,4:4}
# s=sorted(dict4)
# print(type(s))

#   7. In-Built Methods on a Python Dictionary

#       keys()                      values()             items()             get()            clear()         copy()
#       pop()                       popitem()              fromkeys()         update()

# s=any({False:False,'':''})
# print(s)




#               11. Nested Dictionary

# dict1={4:{1:2,2:4},8:16}
# print(dict1)
# print(dict1[4])
