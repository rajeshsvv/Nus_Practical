# https://www.quora.com/What-are-the-most-important-topics-to-learn-in-Python

"""
a=[1,2,3,4,5]
# result=list(map(lambda element:element+1,a))
# result=list(map(lambda x,y:x+y,a))
a=[element+1 for element in a]
print(a)


for index in range(len(a)):
    a[index]+=1
print(a)


print(list(range(1,10)))

stringone = "Python is Powerful"

enumlist=enumerate(stringone)
for i in enumlist:
    print(i)
"""

# list comprehension
listdata=[i for i in range(1,5)]
print(listdata)

# dict comprehension
dictdata={i:i**2 for i in range(1,10) if i%2==0}
print(dictdata)

#generators

gen=(i**i for i in range(1,5))
print(gen)
print(next(gen))
print(next(gen))


#iterator


iterate=iter(['a','b','c'])
print(iterate)

print(next(iterate))
print(next(iterate))


def generate(a):
    for i in range(1,a):
        yield i*i


# Terenary Operator

a=5;b=3

answer="a is greater than b" if a>b else "b is greater than a"
print(answer)



# Lambda Functions
#
# Lambda functions are referred as anonymous functions. It is suitable for simple operations

def say_hello():
    return "Hello"

say_hello=lambda:"hello"


months = ['jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sep', 'oct', 'nov', 'dec']
oddMonths = [iter for index, iter in enumerate(months) if (index%2 == 0)]
oddMonths

item=[n*2 for n in range(10)]
print(item)


