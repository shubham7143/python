#make game of stone paper scissors played b/w computer and user.
import random

inp = input("Enter your move: ")
inp = inp.lower()
moves = ("stone", "paper", "scissors")
cmove = random.choice(moves)
if(inp == cmove):
    print("Game draw!!!")
elif((inp == "stone" and cmove == "scissors") or (inp == "paper" and cmove == "stone") or (inp == "scissors" and cmove == "paper")):
    print("Congratulions, You won!!!")
else:
    print("You lost!!!")