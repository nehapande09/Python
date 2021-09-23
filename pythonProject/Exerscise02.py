# Exerscise 02 : Faulty calculator
num1=int(input("Give First number : "))
num3=input("Give operand : ")
num2=int(input("Give second number : "))
if num1 == 45 and num2 == 3 and num3 == '*':
    print("555")
elif num1 == 56 and num2 == 9 and num3 == '+':
    print("77")
elif num1 == 56 and num2 == 6 and num3 == '/':
    print("4")
elif num3 == '*':
    num4 = num1 * num2
    print(num4)
elif num3 == '+':
    plus = num2 + num1
    print(plus)
elif num3 == '/':
    Dev = num2 / num1
    print(Dev)
elif num3 == '-':
    Dev = num2 - num1
    print(Dev)
elif num3 == '%':
    percent = num2 % num1
    print(percent)
else:
    print("Error! Please check your input")

