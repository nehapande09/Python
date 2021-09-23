# Seek(),tell(),and more on python
f=open("neha.txt")
# print(f.tell()) # tell() shows pointer location
print(f.readline())
# print(f.tell())
f.seek(10) # this is used to from where the file read or move pointer
print(f.readline())
# print(f.tell())
print(f.readline())
# print(f.tell())
f.close()