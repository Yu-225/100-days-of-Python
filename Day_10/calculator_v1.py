"""Calculator program."""

from art import BANNER


def add(n1, n2):
    """Add two numbers."""
    return n1 + n2


def subtract(n1, n2):
    """Subtract two numbers."""
    return n1 - n2


def multiply(n1, n2):
    """Multiply two numbers."""
    return n1 * n2


def divide(n1, n2):
    """Divide two numbers."""
    return n1 / n2


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}


def calculator():
    """Calculator program."""

    print(BANNER)

    should_accumulate = True
    num1 = float(input("What's the first number?: "))

    while should_accumulate:
        for symbol in operations:
            print(symbol)
        operation_symbol = input("Pick an operation from the line above: ")
        num2 = float(input("What's the second number?: "))
        answer = operations[operation_symbol](float(num1), float(num2))
        print(f"{num1} {operation_symbol} {num2} = {answer}")

        choice = input(
            f"Type 'y' to continue calculating with {answer}, \
            or type 'n' to start a new calcula tion: "
        )

        if choice == "y":
            num1 = answer
        else:
            should_accumulate = False
            print("\n" * 20)
            calculator()


calculator()
