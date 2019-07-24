#in real time scenario when we call web service it will take time to give repsonse so in that time CPU
# ideal.so we have to do some task for CPU to make it performance optimization.

import time
import threading

various_result=[]
def calc_sqaures(numbers):
    # global vaarious_result
    print("Perform square numbers")
    for n in numbers:
        time.sleep(.2)
        print("square:",n*n)



def calc_qube(numbers):
    # global vaarious_result
    print("Perform Cube Numbers")
    for n in numbers:
        time.sleep(.2)
        print("cube:",n*n*n)

arr=[2,3,4,5]


t=time.time()

# print(calc_sqaures(arr))
# print(calc_qube(arr))

t1=threading.Thread(target=calc_sqaures,args=(arr,))
t2=threading.Thread(target=calc_qube,args=(arr,))

t1.start()
t2.start()

t1.join()
t2.join()

print("result",various_result)
print("done in",time.time())
print("Done all the work right now")