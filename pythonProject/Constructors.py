"""
Constructors in python :
                    Constructors are generally used for instantiating an object .The task of constructor is to initialize to the data
                    members of the class when an object of the class is created.

                    
"""
class Employee:
    no_of_leaves=8
    def __init__(self,aname,asalary,ajob):
        self.name=aname
        self.salary=asalary
        self.job=ajob

    def printdetail(self): #---> self is object
        return f"Name is {self.name } salary is {self.salary}  Job is {self.job}"


neha=Employee("Neha",8000,"developer")
shweta=Employee("Shweta",9000,"Developer")
# neha.salary= 60000
# neha.job= "Developer"
# neha.name="Neha"
print(neha.printdetail())

# shweta.salary= 7000]
# shweta.job= "Developer"
# shweta.name="Shweta"
print(shweta.printdetail())


