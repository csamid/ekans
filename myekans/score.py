from turtle import Turtle
import os

file_path = f"{os.path.dirname(__file__)}\score.txt"

FONT = ("Moonhouse", 20, "bold")
ALIGNMENT = "center"


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.current_score = 0
        self.high_score = self.read_data()
        self.hideturtle()
        self.goto(0, 260)
        self.color("white")
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score = {self.current_score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.current_score > self.high_score:
            self.high_score = self.current_score
        self.current_score = 0
        self.update_scoreboard()
        self.write_data()

    def increase_score(self):
        self.current_score += 1
        self.update_scoreboard()

    def read_data(self):
        with open(file_path, mode="r") as file:
            return int(file.read())

    def write_data(self):
        with open(file_path, mode="w") as file:
            file.write(f"{self.high_score}")
