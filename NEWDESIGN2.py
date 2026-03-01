import turtle as t

def generate_gradient(color1, color2, steps):
    r1, g1, b1 = int(color1[1:3], 16), int(color1[3:5], 16), int(color1[5:7], 16)
    r2, g2, b2 = int(color2[1:3], 16), int(color2[3:5], 16), int(color2[5:7], 16)
    gradient = []
    for i in range(steps):
        t_ratio = i / (steps - 1)
        r = int(r1 * (1 - t_ratio) + r2 * t_ratio)
        g = int(g1 * (1 - t_ratio) + g2 * t_ratio)
        b = int(b1 * (1 - t_ratio) + b2 * t_ratio)
        gradient.append(f"#{r:02x}{g:02x}{b:02x}")
    return gradient

COLOR_START = "#4B0082"
COLOR_MIDDLE = "#D745D7"
COLOR_END = "#FFDCFF"

part1 = generate_gradient(COLOR_START, COLOR_MIDDLE, 80)
part2 = generate_gradient(COLOR_MIDDLE, COLOR_END, 80)
gradient_colors = part1 + part2

t.speed(1000)
screen = t.Screen()
screen.bgcolor("black")
t.hideturtle()

num_layers = 30
for i in range(num_layers):
    color_index = int((i / num_layers) * (len(gradient_colors) - 1))
    t.pencolor(gradient_colors[color_index])
    t.width(2.25)
    size = 15 + i * 10
    radius = i * 10
    num_curves = 10
    for _ in range(num_curves):
        t.penup()
        t.forward(radius)
        t.pendown()
        t.circle(size, 90)
        t.left(90)
        t.circle(size, 90)
        t.left(90)
        t.penup()
        t.backward(radius)
        t.left(360 / num_curves)
        
screen.done()