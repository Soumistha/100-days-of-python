import time
import turtle as t
import random

starting_position = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20


class Snake:
    def __init__(self):
        self.seg = []
        self.create_snake()
        self.head = self.seg[0]
        
    def create_snake(self):
        for pos in starting_position:
            segment = t.Turtle("square")
            segment.color("green")
            segment.penup()
            segment.goto(pos)
            self.seg.append(segment)

#moves the last segment to the position of the second last segment,
#then moves the second last segment to the position of the third last segment 

    def move(self):
        for seg_num in range(len(self.seg)-1, 0, -1):
            new_x = self.seg[seg_num-1].xcor()#gets the x coordinate of the previous segment
            new_y = self.seg[seg_num-1].ycor()#gets the y coordinate of the previous segment
            self.seg[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)
        
    def up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270) 

    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180) 

    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)

    def add_segment(self,position):
        new_segment = t.Turtle("square")
        new_segment.color("green")
        new_segment.penup()
        new_segment.goto(position)
        self.seg.append(new_segment)
    
    def reset(self):
        for seg in self.seg:
            seg.goto(1000, 1000)
        self.seg.clear()
        self.create_snake()
        self.head = self.seg[0]
    
    def extend(self):
        self.add_segment(self.seg[-1].position())
