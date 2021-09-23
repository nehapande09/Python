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
    @classmethod
    def from_str(cls,string):
        # params=string.split("-")
        # print(params)
        # return cls(params[0],params[1],params[2])
        return cls(*string.split("-"))


# neha=Employee("Neha",8000,"developer")
# shweta=Employee("Shweta",9000,"Developer")
NP=Employee.from_str("Np-480-student")
# shweta.change_leaves(67)
# print(shweta.no_of_leaves)
# print(neha.no_of_leaves)
print(NP.salary)

