import turtle
t=turtle.Turtle()
w=turtle.Screen()
w.title('FLAG')
t.up()
t.goto(0,-200)

t.pensize(2)
t.left(90)
t.down()
t.forward(400)
t.right(90)

t.begin_fill()
t.fillcolor('dark orange')
t.forward(150)
t.right(90)

t.forward(35)
t.right(90)
t.forward(150)
t.end_fill()

t.left(90)
t.up()
t.forward(35)
t.left(90)
t.down()

t.forward(150)

t.left(90)
t.forward(35)
t.up()
t.left(180)
t.forward(35)


t.down()
t.begin_fill()
t.fillcolor("green")
t.forward(35)
t.right(90)
t.forward(150)
t.right(90)
t.forward(35)
t.end_fill()

t.up()
t.forward(35)
t.down()
t.forward(35)

t.right(180)
t.up()
t.forward(35)
t.left(90)
t.forward(75)
t.down()
t.begin_fill()
t.fillcolor('blue')
t.circle(-17.5)
t.end_fill()

t.right(90)
t.forward(35)
t.left(180)

t.up()
t.forward(17.5)
t.right(90)
t.down()
t.forward(17.5)

t.right(180)
t.up()
t.forward(17.5)
t.right(45)
t.down()
t.forward(17.5)

t.right(180)
t.up()
t.forward(17.5)
t.down()
t.forward(17.5)

t.right(180)
t.up()
t.forward(17.5)

t.left(90)
t.down()
t.forward(17.5)

t.left(180)
t.up()
t.forward(17.5)
t.down()
t.forward(17.5)

t.left(180)
t.up()
t.forward(17.5)

t.right(45)
t.down()
t.forward(17.5)

t.up()
t.home()

t.right(90)
t.forward(200)
t.begin_fill()
t.fillcolor('brown')
t.down()
t.left(90)
t.forward(100)
t.right(90)
t.forward(30)
t.left(90)
t.forward(100)
t.right(90)
t.forward(30)
t.left(90)
t.forward(100)
t.right(90)
t.forward(30)
t.right(90)
t.forward(600)
t.right(90)
t.forward(30)
t.right(90)
t.forward(100)
t.left(90)
t.forward(30)
t.right(90)
t.forward(100)
t.left(90)
t.forward(30)
t.right(90)
t.forward(100)
t.end_fill()

t.right(180)
t.up()
t.forward(10)
t.begin_fill()
t.fillcolor('dark red')
t.down()
t.right(90)
t.forward(400)
t.right(90)
t.forward(10)
t.right(90)
t.forward(400)
t.end_fill()
t.hideturtle()
w.exitonclick()