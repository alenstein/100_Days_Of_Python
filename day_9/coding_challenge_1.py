#!/usr/bin/python3
# exercise_1 - Grading program

student_scores = {
     "Harry": 81,
     "Ron": 78,
     "Hermione": 99,
     "Draco": 74,
     "Neville": 62,
 }

student_grades = {}


for key in student_scores:
    val = int(student_scores[key])
    if val > 90:
        student_grades[key] = "Outstanding"
    elif val > 80:
        student_grades[key] = "Exceed Expectations"
    elif val > 70:
        student_grades[key] = "Acceptable"
    else:
        student_grades[key] = "Fail"

print(student_grades)
