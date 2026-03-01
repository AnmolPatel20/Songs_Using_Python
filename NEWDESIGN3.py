import turtle 
screen= turtle.Screen()
screen.setup(width = 800 , height = 800)
screen.bgcolor("#111111")

t = turtle.Turtle()
t.speed(0)
t.hideturtle()
t.width(1.5)

colors = ["#00C3FF", "#004CFF", "#FF00FB","#00BBFF", "#2200FF","#E22BD3"]
side_length = 5
num_hexagons = 120

for i in range(num_hexagons):
    t.pencolor(colors[i%len(colors)])

    for _ in range(6):
        t.forward(side_length)
        t.right(60)
    t.right(8)

    side_length += 4
screen.exitonclick()