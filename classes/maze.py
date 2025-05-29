from classes.cell import Cell
import time
import random

class Maze:
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win=None, seed=None):
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = win
        if seed is not None:
            self.seed = random.seed(seed)
        else:
            self.seed = seed
        self.__cells = []
        self.__create_cells()
    
    def __create_cells(self):
        win_check = self.win is not None
        if self.num_cols < 1 or self.num_rows < 1:
            raise Exception("Invalid number of rows or columns")
        for i in range(0, self.num_cols):
            self.__cells.append([])
            for j in range(0, self.num_rows):
                self.__cells[i].append(Cell(self.win))
                if win_check:
                    self.__draw_cell(i, j)
        self.__break_entrance_and_exit()
    
    def __draw_cell(self, i, j):
        x1 = ((i+1) * self.cell_size_x) - self.cell_size_x + self.x1
        x2 = (i+1) * self.cell_size_x + self.x1
        y1 = ((j+1) * self.cell_size_y) - self.cell_size_y + self.y1
        y2 = (j+1) * self.cell_size_y + self.y1
        self.__cells[i][j].draw(x1, y1, x2, y2)
        self.__animate()
        return
    
    def __animate(self):
        self.win.redraw()
        time.sleep(0.05)
        return
    
    def __break_entrance_and_exit(self):
        self.__cells[0][0].has_top_wall = False
        self.__cells[self.num_cols - 1][self.num_rows - 1].has_bottom_wall = False
        if self.win is not None:
            self.__draw_cell(0, 0)
            self.__draw_cell(self.num_cols - 1, self.num_rows - 1)

        
