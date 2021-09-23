"""
OOP - Object Oriented programming
classes - Template
object - Instance of the class
DRY
"""
# class student :
#     pass                                                 # pass means nothing
# s1=student()
# s2=student()
# s1.name="Neha"
# s1.rollno=19
# s2.name="Shweta"
# #print(s1,s2)
# print(s1.name,s2.name)
class Employee:
    no_of_leaves=8
    pass
E1=Employee()
E2=Employee()
E1.name="Nishant"
E1.job="Developer"
E1.sal="60,000"
E1.no_of_leaves=9

E2.name="Neha"
E2.job="Developer"
E2.sal="40,000"

print(E1.__dict__)
print(Employee.__dict__)
