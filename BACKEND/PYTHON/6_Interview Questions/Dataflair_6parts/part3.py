'''
class A:
    def sayHello(self):
        print("Hello Iam in A")

class B(A):
    def sayHello(self):
        print("Hello Iam in B")


b=B()
a=A()


print(a.sayHello())
print(b.sayHello())

'''


'''
class A:
    pass

class B(A):
    pass


print(issubclass(B,A))

A=range(10)
print(A)
'''

import urllib.request
urllib.request.urlretrieve('https://yt3.ggpht.com/a-/ACSszfE2YYTfvXCIVk4NjJdDfFSkSVrLBlalZwYsoA=s900-mo-c-c0xffffffff-rj-k-no','dataflair.jpg')
