#!/usr/bin/python3
""" 
    Program generates a random strong password with key features desired by user.
"""

import random

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password? "))
nr_symbols = int(input("How many symbols would you like? "))
nr_numbers = int(input("How many numbers would you like? "))
word = list()
pas = list()
password = ''

for i in range(0, nr_letters):
    r = random.randint(1, len(alphabet) - 1)
    word.append(alphabet[r])

for j in range(0, nr_numbers):
    p = random.randint(1, len(numbers) - 1)
    word.append(numbers[p])

for k in range(0, nr_symbols):
    q = random.randint(1, len(symbols) - 1)
    word.append(symbols[q])

taken_index = list()
for index in range(0, len(word)):
    x = random.randint(0, len(word) - 1)
    while x in taken_index:
        x = random.randint(0, len(symbols) - 1)
    taken_index.append(x)
    pas.insert(x, word[index])

for item in pas:
    password = password + item

print(password)
