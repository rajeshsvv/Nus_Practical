    '''

                            Online Python Interpreter.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''

# print("Hello World")


# knights = {'gallahad': 'the pure', 'robin': 'the brave',"Johnson":"Harley"}

# for k,v in knights.items():
#     print(k,v)
    
# for k,v in enumerate(["tic","tac","videos"]):
#         print(k,v)        
        
# questions = ['name', 'quest', 'favorite color']
# answers = ['lancelot', 'the holy grail', 'blue']

# for q,v in zip(questions,answers):
#     # print("what is your {0} It is {1}".format(q,v))
#     print({f"what is your {q} It is {v}"})

# for i in reversed(range(1, 10, 2)):
#     print(i)
    
# basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
# for f in sorted(set(basket)):
#     print(f)
    
# import math
# raw_data = [56.2, 51.7, 55.3, 52.5, float('NaN'),47.8]
# filtered_data = []
# for value in raw_data:
#     if not math.isnan(value):
#         filtered_data.append(value)
        
# print(filtered_data)

# import sound.effects.echo
# import sound.effects.surround
# from sound.effects import *

# import logging
# logging.debug('Debugging information')
# logging.info('Informational message')
# logging.warning('Warning:config file %d not found', 'server.conf')
# logging.error('Error occurred Execute Anyway')
# logging.critical('Critical error -- shutting down')

# import weakref, gc
# class A:
#     def __init__(self, value):
#          self.value = value
#     def __repr__(self):
#          return str(self.value)

# a = A(10)                   # create a reference
# d = weakref.WeakValueDictionary()
# d['primary'] = a            # does not create a reference
# d['primary']                # fetch the object if it is still alive
# 10
# del a                       # remove the one reference
# gc.collect()                # run garbage collection right away


from array import array
a = array('H', [4000, 10, 700, 22222])
print(sum(a))
print(a[1:3])

# from collections import deque
# d = deque(["task1", "task2", "task3"])
# d.append("task4")
# print("Handling", d.popleft())

