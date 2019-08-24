
import copy
a=[1,2,3]
b=a.copy()
print(a,b)
a.append(40)
print(b,a)

import copy
c=copy.deepcopy(a)
print(c,a)
c.append(5)
print(a,c)

print('---')

a={1:[1,2,3]}
b=a.copy()
print(a,b)
a[1].append(100)
print(a,b)

c=copy.deepcopy(a)
print(a,c)
a[1].append(300)
print(c,a)
