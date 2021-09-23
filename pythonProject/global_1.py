# Scope,Global variables and Global keywords
# Value of Global variable is read only value It can not change
# Global keyword is used to change value of global value
# l=10 #Global
# def func1(n) :
#     #l=5   #local
#     global l
#     l=l+50
#     print(l)
#     print(n,"This is function 1")
# func1("Hello")
# print(l)
def neha() :
    x=20
    def nishant():
          global x
          x=75
    print("before calling nishant value of x : ",x)
    nishant()
    print("after calling nishant value of x : ",x)
neha()


