'''
import copy
a=[1,2,3]
b=a.copy()
print(a,b)
a.append(40)
print( b,a)

print('-------')
import copy
c=copy.deepcopy(a)
print(c,a)
c.append(5)
print(a,c)

# print(c,a)

a={1:[1,2,3]}
b=a.copy()
print(a,b)
a[1].append(100)
print(a,b)

c=copy.deepcopy(a)
print(a,c)
a[1].append(300)
print(c,a)
'''


'''
x=9
def fun():
    y=3
    z=y+x
    z=globals()['x']=z
    return z
    ret=fun()
    print(ret)
'''

def dec_sample(fun):
    def dec_hook(*args,**kwargs):
        print("Before the function call")

        print("After the function call")
        result = fun(*args, **kwargs)
        return result
    return dec_hook

@dec_sample
def product(x,y):
    return x*y

print(product(2,3))

def fun(*args):
    for i in (args):
        print(i)
fun("Right now we are in flow")


def func(**kwargs):
    for emp,age in kwargs.items():
        print("%s age is %d" %(emp,age))
func(John=26,kalley=22,Manoj=52)
