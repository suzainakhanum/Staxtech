import random
userchoice=input("select the type (rock,paper,scissors): ").lower()
options=["rock","paper","scissors"]
computerchoice=random.choice(options)
print("computer choice is: ",computerchoice)
if (userchoice == computerchoice):
    print("It is draw")
elif(userchoice == "rock" and computerchoice == "scissors"):
    print("you wins")
elif(userchoice == "scissors" and computerchoice == "rock"):
    print("computer wins")
elif(userchoice == "paper" and computerchoice == "rock"):
    print("you wins")
elif(userchoice == "rock" and computerchoice == "paper"):
    print("computer wins")
elif(userchoice == "scissors" and computerchoice == "paper"):
    print("you wins")
elif(userchoice == "paper" and computerchoice == "scissors"):
    print("computer wins")
else:
    print("Error : Invalid choice. Please select rock, paper, or scissors.")
# Note: The code above is a simple rock-paper-scissors game.