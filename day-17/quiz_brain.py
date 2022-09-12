class quizBrain:
    def __init__(self, questionList):
        self.questionnumber= 0
        self.score =0
        self.questionlist = questionList

    def still_has_question(self):
        return self.questionnumber < len(self.questionlist)

    def nextQuestion(self):
        currentQuestion = self.questionlist[self.questionnumber]
        self.questionnumber+=1
        if input(f"{currentQuestion.text} (True/False)") == currentQuestion.answer.lower():
            print("ok")
            self.score+=1
        else:
            print("wrong")
        print(f"Your score: {self.score}")
