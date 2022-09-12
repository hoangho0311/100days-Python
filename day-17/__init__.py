# class User:
#     def __init__(self, id, name):
#         self.id = id
#         self.name = name
#     def replayName(self):
#         self.name = "Long"
#
# user = User(1, "Hoang")
# user.replayName()
# print(user.name)

import random

from question_model import Question
from data import question_data
from  quiz_brain import quizBrain
question_bank=[]
for question in question_data:
    mylist = random.choice(question_data)
    question_text= mylist['question']
    question_answer = mylist['correct_answer']
    question_bank.append(Question(question_text, question_answer))

quiz = quizBrain(question_bank)
while quiz.still_has_question():
    quiz.nextQuestion()