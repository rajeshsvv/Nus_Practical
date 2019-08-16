'''
list=[]
for i in range(0,5):
    list.append(i*2)
    print(i)
print('---')
print(i)

list=[n for n in list]
print(list)

dict={i:i**2 for i in range(10) if(i%2>0)}
print(dict)

import random
import sys
print(random.randrange(0,2))
print(random.randrange(0,2,1))
print(random.uniform(0,1))
'''


'''
from datetime import date

class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    #class method to create a Person Object by birth Year
    @classmethod
    def fromBirthYear(cls,name,year):
        return cls(name,date.today().year-year)

    # a static method to check if a person is adult or not
    @staticmethod
    def isAdult(age):
        if age>18:
            print("Elder")
        else:
            print("Younger")
        # return age>18

person1=Person('mayank',10)
person2=Person.fromBirthYear('mayank',1996)

print(person1.age)
print(person2.age)

# print(Person.isAdult(103))
Person.isAdult(52)
'''


