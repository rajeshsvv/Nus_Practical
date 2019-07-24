# within process we get result set.. but outside we did not get result set.
# so for this we need shared memry concept
# and do this in two ways either in value or array.

    # 1 st scenario
# import multiprocessing
#
# result=[]
# def square_numbers(numbers):
#     global result
#     for n in numbers:
#         print("square",n*n)
#         result.append(n*n)
#     print("inside process", result)
#
# if __name__=="__main__":
#     numbers=[2,3,4,5]
#     p1=multiprocessing.Process(target=square_numbers,args=(numbers,))
#
#     p1.start()
#     p1.join()
#
#     print("outside process:",str(result))


#         # 2nd scenario use shared memory by Array
# import multiprocessing
#
#
# def square_numbers(numbers,result):
#     for idx,n in enumerate(numbers):
#         result[idx]=n*n
#     print("inside the process",result[:])
#
#
# if __name__=="__main__":
#     numbers=[2,3,4,5]
#     result=multiprocessing.Array('i',4)
#     p1=multiprocessing.Process(target=square_numbers,args=(numbers,result))
#
#     p1.start()
#     p1.join()
#
#     # print("outside process:",str(result))             # u get synchronize array wrapper
#     print("outside the process",result[:])              # u get result

        # 3rd scenario use shared memory by Value
import multiprocessing


def square_numbers(numbers,result,v):
    v.value=50.67
    for idx,n in enumerate(numbers):
        result[idx]=n*n
    print("inside the process",result[:])


if __name__=="__main__":
    numbers=[2,3,4,5]
    result=multiprocessing.Array('i',4)
    v=multiprocessing.Value("d",22)
    p1=multiprocessing.Process(target=square_numbers,args=(numbers,result,v))


    p1.start()
    p1.join()

    # print("outside process:",str(result))             # u get synchronize array wrapper
    print("outside the process",result[:])              # u get result
    print(v.value)