# https://www.techbeamers.com/python-programming-questions-list-tuple-dictionary/
# Tuples


'''
init_tuple = (1,.2,3)
print(init_tuple.__len__())                 # answer:0
'''


"""
init_tuple_a = 'a', 'b',
init_tuple_b = ('a', 'b')
print (init_tuple_a == init_tuple_b)                     # answer:True
"""


'''
init_tuple_a = '1', '2'
init_tuple_b = ('3', '4')
print (init_tuple_a + init_tuple_b)                     #   answer:('1', '2', '3', '4')
'''


'''
init_tuple_a = [1, 2]
init_tuple_b = [3, 4]
[print(sum(x)) for x in [init_tuple_a + init_tuple_b]]      #   answer:10
'''

'''
init_tuple = [(0, 1), (1, 2), (2, 3)]
result = sum(n for _,n in init_tuple)
print(result)                                                #   answer:6
'''



'''
Tuples have structure, lists have an order
Tuples are immutable, lists are mutable.
'''


'''
l = [1, 2, 3]
init_tuple = ('Python',) * (l.__len__() - l[::-1][0])
print(init_tuple)                                                   #       answer: ()
'''


'''
init_tuple = ('Python') * 0
print(type(init_tuple))                                             #       answer:str
'''


'''
init_tuple = (1,) * 3
init_tuple[0] = 2
print(init_tuple)                                #   answer:tuple object does not support item assignment
'''


'''
init_tuple = ((1, 2),) * 7
print(len(init_tuple[3:8]))                             #         answer:4
'''