from classes.window import Window
from classes.point import Point
from classes.line import Line

class Cell:
    def __init__(self, window:Window = None):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self.__x1 = -1
        self.__x2 = -1
        self.__y1 = -1
        self.__y2 = -1
        self.__win = window
        self.visited = False

    def draw(self, x1, y1, x2, y2):
        win_check = self.__win is not None
        self.__x1 = min(x1, x2)
        self.__y1 = min(y1, y2)
        self.__x2 = max(x1, x2)
        self.__y2 = max(y1, y2)
        line_color_left = "#d9d9d9"
        line_color_right = "#d9d9d9"
        line_color_top = "#d9d9d9"
        line_color_bottom = "#d9d9d9"
        if self.has_left_wall:
            line_color_left = "black"
        if self.has_right_wall:
            line_color_right = "black"
        if self.has_top_wall:
            line_color_top = "black"
        if self.has_bottom_wall:
            line_color_bottom = "black"
        
        point1 = Point(x1, y1)
        point2 = Point(x1, y2)
        l1 = Line(point1, point2)
        if win_check:
            self.__win.draw_line(l1,line_color_left)
        
        point3 = Point(x2, y1)
        point4 = Point(x2, y2)
        l2 = Line(point3, point4)
        if win_check:
            self.__win.draw_line(l2,line_color_right)
    
        point5 = Point(x1, y1)
        point6 = Point(x2, y1)
        l3 = Line(point5, point6)
        if win_check:
            self.__win.draw_line(l3,line_color_top)
    
        point7 = Point(x1, y2)
        point8 = Point(x2, y2)
        l4 = Line(point7, point8)
        if win_check:
            self.__win.draw_line(l4,line_color_bottom)
    
    def draw_move(self, to_cell, undo=False):
        win_check = self.__win is not None
        line_color = "red"
        if undo == True:
            line_color = "gray"
        draw_point1 = Point((self.__x1 + self.__x2)/2, (self.__y1 + self.__y2)/2)
        draw_point2 = Point((to_cell.__x1 + to_cell.__x2)/2, (to_cell.__y1 + to_cell.__y2)/2)
        line1 = Line(draw_point1, draw_point2)
        if win_check:
            self.__win.draw_line(line1, line_color)