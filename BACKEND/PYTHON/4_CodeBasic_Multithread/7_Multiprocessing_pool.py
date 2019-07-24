
# def f(n):
#     return n*n
#
#
# if __name__=="__main__":
#     array=[1,2,3,4,5]
#
# result=[]
# for n in array:
#     result.append(f(n))
#
# print(result)



# from multiprocessing import Pool
#
# def f(n):
#     return n*n
#
#
# if __name__=="__main__":
#     array=[1,2,3,4,5]
#     p=Pool()
#     result=p.map(f,array)
#     print(result)


from multiprocessing import Pool
import time

def f(n):
     sum=0
     for x in range(1000):
         sum +=x*x
     return sum


if __name__=="__main__":
    t1=time.time()
    p=Pool()
    result=p.map(f,range(1000))
    p.close()
    p.join()

    print("Pool Link:",time.time()-t1)

    t2=time.time()
    result=[]
    for x in range(10000):
        result.append(f(x))

    print("Serial Processing Took:",time.time()-t2)


