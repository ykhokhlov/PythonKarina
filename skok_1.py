from tkinter import *
import random
import time

class Ball:
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.id = canvas.create_oval(20, 20, 50, 50, fill=color)
        self.canvas.move(self.id, 245, 100)

        def draw(self):
            pass

tk = Tk()
tk.title("Гра")
tk.resizable(0,0)
tk.wm_attributes("-topmost", 1)
canvas = Canvas(tk, width=500, height=400, bd=0, \
                highlightthickness=0)
canvas.pack()
tk.update()

ball = Ball(canvas, 'red')
