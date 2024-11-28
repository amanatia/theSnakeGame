from turtle import Turtle

POSITIONS = [(0,0), (-20, 0), (-40,0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    
    def __init__(self):
        self.turtles = []
        self.create_snake() #I initialize the create_snake method here so that I do not need to call the create_snake methon in main.py.
        self.head = self.turtles[0]
        
    def create_snake(self):
        for position in POSITIONS:
            self.add_turtle(position)
        
    
    def add_turtle(self, position):
            new_turtle = Turtle(shape= "square")
            new_turtle.color("DeepPink")
            new_turtle.penup()
            new_turtle.goto(position)
            self.turtles.append(new_turtle)
            
    # reset does everything the init does because we are initiallizing the snake again         
    def reset(self):
        for turtle in self.turtles:
            turtle.goto(1000, 1000)
        self.turtles.clear()
        self.create_snake()
        self.head = self.turtles[0]
            
    def extend(self):
        self.add_turtle(self.turtles[-1].position()) #we are getting hold of the position of the last turtle
        
    
    def move(self):
        # When the snake turns all the turtles should follow not just one 
        for index in range( len(self.turtles) - 1 ,  0,  -1):    # (start = ... , stop = ... , step = ... )
            #The last turtle goes to the position of the second to last turtle 
            new_x = self.turtles[index -1].xcor()
            new_y = self.turtles[index -1].ycor()
            self.turtles[index].goto(new_x, new_y)
        #Get a hold of the first turtle
        self.head.forward(MOVE_DISTANCE)        
        
        
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
        
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
        
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
        
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
         