#class snake
from turtle import Turtle
class Snake:
    def __init__ (self):
        self.turtles = []
        self.position = [(-40,0),(-20,0),(0,0)]
        self.creat_snake()
        self.head = self.turtles[-1]
# creat snake
    def creat_snake(self):
        for x in range (len(self.position)):
            new_turtle = Turtle("square")
            new_turtle.color("white")
            new_turtle.penup()
            new_turtle.goto(self.position[x])
            self.turtles.append(new_turtle)

# extend snake
    def extend (self):
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        self.turtles.insert(0,new_segment)

    
# move snake
    def move (self):
        for x in range (len(self.turtles)-1):
            self.turtles[x].goto(self.turtles[x+1].pos())
        self.head.forward(20)

        
#up
    def up (self):
        self.head.setheading(90)
#down
    def down (self):
        self.head.setheading(270)
#right  
    def right (self):
        self.head.setheading(0)
#left
    def left (self):
        self.head.setheading(180)