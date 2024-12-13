from turtle import Turtle
import random
class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("red")
        self.penup()
        self.shapesize(stretch_wid = 0.5, stretch_len = 0.5)
        self.display()
    def display(self):
        x_position = random.randint(-220,220)
        y_position = random.randint(-220,220)
        self.goto(x_position, y_position)
