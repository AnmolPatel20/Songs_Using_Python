import turtle as t

# Setup
t.bgcolor("black")
t.speed(0)
t.pensize(2)

# Draw the rose (spiral petals)
t.color("red")
t.begin_fill()
for i in range(36):
    t.circle(120 - i*3, 90)  
    t.left(90)
    t.circle(120 - i*3, 90)
    t.left(10)
t.end_fill()

# Move to draw stem
t.right(90)
t.color("green")
t.pensize(10)
t.forward(300)  # stem

# Draw left leaf
t.pensize(2)
t.begin_fill()
t.left(45)
t.forward(100)
t.circle(50, 90)
t.left(90)
t.circle(50, 90)
t.forward(100)
t.left(135)
t.end_fill()

# Draw right leaf
t.begin_fill()
t.right(45)
t.forward(100)
t.circle(50, 90)
t.left(90)
t.circle(50, 90)
t.forward(100)
t.left(135)
t.end_fill()

t.hideturtle()
t.done()
