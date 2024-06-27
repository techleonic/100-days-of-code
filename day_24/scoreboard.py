from turtle import  Turtle

ALIGNMENT = "center"
FONT = ('Arial', 15, 'normal')


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0,250)
        self.print_score()
    def update_score(self):
        self.clear()
        self.print_score()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
        self.score = 0
        self.update_score()
    # def game_over(self):
    #     self.goto(0,0)
    #     self.write("GAME OVER", False, align=ALIGNMENT, font=FONT)


    def print_score(self):
        self.write(f"Score: {self.score} High score: {self.high_score}", False, align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score +=1
        self.update_score()