import turtle

screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Centered Sun Shape")

sun = turtle.Turtle()
sun.speed(10)
sun.color("yellow")
sun.speed(5)

sun.penup()
sun.goto(0,-100)
sun.pendown()
sun.begin_fill()
sun.circle(100)
sun.end_fill()

for i in range(36):
    sun.penup()
    sun.goto(0,0)
    sun.setheading(i*10)
    sun.forward(100)
    sun.pendown()
    sun.forward(50)
    sun.penup()

sun.hideturtle()
turtle.done()