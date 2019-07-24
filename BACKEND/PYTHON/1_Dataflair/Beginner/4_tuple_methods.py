#   Built - in Methods



#           index()         This method takes one argument and returns the index of the first appearance of an item in a tuple.
#           count()         This method takes one argument and returns the number of times an item appears in the tuple

a=(1,2,3,2,4,5,2,5)
print(a.index(3))
print(a.count(5))
#
# a=(1,2,3)<(4,5,6)
# print(a)


#                               Iterating on a Python Tuple

# for i in (1,3,2):
#     print(i)

#                               12. Nested Tuples in Python

a=((1,2,3),(4,(5,6)))
print(a[1][1][0])

#   Python tuple may also contain other constructs, especially, lists.
#   After all, it is a collection of items, and items can be anything.

# tuple=(1,2,[3,4])
# print(tuple[2][0])