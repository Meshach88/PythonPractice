from turtle import *
from random import *

def moveToRandomLocation():
    penup()
    setpos(randint(-300,300),randint(-300,300))
    

def drawStar(starsize,starcolor):  #parameters or input
    color(starcolor)
    pendown()
    begin_fill()
    
    for side in range(5):
        left(144)
        forward(starsize)
    
    end_fill()
    penup()
    
bgcolor('midnight blue')
speed(10)

for star in range(30):
    moveToRandomLocation()
    drawStar(50,'white')

hideturtle()
done()

#Assignment: Draw 30 stars of different sizes. Use a loop to draw the stars

