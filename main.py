# # The code commented below was used to pick the colors from an image of Damien Hirst paint
# import colorgram
#
# rgb_colors_from_model = []
# colors = colorgram.extract('damien3.jpg', 30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors_from_model.append(new_color)
# print(rgb_colors_from_model)

import turtle as turtle_module
import random

turtle_module.colormode(255)
hirst = turtle_module.Turtle()
hirst.speed("fastest")
hirst.penup()
hirst.hideturtle()
rgb_color_list = [
                  (31, 105, 179), (237, 208, 106), (232, 149, 78), (216, 232, 244), (127, 83, 40), (236, 116, 145),
                  (189, 48, 84), (114, 103, 191), (247, 234, 238), (211, 63, 86), (145, 172, 7), (40, 182, 101),
                  (204, 10, 34), (112, 187, 134), (228, 48, 39), (120, 182, 219), (33, 55, 114), (6, 146, 108),
                  (185, 168, 226), (6, 166, 174), (149, 224, 186), (87, 34, 37), (40, 43, 83), (146, 35, 34),
                  (231, 168, 181), (84, 38, 37), (235, 171, 162), (151, 207, 220)
                  ]

hirst.setheading(225)
hirst.forward(300)
hirst.setheading(0)
number_of_dots = 100

for dot_count in range(1, number_of_dots + 1):
    def draw_spireograph(size_gap):
        for i in range (int(360 / size_gap)):
             hirst.color(random.choice(rgb_color_list))
             hirst.circle(5)
             hirst.setheading(hirst.heading() + size_gap)
    hirst.pendown()
    draw_spireograph(10)
    hirst.penup()
    hirst.forward(50)
    if dot_count % 10 == 0:
        hirst.setheading(90)
        hirst.forward(50)
        hirst.setheading(180)
        hirst.forward(500)
        hirst.setheading(0)

screen = turtle_module.Screen()
screen.exitonclick()
