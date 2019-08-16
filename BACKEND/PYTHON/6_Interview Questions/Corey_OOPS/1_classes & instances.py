class Employee:
    def __init__(self,first,last,pay):
        self.first=first
        self.last=last
        self.pay=pay
        self.mail=first+"."+last+"@gmail.com"

    def fullname(self):
        # return f"full name {self.first}.{self.last}"
        # return '{}.{}'.format(self.first,self.last)
        return '%s.%s' %(self.first, self.last)
        # return True

e1=Employee("Harsha","Bhogle",100)
e2=Employee("Siva","Ramakrishnan",100)


# e1.first="Ashok"
# e1.last="Natasha"
# e1.pay=6000

#e2.first="Sumeet"
# e2.last="Harare"
# e2.pay=4000


print(e1.mail)
print(e2.mail)
print(e1.fullname())
print(Employee.fullname(e2))