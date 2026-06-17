import turtle
import random
#import colorgram # used to extract colours from a pic

bella = turtle.Turtle()

turtle.colormode(255)

bella.penup()#to not show the lines
bella.hideturtle()#to hide the turle shape
bella.speed("fastest")

bella.setheading(225)#to get the turtle in the correct position
bella.forward(330)
bella.setheading(0)


for i in range(1,101):
    r = random.randint(0,200)
    g = random.randint(0,200)
    b = random.randint(0,200)
    col = (r,g,b)
    bella.dot(20,col)#20 is the size
    bella.forward(50)
    
    if i%10 == 0:
        bella.setheading(90)
        bella.forward(50)
        bella.setheading(180)
        bella.forward(500)
        bella.setheading(0)
    
        

screen = turtle.Screen()
screen.exitonclick()