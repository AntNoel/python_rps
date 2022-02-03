
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

player_wins = 0
computer_wins = 0

while player_wins < 2 and computer_wins < 2:
    print(f"Player Score: {player_wins}")
    print(f"Computer Score: {computer_wins}")

    player = input("(Enter Player 1's choices): ").lower()
    if player == 'quit()' or player == 'q':
        break
    # p2 = input("(Enter Player 2's choices): ").lower()
    computer = random.choice(["rock", "paper", "scissors"])


    print(f"The computer plays: {computer}")

    #tie
    if player == computer:
        print("It's a TIE!")
    elif (player == 'rock' and computer == 'scissors') or (player == 'paper' and computer == 'rock') or (player == 'scissors' and computer == 'paper'):
        player_wins += 1
        print("Player WINS!")
    elif (computer == 'rock' and computer == 'scissors') or (computer == 'paper' and player == 'rock') or (computer == 'scissors' and player == 'paper'):
        print("Computer WINS!")
        computer_wins += 1

    print(f'Final Scores... Player: ${player_wins}  Computer...{computer_wins}')
  
