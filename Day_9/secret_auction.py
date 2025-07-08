"""Secret auction program."""

import os

import art

print(art.LOGO)


def clear():
    """Clears the console."""
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")


def find_highest_bidder(bidding_dict):
    """Finds the highest bidder."""
    highest_bid = 0
    winner = ""
    for user in bidding_dict:
        curr_bid = int(bidding_dict[user])
        if curr_bid > highest_bid:
            highest_bid = curr_bid
            winner = user
    return {f"{winner}": highest_bid}


users = {}
CONTINUE_BIDDING = True
while CONTINUE_BIDDING:
    clear()
    user_name = input("Whats your name: ")
    user_bid = input("Whats your bid: ")
    users[user_name] = user_bid
    should_continue = input("Add another user? (y/n): ").lower()
    if should_continue == "n":
        CONTINUE_BIDDING = False
        print(find_highest_bidder(users))
