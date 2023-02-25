from os import system
from art import logo
from kosh import alphabet, special_chars, numbers

def caesar(start_text, shift_amount, cipher_direction):
    end_text = ""
    if cipher_direction == "decode":
        shift_amount *= -1
    for char in start_text:

        if char.isalpha():
            position = alphabet.index(char)
            new_position = position + shift_amount
            end_text += alphabet[new_position]
        elif char.isnumeric():
            position = numbers.index(char)
            new_position = position + shift_amount
            end_text += numbers[new_position]
        else:
            position = special_chars.index(char)
            new_position = position + shift_amount
            end_text += special_chars[new_position]

    print(f"Here's the {cipher_direction}d result: {end_text}\n")


print(logo)

go_again = True
while (go_again):
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift = shift % 26

    caesar(start_text=text, shift_amount=shift, cipher_direction=direction)
    ans = input("Wanna go again?(y/n)\n").lower()
    system('clear')
    if ans == 'n':
        print("Goodbye.")
        go_again = False
