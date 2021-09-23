# f=open("Neha.txt")
# print(f.readlines())

with open("Neha.txt") as f:
    a= f.readlines()
    print(a)
# -- This is syntax of with block to open file,
# While using with block there is no need to close file because file is closed automatically
