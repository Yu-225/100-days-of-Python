"""Hangman game."""

import random
import os

import hangman_world
import hangman_stages


def clear_screen():
    """Clears the terminal screen."""
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")


chosen_word = random.choice(hangman_world.word_list)
# print(chosen_word)
placeholder = "_" * len(chosen_word)
# print(placeholder)

correct_letters = []
LIVES = 6


GAME_OVER = False
while not GAME_OVER:
    # clear_screen()

    guess = input("Guess a letter: ").lower()

    DISPLAY = ""

    for letter in chosen_word:
        if letter == guess:
            DISPLAY += letter
            correct_letters.append(letter)

        elif letter in correct_letters:
            DISPLAY += letter

        else:
            DISPLAY += "_"

    if "_" not in DISPLAY:
        GAME_OVER = True
        print(f'{" You won! ":*^38}')

    if guess not in chosen_word:
        LIVES -= 1
        print("Wrong guess! You lose a life.")

        if LIVES == 0:
            GAME_OVER = True
            print(f'{" You lost! ":*^38}')

    print(DISPLAY)
    print(hangman_stages.stages[LIVES])
    print(f'{"*" * 10} {LIVES} / 6 LIVES LEFT {"*" * 10}')
