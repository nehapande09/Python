# Functions and Docstrings
a= 7
b=2
c = sum((a,b)) # Built in function
print(c)

#User defined function
def fun1(a,b):
    """ This is function used to return addition(This is doc string)"""
    print("hello you are in func 1 ",a+b)
    print(fun1.__doc__)
fun1(5,7)
def fun2(a,b) :
    c=(a+b)/2
    return c
Q=fun2(10,50)
print(Q)