#           Python Tuples Packing

b=1,2.0,"three",
x,y,z=b
print(b)
print(type(b))
percentages=(99,95,90,89,93,96)
a,b,c,d,e,f=percentages
# print(a,b,d,e,f,c)
# print(type(percentages))
# print(percentages[1])

# print(percentages[2:-1])
# print(percentages)
# print(percentages[:-2])
# print(percentages[2:-3])
# print(percentages[:])
# del percentages[:2]    tuple does not support item deletion
# print(percentages)
# del percentages
# print(percentages)

# percentages[3]=9      tuple does not support item assignment
# print(percentages)


#                                   13. Built-in List Functions
#A lot of functions that work on lists work on tuples too.
# A function applies on a construct and returns a result. It does not modify the construct

# sum()          max()       min()              any()
# all()         tuple()      sorted()            len()

h=max(('Hi','hi','Hello'))
print(h)

# b=max(('Hi', 9))              #  not supported between instances of 'int' and 'str'
# print(b)


a=any(('','0',''))                  #If even one item in the tuple has a Boolean value of True, then this function returns True
print(a)

b=any(('',0,''))                   #The string ‘0’ does have a Boolean value of True. If it was rather the integer 0
print(b)

#
# list=[1,2,3,4,5,6]
# print(tuple(list))
#
string1="string"
print(tuple(string1))
#
# set1={2,1,3}
# print(tuple(set1))
# print(set1)

#