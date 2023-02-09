from turtle import Turtle
from random import randrange


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.create_food()
        self.new_location()

    def create_food(self):
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("#1c9099")
        self.speed("fastest")

    def new_location(self):
        new_x = randrange(-260, 260, 20)
        new_y = randrange(-260, 260, 20)
        new_pos = (new_x, new_y)
        self.goto(new_pos)
