
from tkinter import *
import time
from Ball import *

window = Tk()

WIDTH = 600
HEIGHT = 600

canvas = Canvas(window, width=WIDTH, height=HEIGHT)
canvas.pack()


VolleyBall = Ball(canvas, 0, 0, 130, 0, 2, "white")
tennis_ball = Ball(canvas, 0, 0, 50, 2, 1, "yellow")
basket_ball = Ball(canvas, 100, 100, 200, 3, 1, "red")

while True:
    VolleyBall.move()
    tennis_ball.move()
    basket_ball.move()
    window.update()
    time.sleep(0.01)

window.mainloop()
