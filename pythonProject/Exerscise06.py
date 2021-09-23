# ** Exerscise 06 **
# Snake Water Gun game
"""
snake - water - snake winner
Gun : Snake - Gun winner
water: GUN - WATER
10 chances --- While loop
"""
import random
print("WELCOME TO SNAKE WATER GUN GAME :) !!!!",
      "\nHere you have 10 chances, If you Win more chances, Then you can Win the Game ;) So lets Start !!!! " )
list=["GUN","WATER","SNAKE"]
choice= random.choice(list)
count=0
chance=3
comp_point=0
user_point=0
while(count<3) :



          c=int(input("\nEnter Your choice here,(1 for GUN , 2 for WATER , 3 for SNAKE  : "))
          if c==1 and choice=="GUN" or c==2 and choice=="WATER" or c==3 and choice=="SNAKE" :
                     print("Your Choice and computer Choice is same, Game DRAW")
                     print("computer and you both get 0 point each :<")
                     count=count+1
                     chance=chance-1
                     print(chance,"Chances are remaining ")
                     print(f"Comp_point : {comp_point} and User_point : {user_point}")
          elif c==1 and choice=="SNAKE" or c==2 and choice=="GUN" or c==3 and choice=="WATER" :
                     print("You Win the chance ")
                     user_point=user_point+1
                     count = count + 1
                     chance=chance-1
                     print(chance, "Chances are remaining")
                     print(f"Comp_point : {comp_point} and User_point : {user_point}")
                     user_point=user_point+1
          elif c==1 and choice=="WATER" or c==2 and choice=="SNAKE" or c==3 and choice=="GUN" :
                     comp_point = comp_point + 1
                     print("Computer Win the Chance")
                     count=count+1
                     chance=chance-1
                     print(chance, "Chances are remaining ")
                     print(f"Comp_point : {comp_point} and User_point : {user_point}")


          else :
                print("Your choice is not valid , Please Give proper choice :")
          print("comp_point=",comp_point)
          print("user_Point=",user_point)

print("GAME OVER")
print("The Final Points are : ", "COMPUTER=",comp_point,"And USER=",user_point)
if comp_point > user_point :
      print("You Lose The game :(, Better Luck Next Time ")
elif comp_point< user_point :
      print("YAYYYY!!! You Win The Game, CONGRATULATIONS :>!!")
else :
      print("Your and Computers points are same, GAME DRAW!!!")
print("PLAYY AGAIN !!")






