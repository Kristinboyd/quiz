# Classes
from question_model import Question
from quiz_brain import QuizBrain
# Data
from data import question_data

# create a bank to hold the data
question_bank = []

# iterate through question data and append new questions into the question bank
for question in question_data:
    question_text = question["text"]
    question_answer = question["answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print(f"You have completed the quiz!")
print(f"Your total score is {quiz.score} out of {quiz.question_number}")