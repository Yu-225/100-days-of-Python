"""Passworg Generator Program."""

import random
from string import ascii_lowercase, ascii_uppercase, digits, punctuation


letters_lowercase = list(ascii_lowercase)
letters_uppercase = list(ascii_uppercase)
numbers = list(digits)
symbols = list(punctuation)


print("Welcome to the PyPassword Generator!")
pass_length = int(
    input("How many letters would you like in your password? (default 8): ") or "8"
)
include_uppercase = (
    input("Would you like to include uppercase letters? (y/n): ") or False
)
include_numbers = input("Would you like to include numbers? (y/n): ") or False
include_symbols = input("Would you like to include symbols? (y/n): ") or False

password = []

for _ in range(pass_length):
    password += random.choice(letters_lowercase)

if include_uppercase:
    for _ in range(pass_length):
        password += random.choice(letters_uppercase)

if include_numbers:
    for _ in range(pass_length):
        password += random.choice(numbers)

if include_symbols:
    for _ in range(pass_length):
        password += random.choice(symbols)

random.shuffle(password)
print(f'Your password is: {"".join(password)[0:pass_length]}')
