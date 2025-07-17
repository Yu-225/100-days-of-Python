"""Blackjack game implementation"""

from random import choice

from art import BANNER


def deal_card():
    """Returns a random card from the deck."""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10]
    return choice(cards)


def calculate_score(cards):
    """Take a list of cards and return the score calculated from the cards"""

    if sum(cards) == 21 and len(cards) == 2:
        return 0

    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)


def compare(u_score: int, c_score: int) -> str:
    """Compare scores"""

    result = "You lose"

    if u_score == c_score:
        result = "Draw"

    if c_score == 0:
        result = "Lose, opponent has Blackjack"

    if u_score == 0:
        result = "Win with a Blackjack"

    if u_score > 21:
        result = "You went over. You lose"

    if c_score > 21:
        result = "Opponent went over. You win"

    if u_score > c_score:
        result = "You win"

    return result


def play_game():
    """Main game function"""

    print(BANNER)
    user_cards = []
    computer_cards = []
    game_over = False
    turn = 0

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        turn += 1

        print()
        print(f" Turn: {turn} ".center(50, "-"))
        print(f"Computer's first card: {computer_cards[0]}")

        print(f"Your cards: {user_cards}, current score: {user_score}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            game_over = True
        else:
            user_should_deal = input(
                "\nType 'y' to get another card, type 'n' to pass: "
            )
            if user_should_deal == "y":
                user_cards.append(deal_card())
                user_score = calculate_score(user_cards)
                print(user_cards, user_score)
            else:
                game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print()
    print(f" Turn: {turn} ".center(50, "-"))
    print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
    print(f"Your final hand: {user_cards}, final score: {user_score}")
    print("\n" + compare(user_score, computer_score).center(50, "-") + "\n")


while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
    print("\n" * 20)
    play_game()
