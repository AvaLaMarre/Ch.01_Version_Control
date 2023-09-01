'''
1.0 Jedi Training (17pts)  Name:__Ava______________


1. Define Forking (1pt): 

2. Define Cloning (1pt): 

3. Define Branching (1pt):

4. Define Committing (1pt): 

5. Define Merging (1pt): 

6. Define Pushing (1pt):

7. Define Pull Request (1pt):


8. TURTORIAL ART (10pts.)

Modify the starter code below to create your own cool drawing. 
Make sure you keep the last two lines of code!!!! 
Your first and last name must be written on your art.
The last line keeps the window open until you click to close.
Turtle Documentation: https://docs.python.org/3.3/library/turtle.html?highlight=turtle
'''
import turtle

tina = turtle.Turtle()
tommy = turtle.Turtle()

tina.color('blue')
tommy.color('green')

tina.shape('turtle')
tommy.shape('turtle')

tommy.speed(0)
tina.speed(0)
tommy.penup()
def petal():
    tina.pendown()
    tina.begin_fill()
    tina.left(45)
    tina.forward(40)
    tina.right(70)
    tina.forward(70)
    tina.right(130)
    tina.forward(70)
    tina.right(70)
    tina.forward(40)
    tina.end_fill()
    tina.penup()

def petalt():
    tommy.pendown()
    tommy.begin_fill()
    tommy.left(45)
    tommy.forward(40)
    tommy.right(70)
    tommy.forward(70)
    tommy.right(130)
    tommy.forward(70)
    tommy.right(70)
    tommy.forward(40)
    tommy.end_fill()
    tommy.penup()

tina.color("light blue")
tina.begin_fill()
tina.goto(200, 200)
tina.goto(200, -200)
tina.goto(-200, -200)
tina.goto(-200, 200)
tina.goto(200, 200)
tina.end_fill()
tina.penup()

tina.color('green')
tina.goto(5, -210)
tina.pendown()
tina.begin_fill()
tina.goto(5, 0)
tina.goto(-5, 0)
tina.goto(-5, -210)
tina.end_fill()
tina.penup()

tina.color("orange")
tina.goto(0, -40)
tina.pendown()
tina.begin_fill()
tina.circle(70)
tina.end_fill()
tina.penup()

tina.color("brown")
tina.goto(0, -25)
tina.pendown()
tina.begin_fill()
tina.circle(50)
tina.end_fill()
tina.penup()

tommy.goto(-15, 70)

tommy.pendown()
tommy.left(120)
tommy.color("light yellow")
petalt()

tommy.goto(25, 70)
tommy.left(170)
petalt()

tommy.goto(25, -20)
tommy.left(100)
petalt()

tommy.goto(-20, -20)
tommy.right(190)
petalt()

tommy.goto(50, 40)
petalt()

tommy.goto(-45, 40)
petalt()

tommy.goto(-45, 10)
tommy.right(80)
petalt()

tommy.goto(50, 10)
tommy.right(10)
petalt()

tina.goto(0, 75)
tina.left(90)
tina.color('yellow')
petal()

tina.goto(0, -25)
tina.left(45)
petal()

tina.goto(50, 25)
tina.right(45)
petal()

tina.goto(-50, 25)
tina.left(45)
petal()

tina.goto(-35, 60)
tina.right(185)
petal()

tina.goto(-35, -10)
tina.right(40)
petal()

tina.goto(40, -10)
tina.right(45)
petal()

tina.goto(40, 60)
tina.right(40)
petal()

tommy.color('green')
tommy.goto(0, -150)
tommy.pendown()
tommy.right(100)
petalt()
tommy.penup()

tommy.goto(2000, 2000)
tina.goto(150, -180)
tina.color("blue")

tina.write('Ava', font=("Arial", 16, "normal")) # signs your name to your art
tina.goto(400,400)
turtle.exitonclick() #Keeps pycharm window open so we can see the drawing