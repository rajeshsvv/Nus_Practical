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

    # def __repr__(self):
    #     return "Employee('{}','{}',{})".format(self.first,self.last,self.pay)

    def __repr__(self):
        # return "Employee('{}','{}',{})".format(self.first,self.last,self.pay)

         return "Employee('%s','%s',%f)" %(self.first, self.last, self.pay)

    def __str__(self):
        return "{} - {}".format(self.fullname(),self.email)

    def __add__(self,other):
        return self.pay+other.pay

    def __len__(self):
        return len(self.fullname())

emp1=Employee("Corey","Schafer",25000)
emp2=Employee("Test","Employee",60000)

print(emp1)
print(repr(emp1))
print(str(emp1))

print(emp1.__repr__())
print(emp1.__str__())

print(1+2)
print(int.__add__(2,96.6))

print(emp1+emp2)

print(len('test'))
print('test'.__len__())
print(len(emp2))