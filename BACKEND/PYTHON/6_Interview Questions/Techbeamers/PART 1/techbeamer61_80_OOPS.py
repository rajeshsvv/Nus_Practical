                        # OOPS from 59 onwards


#   Q-60: What Are Attributes And Methods In A Python Class?

class Human:
    profession="Sales Manager"

man=Human()
man.profession="Division Head"
print(man.profession)


# now we can define methods.in method signature we always have to provide
# first argument with self keyword.

class Human:
    profession = "Head Master"

    def set_profession(self,new_profession):
        self.profession=new_profession

man=Human()
man.set_profession("Principle")
print(man.profession)


# Q-61: How To Assign Values For The Class Attributes At Runtime?

'''
class Human:
    def __init__(self,profession):
        self.profession=profession

    def set_profession(self,new_profession):
        self.profession=new_profession
man=Human("ASSISTANT MANAGER")
print(man.profession)
'''


                            #     62.INHERITANCE

'''
class PC:                           # Base class
    processor="Xeon"                   #Common attribute
    def __init__(self,processor):       #run time assignment of attributes
        self.processor=processor

    def set_processor(self,new_processor):
        self.processor=new_processor

class DESKTOP(PC):                  #   Derived class
    os="MAC OS High Sierra"          # Personalized attribute
    ram="32 GB"

class LAPTOP(DESKTOP):
    os="WINDOWS 10 PRO"
    ram="64 GB"

desk=DESKTOP("Apple")
print(desk.processor,desk.os,desk.ram)

lap=LAPTOP("Apple")
print(lap.processor,lap.os,lap.ram)

'''

                                # Q-63: What Is Composition In Python?

'''
class PC:
    processor="Xeon"
    def __init__(self,processor,ram):
        self.processor=processor
        self.ram=ram

    def set_processor(self,new_processor):
        self.processor=new_processor

    def get_PC(self):
        return "%s cpu %s ram" %(self.processor,self.ram)

class Tablet():
    make="Intel"
    def __init__(self,processor,ram,make):
        self.PC=PC(processor,ram)
        self.make=make

    def get_Tablet(self):
        return "Tablet with %s CPU & %s ram by %s" %(self.PC.processor,self.PC.ram,self.make)

if __name__=="__main__":
    tab=Tablet("i7","16 GB","Intel")
    print(tab.get_Tablet())

'''

        # 66    How Do You Raise Exceptions For A Predefined Condition In Python?

'''
while True:
    try:
        value=int(input("enter some odd number:"))
        if value%2==0:
            print("Exited due to invalid input")
        else:
            print("Value entered is :%s" %(value))

    except ValueError as ex:
        print(ex)
        # break

'''

                                    # 69 Generator

# A Generator is a kind of function which lets us specify a function that acts like an iterator
# and hence can get used in a “for” loop.

'''
def fun():
    return True
fun()
print(fun())


def gen_func():
    yield "dig into genrator function"
    yield "dig into some other function"

print(next(gen_func()))
print(next(gen_func()))

'''

                                    # 70 Closures

#python closures are function object return from some other function.use to eliminate code redundancy.

'''
def multiply_number(number):
    def product(num):
        'product here is a closure'
        return num*number
    return product

num_2=multiply_number(3)
print(num_2(11))
print(num_2(24))

num_6=multiply_number(6)
print(num_6(1))
'''


                                #   71 Decorators

'''
def decorator_sample(func):
    def decorator_hook(*args,**kwargs):
        print("Before the function call")
        result=func(*args,**kwargs)
        print("After the function call")
        return result
    return decorator_hook

@decorator_sample
def product(x,y,z,p=90):
    'function to multiply two numbers'
    print(x*y*z)
    # return x*y*z*90

product(2,3,4)
# print(product(2,3,4))

'''

                            # 74 Traverse through Decorators

'''
site_stats={'site': 'tecbeamers.com', 'traffic': 10000, "type": "organic"}
for i,v in site_stats.items():
    # print(i,v)
    print(" the key is %s" %(i))
    # print("the value is %s" %(v))
    # print(f"the value is: {v}")
    print("the value is {}".format(v))
    print("-------------------")
    
print(site_stats.pop("site"))
'''


                            # DICT COMPREHENSION

# adict = {var:var**2 for var in range(10, 15)}
# print(adict)





