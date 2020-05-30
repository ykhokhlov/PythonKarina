from tkinter import *
import random
import time

class Ball:
    def __init__(self, canvas, color, yOffset = 0):
        self.currentPossitionX = 245
        self.currentPossitionY = 100 + yOffset
        self.canvas = canvas
        self.id = canvas.create_oval(20, 20, 50, 50, fill=color)
        self.canvas.move(self.id, self.currentPossitionX, self.currentPossitionY)

    def draw(self):
        moveForward(5)

    def moveForward(self, pixelsForward):
        self.canvas.move(self.id, pixelsForward, 0)


tk = Tk()
tk.title("Гра")
tk.resizable(0,0)
tk.wm_attributes("-topmost", 1)
canvas = Canvas(tk, width=800, height=400, bd=0, \
                highlightthickness=0)
canvas.pack()
tk.update()

ball1 = Ball(canvas, 'red')
ball2 = Ball(canvas, 'green')

##while 1:
##    ball1.moveForward(5)
##    tk.update_idletasks()
##    tk.update()
##    time.sleep(1)

time.sleep(0.1)


for i in range(0,123):
    if(i > 30):
        ball1.moveForward(4);
    ball2.moveForward(3);
    tk.update_idletasks()
    tk.update()
    time.sleep(0.1)
