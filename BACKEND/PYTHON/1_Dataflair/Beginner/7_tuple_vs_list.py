#The major difference is that a list is mutable, but a tuple isn’t.
#So, we use a list when we want to contain similar items, but use a tuple when we know what information goes into it.

person = ('ABC', 'admin', '12345')
groceries=['bread','butter','cheese']

# numbers=(1,2,3)
# numbers=4,5,6
# a,b,c=numbers
# print(numbers,a,b,c,type(numbers))


# import time
# print(time.localtime())
# print(dir(time))


#   a. A List is Mutable

# list1=[0,1,2,3,4,5,6,7]
# list1[1]=3
# print(list1)
#
# del list1[1:4]
# print(list1)
#
# nums=[1,2,3,4,5]
# nums[1:3]=[6,7,8]
# print(nums)


# mytuple=0,1,2,3,4,5,6,7
# a,b,c,d,e,f,g,h=mytuple
# print(a,b,c,d,e,f,g,h)


#   As is visible, we can slice it to access it, but we can’t delete a slice. This is because it is immutable.

# Some python functions apply on both, these are- len(), max(), min(), sum(), any(), all(), sorted().
# We’ll take just one example here for both containers.

# s=max((1,3,-1))
# print(s)
#
# s=max([1,5,8])
# print(s)


#Lists and tuples share the index() and count() methods. But other than those, there are a few methods that apply to lists.
# These are- append(), insert(), remove(), pop(), clear(), sort(), and reverse(). Let’s take an example of one of these.


#   7. Tuples in a List

mylist=[(1,2,3),(4,5,6)]
print(type(mylist))
print(type(mylist[0]))


#   8. Lists in a Tuple

mytuple=([1,2],[3,4],[5,6])
print(mytuple)

#   9. Nested Tuples

#   A tuple may hold more tuples, and this can go on in more than two dimensions.

mytuple=((1,2),(3,(4,5),(6,(7,(8,9)))))
print(mytuple[1][2][1][1][1])


