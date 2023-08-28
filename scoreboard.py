from turtle import Turtle

ALIGN = "center"
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto((-220, 260))
        self.level = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Level: {self.level}", align=ALIGN, font=FONT)

    def update_level(self):
        self.clear()
        self.level += 1
        self.update_scoreboard()
