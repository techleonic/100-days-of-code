class QuizBrain:  # this is a class that will have all the questions and answers

    def __init__(self, qz_question_list):  # store the questions and answers
        self.question_number = 0
        self.score = 0
        self.question_list = qz_question_list

    def next_question(self):
        """this function prints out the question and ask for the user answer"""
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"{self.question_number}: {current_question.text} (True/False): ")
        self.check_answer(user_answer, current_question.answer)

    @property
    def still_have_questions(self):
        """checks if we have any questions left"""
        return self.question_number < len(self.question_list)

    def check_answer(self, user_answer, current_answer):
        if user_answer.lower() == current_answer.lower():
            print("you got it right")
            self.score +=1
        else:
            print("you got it wrong")
        print(f"The correct answer is {current_answer}")
        print(f"Your current score is {self.score}/{self.question_number}")
