from turtle import *
shape("turtle")
for i in range(100):
    forward(100)
    left(90)
    shapesize(2*(i + 1), 2*(i + 1), 2)
    if i % 4 == 1:
        color("red")
        fillcolor("blue")
    elif i % 4 == 2:
        color("green")
        fillcolor("black")
    elif i % 4 == 3:
        color("blue")
        fillcolor("red")
    else:
        color("black")
        fillcolor("green")

mainloop()
