# Access Modifier
"""
Public    : In public, all the functions, variables, methods can be used publicly.

Protected : its members and functions can only be accessed by the classes derived from it.
            To declare a class as protected, we use a single underscore “_” sign before the data members of the class.

Private   :  the variables and functions can only be accessed within the class.
             we use a double underscore “_­_” sign before the data members of the class.

"""

class Employee:
    no_of_leaves = 8
    var = 8
    _protec = 9
    __pr = 98

    def __init__(self, aname, asalary, arole):
        self.name = aname
        self.salary = asalary
        self.role = arole

    def printdetails(self):
        return f"The Name is {self.name}. Salary is {self.salary} and role is {self.role}"

    @classmethod
    def change_leaves(cls, newleaves):
        cls.no_of_leaves = newleaves

    @classmethod
    def from_dash(cls, string):
        return cls(*string.split("-"))

    @staticmethod
    def printgood(string):
        print("This is good " + string)

emp = Employee("harry", 343, "Programmer")
print(emp._Employee__pr)

