# TOTAL 67 BULIT IN FUNCTIONS


#   1. Python abs()             returns negative value into positive value

print(abs(-9))

#   2. Python all()             it returns true except in case of  '' and 0  in this case it will return false

print(any(['ab','cd',1,2,3,4,5,'']))
print(all(({1,2,3,3,5,"e","g"})))
print(any((["",0])))


#   4. Python ascii()

#   Python ascii(), is important Python built-in functions,
#   returns a printable representation of a python object (like a string or a Pytho"n list)


print(ascii('use@'))

#   5. Python bin()

#   Python bin() converts an integer to a binary string.

print(bin(8))

#   6. Python bool()

#   Python bool() converts a value to Boolean.

print(bool(0.5))
print(bool(""))
print(bool(0))
print(bool(" "))

#   7. Python bytearray()

#   Python bytearray() returns a python array of a given byte size.

print(bytearray(3))
print(bytearray([1,2,3]))

#   8. Python bytes()

#   Python bytes() returns an immutable bytes object.

print(bytes(3))

#   Both bytes() and bytearray() deal with raw data, but bytearray() is mutable, while bytes() is immutable

#   9. Python callable()

#   Python callable() tells us if an object can be called.

print(callable(callable))
print(callable(list))
print(callable(tuple))

#   A function is callable, a list is not. Even the callable() python Built In function is callable.

#   10. Python chr()

#   Python chr() Built In function returns the character in python for an ASCII value

print(chr(65))
print(chr(97))
print(chr(9))
print(chr(48))

#    11. Python classmethod()
#   Python classmethod() returns a class method for a given method

class fruit():
    def __init__(self):
        pass
    def sayhi(self):
        print("Hi Iam fruit")

fruit.sayhi=classmethod(fruit.sayhi)
fruit.sayhi()

#   12. Python compile()
#   Python compile() returns a Python code object. We use Python in built function to convert a string code into object code.

exec(compile('a=5\nb=7\nprint(a+b)','','exec'))
exec(compile('a=5.9\nb=7.7\nprint(a+b)','','exec'))

#   13. Python complex()
#   Python complex() function creates a complex number. We have seen this is our article on Python Numbers.

print(complex(4))
print(complex(4+6*9j))

#   14. Python delattr()
#   Python delattr() takes two arguments- a class, and an attribute in it. It deletes the attribute.

class fruit:
    size=7
orange=fruit()

orange.size

delattr(fruit,'size')
# orange.size

#   15. Python dict()
#   Python dict(), as we have seen it, creates a python dictionary.

list=[]
print(list)
set=set()
print(set)


#   16. Python dir()
#   Python dir() returns an object’s attributes.

#   17. Python divmod()
#   Python divmod() in Python built-in functions, takes two parameters, and returns a tuple of their quotient and remainder.

