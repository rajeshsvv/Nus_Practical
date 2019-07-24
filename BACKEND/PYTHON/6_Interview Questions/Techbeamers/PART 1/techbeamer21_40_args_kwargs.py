'''
A docstring is a unique text that happens to be the first statement in the following Python constructs:
Module, Function, Class, or Method definition.
A docstring gets added to the __doc__ attribute of the string object.

print(), dir(), len(), and abs() etc. are basic built in functions.

'''
print(id(object))


                                            # ARGS
'''
def fun(*argList):
    for i in argList:
        print(i)
    return True

# fun('I','am',"Learning","python")
print(fun('I','am',"Learning","python"))
'''
                                            # KWARGS

'''
def fun(**kwargs):
    for emp,age in kwargs.items():
        # print(emp,name)
        # print("%s age is %d." %(emp,age))
        # print("{} age is {}".format(emp,age))
        print(f"{emp} age is {age}")
    return None


# fun(Naveen=25,Kalley=25,Tom=25)
print(fun(Naveen=25,Kalley=25,Tom=25))
'''

                                            # MAIN METHOD
'''
print("welcome")
print("__name__ contains:",__name__)
print("Execute if not in main")
def fun():
    print("Testing the main Function")


if __name__=="__main__":
    # print(fun())
    fun()
'''


