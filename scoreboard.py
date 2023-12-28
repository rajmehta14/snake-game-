from turtle import Turtle

ALLIGNMENT="center"
FONT=("Arial",24,"normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        with open("data.txt") as data:
           self.highest_score= int(data.read())
        self.penup()
        self.color("white")
        self.goto(0,270)
        self.write(f"Score:{self.score}",align=ALLIGNMENT,font=FONT)
        self.hideturtle()

    def update_scoreboard(self):
        self.clear()
        self.write(f"score : {self.score} High Score : {self.highest_score}" , align=ALLIGNMENT, font=FONT)


    def reset(self):
        if self.score>self.highest_score:
            self.highest_score=self.score
            with open("data.txt" , mode="w") as data:
                data.write(f"{self.highest_score}")
        self.score=0
        self.update_scoreboard()




    def increase_score(self):
        self.score+=1

        self.update_scoreboard()

