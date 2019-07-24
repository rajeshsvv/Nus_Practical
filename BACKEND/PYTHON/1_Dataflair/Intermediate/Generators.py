#A Python generator is a kind of an iterable, like a Python list or a python tuple.
# It generates for us a sequence of values that we can iterate on.
# You can use it to iterate on a for-loop in python, but you can’t index it

# def counter():
#     i=1
#     while i<10:
#         yield i
#         i+=1
#
# for i in counter():
#     print(i)



# def even(x):
#     while(x>0):
#         if x%2==0:
#             yield 'Even'
#         else:
#             yield "odd"
#         x-=1
# for i in even(8):
#     print(i)


# def square_numbers(x):
#     for i in range(x):
#         if i**2%2==0:
#             yield i**2
#
# print(list(square_numbers(9)))


# mylist=(3,6,9,1,2)
# s=(x**2 for x in mylist)
#
# print(s)
# print(next(s))
# print(next(s))
# print(next(s))
# print(next(s))
# print(next(s))
# print(next(s))
#
#
# # for i in s:
# #     print(i)
# print(type(mylist))


