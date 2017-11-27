from turtle import *

for x in range(100, 0, -1):
    forward(x)
    right(90)

for x in range(100):
    circle(x)
    left(91)

bgcolor("black")
sides = 6
colors = ["red", "yellow", "blue", "orange", "green", "purple"]
for x in range(360):
    pencolor(colors[x%sides])
    forward(x * 3/sides + x)
    left(360/sides + 1)
    width(x*sides/200)