# MULTIPLE INHERITANCE

class Player :
    no_of_games=4
    def __init__(self,name,game):
        self.name=name
        self.game=game
    def print(self,name,game):
        f"The name of player is {self.name} the game is {self.game}"

class Employee :
    noofleaves=8
    def __init__(self,name,salary,job):
        self.name=name
        self.salary=salary
        self.job=job
    def printdetail(self,name,salary,job):
        return f"The name of the Employee is {self.name} Salary is {self.salary} and Job is {self.job}"
    @classmethod
    def changeleaves(cls,newleaves):
        cls.noofleaves=newleaves
        return f" The no of new leves are {cls.noofleaves}"
    @staticmethod
    def printfunc(string):
        print("Good Morning " + string)

class Cool_Employee(Employee,Player):
    language = "C++"

    def printlanguage(self):
            print(self.language)


neha = Cool_Employee("Neha", 8000, "developer")

shweta = Employee("Shweta", 9000, "Developer")
np=Player("NP",["cricket"])



