import turtle as t

def generate_gradient(color1, color2, steps):
    # This function now correctly uses color1 and color2
    r1, g1, b1 = int(color1[1:3], 16), int(color1[3:5], 16), int(color1[5:7], 16)
    r2, g2, b2 = int(color2[1:3], 16), int(color2[3:5], 16), int(color2[5:7], 16)
    gradient = []
    for i in range(steps):
        t_ratio = i / (steps - 1)
        # The int() conversion now correctly wraps the entire calculation
        r = int(r1 * (1 - t_ratio) + r2 * t_ratio)
        g = int(g1 * (1 - t_ratio) + g2 * t_ratio)
        b = int(b1 * (1 - t_ratio) + b2 * t_ratio)
        gradient.append(f"#{r:02x}{g:02x}{b:02x}")
    
    # This return statement is now correctly de-dented
    return gradient

# Added the required '#' prefix to the color strings
LIGHT_CYAN = "#E0FFFF"
DEEP_SKY_BLUE = "#00BFFF"
DARK_SLATE_BLUE = "#483D8B"

part1 = generate_gradient(LIGHT_CYAN, DEEP_SKY_BLUE, 80)
part2 = generate_gradient(DEEP_SKY_BLUE, DARK_SLATE_BLUE, 80)
gradient_colors = part1 + part2

t.speed(0)
screen = t.Screen()
screen.bgcolor("black")
t.hideturtle()

num_layers = 15
for i in range(num_layers):
    color_index = int((i / num_layers) * (len(gradient_colors) - 1))
    t.pencolor(gradient_colors[color_index])
    
    size = 10 + i * 7
    
    for _ in range(8):
        t.forward(size)
        t.left(50)
        t.forward(size)
        t.left(130)
        t.forward(size)
        t.left(50)
        t.forward(size)
        t.left(130)
        t.left(360 / 8)

screen.done()