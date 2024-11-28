
from turtle import Turtle


class ScoreBoard (Turtle):
    
    def __init__(self):
        super().__init__()
        self.score = 0 
        with open("C:/Users/FANARA/OneDrive - Pfizer/Desktop/Python/Intermediate/Day20/data.txt") as data:
            self.high_score = int(data.read())
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 280)
        self.update_scoreboard()
     
    
    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score}  High Score: {self.high_score}", align = "center", font= ("Arial", 14, "bold"))
        
           
    def get_score(self):
        self.score += 10 
        self.update_scoreboard()
        
        
    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open ("data.txt", mode="w") as data:
                data.write(f"{self.high_score}")
        self.score = 0
        self.update_scoreboard()
    
    
    
        
        

        
        