import turtle
import time

rose = turtle.Turtle()
rose.hideturtle()

# Set initial position
rose.penup()
rose.left(90)
rose.fd(200)
rose.right(90)

# Flower base
rose.fillcolor("red")
rose.begin_fill()
rose.circle(10, 180)
rose.circle(25, 110)
rose.left(50)
rose.circle(60, 45)
rose.circle(20, 170)
rose.right(24)
rose.fd(30)
rose.left(10)
rose.circle(30, 110)
rose.fd(20)
rose.left(40)
rose.circle(90, 70)
rose.circle(30, 150)
rose.right(30)
rose.fd(15)
rose.circle(80, 90)
rose.left(15)
rose.fd(45)
rose.right(165)
rose.fd(20)
rose.left(155)
rose.circle(150, 80)
rose.left(50)
rose.circle(150, 90)
rose.end_fill()

# Petal 1
rose.left(150)
rose.circle(-90, 70)
rose.left(20)
rose.circle(75, 105)
rose.setheading(60)
rose.circle(80, 98)
rose.circle(-90, 40)

# Petal 2
rose.left(180)
rose.circle(90, 40)
rose.circle(-80, 98)
rose.setheading(-83)

# Leaves 1
rose.fd(30)
rose.left(90)
rose.fd(25)
rose.left(45)
rose.fillcolor("green")
rose.begin_fill()
rose.circle(-80, 90)
rose.right(90)
rose.circle(-80, 90)
rose.end_fill()
rose.right(135)
rose.fd(60)
rose.left(180)
rose.fd(85)
rose.left(90)
rose.fd(80)

# Leaves 2
rose.right(90)
rose.right(45)
rose.fillcolor("green")
rose.begin_fill()
rose.circle(80, 90)
rose.left(90)
rose.circle(80, 90)
rose.end_fill()
rose.left(135)
rose.fd(60)
rose.left(180)
rose.fd(60)
rose.right(90)
rose.circle(200, 60)

def curve():
    turtle.speed(0)
    for t in range (45):
        turtle.right(5)
        turtle.forward(1)

def hearts (x, y):
    turtle.speed(100000)
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.pensize(1)
    turtle.color("red")
    turtle.begin_fill()
    turtle.left(140)
    turtle.forward(25)
    curve()

    turtle.left(160)
    curve()
    turtle.forward(25)
    turtle.end_fill()
    turtle.hideturtle()
    turtle.left(150)

text = turtle.Turtle()

def write(message, pos, color):
    x, y = pos
    text.hideturtle()
    text.color(color)
    text.penup()
    text.goto(x, y)
    text.pendown()
    style = ("Arial", 40, "italic")
    text.write(message,font=style)

write("Happy", (-185, -230), "red")
time.sleep(1)
write("Valentine", (-230, 290), "red")
time.sleep(1)
write("Day!", (-180, -340), "red")

turtle.onscreenclick(hearts, 1)

turtle.mainloop()