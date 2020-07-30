import time, random
user_score=0
computer_score=0
overs=0
balls=1
user_duck=True
computer_duck=True
user_out=False
computer_out=False
toss  = ['heads', 'tails']
bat_or_bowl=["Bat","Bowl"]
print("Toss time!")
choice=input("Head/Tails?\n1.Heads\n2.Tails\nEnter your choice: ")
if choice=='1' or choice=='2':
   who=random.choice(toss)
   #User won the toss!
   if who==choice:

      print("Hurray you won the toss!")
      option=input("What do you wish to do?\n1.Bat\n2.Bowl\nEnter the option: ")
      if option=='1' or option=='2':

         #User chose to bat
         if option=='1':
            print("You chose to bat!")
            print("Let's begin!")
            user_input=int(input("Enter a number between 1-6:"))
            computer_input=random.randint(1,6)
            if user_input==computer_input:
                  computer_out=True

            if user_input!=computer_input:
               user_score+=user_input
            if user_input<=0 or user_input>6:
                  print("Invalid input!")
                  user_score=0
                  balls=0
            else:
                 print()
                 print("Your input is: ",user_input," and computer input is: ",computer_input)
                 print()
                 print("Current score:",user_score)
                 print("Overs:",overs,".",balls)
                 print()
                 print()
            while user_input!=computer_input:
               user_duck=False
               user_input=int(input("Enter a number between 1-6:"))
               if user_input<=0 or user_input>6:
                  print("Invalid input!")
                  continue
               computer_input=random.randint(1,6)
               user_score+=user_input
               balls+=1
               if balls%6==0:
                  overs+=1
               if balls==6:
                  balls=0

               print()
               print("Your input is",user_input," and computer input is ",computer_input)
               print()
               print("Current score:",user_score)
               print("Overs:",overs,".",balls)
               print()
            print("Out!!!")
            if user_duck:
               user_score=0
            if user_score==0:
               print("Duck!!!")
            else:
               if overs<=1:
                  print("You scored ",user_score," from ",overs," over and",balls," balls.")
               else:
                  print("You scored ",user_score," from ",overs," overs and",balls," balls.")

            #User's turn to bowl
            balls=1
            overs=0
            print("Now your turn to bowl\n\nNever allow the opponent to cross your score\nAll the best!")
            user_input=int(input("Enter a number between 1-6:"))
            computer_input=random.randint(1,6)
            computer_score+=computer_input
            if computer_score!=user_score:
               computer_duck=False
            else:
               computer_score=0
            if user_input<=0 or user_input>6:
                  print("Invalid input!")
                  computer_score=0
                  balls=0
            else:
                 print("Your input is: ",user_input," and computer input is: ",computer_input)
                 print("Current score:",computer_score)
                 print("Overs:",overs,".",balls)
            while computer_score<user_score:
               user_input=int(input("Enter a number between 1-6:"))
               if user_input<=0 or user_input>6:
                  print("Invalid input!")
                  continue
               computer_input=random.randint(1,6)
               if user_input==computer_input:
                  break
               computer_score+=computer_input
               balls+=1
               if balls%6==0:
                  overs+=1
               if balls==6:
                  balls=0
               print()
               print("Your input is",user_input," and computer input is ",computer_input)
               print("Current score:",computer_score)
               print("Overs:",overs,".",balls)
               print()
            if computer_out:
               print("Out!!!")
            if computer_duck:
               computer_score=0
            if overs<=0:
               print("Computer scored ",computer_score," from ",overs," over and",balls+1," balls")
            else:
               print("Computer scored ",computer_score," from ",overs," overs and",balls+1," balls")
            if user_score>computer_score:
               print("You won!")
               print("Scores:\nYou:",user_score,"\nComputer:",computer_score)
            else:
               print("Computer won!!!\nBetter luck next time")
               print("Scores:\nComputer:",computer_score,"\nYou:",user_score)

         #User chose to bowl
         else:

            print("You chose to bowl!")
            user_input=int(input("Enter a number between 1-6:"))
            computer_input=random.randint(1,6)
            computer_score+=computer_input
            if computer_input!=user_input:
               computer_duck=False
            else:
               computer_score=0
            if user_input<=0 or user_input>6:
                  print("Invalid input!")
                  computer_score=0
                  balls=0
            else:
                 print()
                 print("Your input is: ",user_input," and computer input is: ",computer_input)
                 print("Current score:",computer_score)
                 print("Overs:",overs,".",balls)
                 print()
            while computer_input!=user_input:
               user_input=int(input("Enter a number between 1-6:"))
               if user_input<=0 or user_input>6:
                  print("Invalid input!")
                  continue
               computer_input=random.randint(1,6)
               if computer_input==user_input:
                  break
               computer_score+=computer_input
               balls+=1
               if balls%6==0:
                  overs+=1
               if balls==6:
                  balls=0
               print()
               print("Your input is",user_input," and computer input is ",computer_input)
               print("Current score:",computer_score)
               print("Overs:",overs,".",balls)
               print()
            print("Out!!!")
            if computer_duck:
               computer_score=0
            if computer_duck:
               print("Duck!!!")
            else:
               if overs<=0:
                   print("Computer scored ",computer_score," from ",overs," over and",balls+1," balls")
               else:
                   print("Computer scored ",computer_score," from ",overs," overs and",balls+1," balls")


            #User's turn to bat
            overs=0
            balls=1
            print("Now it's your turn to bat\nTry to defeat the oppponent\nAll the best!")
            print("Let's begin!")
            user_input=int(input("Enter a number between 1-6:"))
            computer_input=random.randint(1,6)
            if user_input!=computer_input:
               user_score+=user_input
            if user_input<=0 or user_input>6:
                  print("Invalid input!")
                  user_score=0
                  balls=0
            else:
                 print()
                 print("Your input is: ",user_input," and computer input is: ",computer_input)
                 print()
                 print("Current score:",user_score)
                 print("Overs:",overs,".",balls)
                 print()
                 print()
            while user_score<computer_score:
               user_duck=False
               user_input=int(input("Enter a number between 1-6:"))
               if user_input<=0 or user_input>6:
                  print("Invalid input!")
                  continue
               computer_input=random.randint(1,6)
               if user_input==computer_input:
                  user_out=True
                  break
               user_score+=user_input
               balls+=1
               if balls%6==0:
                  overs+=1
               if balls==6:
                  balls=0
               print()
               print("Your input is",user_input," and computer input is ",computer_input)
               print()
               print("Current score:",user_score)
               print("Overs:",overs,".",balls)
               print()
            if user_out:
               print("Out!!!")
            if user_duck:
               user_score=0
            if overs<=0:
               print("You scored ",user_score," from ",overs," over and",balls+1," balls")
            else:
               print("You scored ",user_score," from ",overs," overs and",balls+1," balls")
            if user_score>computer_score:
               print("You won!")
               print("Scores:\nYou:",user_score,"\nComputer:",computer_score)
            elif computer_score>user_score:
               print("Computer won!!!\nBetter luck next time")
               print("Scores:\nComputer:",computer_score,"\nYou:",user_score)
            else:
               print("Tie!!!")
               print("No one gives up!")
      else:
         print("Invalid option begin given!")

   #Computer won the toss!
   else:
      computer_option=random.choice(bat_or_bowl)
      print("Bad luck! computer won the toss and chose to ",computer_option)
      print("Let the battle begin!!!")

      #If computer choses batting
      if computer_option=="Bat":

            print("Computer bats!")
            user_input=int(input("Enter a number between 1-6:"))
            computer_input=random.randint(1,6)
            computer_score+=computer_input
            if computer_input!=user_input:
               computer_duck=False
            else:
               computer_score=0
            if user_input<=0 or user_input>6:
                  print("Invalid input!")
                  computer_score=0
                  balls=0
            else:
                 print()
                 print("Your input is: ",user_input," and computer input is: ",computer_input)
                 print("Current score:",computer_score)
                 print("Overs:",overs,".",balls)
                 print()
            while computer_input!=user_input:
               user_input=int(input("Enter a number between 1-6:"))
               if user_input<=0 or user_input>6:
                  print("Invalid input!")
                  continue
               computer_input=random.randint(1,6)
               if computer_input==user_input:
                  break
               computer_score+=computer_input
               balls+=1
               if balls%6==0:
                  overs+=1
               if balls==6:
                  balls=0
               print()
               print("Your input is",user_input," and computer input is ",computer_input)
               print("Current score:",computer_score)
               print("Overs:",overs,".",balls)
               print()
            print("Out!!!")
            if computer_duck:
               print("Duck!!!")
               computer_score=0
            else:
               if overs<=0:
                   print("Computer scored ",computer_score," from ",overs," over and",balls+1," balls")
               else:
                   print("Computer scored ",computer_score," from ",overs," overs and",balls+1," balls")

            #Computer's turn to bowl


            overs=0
            balls=1
            print("Computer bowls!")
            user_input=int(input("Enter a number between 1-6:"))
            computer_input=random.randint(1,6)
            if user_input!=computer_input:
               user_score+=user_input
            if user_input<=0 or user_input>6:
                  print("Invalid input!")
                  user_score=0
                  balls=0
            else:
                 print()
                 print("Your input is: ",user_input," and computer input is: ",computer_input)
                 print()
                 print("Current score:",user_score)
                 print("Overs:",overs,".",balls)
                 print()
                 print()
            while user_score<=computer_score:
               user_duck=False
               user_input=int(input("Enter a number between 1-6:"))
               if user_input<=0 or user_input>6:
                  print("Invalid input!")
                  continue
               computer_input=random.randint(1,6)
               if user_input==computer_input:
                  user_out=True
                  break
               user_score+=user_input
               balls+=1
               if balls%6==0:
                  overs+=1
               if balls==6:
                  balls=0
               print()
               print("Your input is",user_input," and computer input is ",computer_input)
               print()
               print("Current score:",user_score)
               print("Overs:",overs,".",balls)
               print()
            if user_out:
               print("Out!!!")
            if user_duck:
               user_score=0
            if overs<=0:
               print("You scored ",user_score," from ",overs," over and",balls+1," balls")
            else:
               print("You scored ",user_score," from ",overs," overs and",balls+1," balls")


            #Announcing the winner


            if user_score>computer_score:
               print("You won!")
               print("Scores:\nYou:",user_score,"\nComputer:",computer_score)
            elif computer_score>user_score:
               print("Computer won!!!\nBetter luck next time")
               print("Scores:\nComputer:",computer_score,"\nYou:",user_score)
            else:
               print("Tie!!!")
               print("No one gives up!")





      #If computer choses to bowl
      else:

            print("Computer bowls!")
            user_input=int(input("Enter a number between 1-6:"))
            computer_input=random.randint(1,6)
            if user_input!=computer_input:
               user_score+=user_input
            if user_input<=0 or user_input>6:
                  print("Invalid input!")
                  user_score=0
                  balls=0
            else:
                 print()
                 print("Your input is: ",user_input," and computer input is: ",computer_input)
                 print()
                 print("Current score:",user_score)
                 print("Overs:",overs,".",balls)
                 print()
                 print()
            while user_input!=computer_input:
               user_duck=False
               user_input=int(input("Enter a number between 1-6:"))
               if user_input<=0 or user_input>6:
                  print("Invalid input!")
                  continue
               computer_input=random.randint(1,6)
               if user_input==computer_input:
                  user_out=True
                  break
               user_score+=user_input
               balls+=1
               if balls%6==0:
                  overs+=1
               if balls==6:
                  balls=0
               print()
               print("Your input is",user_input," and computer input is ",computer_input)
               print()
               print("Current score:",user_score)
               print("Overs:",overs,".",balls)
               print()
            if user_out:
               print("Out!!!")
            if user_duck:
               user_score=0
            if overs<=0:
               print("You scored ",user_score," from ",overs," over and",balls+1," balls")
            else:
               print("You scored ",user_score," from ",overs," overs and",balls+1," balls")

           #Computer's turn to bat

            overs=0
            balls=1
            print("Computer bats!")
            user_input=int(input("Enter a number between 1-6:"))
            computer_input=random.randint(1,6)
            computer_score+=computer_input
            if computer_input!=user_input:
               computer_duck=False
            else:
               computer_score=0
            if user_input<=0 or user_input>6:
                  print("Invalid input!")
                  computer_score=0
                  balls=0
            else:
                 print()
                 print("Your input is: ",user_input," and computer input is: ",computer_input)
                 print("Current score:",computer_score)
                 print("Overs:",overs,".",balls)
                 print()
            while computer_score<=user_score:
               computer_duck=False
               user_input=int(input("Enter a number between 1-6:"))
               if user_input<=0 or user_input>6:
                  print("Invalid input!")
                  continue
               computer_input=random.randint(1,6)
               if computer_input==user_input:
                  computer_out=True
                  break
               computer_score+=computer_input
               balls+=1
               if balls%6==0:
                  overs+=1
               if balls==6:
                  balls=0
               print()
               print("Your input is",user_input," and computer input is ",computer_input)
               print("Current score:",computer_score)
               print("Overs:",overs,".",balls)
               print()
            if computer_out:
               print("Out!!!")
            if computer_duck:
               print("Duck!!!")
               computer_score=0
            else:
               if overs<=0:
                   print("Computer scored ",computer_score," from ",overs," over and",balls+1," balls")
               else:
                   print("Computer scored ",computer_score," from ",overs," overs and",balls+1," balls")







          #Announcing the winner

            if user_score>computer_score:
               print("You won!")
               print("Scores:\nYou:",user_score,"\nComputer:",computer_score)
               print("You Won By: ", user_score - computer_score)
            elif computer_score>user_score:
               print("Computer won!!!\nBetter luck next time")
               print("Scores:\nComputer:",computer_score,"\nYou:",user_score)
               print("Computer won by: ", computer_score - user_score)


            else:
               print("Tie!!!")
               print("No one gives up!")


else:
    print("Invalid option given!")
