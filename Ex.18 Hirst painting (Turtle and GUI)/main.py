# import colorgram      # We use this tool to retrieve the colors from the image.

# rgb_colors = []
# colors = colorgram.extract('image.jpg', 30)
#
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     rgb_tuple = (r, g, b)
#     rgb_colors.append(rgb_tuple)

import turtle as t
import random

color_list = [(246, 242, 244), (202, 164, 110), (236, 239, 243), (149, 75, 50), (222, 201, 136), (53, 93, 123),
              (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35),
              (145, 178, 149), (14, 98, 70), (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77),
              (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102),
              (12, 70, 64), (107, 127, 153), (176, 192, 208), (168, 99, 102)]
art = t.Turtle()
art.shape("arrow")
art.speed("fastest")
art.hideturtle()
t.colormode(255)
x = -325
y = -325

def starting_position():
    art.pu()
    art.setpos(x, y)
    art.pd()

def draw_a_circle():
    color = random.choice(color_list)
    art.fillcolor(color)
    art.color(color)
    art.begin_fill()
    art.circle(20)
    art.end_fill()

def draw_one_row():
    for _ in range(10):
        draw_a_circle()
        art.pu()
        art.forward(70)
        art.pd()

for _ in range(10):
    starting_position()
    draw_one_row()
    y += 70

screen = t.Screen()
screen.exitonclick()
