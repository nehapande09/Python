# Create a list and print number grater than 6
list=[int,float,"neha ",8,76,5,4,3,44,2,1,3,6,78,87]
for item in list:
    if str(item).isnumeric() and item>6:
        print(item)