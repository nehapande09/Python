#from abc import ABCmeta and abstractmethod
from abc import ABCMeta,abstractmethod

class Shape(metaclass=ABCMeta) :
    @abstractmethod
    def printarea(self):
        return 0



class Rectangle(Shape) :
    type = "Rectangle"
    sides = 4
    def __init__(self):
         self.length = 7
         self.breadth = 6
    def printarea(self):
         return self.length * self.breadth

rec1=Rectangle()
print(rec1.printarea())
