from turtle import  Turtle

ALIGNMENT = "center"
FONT = ('Arial', 15, 'normal')


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

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", False, align=ALIGNMENT, font=FONT)


    def print_score(self):
        self.write(f"Score: {self.score}", False, align=ALIGNMENT, font=FONT)
