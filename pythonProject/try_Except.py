# Try Except Exception handling in python
print("Enter a number num1")
num1=input()
print("Enter a number num2")
num2=input()
try:
    print("The sum of two number is : ", int(num1)+int(num2))
except Exception as e:
    print(e)
print("Program End here")

