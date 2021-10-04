class Employee :
    def __init__(self,fname,lname):
        self.fname = fname
        self.lname = lname
    def explain(self):
        return f"This is employee {self.fname} {self.lname}"

    @property
    def email(self):
        if self.fname==None or self.lname==None :
            return "Email is not set. Please set it using setter"
        return f"{self.fname}.{self.lname}@mail.com"




    @email.setter
    def email(self,string):
        print("Setting now....")
        names=string.split("@") [0]
        self.fname = names.split(".")[0]
        self.lname = names.split(".")[1]
    @email.deleter
    def email(self):
        self.fname= None
        self.lname= None


skillf=Employee("Skill","F")
o="This is string"
# print(skillf.email)
# print(type(skillf))
# print(type(o))
# print(id(o))
# print(id(skillf))
# print(dir(skillf))
# print(dir(o))
import  inspect
print(inspect.getmembers(skillf))
