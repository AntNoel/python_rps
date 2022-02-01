
import random

# print texts for rps
#request p1 input from user
#request p2 input fgrom user
#print shoot text
# logic to decide who wins
#
#
#


print("...rock...")
print("...paper...")
print("...scissors...")

p1 = input("(Enter Player 1's choices): ").lower()
# p2 = input("(Enter Player 2's choices): ").lower()
computer = random.choice(["rock", "paper", "scissors"])


print(f"The computer plays: {p2}")

#tie
if p1 == computer:
    print("It's a TIE!")
elif (p1 == 'rock' and computer == 'scissors') or (p1 == 'paper' and computer == 'rock') or (p1 == 'scissors' and computer == 'paper'):
    print("Player 1 WINS!")
elif (computer == 'rock' and computer == 'scissors') or (computer == 'paper' and p1 == 'rock') or (computer == 'scissors' and p1 == 'paper'):
    print("Computer WINS!")

