from Quiz_brain import QuizBrain # function to manipulate the list of questions
from data import question_data # dict in a list (data source)
from question_model import Question # type of data question proprieties (text & answer)

# list of objects type Question
question_bank = []
for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)


while quiz.still_have_questions:
    quiz.next_question()

print("You've completed the quiz")
print(f"Your final score is {quiz.score}/{quiz.question_number}")


"""question_a = question_data[random.randint(0, len(question_data))]
select_question = Question(question_a["text"], question_a["answer"])
print(select_question.text)
user_answer = input("Write your answer 'Ture' or 'False' ")
if user_answer == select_question.answer:
    print("Correct Answer")
else:
    print("Incorrect Answer")"""
