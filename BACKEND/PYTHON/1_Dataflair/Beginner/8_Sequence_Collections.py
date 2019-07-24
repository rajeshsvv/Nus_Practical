#sequence has a deterministic ordering, #but a collection does not.
#Examples of sequences include strings, lists, tuples, bytes sequences, bytes arrays, and range objects.
# Those of collections include sets and dictionaries


name=str()
print(name)

name=list(['Ayushi','Sharma'])
print(type(name))

print(bytes('hello','utf-8'))

#   Since Bytes Sequence is immutable, if we try to change an item, it will raise a TypeError.

a=bytes([1,2,3,4,5])
print(a)


#   e. Bytes Arrays
# In that article, we discussed this one too.
# A bytesarray object is like a bytes object, but it is mutable. It returns an array of the given byte size.

for i in range(7,0,-1):
    print(i)

print("\n")
s='banana'.index('n')
print(s)


#   6. Python Collections       Examples include sets and dictionaries
#   Python collection, unlike a sequence, does not have a deterministic ordering.

nums=set([1,3,2])
print(nums.discard(2))
print(nums)


a={(1,2,3):1,1:[1,2,3]}
print(a)