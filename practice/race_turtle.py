import turtle as t
import random



screen = t.Screen()

screen.setup(width =500,height= 500) # to control the size of the screen

bet = screen.textinput(title = "make ur bet:",prompt = "enter the colour")
print("you bet "+bet)

'''
bella = t.Turtle()
james = t.Turtle()
thomas = t.Turtle()
elsa = t.Turtle()
anna = t.Turtle()

bella.shape("turtle")
james.shape("turtle")
thomas.shape("turtle")
elsa.shape("turtle")
anna.shape("turtle")
#changes the shape from arrow to turtle
t.colormode(255)

james.color("yellow")
thomas.color("red")
elsa.color("blue")
anna.color("green")
bella.color("violet")

bella.penup()
james.penup()
thomas.penup()
elsa.penup()
anna.penup()

bella.goto(x =-230,y = -200)
james.goto(x =-230,y = -100)
thomas.goto(x =-230,y = 0)
elsa.goto(x =-230,y = 100)
anna.goto(x =-230,y = 200)
'''
all_t = []

y = [ -200,-100,0,100,200]
c = ["pink","red","blue","green","yellow"]

for ti in range(5):
    bella = t.Turtle()
    bella.shape("turtle")
    bella.color(c[ti])
    bella.penup()
    bella.goto(x =-230,y = y[ti])
    all_t.append(bella)

if bet:
    race = True

while race:
    
    for i in all_t:
        if i.xcor()>230:
            col = i.pencolor()
            if col == bet:
                print("u won!!!!!!")
            else:
                race = False
                print("u lost :(")
                print(i.pencolor()+" won")
            
        dis = random.randint(0,10)
        i.forward(dis)

screen.exitonclick()