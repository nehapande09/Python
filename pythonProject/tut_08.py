str = "My name is Neha"
print(str[0:8])
print(len(str))
print(str[::])
print(str[0:5:2])
#The bydefault values of slicing are like "0:length of string:1"


#Functions
print(type(str))  #----> Use to know datatype of variable
print(str.isalnum())
print(str.isalpha())
print(str.islower())
print(str.endswith("Neha"))
print(str.count("a"))
print(str.capitalize())
print(str.find("is"))
print(str.lower())
print(str.upper())
print(str.replace("is","are"))
