
def draw_circle(x,y,color,rad):
    
    t.goto(x,y)
    t.begin_fill()
    t.fillcolor(color)
    t.circle(rad)
    t.end_fill()
    
    t.home()


import turtle
t=turtle.Turtle()
window=turtle.Screen()
window.title('CIRCLES')
window.screensize(50)
t.pensize(5)
t.pencolor('white')
t.up()

draw_circle(0,-50,'red',50)
draw_circle(200,200,'blue',50)
draw_circle(-200,200,'green',50)
draw_circle(-200,-200,'orange',-50)
draw_circle(200,-200,'yellow',-50)    
window.exitonclick()