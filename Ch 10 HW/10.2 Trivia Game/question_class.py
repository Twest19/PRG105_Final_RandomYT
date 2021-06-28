

class Question:

    def __init__(self, question, ans1, ans2, ans3, ans4, answer):
        self.question = question
        self.ans1 = ans1
        self.ans2 = ans2
        self.ans3 = ans3
        self.ans4 = ans4
        self.answer = answer

    def set_question(self, question):
        self.question = question

    def set_ans1(self, ans1):
        self.ans1 = ans1

    def set_ans2(self, ans2):
        self.ans2 = ans2

    def set_ans3(self, ans3):
        self.ans3 = ans3

    def set_ans4(self, ans4):
        self.ans4 = ans4

    def set_answer(self, answer):
        self.answer = answer

    def get_question(self):
        return self.question

    def get_ans1(self):
        return self.ans1

    def get_ans2(self):
        return self.ans2

    def get_ans3(self):
        return self.ans3

    def get_ans4(self):
        return self.ans4

    def get_answer(self):
        return self.answer
