from classes.point import Point
from tkinter import Canvas

class Line:
    def __init__(self, first_point:Point, second_point:Point):
        self.first_point = first_point
        self.second_point = second_point
    
    def draw(self, canvas: Canvas, fill_color):
        canvas.create_line(self.first_point.x, self.first_point.y, self.second_point.x, self.second_point.y, fill=fill_color, width=2)