# import more_itertools
# import timeit
# import random
#
# subStrings = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat']
#
#
# def simpleString(subStrings):
#     finalString = ''
#     for part in subStrings:
#         finalString += part
#     return finalString
#
#
# def formatString(subStrings):
#     finalString = "%s%s%s%s%s%s%s" % (subStrings[0], subStrings[1],
#                                       subStrings[2], subStrings[3],
#                                       subStrings[4], subStrings[5],
#                                       subStrings[6])
#     return finalString
#
#
# def joinString(subStrings):
#     return ''.join(subStrings)
#
#
# print('joinString() Time   : ' + str(
#     timeit.timeit('joinString(subStrings)', setup='from __main__ import joinString, subStrings')))
# print('formatString() Time : ' + str(
#     timeit.timeit('formatString(subStrings)', setup='from __main__ import formatString, subStrings')))
# print('simpleString() Time : ' + str(
#     timeit.timeit('simpleString(subStrings)', setup='from __main__ import simpleString, subStrings')))
#


'''

class Employee:
    def __init__(self, name, workexp):
        self.name = name
        self.workexp = workexp
        self._avgsal = workexp * 2.5 * 100000
        self.skills=""

    @property
    # Relocated the logic for returning work exp to a new method.
    def getAvgSal(self):
        return self._avgsal

    def skills(self):
        return self.skills





emp = Employee("Python Programmer", 4)
print(emp.getAvgSal)
print(emp.skills)

'''

alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i','o']
vowels = ['a', 'e', 'i', 'o', 'u']


output = list(filter(lambda x: (x in vowels), alphabets))


print(output)