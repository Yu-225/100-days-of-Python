"""Rock Paper Scissors Game."""

import random

# Rock
rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

# Paper
paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

# Scissors
scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
game_images = [rock, paper, scissors]


print('What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors')
player_choice = int(input())
computer_choice = random.randint(0, 2)

if player_choice >= 3 or player_choice < 0:
    print('You typed an invalid number, you lose!')

else:
    print(game_images[player_choice])
    print('Computer chose:')
    print(game_images[computer_choice])


    if player_choice == 0 and computer_choice == 2:
        print('You win!')

    elif player_choice == 2 and computer_choice == 0:
        print('You lose!')

    elif computer_choice > player_choice:
        print('You lose!')

    elif player_choice > computer_choice:
        print('You win!')


    elif player_choice == computer_choice:
        print('It\'s a draw!')
