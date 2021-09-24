"""
Dunder methods in Python are special methods. In Python, we sometimes see method names with double undescore (__),
such as __init__ method that every Class has. These methods are called “dunder” methods.
In Python, Dunder methods are used for operator overloading and for customizing the behaviour of some other function.
"""

 # mapping operators to function
class Employee:
    no_of_leaves=8
    def __init__(self,aname,asalary,ajob):
        self.name=aname
        self.salary=asalary
        self.job=ajob

    def printdetail(self): #---> self is object
        return f"Name is {self.name } salary is {self.salary}  Job is {self.job}"
    def __truediv__(self, other):
        return self.salary / other.salary

    def __add__(self, other):
        return self.salary + other.salary

    def __repr__(self):
        return f"Employee('{self.name}', {self.salary}, '{self.job}')"

    def __str__(self):
        return f" Name is {self.name } salary is {self.salary}  Job is {self.job}"


nishant=Employee("Nishant", 80000, "IAS")
neha=Employee("Neha",40000,"Developer")
print(nishant/neha)
print(nishant+neha)
print(repr(neha))
#print(neha)
print(str(neha))

#print(nishant.printdetail())