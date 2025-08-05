"""..."""


def odd_or_even(number):
    """Check if a number is odd or even.

    Args:
        number (int): The number to check.

    Returns:
        str: "even" if the number is even, "odd" if the number is odd.
    """

    if number % 2 == 0:
        return "even"
    return "odd"


if __name__ == "__main__":
    print(odd_or_even(2))
    print(odd_or_even(3))
    print(odd_or_even(0))
    print(odd_or_even(-1))
    print(odd_or_even(-5.2))
    print(odd_or_even(100))
    print(odd_or_even(101))
