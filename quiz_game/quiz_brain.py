class QuizBrain:

    def __init__(self,question_list):
        self.question_number = 0
        self.question_list = question_list
        self.count = 0

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        n = input(f"Q.{self.question_number} {current_question.text} (True or False) ")
        self.check_answer(n,current_question.answer)

    def check_answer(self,n,correct_answer):
        if n == correct_answer:
            self.count+=1
            print(f"you are right your score is {self.count}/{self.question_number}")
        else:
            print(f"you are wrong your score is {self.count}/{self.question_number}")




