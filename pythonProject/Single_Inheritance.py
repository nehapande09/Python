# Single line inheritance
class Employee:
    no_of_leaves=8
    def __init__(self,aname,asalary,ajob):
        self.name=aname
        self.salary=asalary
        self.job=ajob


    def printdetail(self): #---> self is object
        return f"Name is {self.name } salary is {self.salary}  Job is {self.job}"
    @classmethod
    def change_leaves(cls,newleaves):
        cls.no_of_leaves=newleaves
class programmer (Employee) :
    def __init__(self,aname,asalary,ajob):
        self.name = aname
        self.salary = asalary
        self.job = ajob


    def printdetail(self): #---> self is object
        return f"Name is {self.name } salary is {self.salary}  Job is {self.job}"


Neha=programmer("Neha",600,"developer")
NP=programmer("NP",600,"developer")
print(Neha.printdetail())

