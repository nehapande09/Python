class Employee :
    def __init__(self,fname,lname):
        self.fname = fname
        self.lname = lname
        #self.email = f"{fname}.{lname}@gmail.com"
    def explain(self):
        return f"This is employee {self.fname} {self.lname}"

    @property
    def email(self):
        if self.fname == None or self.lname == None:
            return "Email is not set. Please set it using setter"
        return f"{self.fname}.{self.lname}@codewithharry.com"

    @email.setter
    def email(self, string):
        print("Setting now...")
        names = string.split("@")[0]
        self.fname = names.split(".")[0]
        self.lname = names.split(".")[1]

    @email.deleter
    def email(self):
        self.fname = None
        self.lname = None

neha_pande  = Employee("Neha","Pande")
nishant_pande = Employee("Nishant","Pande")
print(neha_pande.email)
neha_pande.fname = "neha"
print(neha_pande.email)
neha_pande.email="abc.xyz@gmail.com"
print(neha_pande.fname)
del neha_pande.email
print(neha_pande.email)
neha_pande.email = "nr.pande@codewithharry.com"
print(neha_pande.email)

