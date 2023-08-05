#!/usr/bin/python3
# Day 4 for 100 days of code _ Randomisation and Lists

# exercise_1 - Average height
"""
    Program calculates the average student height from a List of heights
"""

print("Enter the heights of the students (use a comma and space to separate the heights)")
heights = input("Enter student heights:\n ")
student_heights = heights.split(", ")
divisor = 0
total = 0

for height in student_heights:
    height = int(height)
    divisor = divisor + 1

print(f"there are {divisor} heights in the list.")

for height in student_heights:
    total = total + int(height)

average_height = round(total / divisor)

print(f'Average height rounded to the nearest whole number = {average_height}')


# exercise_2 - Highest in the room.
"""
    Program calculates the highest score from a List of scores.
"""
student_scores = [160, 170, 165, 178, 192, 187, 163, 181]
highest_score = int(student_scores[0])

for i in range(0, len(student_scores)):
    if highest_score < int(student_scores[i]):
        highest_score = int(student_scores[i])

print(f"The highest score is {highest_score}.")

# exercise_3 - Adding evens
"""
    Program calculates the sum of all even numbers from 1 to 100,
    including 1 and 100.
"""
total = 0
for i in range(2, 101, 2):
    total = total + i

print(f'total of all evens in [1, 100] is {total}')

# exercise_4 - Fizz Buzz
for n in range(1, 101):
    if n % 3 == 0:
        if n % 5 == 0:
            print("FizzBuzz")
        else:
            print("Fizz")
    elif n % 5 == 0:
        print("Buzz")
    else:
        print(n)

