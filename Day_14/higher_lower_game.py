"""Higher Lower Game"""

import os
import sys
import random

from art import LOGO, VS  # pylint: disable=no-name-in-module
import game_data


def clear_screen():
    """Clears the console screen."""
    os.system("cls" if os.name == "nt" else "clear")


def main(current_score: int = 0) -> None:
    """Main function."""

    # clear screen before starting the game
    clear_screen()

    # print logo
    print(LOGO)

    print(f" score: {current_score} ".center(40, "-"), end="\n")

    # choose and print random item from game_data
    compare_a = random.choice(game_data.data)
    game_data.data.remove(compare_a)
    print(
        "Compare A: "
        + compare_a["name"]
        + ", a "
        + compare_a["description"]
        + ", from "
        + compare_a["country"]
        + "."
    )

    # print vs
    print(VS)

    # Against the chosen item, choose another random item from game_data
    compare_b = random.choice(game_data.data)
    game_data.data.remove(compare_b)

    print(
        "Against B: "
        + compare_b["name"]
        + ", a "
        + compare_b["description"]
        + ", from "
        + compare_b["country"]
        + "."
    )

    # print Who has more followers? Type 'A' or 'B':
    print("Who has more followers? Type 'A' or 'B':")

    # Check if the user input is correct
    # If correct, add 1 to the score and choose another item from game_data
    user_guess = input()

    # If incorrect, print the score and end the game
    if (
        user_guess.lower() == "a"
        and compare_a["follower_count"] > compare_b["follower_count"]
    ):
        current_score += 1
        main(current_score)

    elif (
        user_guess.lower() == "b"
        and compare_b["follower_count"] > compare_a["follower_count"]
    ):
        current_score += 1
        main(current_score)

    else:
        print(f"Wrong! Final score: {current_score}")
        sys.exit()


if __name__ == "__main__":
    main()
