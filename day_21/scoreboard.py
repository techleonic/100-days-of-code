from turtle import  Turtle

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0,250)
        self.print_score()
    def update_score(self):
        self.score +=1
        self.clear()
        self.print_score()
    def print_score(self):
        self.write(f"Score: {self.score}", False, align="center", font=('Arial', 15, 'normal'))