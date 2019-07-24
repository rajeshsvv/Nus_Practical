# Sharing data between Processes Using Queue

# what kind of problem it can solve

 # multiple processes have their own space They dont share the address space.

import multiprocessing

# Child Process
def square_numbers(numbers,q):

     for n in numbers:
            q.put(n*n)

# Parent Process
if __name__=="__main__":
    numbers=[2,3,4,5]
    q=multiprocessing.Queue()
    p=multiprocessing.Process(target=square_numbers,args=(numbers,q))

    p.start()
    p.join()

    while q.empty() is False:
        print(q.get())
