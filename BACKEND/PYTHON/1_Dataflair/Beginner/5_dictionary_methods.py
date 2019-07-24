# mydict2={1:2,2:3,1:4,2:4,1:5,2:1}
# print(mydict2)


# built in functions

#len()      any()       all()       sorted()

# sort function will sort the values for the keys not the values
# dict4={3:3,1:1,4:4,6:9,0:1}
# print(sorted(dict4))


#1   keys()
#   The keys() method returns a list of keys in a Python dictionary.

dict4  ={3: 3, 1: 1, 4: 9, 5:9}
# dict4.keys()
# print(dict4)

#2  values()
# b. values()
# Likewise, the values() method returns a list of values in the dictionary.

# s=dict4.values()
# print(s)


# 3. items()
# This method returns a list of key-value pairs.

# print(dict4.items())

# 4. get()#
# It takes one to two arguments.
# While the first is the key to search for, the second is the value to return if the key isn’t found.
# The default value for this second argument is None.
# print(dict4.get(3,0))
# print(dict4.get(1,0))


# 5. clear()
# The clear function’s purpose is obvious. It empties the Python dictionary.

# dict4.clear()
# print(dict4)


# 6. copy()

# newdict=dict4.copy()
# print(newdict)


# 7. pop()
# This method is used to remove and display an item from the dictionary.
# It takes one to two arguments. The first is the key to be deleted,
# while the second is the value that’s returned if the key isn’t found.

# dict4.pop(5)
# print(dict4)
#
#
# However, unlike the get() method, this has no default None value for the second parameter.
#
# >>> newdict.pop(5)
# Traceback (most recent call last):
#
# File “<pyshell#191>”, line 1, in <module>
#
# newdict.pop(5)
#
# KeyError: 5

# As you can see, it raised a KeyError when it couldn’t find the key.

# 8 popitem()
#As you can see, the same pair was popped. We can interpret from this that
# the internal logic of the popitem() method is such that for a particular dictionary, it always pops pairs in the same order.

# newdict={3:3,1:1,4:4,7:7}
# newdict.popitem()
# print(newdict)



#9.fromkeys()
# i. fromkeys()
# This method creates a new Python dictionary from an existing one. To take an example,
# we try to create a new dictionary from newdict. While the first argument
# takes a set of keys from the dictionary, the second takes a value to assign to all those keys. But the second argument is optional.

# dict4  ={3: 3, 1: 1, 4: 9, 5:9}
# s=dict4.fromkeys({1,2,3,4,7},)
# print(s)


# 10. update()
# The update() method takes another dictionary as an argument.
# Then it updates the dictionary to hold values from the other dictionary that it doesn’t already.

dict1={1:1,2:2,5:5}
dict2={2:2,3:3,1:1}
dict1.update(dict2)
print(dict1)


dic={1:1,2:2,9:9,8:8,5:5,4:6,2:4}
print(dic)