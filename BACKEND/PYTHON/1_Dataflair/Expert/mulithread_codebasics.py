# refer link for threading https://www.youtube.com/watch?v=EvbA3qVMGaw

#codebasics

#   for a given list of numbers print square and cube of every numbers

import threading


# print(threading.enumerate())


# mydata=threading.local()
# mydata.x=7
# print(mydata)
# threading.Thread.start(threading.current_thread())


import time
import threading

def square(numbers):
    print("calculate square numbers")
    for n in numbers:
        time.sleep(1)
        print("square",n*n)


def cube(numbers):
    print("calculate qubical numbers")
    for n in numbers:
        time.sleep(.1)
        print("cube",n*n*n)

arr=[2,3,8,9]


t=time.time()
# square(arr)
# cube(arr)
t1=threading.Thread(target=square,args=(arr,))
t2=threading.Thread(target=cube,args=(arr,))

t1.start()
t2.start()

t1.join()
t2.join()

print("done in :",time.time()-t)
print("Iam done with all my program now")
