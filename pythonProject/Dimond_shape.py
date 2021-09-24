class A :
    def meth(self):
        print("This ismethod of class A ")
class B(A) :
    def meth(self):
        print("This ismethod of class B")
class C(A) :
    def meth(self):
        print("This ismethod of class C")
class D(B,C) :
    def meth(self):
        print("This ismethod of class D")
a=A()
b=B()
c=C()
d=D()

print(d.meth())