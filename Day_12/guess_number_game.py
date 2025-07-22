"""Guess the number game."""

from random import randint

from art import BANNER


print(BANNER)


computer_number = randint(1, 100)
USER_GUESS = 0
ATTEMPTS = 0
DIFFICULTY = ""

DIFFICULTY = input("Choose a difficulty. Type 'easy' or 'hard': ")
if DIFFICULTY == "easy":
    ATTEMPTS = 10
elif DIFFICULTY == "hard":
    ATTEMPTS = 5
else:
    print("Error")


while ATTEMPTS > 0:
    print()
    print(f" You have {ATTEMPTS} attempts to guess the number. ".center(50, "-"))
    USER_GUESS = int(input("Guess a number between 1 and 100: "))

    if USER_GUESS <= 0 or USER_GUESS >= 101:
        print("Wrong number. Try number from 1 to 100.")

    elif USER_GUESS > computer_number:
        print("Too high")
        ATTEMPTS -= 1

    elif USER_GUESS < computer_number:
        print("Too low")
        ATTEMPTS -= 1

    elif USER_GUESS == computer_number:
        print("You win")
        break

if ATTEMPTS == 0:
    print("You lose")
