from turtle import *
w=Screen()
t=Turtle()
colors=['red','blue','green','yellow','purple','orange']
import random
t.speed(0)
t.up()
t.goto(-200,0)
t.width(5)                          # change pen thickness
t.down()
t.hideturtle()
for i in range(9001):
    colorchoice=random.choice(colors)
    t.color(colorchoice)
    t.forward(400)
    t.right(500)
    