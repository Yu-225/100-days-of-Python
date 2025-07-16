"""Cooler calculator program."""

from art import BANNER

from colorama import Fore


RUN = True
while RUN:
    print("\n" * 20)
    print(
        f"""
    {Fore.YELLOW}{BANNER}
    {Fore.YELLOW}Chose an operation:

    {Fore.GREEN}[{Fore.YELLOW}1{Fore.GREEN}] Add
    {Fore.GREEN}[{Fore.YELLOW}2{Fore.GREEN}] Subtract
    {Fore.GREEN}[{Fore.YELLOW}3{Fore.GREEN}] Multiply
    {Fore.GREEN}[{Fore.YELLOW}4{Fore.GREEN}] Divide

    {Fore.GREEN}[{Fore.YELLOW}0{Fore.GREEN}] Exit
    """
    )

    choise = int(input("> " + Fore.YELLOW))
    if choise == 0:
        RUN = False
        break

    num1 = float(input("First number: "))
    num2 = float(input("Second number: "))

    match choise:
        case 1:
            print(num1 + num2)
        case 2:
            print(num1 - num2)
        case 3:
            print(num1 * num2)
        case 4:
            print(num1 / num2)
        case _:
            RUN = False
            break

    RUN = input("Should continue? (y/n): ") == "y"

    # should_continue = input("Should continue? (y/n): ")
    # if should_continue == "n":
    #     RUN = False
    #     break


print(Fore.RESET)
