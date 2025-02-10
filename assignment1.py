import turtle
import random

pen=turtle.Turtle()
pen.speed(10)
pen.pensize(3)

for i in range(150):
	pen.color(random.choice(["red","orange","yellow","green","blue"]))
	pen.forward(i*2)
	pen.left(144)


turtle.done()

