'''
a = [1,2,2,3]
print(list(set(a)))


print(sum(range(1,10)))
'''

globvar = 0
def set_globvar_to_one():
    global globvar    # Needed to modify global copy of globvar
    globvar = 1
def print_globvar():
    print(globvar)     # No need for global declaration to read value of globvar
set_globvar_to_one()
print(print_globvar())


import copy

a={1:[1,2,3]}
# a=[1,2,3]
# a=[0,1,2,3]
b=a.copy()
print(a,b)
a[1].append(4)

# a.append(4)
print(a,b)

c=copy.deepcopy(a)
print(c,a)
a[1].append(5)

print(a,c)

