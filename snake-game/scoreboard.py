import turtle as t

class Score(t.Turtle):
    def __init__(self):
        super().__init__()
        self.sc =0
        self.clear()
        self.penup()
        self.hideturtle()
        self.goto(0, 270)
        self.write(f"Score: {self.sc}", align="center", font=("Arial", 24, "normal"))
        #self.write(f"Score: {self.sc}", align="center", font=("Arial", 24, "normal"))
    
    def increase_score(self):
        self.sc += 1
        self.clear()

        self.write(f"Score: {self.sc}", align="center", font=("Arial", 24, "normal"))
        
        
        
        
        