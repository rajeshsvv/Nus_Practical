# https://www.techbeamers.com/python-programming-questions-list-tuple-dictionary/'''

# Tuples have structure, lists have an order
# Tuples are immutable, lists are mutable.
# '''




"""
a=[1,2,3,4,5,6,7,8,9]
print(a[::2])                                               answer [1, 3, 5, 7, 9]
"""


'''
a=[1,2,3,4,5,6,7,8,9]
a[::2]=10,20,30,40,50,60
print(a)                       #    answer:ValueError: attempt to assign sequence of size 6 to extended slice of size 5
'''


'''
a=[1,2,3,4,5,6,7]
print(a[1::-2])                     # answer:[4, 3, 2]
'''


'''
def f(value, values):
    v = 1
    values[0] = 44
t = 3
v = [1, 2, 3]
f(t, v)
print(t, v[0])                         #  answer:3 44
'''


'''
import random
fruit=['apple', 'banana', 'papaya', 'cherry']
random.shuffle(fruit)
print(fruit)
'''


'''
data = [[[1, 2], [3, 4]], [[5, 6], [7, 8]]]
def fun(m):
    v = m[0][0]

    for row in m:
        for element in row:
            if v < element: v = element

    return v
print(fun(data[0]))                                # answer:4
'''


arr = [[1, 2, 3, 4],[4, 5, 6, 7],[8, 9, 10, 11],[12, 13, 14, 15]]
for i in range(0,4):
    print(arr[i].pop())                           # answer:4 7 11 15



'''
def f(i, values = []):
    values.append(i)
    print (values)
    return True
f(1)
f(2)
f(3)
'''



'''
arr = [1, 2, 3, 4, 5, 6,7]
for i in range(1, 6):
    arr[i - 7] = arr[i]
for i in range(0, 7):
    print(arr[i], end = " ")
'''


'''
fruit_list1 = ['Apple', 'Berry', 'Cherry', 'Papaya']
fruit_list2 = fruit_list1
fruit_list3 = fruit_list1[:]

fruit_list2[0] = 'Guava'
fruit_list3[1] = 'Kiwi'

sum = 0
for ls in (fruit_list1, fruit_list2, fruit_list3):
    if ls[0] == 'Guava':
        sum += 1
    if ls[1] == 'Kiwi':
        sum += 20

print (sum)                                                             answer:22
'''



'''
init_tuple = ()
print (init_tuple.__len__())                                              answer:0
'''


'''
init_tuple_a = 'a', 'b'
init_tuple_b = ('a', 'b')

print (init_tuple_a == init_tuple_b)                                    answer:True
'''


'''
init_tuple_a = '1', '2'
init_tuple_b = ('3', '4')

print (init_tuple_a + init_tuple_b)                                 answer:('1', '2', '3', '4')
'''

'''
init_tuple_a = 1, 2
init_tuple_b = (3, 4)

[print(sum(x)) for x in [init_tuple_a + init_tuple_b]]               answer:10
'''

'''
init_tuple = [(0, 1), (1, 2), (2, 3)]
result = sum(n for _, n in init_tuple)
print(result)                                                         answer:6
'''


'''
l = [1, 2, 3]
init_tuple = ('Python',) * (l.__len__() - l[::-1][0])
print(init_tuple)                                                   #   answer: ()
'''


'''
init_tuple = ('Python') * 5
print(init_tuple,"\n")
print(type(init_tuple))                                            #  answer:str
'''


'''
init_tuple = (1,) * 3
init_tuple[0] = 2
print(init_tuple)                               #   answer:tuple object does not support item assignment
'''

'''
init_tuple = ((1, 2),) * 7
print(init_tuple)
print(len(init_tuple[3:8]))                     #   answer:4
'''


