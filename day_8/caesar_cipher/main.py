#!/usr/bin/python3
# Final caesarean cipher program for day 8 project

import art

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

ans = True

#TODO-1: Combine the encrypt() and decrypt() functions into a single function called caesar(). 

def caesar(txt, cmd, sa):
    """
        Function encrypts or decrypts text into different characters
        or original form.

        Params:
            txt (str): text to be encrypted or decrypted
            sa (int): shift amount
            cmd: selector which specifies decode or encode command.

        Return:
            encrypted or decrypted characters.
    """
    chars = ""
    for letter in txt:
        position = alphabet.index(letter)
        if cmd == "encode":
            new_position = position + sa
        elif cmd == "decode":
            new_position = position - sa
        else:
            print("ERROR: Invalid input")
        chars += alphabet[new_position]
    print(f"The {cmd}d text is {chars}")

def reload_game(char='n'):
    if char == 'n':
        return False
    elif char == 'y':
        return True
    else:
        print("ERROR: invalid input!")

#TODO-2: Call the caesar() function, passing over the 'text', 'shift' and 'direction' values.
while ans:
    print("\033c", end="")
    print(art.logo)

    # input data
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n")) % len(alphabet)
    
    # modulating the shift number so that its not out of range.
    shift = shift % (len(alphabet) - 1)
    # perfom algorithm
    caesar(text, direction, shift)
    reload = input("Do you want to reload the algorithm (Y or N): ").lower()
    ans = reload_game(reload)
