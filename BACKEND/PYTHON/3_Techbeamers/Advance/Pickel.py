listofCountries = ["India","America","England","Germany","Brazil","Vietnam"]
firstLetters = [ country[:3:-1] for country in listofCountries]
print(firstLetters)

# print(list(range(10)))
# for i in range(10):
#     print(i)

string='HelloRajaSekhar'
result=string[-3:-8:-2]
print(result)


import copy
list1=[1,2,3,4,5,6]

list2=list1.copy()

print(list1,list2)

list1.append(10)
print(list1,list2)

list3=copy.deepcopy(list1)
print(list1,list3)
list1.append(11)
print(list1,list2)