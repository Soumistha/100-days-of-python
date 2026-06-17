import turtle as t
import random
bella = t.Turtle()
screen = t.Screen()
print(bella)
bella.shape("turtle") #changes the shape from arrow to turtle
t.colormode(255)

bella.color("red","yellow")#gives red border and yellow body colour
#bella the turtle is already facing right
#bella.forward(100)#moved a 100 spaces from where it is and towards where its facing
'''
col = ["DarkOrchid","CornflowerBlue","IndianRed","Wheat","SlateGray"]
dire = [0,90,180,270,60,135]
#bella.left(90)#turns the turtle left by 90 deg
#bella.forward(100)
#bella.left(90)
#bella.forward(100)
#bella.left(90)
#bella.forward(100)
#this makes a square
"""
for i in range(0,15):
    bella.forward(10)
    bella.up()
    bella.forward(10)
    bella.down()
"""

print(screen.canvheight) # gives screen height
"""
screen.exitonclick() #instead of the screen going as soon as the code finishes running 
                     #it will exit from the screen when we click the screen
"""

#bella.pensize(10)
bella.speed("fastest")


for i in range(100):
    #bella.color(random.choice(col))
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    col = (r,g,b)
    bella.pencolor(col)
    bella.forward(20)
    bella.setheading(random.randint(0,365))    #setheading will randomly call left or right

h = bella.heading()#gives the heading of the turtle
#bella.circle(100)
#bella.setheading(h+10)
#bella.circle(100)

for i in range (int(360/5)):
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    col = (r,g,b)
    bella.pencolor(col)
    bella.circle(100)
    h+=5
    bella.setheading(h)
    bella.circle(100)
'''
def move():
    bella.forward(10)

def backy():
    bella.backward(10)

def lefty():
    bella.left(90)

def righty():
    bella.right(90)

def cleary():
    bella.home()
    bella.clear()
    

screen.listen()#makes the screen listen to u or will wait for keyboard input programed by u to do some work
#screen.onkey(key ="space",fun = righty)#this will run the function move whenever the space bar is hit

screen.onkey(key ="w",fun = move)
screen.onkey(key ="s",fun = backy)
screen.onkey(key ="a",fun = lefty)
screen.onkey(key ="d",fun = righty)
screen.onkey(key ="c",fun = cleary)



screen.exitonclick()