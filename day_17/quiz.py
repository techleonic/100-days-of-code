import random
from data import question_data
from question_model import Question

question_a = question_data[random.randint(0, len(question_data))]
select_question = Question(question_a["text"], question_a["answer"])
print(select_question.text)
user_answer = input("Write your answer 'Ture' or 'False' ")
if user_answer == select_question.answer:
    print("Correct Answer")
else:
    print("Incorrect Answer")
