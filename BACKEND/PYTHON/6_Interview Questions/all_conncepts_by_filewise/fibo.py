
def fib(a,n):
	a,b=0,1
	while a<n:
		print(a)
		a,b=a,a+b
	print()





import sys

print("This is the name of the project:",sys.argv[0])
print("Number of Arguments",len(sys.argv))
print("The Arguments are:",str(sys.argv))


'''
import sys
import os
for i in range(2,10):
	input_string="python count "+str(i)
	os.system(input_string)
print(len(sys.argv))
'''


'''
list1=[i for i in range(2,16,2) if i>10]
print(list1)
print("---")

list2 = [(x,x**2,y) for x in range(1,5) for y in range(2,4)]
print(list2)
'''

'''
list3=[[1 for i in range(3)] for j in range(5)]
print(list3)
'''



