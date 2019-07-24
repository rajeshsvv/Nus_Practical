# Python is one of the most successful interpreted languages.
# When you write a Python script, it doesn’t need to get compiled before execution


'''
def extendList(val, list=[]):
    list.append(val)
    return list

# def extendList(val, list=None):
#     if list is None:
#         list=[]
#     list.append(val)
#     return list

list1 = extendList(10,)
list2 = extendList(123,[])
list3 = extendList('a',)



print("list1 = %s" % list1)
print("list2 = %s" % list2)
print("list3 = %s" % list3)


# reason:It works like this because the calculation of expressions (in default arguments)
# occurs at the time of function definition, not during its invocation.
'''

'''
letter="hai sentdex"
for i in letter:
    if i=="x":
        pass
        print("pass statement is execute")
else:
    print("i")
    
'''




#Q-4: What’s The Process To Get The Home Directory Using ‘~’ In Python?
import os
print(os.path.expanduser("~"))



'''
#12 Regular Expression
import re
print(re.search(r"[0-9a-zA-Z.]+@[a-zA-Z]+\.(com|co\.in)$","micheal.pages@mp.com"))
'''



list = ['a', 'b', 'c', 'd', 'e']
# print(list[10])           #    in case of accessing it will give index out of range error
# print(list[10:])          #    in case of slicing it will give []



# for i in range(1,5):
#     print(i,end="")             #1,2,3,4
#     print(" ")

# for i in range(5):
#     print(i,end="")             #0,1,2,3,4


'''
string="python tutorial"

print(string)
result=','.join(string)
print(result)
pure=result.split('_')
print(pure)
'''


str1 = "Bob,"
str2 = "Bobby"
b3=4.006359
print("Hello %s hello %s hello %s" %(str1, str2,b3))
print(("Hello {0} hello {1}".format(str1, str2)))
print(f'name1:{str1.isupper()},name2:{str2.islower()}')
# print("name:%,name:s")


                                                # END


print("Let's learn " , end = '')
print("Python")

# Printing a dot in the end.
print("Learn to code from techbeamers" , end = "-")
print("com", end = ' ')

                                                # LENGTH



string="Enter into the new dragon"
# value=len(string)

print(len(string))








