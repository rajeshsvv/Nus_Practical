

str="""First, we focus on Python sets. A set in Python holds a sequence of values. 
It is sequenced but does not support indexing"""
import random

# a={1,3,2,5,8,9}
# print(a)
# print(type(a))
#
# a={2,3,4}
# print(type(a))




#   A set is mutable, but may not contain mutable items like a list, set, or even a dictionary

# d={[1,2,3],4,(2,3,4,4,5,5)}
# # print(d)
#
# d={}
# print(d)

#   Also, since sets do not support indexing, they cannot be sliced. Let’s try slicing one.


#   Again, because a set isn’t indexed, you can’t delete an element using its index

# numbers={3,2,1,4,6,5}
# print(numbers)
# numbers.discard(2)
# print(numbers)
#
numbers={3,2,1,4,6,5}
# print(numbers)
# numbers.remove(5)
# print(numbers)


# discard() vs remove()-
# These two methods may appear the same to you, but there’s actually a difference.
# If you try deleting an item that doesn’t exist in the set, discard() ignores it, but remove() raises a KeyError.


#pop()   no need to pass index here because set does not support indexing
#clear()


#   d. Updating a Set by using           add()              and               update() methods
numbers.add(100)
print(numbers)
numbers.update([2,8,7,4])
print(numbers)



#           Functions on sets
#  len()            max()               min()               sum()
#   any()           all()               sorted()

#           Methods on sets

#   union()                         intersection()              difference()                        symmetric_difference()
#   intersection_update()           difference_update()         symmetric_difference_update()       copy()
#   isdisjoint()                    issubset()                  issuperset()


#i. The frozenset
#   A frozen set is in-effect an immutable set.
#   You cannot change its values. Also, a set can’t be used a key for a dictionary, but a frozenset can.

a={frozenset([1,2]):3}
print(type(a))


days=True
print(days)
print(type(days))