"""Ceaser cipher"""

from art import BANNER


alphabet_eng = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
]


def ceaser(text: str, shift: int, encode_or_decode: str, alphabet: list):
    """
    Encrypts or decrythras with Caesar Code and prints a result.

    Parameters:
        text (str): Text for encryption or decryption.
        shift (int): Shift amount.
        encode_or_decode (str): "encode" or "decode".
        alphabet (list)

    Returns:
        None
    """

    output_text = ""

    if encode_or_decode == "decode":
        shift *= -1

    for letter in text:
        if letter not in alphabet:
            output_text += letter
            continue

        shifted_position = alphabet.index(letter) + shift
        shifted_position %= len(alphabet)
        output_text += alphabet[shifted_position]

    print(f"The {encode_or_decode}d text is {output_text}")


print(BANNER)


RUN = True
while RUN:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n> ")

    if direction == "exit":
        RUN = False

    else:
        user_input = input("Type your message:\n> ").lower()
        shift_amount = int(input("Type the shift number:\n> "))
        ceaser(
            text=user_input,
            shift=shift_amount,
            encode_or_decode=direction,
            alphabet=alphabet_eng,
        )
