# def fun1():
#     print("Subscribe ")
# fun2 = fun1
# del fun1
# fun2()
# def funcre(num) :
#     if num==0 :
#         return print
#     if num== 0:
#         return sum
# print(funcre(1))
# def executor(func) :
#     func("This")
# executor(print)
def dec1(func1):
    def nowexe():
        print("Executing now")
        func1()
        print("Executed")
    return  nowexe
@dec1
def mm():
    print("This is my laptop")
# mm=dec1(mm)
mm()