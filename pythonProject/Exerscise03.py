a=58
number=1
chance=9
print("Welcome to the number guessing Game ", "\nEnter one number here")
while(number <=9):

         inp=int(input())
         if inp==a :
              print("YAYY!!, You guess the correct number")
              break;

         elif inp > a :
               print("The required number is smaller than entred number")
         elif inp < a:
                print("The required number is Larger than entred number")
         chance = chance - 1
         print("Number of chances left = ", chance)
         if (chance == 0):
             print("Game over :(","Try Again")
         number=number +1







