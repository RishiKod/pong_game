from turtle import Turtle


class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.color('white')
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update_score()

    def update_score(self):
        self.goto(x=-100, y=200)
        self.write(self.l_score, align='center', font=('Courier', 40, 'normal'))
        self.goto(x=100, y=200)
        self.write(self.r_score, align='center', font=('Courier', 40, 'normal'))

    def l_score_count(self):
        self.clear()
        self.l_score += 1
        self.update_score()

    def r_score_count(self):
        self.clear()
        self.r_score += 1
        self.update_score()

    def game_finished(self):
        self.color('white')
        self.penup()
        self.hideturtle()
        self.goto(0, 0)
        self.write("Game finished", False, align='center', font=('Courier', 30, 'normal'))
