from turtle import Turtle

MOVE_DISTANCE = 20
UP = 90
LEFT = 180
DOWN = 270
RIGHT = 0
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]


class Ekans:
    def __init__(self):
        self.segs = []
        self.color1 = "white"
        self.color2 = "white"
        self.create_ekans()
        self.head = self.segs[0]

    def create_ekans(self):
        for position in STARTING_POSITIONS:
            self.add_seg(position)

    def add_seg(self, position):

        new_seg = Turtle("square")
        new_seg.penup()
        new_seg.speed("slow")
        if len(self.segs) > 3:
            if self.segs[-1].color()[0] == self.color1:
                new_seg.color(self.color2)
            else:
                new_seg.color(self.color1)
        else:
            new_seg.color(self.color1)
        new_seg.setpos(position)
        self.segs.append(new_seg)

    def reset(self):
        for seg in self.segs:
            seg.goto(1000, 1000)
        self.segs.clear()  # removes all items from list
        self.create_ekans()
        self.head = self.segs[0]

    def extend(self):
        self.add_seg(self.segs[-1].pos())

    def move(self):
        for seg in range(len(self.segs) - 1, -1, -1):
            if seg != 0:
                self.segs[seg].goto(self.segs[seg - 1].pos())
            else:
                self.segs[seg].fd(MOVE_DISTANCE)
            pass

    def up(self):
        check_x = abs(self.head.xcor() - self.segs[2].xcor())
        if check_x >= 20:
            head_heading = self.head.heading()
            if head_heading == RIGHT or head_heading == LEFT:
                self.head.setheading(UP)

    def left(self):
        check_y = abs(self.head.ycor() - self.segs[2].ycor())
        if check_y >= 20:
            head_heading = self.head.heading()
            if head_heading == UP or head_heading == DOWN:
                self.head.setheading(LEFT)

    def down(self):
        check_x = abs(self.head.xcor() - self.segs[2].xcor())
        if check_x >= 20:
            head_heading = self.head.heading()
            if head_heading == RIGHT or head_heading == LEFT:
                self.head.setheading(DOWN)

    def right(self):
        check_y = abs(self.head.ycor() - self.segs[2].ycor())
        if check_y >= 20:
            head_heading = self.head.heading()
            if head_heading == UP or head_heading == DOWN:
                self.head.setheading(RIGHT)

    def head_bounds(self):
        head_heading = self.head.heading()
        head_bounds = []
        if head_heading == 0 or head_heading == 180:
            for i in range(-10, 15, 5):
                head_bounds.append(
                    (
                        round(self.head.xcor()),
                        round(self.head.ycor() + i),
                    )
                )
        else:
            for i in range(-10, 15, 5):
                head_bounds.append(
                    (
                        round(self.head.xcor() + i),
                        round(self.head.ycor()),
                    )
                )

        return head_bounds

    def out_of_bounds(self):
        xpos = self.head.xcor()
        ypos = self.head.ycor()
        if xpos > 280 or ypos > 280 or xpos < -280 or ypos < -280:
            return True
        else:
            return False

    def tail_collision(self):
        for i, seg in enumerate(self.segs[1:], start=1):
            if self.head.distance(seg) < 10:
                self.segs[i].color("#fc9272")
                return True
        return False

    def color_change(self, color1, color2):
        self.color1 = color1
        self.color2 = color2
        for i in range(0, len(self.segs)):
            if i % 2 == 0:
                self.segs[i].color(color2)
            else:
                self.segs[i].color(color1)
