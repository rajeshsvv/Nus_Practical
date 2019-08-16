class Employee:
    no_of_emps=0
    raise_amount=10.04                   # class variable

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.mail = first + "." + last + "@gmail.com"
        Employee.no_of_emps+=1

    def fullname(self):
        # return f"full name {self.first}.{self.last}"
        return '{}.{}'.format(self.first, self.last)
        # return "fullname %s.%s" %(self.first,self.last)
        # return True

    def apply_raise(self):
        # self.pay=(self.pay*10)
        self.pay = (self.pay * Employee.raise_amount)           # through class variable
        # self.pay = (self.pay * self.raise_amount)

print(Employee.no_of_emps)
e1 = Employee("Harsha", "Bhogle", 100)
e2 = Employee("Siva", "Ramakrishnan", 500)
e3 = Employee("Nanda", "krish", 300)
print(Employee.no_of_emps)

print(e1.mail)
print(e2.mail)
print(e2.fullname())

# print(Employee.fullname(e1))            # through class we are calling the e1 full name
# print(Employee.fullname(e2))            # through class we are calling the e2 full name

'''
# print(e2.pay)
# e2.apply_rasie()
# print(e2.pay)
# print('---')
#
# print(e2.pay)
# e2.apply_raise()
# print(e2.pay)
'''

'''
Employee.raise_amount=2.05
print(Employee.raise_amount)
print(e1.raise_amount)
print(e2.raise_amount)
'''

'''
e1.raise_amount=20
e2.raise_amount=30
Employee.raise_amount=40
print(e1.__dict__)              #if u declare e1.raise_amount=20 like here Now raise amount in dict list
print(e2.__dict__)              # No raise amount here
print(Employee.__dict__)      # raise amount here because this is class variable it will contain raise amount
'''

