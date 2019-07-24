'''

import random
list = [2, 18, 8, 4]
print("Prior Shuffling - 0", list)
random.shuffle(list)
print("After Shuffling - 1", list)
random.shuffle(list)
print("After Shuffling - 2", list)

print('{0:b}'.format(1))

langs = ['C', 'C++', 'CSharp',"Python"]
print('Skillset: {}'.format(langs))
print('Skillset: {0[3]}'.format(langs))


test = "I am into middle now."
print(test.split(","))

'''


'''

items=[]
for i in range(1,5):
    items.append(i*2)
print(items)

item={n:n**2 for n in range(10)}
print(item)


class Test:
    def __init__(self,name):
        self.name=name
        self.cars=[]
    def __str__(self):
        return "{} holds ".format(self.name)

obj=Test("name")
obj.name="Singam"
print(obj.name)

'''

# def multiplexers ():
#
#     return [lambda n: index * n for index in range (4)]
#
# print([m (2) for m in multiplexers ()])

class Taxi:

    def __init__(self, model, capacity, variant):
        self.__model = model      # __model is private to Taxi class
        self.__capacity = capacity
        self.__variant = variant

    def getModel(self):          # getmodel() is accessible outside the class
        return self.__model

    def getCapacity(self):         # getCapacity() function is accessible to class Vehicle
        return self.__capacity

    def setCapacity(self, capacity):  # setCapacity() is accessible outside the class
        self.__capacity = capacity

    def getVariant(self):         # getVariant() function is accessible to class Vehicle
        return self.__variant

    def setVariant(self, variant):  # setVariant() is accessible outside the class
        self.__variant = variant

class Vehicle(Taxi):

    def __init__(self, model, capacity, variant, color):
        # call parent constructor to set model and color
        super().__init__(model, capacity, variant)
        self.__color = color

    def vehicleInfo(self):
        return self.getModel() + " " + self.getVariant() + " in " + self.__color + " with " + self.getCapacity() + " seats"

# In method getInfo we can call getmodel(), getCapacity() as they are
# accessible in the child class through inheritance

v1 = Vehicle("i20 Active", "4", "SX", "Bronze")
print(v1.vehicleInfo())
print(v1.getModel()) # Vehicle has no method getModel() but it is accessible via Vehicle class

v2 = Vehicle("Fortuner", "7", "MT2755", "White")
print(v2.vehicleInfo())
print(v2.getModel()) # Vehicle has no method getModel() but it is accessible via Vehicle class

