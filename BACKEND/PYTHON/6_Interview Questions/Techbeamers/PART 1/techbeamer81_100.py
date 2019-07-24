
# 100 Different ways to create an empty array

'''
import numpy

print(numpy.array([]))

print(numpy.empty(shape=(0,0)))
'''



            #       Write A Conditional Expression

'''
no_of_days=365
is_leap_year="Yes" if no_of_days==366 else "No"
print(is_leap_year)
'''

'''
def testGen(index):
    weekdays=["sun","mon","tue","wed","thu","fri"]
    yield weekdays[index]
    yield weekdays[index+1]
    yield weekdays[index+2]
    yield weekdays[index+3]
    yield weekdays[index+4]
    yield weekdays[index+5]

day =testGen(0)
print(next(day),next(day),next(day),next(day),next(day),next(day))
'''


'''
weekdays=["sun","mon","tues","wed","thu","fri","sat","tues"]
lstring=" ".join(weekdays)

print(lstring)

weekdays = ['sun','mon','tue','wed','thu','fri','sat']
listAsTuple = set(weekdays)
print(listAsTuple)


weekdays = ['sun','mon','tue','wed','thu','fri',"sat","Riya"]
listAsDict = dict(zip(weekdays[1::2],weekdays[1::3]))
print(listAsDict)
'''

#98 count the items in list
import collections

'''
weekdays=["sun","mon","tues","wed","thu","fri","sat"]
print(weekdays.count("sun"))
result=([[y,weekdays.count(y)] for y in set(weekdays)])
print(result)
'''

                        #   Enumerate Function

'''
alist=["apple","mango","banana"]
astr="mosambi"

list_obj=enumerate(alist)
str_obj = enumerate(astr)

print("list_obj type:", type(list_obj))
print("str_obj type:", type(str_obj))

print(list(enumerate(alist)))
# Move the starting index to two from zero
print(list(enumerate(astr, 1)))
'''

                # 83  use of Global() Function
'''
x=9

def fun():
    y=3
    z=y+x
    #calling the globals function
    z=globals()['x']=z
    return z

ren=fun()
print(ren)
'''

                # 84 Zip() Method

'''
emp=["tom","john","jerry","jake"]
age=[32,25,65,98]
dept=["HR","Accounts","R & D","IT"]

out=zip(dept,emp,age)

out=set(out)

print((out))
print(list(out))
print(tuple(out))
'''


                # 85 static and instance variables

'''
class OOPS:
    var="programming"
    def __init__(self,another):
        self.another=another


test1=OOPS(1)
test2=OOPS(2)

print(test1.another)
print(OOPS.var)
print(test1.var)
'''



# how to monitor a python program
import sys

def trace_calls(frame, event, arg):
    # The 'call' event occurs before a function gets executed.
    if event != 'call':
        return
    # Next, inspect the frame data and print information.
    print('Function name=%s, line num=%s' % (frame.f_code.co_name, frame.f_lineno))
    return

def demo2():
    print('in demo2()')

def demo1():
    print('in demo1()')
    demo2()

sys.settrace(trace_calls)
demo1()
