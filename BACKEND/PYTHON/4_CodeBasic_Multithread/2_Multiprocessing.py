# create two processes
# 1)first to calculate square of all numbers
# 2)to calculate  cube of all numbers.

import time
import multiprocessing

various_result=[]

def calc_square(numbers):
    global various_result
    for n in numbers:
        # time.sleep(5)
        print("squares",n*n)
        various_result.append(n*n)
    print("within process result",various_result)

def calc_qube(numbers):
    global various_result
    for n in numbers:
        # time.sleep(5)
        print("cubes",n*n*n)
        various_result.append(n*n*n)
    print("within process result", various_result)

if __name__=="__main__":
    arr=[2,3,8,9]
    p1=multiprocessing.Process(target=calc_square,args=(arr,))
    p2=multiprocessing.Process(target=calc_qube,args=(arr,))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print("result",str(various_result))
    print("Done")
