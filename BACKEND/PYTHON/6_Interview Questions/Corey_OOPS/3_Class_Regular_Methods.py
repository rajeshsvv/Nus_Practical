import datetime

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
        # return "fullname %s.%s" %(self.first,self.last)
        return '{}.{}'.format(self.first, self.last)

        # return True

    def apply_raise(self):
        # self.pay=(self.pay*10)
        # self.pay = (self.pay * Employee.raise_amount)           # through class variable
        self.pay = (self.pay * self.raise_amount)

    # create class method for class variables
    @classmethod
    def set_raise_amount(cls,amount):
        cls.raise_amount=amount

    @classmethod
    def from_string(cls,emp_str):
        first, last, pay = emp_str.split("-")
        return cls(first, last, pay)

    @staticmethod
    def weekday(day):
        if day.weekday()==5 or day.weekday()==6:
            return False
        return True

e1=Employee("Anish","Sarvanand",1000)
e2=Employee("Sarath","Nidugula",2000)

# e1.set_raise_amount(2.5)            # run the class method from the instance.
Employee.set_raise_amount(1.10)       # assign new class variable through defined method
# Employee.raise_amount=10.9          # assign new class variable through manually


print(Employee.raise_amount)
print(e1.raise_amount)
print(e2.raise_amount)



emp_str_1="John-Doe-70000"
emp_str_2="Steve-smith-30000"
emp_str_3="Arjun-Durga-5000"

'''
first,last,pay=emp_str_1.split("-")
new_emp_1=Employee(first,last,pay)

first,last,pay=emp_str_2.split("-")
new_emp_2=Employee(first,last,pay)

first,last,pay=emp_str_3.split("-")
new_emp_3=Employee(first,last,pay)
'''
new_emp_1=Employee.from_string(emp_str_1)
new_emp_2=Employee.from_string(emp_str_2)
new_emp_3=Employee.from_string(emp_str_3)

print(new_emp_1.fullname())
print(new_emp_2.pay)
print(new_emp_3.fullname())

today_date=datetime.date(2019,8,18)
print(Employee.weekday(today_date))


