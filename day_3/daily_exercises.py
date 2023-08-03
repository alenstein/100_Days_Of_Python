# exercise_1 - Odd or Even
"""
    Program works out if a given number is an odd or even number.
"""
num = int(input("Enter any integer: "))

if num % 2 == 0:
    print("The number is even")
else:
    print("This is definitely an odd number!")
print()

# exercise_2 - BMI 2.0
"""
    Program interprets the Body Mass Index (BMI) based on a user's weight
    and height.
"""
# Data collection
height = float(input("Enter your height in metres: "))
weight = float(input("Enter your weight in kg's: "))

# Data Analysis
BMI = round(weight / (height ** 2))

# Results
if BMI < 18.5:
    print(f"Your BMI is {BMI}, indicates you are under weight!")
elif BMI < 25:
    print(f"Your BMI is {BMI}, indicates you are normal weight.")
elif BMI < 30:
    print("Your BMI is {BMI}, indicates you are overweight!")
elif BMI < 35:
    print("Your BMI is {BMI}, indicates you are obese!")
else:
    print("Your BMI is {BMI}, indicates you are clinically obese")
print()

# exercise_3 - Leap year 
"""
    Program works out whether if a given year is a leap year.
"""
year = int(input("enter a year: "))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print(f"{year} is a leap year.")
        else:
            print(f"{year} is not a leap year.")
    else:
        print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")
print()
