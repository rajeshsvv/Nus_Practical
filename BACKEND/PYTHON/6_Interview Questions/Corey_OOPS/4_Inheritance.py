class Employee:

    raise_amount=1.04
    def __init__(self,first,last,pay):
        self.first=first
        self.last=last
        self.pay=pay
        self.email=first+"."+last+"@gmail.com"

    def fullname(self):
        return f"fullname:{self.first}.{self.last}"

    def apply_raise(self):
        self.pay=int(self.pay*self.raise_amount)


class Developer(Employee):
    raise_amount = 1.62             # it does not reflect the parent class variable

    def __init__(self,first,last,pay,prog_lang):
        super().__init__(first,last,pay)
        # Employee.__init__(self,first,last,pay)          # use parent class in this way also but 1st one is good
        self.prog_lang=prog_lang

class Manager(Employee):
    def __init__(self,first,last,pay,employees=None):
        super().__init__(first,last,pay)
        if employees is None:
            self.employees=[]
        else:
            self.employees=employees


    def add_emp(self,emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self,emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emps(self):
        for emp in self.employees:
            print('->',emp.fullname())


dev1=Developer("Abhi","Adire",20000,"Python")
dev2=Developer("Sachin","Tendulkar",60000,"Java")

mngr=Manager('Arjit',"Chatarjee",50000,[dev2])
mngr.print_emps()
print(mngr.email)
mngr.remove_emp(dev1)

print(dev1.pay)
dev1.apply_raise()
print(dev1.pay)
print(dev2.email)
print(dev2.prog_lang)

print(isinstance(mngr,Manager))                 # True
print(isinstance(mngr,Employee))                # True
print(isinstance(Manager,Developer))            # false

# print(help(Developer))        # it shows the o/p of MRO output wise it inherits from employee class.

print(issubclass(Developer,Employee))       # True means Developer is subclass of Employee
print(issubclass(Employee,Developer))       # False
print(issubclass(Manager,Developer))        # False
print(isinstance(dev1,Employee))            # True