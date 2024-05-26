import turtle as t
import random

timmy = t.Turtle()
timmy.shape("arrow")
timmy.speed("fastest")
# timmy.color("red")

# Spirograph
t.colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color

def draw_spirograph(turn_angle):
    for _ in range(int(360 / turn_angle)):
        timmy.circle(200)
        timmy.right(turn_angle)
        timmy.color(random_color())

draw_spirograph(1)


# # Random Walk
# t.colormode(255)
#
# def random_color():
#     r = random.randint(0, 255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
#     color = (r, g, b)
#     return color
#
# # colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
# directions = [0, 90, 180, 270]
# timmy.pensize(15)
# timmy.speed("fastest")
#
# for _ in range(200):
#     timmy.forward(30)
#     timmy.setheading(random.choice(directions))
#     timmy.color(random_color())


# # Draw Different Shapes
# colours = ["tan", "orange red", "dark magenta", "dark cyan", "sky blue", "pale green", "gold", "dim gray"]
# def draw_shape(num_sides):
#     angle = 360 / num_sides
#     for _ in range(num_sides):
#         timmy.forward(100)
#         timmy.right(angle)
#
#
# for shape_side_n in range(3, 11):
#     draw_shape(shape_side_n)
#     timmy.color(random.choice(colours))


# # Creating Dashed Line
# for _ in range(20):
#     timmy.forward(5)
#     timmy.pu()
#     timmy.forward(5)
#     timmy.pd()

screen = t.Screen()
screen.exitonclick()
