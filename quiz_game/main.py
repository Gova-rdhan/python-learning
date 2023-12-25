from question_model import Question
from data import question_data
from quiz_brain import QuizBrain


qb = []
for i in question_data:
    question = i['text']
    answer = i['answer']
    q_obj = Question(question,answer)
    qb.append(q_obj)
quiz = QuizBrain(qb)
while quiz.still_has_questions():
    quiz.next_question()
print("you are completed the quiz")
print(f"your total score is {quiz.count}/{quiz.question_number}")