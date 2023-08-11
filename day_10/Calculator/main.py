#!/usr/bin/python3
# Calculator project for day 10 

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

def reload_calc(answer=""):
    if answer == "y":
        return True
    elif answer == "n":
        return False
    else:
        print("ERROR: invalid input.")

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
    }
should_continue = True

while should_continue:

    num1 = int(input("What's the first number?: "))
    num2 = int(input("What's the second number?: "))

    print("Available operatios: \n")
    for k in operations:
        print(k)
    key = input("\nPick an operation from the lines above: ")
    result = operations[key](num1, num2)
    print(f"{num1} {key} {num2} = {result}")
    
    ans = input("Do you want to perfom another calculation?(y or n): ").lower()
    should_continue = reload_calc(ans)

