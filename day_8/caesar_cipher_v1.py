#!/usr/bin/python3
# day 8 project - Caesar cipher
# Program encodes and decodes text using the caesarian cipher algorithm.

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type \'encode\' to encrypt, type \'decode\' to decrypt:")
text = input("Type your message: ").lower()
shift = int(input("Type the shift number: "))

def encrypt(text="", shift=0):
    for letter in text:
            index = alphabet.find(letter, 0, len(alphabet))
            print(f"{letter} is found at index: {index}")
