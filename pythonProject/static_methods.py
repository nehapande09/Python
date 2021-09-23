#Static Method :
class Employee:
    no_of_leaves=8
    def __init__(self,aname,asalary,ajob):
        self.name=aname
        self.salary=asalary
        self.job=ajob

    def printdetail(self): #---> self is object
        return f"Name is {self.name } salary is {self.salary}  Job is {self.job}"
    @staticmethod
    def printfunc(string):
        print("Good Morning " + string)

neha=Employee("Neha",8000,"developer")
shweta=Employee("Shweta",9000,"Developer")
shweta.printfunc("shweta")
print(shweta.no_of_leaves)
print(neha.no_of_leaves)


