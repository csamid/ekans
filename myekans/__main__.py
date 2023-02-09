# Main Ekans
from turtle import Screen
from myekans.ekans import Ekans
from myekans.food import Food
from myekans.score import Scoreboard
import time


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("#000000")
screen.title("Ekans")
screen.tracer(0)  # turn tracer off

# create scoreboard
scoreboard = Scoreboard()

# create ekans starting body
ekans = Ekans()

# create food
food = Food()
screen.listen()
screen.onkey(ekans.up, "w")
screen.onkey(ekans.left, "a")
screen.onkey(ekans.down, "s")
screen.onkey(ekans.right, "d")

# stops while loop before destroying window
def on_quit():
    global game_is_on
    game_is_on = False
    screen._root.after(100, screen._root.destroy)


screen._root.protocol("WM_DELETE_WINDOW", on_quit)
game_is_on = True


def main():
    while game_is_on:
        screen.update()
        time.sleep(0.1)
        ekans.move()

        # Color change with high score
        if scoreboard.current_score == 10:
            ekans.color_change(ekans.color1, "#756bb1")
        elif scoreboard.current_score == 20:
            ekans.color_change(ekans.color2, ekans.color2)
        elif scoreboard.current_score == 30:
            ekans.color_change(ekans.color1, "#3182bd")
        elif scoreboard.current_score == 40:
            ekans.color_change(ekans.color2, ekans.color2)
        elif scoreboard.current_score == 50:
            ekans.color_change(ekans.color1, "#9ecae1")

        # Dectect collision w/ food
        if food.pos() in ekans.head_bounds():
            scoreboard.increase_score()

            # new food location and extend snake
            food.new_location()
            ekans.extend()

        # Detect collision with wall
        if ekans.out_of_bounds():
            ekans.head.color("#fc9272")
            screen.update()
            scoreboard.reset()
            time.sleep(1)
            ekans.reset()
            ekans.color_change("white", "white")

        # Detect collision w/ tail
        if ekans.tail_collision():
            screen.update()
            scoreboard.reset()
            time.sleep(1)
            ekans.reset()
            ekans.color_change("white", "white")


if __name__ == "__main__":
    main()
