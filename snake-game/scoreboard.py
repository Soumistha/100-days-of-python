import turtle as t


class Score(t.Turtle):
    def __init__(self):
        super().__init__()
        with open("score.txt",mode="r") as f:
            self.high_score = int(f.read())
        self.sc = 0
        self.clear()
        self.penup()
        self.hideturtle()
        self.goto(0, 270)
        self.write(f"Score: {self.sc} High Score: {self.high_score}", align="center", font=("Arial", 24, "normal"))
    
    def update_score(self):
        self.clear()
        self.write(f"Score: {self.sc} High Score: {self.high_score}", align="center", font=("Arial", 24, "normal"))
       

    def increase_score(self):
        self.sc += 1
        self.update_score()
        
    def reset(self):
        if self.sc > self.high_score:
            self.high_score = self.sc
            with open("score.txt",mode="w") as f:
                f.write(f"{self.high_score}")
        self.sc = 0
        self.update_score()
        
        