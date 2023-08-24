#!/usr/bin/python3
# day 17 for 100 days of Python - creating adn using classes
import data
import question_model
from quiz_brain import QuizBrain

question_bank = []
score = 0

for qtn in data.question_data:
    question_bank.append(question_model.Question(qtn['text'], qtn['answer']))
print("Quiz Game")

quiz = QuizBrain(question_bank)
while quiz.still_has_questions():
    answer = quiz.next_question()

print(f"You total score is {quiz.score}")
