# map function apply list as a function
# numbers=["3","67","78"]
# numbers =list(map(int,numbers))
# # for i in range (len(numbers)):
# #     numbers[i]=int(numbers[i])
# numbers[2]=numbers[2]+1
# #print(numbers[2])
# # def sq(a):
# #     return a*a
# # num=[2,3,4,5,6,7,8]
# # square=list(map(sq,num))
# # print(square)
#
# num=[2,3,4,5,6,7,8]
# square=list(map(lambda x: x*x ,num))
# print(square)
# def square (a):
#     return a*a
# def cube(a) :
#     return a*a*a
# func=[square,cube]
# for i in range(5):
#     val=list(map(lambda x: x(i),func))
#     print(val)
# +++++++++++++++++++++++++++Filter+++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# list1=[1,2,3,4,5,6,7]
# def grater_5 (num):
#     return num>5
# gr_than_5= list(filter(grater_5,list1))
# print(gr_than_5)


# ++++++++++++++++++++++++++++++++++ REDUCE ++++++++++++++++++++++++++++++++++++++++++++++++++++++
from functools import reduce
list_1=[1,2,3,4,5,6]
# num = 0
# for i in list_1:
#     num=num+i
# print(num)
num=reduce(lambda x,y:x+y, list_1)
print(num)
