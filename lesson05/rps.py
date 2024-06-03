import sys
import random
from enum import Enum


class RPS(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3

    # print(RPS.ROCK)           # RPS.ROCK
    # print(RPS(2))             # RPS.PAPER
    # print(RPS['ROCK'])        # RPS.ROCK
    # print(RPS.ROCK.value)     # 1
    # sys.exit()


print('')
player_choice_str = input(
    "Enter...\n1 for rock,\n2 for paper,\n3 for scissors:\n\n")

player_choice = int(player_choice_str)

if player_choice < 1 or player_choice > 3:
    sys.exit("You must enter 1, 2, or 3.")

computer_choice_str = random.choice("123")
computer_choice = int(computer_choice_str)
print('')
print("You chose " + str(RPS(player_choice)).replace('RPS.', '') + ".")
print("Computer chose " + str(RPS(computer_choice)).replace('RPS.', '') + ".")
print('')

if (player_choice == 1 and computer_choice == 2) or (player_choice == 2 and computer_choice == 3) or (player_choice == 3 and computer_choice == 1):
    print("You lose!")
elif (player_choice == computer_choice):
    print("It's a draw!")
else:
    print("You win!")
