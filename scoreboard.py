from turtle import Turtle
class Score_board(Turtle):
    def __init__ (self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(0,250)
        self.display()
    def display(self):
        self.write(f"Score: {self.score}", font = ["Arial", 25, "normal"],align = "center")
    def update_score(self):
        self.score += 1
        self.clear()
        self.display()
    def game_over (self):
        self.screen.bgcolor("dark red")
        self.goto(0,0)
        self.write(f"Game over\nFinal score: {self.score}", font = ["Arial", 25, "normal"], align = "center")