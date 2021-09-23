# Health management system
# 3 clients --- Neha Nishant
# Total 6 files to lock food and exerscise
# Write function take input as client name
import datetime
def getdate():
    return datetime.datetime.now()

def write(a) :
     if a==1:
        print("what do u want to lock Diet or exerscise of Neha?", "Enter 1 for Exerscise and 2 For Diet")
        b = int(input())
        if b == 1:
             f = open("NehaE.txt", "a")
             print("Give Exerscise of Neha")
             value = input()
             f.write(str(str(getdate())) + ": " + value + "\n")
             f.close()

        elif b == 2:
            f = open("NehaD.txt", "a")
            print("Give todays Diet  of neha")
            value = input()
            f.write(str(str(getdate())) + ": " + value + "\n")
            f.close()

        else :
            print("Your choice is wrong, please give correct choise either 1 or 2 !!")

     elif a == 2:
        print("what do u want to lock Diet or exerscise of Nishant?", "Enter 1 for Diet and 2 For Exerscise")
        b = int(input())
        if b == 1:
            f = open("NishantD.txt", "a")
            print("Give todays Diet of Nishant")
            f.write(str[str(getdate())])
            value = input()
            f.write(str(str(getdate())) + ": " + value + "\n")
            f.close()
        elif b == 2:
            f = open("NishantE.txt", "a")
            print("Give todays Exerscise of Nishant ")
            value = input()
            f.write(str(str(getdate())) + ": " + value + "\n")
            f.close()
        else:
            print("Your choice is wrong, please give correct choise either 1 or 2 !!")

     elif a == 3:
        print("what do u want to lock Diet or exerscise of Nishant?", "Enter 1 for Diet and 2 For Exerscise")
        b = int(input())
        if b == 1:
            f = open("NpD.txt", "a")
            print("Give todays Diet ")
            value=input()
            f.write(str(str(getdate())) + ": " + value + "\n")
            f.close()
        elif b == 2:
            f = open("NpE.txt", "a")
            print("Give todays Exerscise ")
            value = input()
            f.write(str(str(getdate()))+ ": " + value + "\n")
            f.close()
        else:
            print("Your choice is wrong, please give correct choise either 1 or 2 !!")

     else:
        print("Your choice for client is wrong, please give correct choice From 1,2 and 3  !!")
def read(a) :
    if a == 1:
        print("what do u want to Read Diet or exerscise of Neha?", "Enter 1 for Exerscise and 2 For Diet")
        b = int(input())
        if b == 1:
            f = open("NehaE.txt", "r")
            q=f.readlines()
            print("This is Exerscise of Neha : ",q)
            f.close()

        elif b == 2:
            f = open("NehaD.txt", "r")
            q=f.readlines()
            print("This is diet of Neha : ",q)
            f.close()

        else:
            print("Your choice is wrong, please give correct choise either 1 or 2 !!")
    elif a == 2:
        print("what do u want to Read Diet or exerscise of Nishant?", "Enter 1 for Diet and 2 For Exerscise")
        b = int(input())
        if b == 1:
            f = open("NishantD.txt", "r")
            q=f.readline()
            print("This is Exerscise of Nishant : ", q)
            f.close()

        elif b == 2:
            f = open("NishantE.txt", "r")
            q=f.readlines()
            print("This is diet of Nishant : ",q )
            f.close()
        else:
            print("Your choice is wrong, please give correct choise either 1 or 2 !!")
    elif a == 3:
        print("what do u want to Read Diet or exerscise of Nishant?", "Enter 1 for Diet and 2 For Exerscise")
        b = int(input())
        if b == 1:
            f = open("NpD.txt", "r")
            q=f.readlines()
            print("This is Exerscise of NP : ", q)
            f.close()

        elif b == 2:
            f = open("NpD.txt", "r")
            q=f.readlines()
            print("This is diet of NP : ",q)
            f.close()
        else:
            print("Your choice is wrong, please give correct choise either 1 or 2 !!")


print(" *** WELCOME TO THE HEALTH MANAGEMENT SYSTEM *** ")
print("Enter a number to select client 1 for Neha,2 for Nishant and 3 for NP ")
d=int(input())
print("\n what do u want - 1) Write the data" ,"\n\t\t\t\t  2) Read the data " , "\" Select 1 for writing data and 2 for Reading data\", Enter Your choice here - ")
c=int(input())
if c==1:
    write(d)
    print("Data Written Successfully in File !!"," Run program Again To perform another actions :)")
elif c==2 :
    read(d)
    print("Data  Successfully Retrive from File !!", " Run program Again To perform another actions :)")
else :
    print("Please Enter Proper choice and Run orogram Again ;)")















