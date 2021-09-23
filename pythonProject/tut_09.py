"""
Lists In python :

Name=["Neha","Nishant"]
print(Name)
student=[34,"ghjsdg",87,98.5,"sdh"]
print(student)
numbers=[5,8,6,3,7,87,66,45,76,98,88]
print(numbers)
print(numbers[1])
# Method used on lists
numbers.sort()
print(numbers)
numbers.remove(87)
print(numbers)
numbers.reverse()
print(numbers)
print(min(numbers))
print(max(numbers))
print(len(numbers))



number=[2,6,9,4,7,3]
print(number[:]) # Slicing
# starting position : length ---> bydefault
print(number[::]) #--> Extended slicing
# Starting position : length : 1 ----> bydefault
print(number[0:6:2])
number.append(8)
print(number)
"""
# Mutable- can change
# Immutable- can not change
# Tuple is immutable
# List is mutable
"""
list=[54,76,87]
print(list)
list[1]=8
print(list)  #----> Mutable
tp=(87,88,79) # ---> In tuple parenthesis is used
print(tp)
a=(1,)
# if Tuple have one value the comma is necessary to define that tuple 


tp[0]=8
print(tp)
This not acceptable here Error is occured Tuple is immutable
"""

#Swapping in python
a=8
b=9
a,b=b,a
print(a,b)




