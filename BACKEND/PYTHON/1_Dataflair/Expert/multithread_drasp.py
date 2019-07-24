# from threading import Thread
import threading
import time

tlock=threading.Lock()

def timer(name,delay,repeat):
    print("Timer: "+name+" Started")
    tlock.acquire()
    print(name+"has acquired the lock")
    while repeat>0:
        time.sleep(delay)
        print(name+":"+str(time.ctime(time.time())))
        repeat-=1
    tlock.release()
    print(name+"has releasing the lock")
    print("Timer: " +name+ " Completed")

def Main():
    t1=threading.Thread(target=timer,args=("Timer1",1,3))
    t2=threading.Thread(target=timer,args=("Timer2",2,3))
    t1.start()
    t2.start()

    print("Main Completed")

if __name__=="__main__":
    Main()



# custom thread
# import time
# import threading
#
# class AsyncWrite(threading.Thread):
#     def __init__(self,text,out):
#         threading.Thread.__init__(self)
#         self.text=text
#         self.out=out
#
#     def run(self):
#         f=open(self.out,'w')
#         f.write(self.text+'\n')
#         f.close()
#         time.sleep(1)
#         print("Finished background file to write to:"+self.out)
#
# def Main():
#     message=input("Enter a string to store:")
#     background=AsyncWrite(message,'out.txt')
#     background.start()
#     print("The program are continue to run while it write in another thread")
#     print("Super Drap you are")
#     background.join()
#
#     print("wait until thread was complete")
# if __name__=="__main__":
#     Main()