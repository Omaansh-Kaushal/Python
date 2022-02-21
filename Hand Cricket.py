import random

print(""" ~~~~~~~~~~ Game of Cricket ~~~~~~~~~~
 
Instructions:
 
1. You have to select any random number from 1 to 6.
2. The computer will also select a number.
3. While batting, if the number selected by you and computer is different, then your number will add to your runs.
   If the number selected by you and computer is same, then you will lose your wicket.
4. While bowling, if the number selected by you and computer is different, then the computer's number will add to its runs.
   If the number selected by you and computer is same, then the computer will lose its wicket.
5. Each player will get 2 wickets and 2 overs (12 balls) for batting and bowling.
6. The innings will end after either the three wickets fell or the overs end.
7. The player with maximum runs wins. """)
 
print("\n---------- Start Game ----------")
 
import random
 
# Toss 
 
print("\nHere comes the Toss")
toss = (input("Choose H for Heads or T for Tails: ")).lower()
 
random_toss = random.randint(1,2)            # In random_toss (1 = Heads) and (2 = Tails)
random_opt = random.randint(1,2)             # In random_opt (1 = bat) and (2 = ball)
 
u_opt = 0
c_opt = 0
 
if random_toss == 1 and toss == "H":
    print("\nYou won the toss")
    u_opt = (input("What would you like to do (Chase or Set)?: ")).lower()
 
elif random_toss == 2 and toss == "T":
    print("\nYou won the toss")
    u_opt = (input("What would you like to do (Chase or Set)?: ")).lower()    
  
else:
    print("\nComputer won the toss")
 
    if random_opt == 1:
        c_opt = "set"
        print("Computer elects to",c_opt, "your target.")
 
    elif random_opt == 2:
        c_opt = "chase"
        print("Computer elects to",c_opt, "your target.")
 
# First Innings 
 
print("\n---------- First Innings Begins ----------")
 
runs_1 = 0
wickets_1 = 0
balls_1 = 0
 
while wickets_1 != 2 and balls_1 != 12:
 
    u_choice = int(input("\nChoose any number from 1 to 6: "))
    c_choice = random.randint(1,6)
 
    if u_choice < 1 or u_choice > 6:
        print("\nThe Chosen Number does belong to range 1-6. Please choose a value from 1 to 6.")
 
    else:
        print("Your choice: ",u_choice,"\nComputer's choice: ",c_choice)
 
        if u_choice == c_choice:
            wickets_1 += 1
 
        else:
            if u_opt == "set" or c_opt == "chase":
                Bat_first = "You"
                Ball_first = "Computer"
                runs_1 += u_choice
 
            elif u_opt == "chase" or c_opt == "set":
                Bat_first = "Computer"
                Ball_first = "You"
                runs_1 += c_choice
 
        print("\nScore =",runs_1,"/",wickets_1)
 
        balls_1 += 1
 
        if balls_1 == 6:
            print("End of Over 1")
            if runs_1 < 12:
                print("The bowler has done an excellent job at keeping the batsmen quiet. Can they replicate it to minimize the target? Let's find out!")
            else:
                print("The opening over of the innings was an expensive one. Can the bowlers pull this one back? Let's find out!")

        elif balls_1 == 12:
            print("End of Over 2")
            if runs_1 < 30:
                print("The bowlers did a fantastic job in keeping batsmen to a low score. Can their teammates chase this down? ")
            else:
                print("The bowlers tried their best but couldn't hold the carnage of the batsmen. Over to the bastmen now!")

        print("Balls remaining: ",12 - balls_1)
 
print("\n---------- End of Innings ----------") 
 
print("\nFinal Score:")
print("Runs =",runs_1)
print("wickets =",wickets_1)
print("Target :", runs_1 + 1)

print("\n",Ball_first,"needs",runs_1 + 1,"runs to win.")
 
# Second Innings 
 
print("\n---------- Second Innings Begins ----------")
 
runs_2 = 0
wickets_2 = 0
balls_2 = 0
 
while wickets_2 != 2 and balls_2 != 12 and runs_2 <= runs_1:
 
    u_choice = int(input("\nChoose any number from 1 to 6: "))
    c_choice = random.randint(1,6)
 
    if u_choice < 1 or u_choice > 6:
        print("\nThe Chosen Number does belong to range 1-6. Please choose a value from 1 to 6.")
 
    else:
        print("Your choice: ",u_choice,"\nComputer's choice: ",c_choice)
 
        if u_choice == c_choice:
            wickets_2 += 1
 
        else:
            if Bat_first == "Computer": 
                runs_2 += u_choice
                Bat_second = "You"
 
            elif Bat_first == "You":
                runs_2 += c_choice
                Bat_second = "Computer"
 
        print("\nScore =",runs_2,"/",wickets_2)
 
        balls_2 += 1
 
        if balls_2 == 6:
            print("End of Over 1")
 
        elif balls_2 == 12:
            print("End of Over 2")
 
        if runs_2 <= runs_1 and balls_2 <= 11 and wickets_2 != 2:
            print("To win:",runs_1 - runs_2 + 1,"runs needed from",12 - balls_2,"balls.")
 
print("\n---------- End of Innings ----------") 
 
print("\nFinal Score:")
print("Runs =",runs_2)
print("wickets =",wickets_2)
 
# Result of Match 
 
print("\n~~~~~~~~~~ Result ~~~~~~~~~~")
 
if runs_1 > runs_2:
 
    if Bat_first == "You": 
        print("\nCongratulations! You won the Match by",runs_1 - runs_2,"runs.")
 
    else:
        print("\nBetter luck next time! The Computer won the Match by",runs_1 - runs_2,"runs.") 
 
elif runs_2 > runs_1:
 
    if Bat_second == "You": 
        print("\nCongratulations! You won the Match by",2 - wickets_2,"wickets.")
 
    else:
        print("\nBetter luck next time! The Computer won the Match by",2 - wickets_2,"wickets.")
 
else:
    print("The Match is a Tie.","\nNo one Wins.")

o