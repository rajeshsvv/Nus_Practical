# Parameters are defined by the names that appear in a function definition,
# whereas arguments are the values actually passed to a function when calling it

# x=10
# def bar():
#     global x
#     print(x)
#     x-=1
#
# bar()
# print(x)

'''
def foo():
    x=10
    def bar():
        nonlocal x
        print(x)
        x+=1
    bar()
    print(x)
foo()

sqaures=[]

for i in range(4):
    sqaures.append(lambda:i**2)

sqaures[2]()
'''

'''
def func(foo, bar=None, **kwargs):
    print(f"{foo},{bar},{kwargs}")
func(23,45,krishna="Hareram")


def func2(a, b):
    a = 'new-value'        # a and b are local names
    b = b + 1              # assigned to new objects
    return a, b            # return new values

x, y = 'old-value', 99
x, y = func2(x, y)
print(x, y)
'''

#   Remove Duplicates from List
'''
mylist=[1,2,3,4,5,6,6,5,4,1,2,3]
# print(list(set(mylist)))
if mylist:
    mylist.sort()
    last = mylist[-1]
    for i in range(len(mylist)-2, -1, -1):
        if last == mylist[i]:
            del mylist[i]
        else:
            last = mylist[i]
print(mylist)
'''

A=[[None]*2]*3
print(A)


