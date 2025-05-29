from tkinter import Tk, BOTH, Canvas
from classes.line import Line

class Window: 
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.root = Tk()
        self.root.title = "Maze builder and solver in Tkinter"
        self.canvas = Canvas(self.root, width=self.width, height=self.height)
        self.canvas.pack()
        self.window_active = False
        self.root.protocol("WM_DELETE_WINDOW", self.close)

    def redraw(self):
        self.root.update_idletasks()
        self.root.update()

    def wait_for_close(self):
        self.window_active = True
        while self.window_active:
            self.redraw()

    def close(self):
        self.window_active = False
    
    def draw_line(self, line:Line, fill_color):
        line.draw(self.canvas, fill_color)