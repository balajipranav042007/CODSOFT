import random
choices=["rock","paper","scissors"]
userchoice=input("Enter your choice(rock,paper,scissors):")
computerchoice=random.choice(choices)
print("user choice:",userchoice)
print("computer choice:",computerchoice)
if userchoice == computerchoice:
    print("IT'S A DRAW MATCH")
elif (
    (userchoice=="rock" and computerchoice=="scissors")or
    (userchoice=="scissors" and computerchoice=="paper")or
    (userchoice=="paper" and computerchoice=="rock")):
    print("USER WIN")
elif(
    (userchoice=="rock" and computerchoice=="paper")or
    (userchoice=="scissors" and computerchoice=="rock")or
    (userchoice=="paper" and computerchoice=="scissors")):
    print("USER LOSE")
else:
    print("INVALID")
      
