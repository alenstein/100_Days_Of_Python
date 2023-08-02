"""
    Data types:
        - Strings
        - Int
        - boolean
        - float
"""

# exercise1
"""
    program that adds the digits in a 2 digit number.
"""
num = int(input("Enter any 2 digit number: "))
temp = str(num)
total = int(temp[0]) + int(temp[1])
print("The total of the digits in " + str(num) + " is " + str(total))
print()

# PEMDAS
# Parentheses
# Exponents
# Multiplication
# Division
# Addition
# Subtraction


# exercise_2 - BMI Calculator exercise
height = float(input("Enter your height in metres: "))
weight = float(input("Enter your weight in kgs:  "))

BMI = weight // (height ** 2)

print("\nYour BMI is " + str(int(BMI)))
print()

# exercise_3 - Your Life in weeks 
age = int(input("Enter your age: "))

ttl = 90 - age
z = ttl * 12
y = ttl * 52
x = ttl * 365

print(f"You have {x} days, {y} weeks, and {z} months left.")
print()

