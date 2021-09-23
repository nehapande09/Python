# Read(),readlines(),open()

f=open("Neha.txt","rt")
# content=f.read(33)
print(f.readline())
print(f.readline())
print(f.readlines())
# print(content)
# for line in f:
#     print(line, end=" ")
f.close()