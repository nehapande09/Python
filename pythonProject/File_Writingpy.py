# Write()
# f=open("Neha.txt", "a")
# a=f.write("Hello, welcome to python")
# print(a) # Return character written in file
# f.close()
"""
If we use write mode while writing then containt of file is deleted and new containt added, 
but in append mode the previous  containt is note deleted and new contai added
"""
import datetime
def getdate():
    return datetime.datetime.now()


#How to handle read and write both?
f=open("Neha.txt","r+")
print(f.read())
f.write("Thank you \n")
f.write(str(str(getdate())))
