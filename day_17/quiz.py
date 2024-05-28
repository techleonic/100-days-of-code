from Quiz_brain import QuizBrain
from data import question_data
from question_model import Question

# list of objects type Question
question_bank = []
for question in question_data:
    question_text = question["text"]
    question_answer = question["answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)


while quiz.still_have_questions:
    quiz.next_question()


"""question_a = question_data[random.randint(0, len(question_data))]
select_question = Question(question_a["text"], question_a["answer"])
print(select_question.text)
user_answer = input("Write your answer 'Ture' or 'False' ")
if user_answer == select_question.answer:
    print("Correct Answer")
else:
    print("Incorrect Answer")"""
