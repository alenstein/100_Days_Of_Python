""" Day 2 project - tip calculator. """
print("Welcome to the tip calculator.")

bill = float(input("What was the total bill? $"))
percentage_tip = float(input("What percentage tip would you like to give? \
10, 12, or 15? "))
number_of_people = int(input("How many people to split the bill? "))

# Calculations
tip = round((bill * (percentage_tip / 100)) / number_of_people, 2)
bill_per_person = round((bill / number_of_people), 2) + tip 

# Results
print(f"Each person should pay: ${bill_per_person}")
