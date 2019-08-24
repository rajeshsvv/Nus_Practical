x=[7,6,8,5,9]
print(x[2:2])


y="Hello"
print(y[:-3:])

print(list(range(9,-2,1)))
print(list(range(-2,-9,-1)))

from collections import Counter
print(Counter([1,3,2,1,4,2,1,3,1,50,50,60,600]))
print(Counter(['Hari',"Sekhar","Ranjith","Hari"]))
print(Counter({1:2,2:3,4:5,4:6,5:9}))


a=[1,2]
b=a
print(a,b)

a[1]=9
print(a,b)
del b
# print(a,b)