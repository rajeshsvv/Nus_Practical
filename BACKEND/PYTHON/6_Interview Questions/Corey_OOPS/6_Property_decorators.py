class Employee:
    def __init__(self,first,last):
        self.first=first
        self.last=last
        # self.email=first+"."+last+"@gmail.com"

    @property
    def fullname(self):
        return '{}.{}'.format(self.first,self.last)

    @property
    def email(self):
        return '{}.{}.@gmail.com'.format(self.first,self.last)

    @fullname.setter
    def fullname(self,name):
        first,last=name.split(' ')
        self.first=first
        self.last=last

    @fullname.deleter
    def fullname(self):
        print("Delete Name!")
        self.first=None
        self.last=None

emp=Employee("John","David")
emp1=Employee("Harsha","Patel")

emp.first="Steven"
print(emp.first)

emp1.fullname="Sachin Tendulkar"


# print(emp.fullname())     #without property decorator u can call like this as method
print(emp.fullname)       # with property decorator u can call like this as attribute

# print(emp.email())      # without poperty decorator u can call like this

print(emp.email)            #with property decorator u can call like this email as property

emp1.first="Sussie"
print(emp1.email)

emp1.fullname="Sachin Tendulkar"
print(emp1.fullname)

del emp.fullname