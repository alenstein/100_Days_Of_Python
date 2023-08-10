#!/usr/bin/python3 
# Day 8 for 100 days of python
import math

# exercise_1 - Area Calc
def paint_calc(height, width, cover):
    """ Function calculates the how many cans of paint you'll need tp buy.
        Params:
            height (int) - height of the wall
            width (int) - width of the wall
            cover (int) - area that i can can cover
        Return:
            the number of cans required for the specified @params
    """
    number_of_cans = math.ceil((height * width) / cover)
    return(number_of_cans)


test_h = int(input("Height of wall: "))
test_w = int(input("Width of the wall: "))
coverage = 5

cans = paint_calc(height=test_h, width=test_w, cover=coverage)

print(f"You Will need {cans} cans of the paint.")


# exercise_2 - Prime number checker
def is_prime(num):
    count = 0
    for divisor in range(1, num):
        if num % divisor == 0:
            count += 1
    if count > 2:
        return True
    else:
        return False

n = int(input("CHeck this number: "))
print(is_prime(num=n))

