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
        if self.win is not None:
            x1 = ((i+1) * self.cell_size_x) - self.cell_size_x + self.x1
            x2 = (i+1) * self.cell_size_x + self.x1
            y1 = ((j+1) * self.cell_size_y) - self.cell_size_y + self.y1
            y2 = (j+1) * self.cell_size_y + self.y1
            self.__cells[i][j].draw(x1, y1, x2, y2)
            self.__animate()    
        return
    
    def __animate(self):
        if self.win is not None:
            self.win.redraw()
        time.sleep(0.01)
        return
    
    def __break_entrance_and_exit(self):
        self.__cells[0][0].has_top_wall = False
        self.__cells[self.num_cols - 1][self.num_rows - 1].has_bottom_wall = False
        if self.win is not None:
            self.__draw_cell(0, 0)
            self.__draw_cell(self.num_cols - 1, self.num_rows - 1)
        self.__break_walls_r(0,0)

    def __break_walls_r(self, i, j):
        self.__cells[i][j].visited = True
        while True:
            new_list = []

            if i - 1 >= 0 and self.__cells[i-1][j].visited != True:
                new_list.append(["left", i-1, j])
            if i + 1 < self.num_cols and self.__cells[i+1][j].visited != True:
                new_list.append(["right", i+1, j])
            if j - 1 >= 0 and self.__cells[i][j - 1].visited != True:
                new_list.append(["top", i, j - 1])
            if j + 1 < self.num_rows and self.__cells[i][j + 1].visited != True:
                new_list.append(["bottom", i, j + 1])
            if new_list == []:
                self.__draw_cell(i, j)
                return
            direction_selection = random.randint(0, len(new_list)-1)
            if new_list[direction_selection][0] == "left":
                self.__cells[i][j].has_left_wall = False
                self.__cells[new_list[direction_selection][1]][new_list[direction_selection][2]].has_right_wall = False
            elif new_list[direction_selection][0] == "right":
                self.__cells[i][j].has_right_wall = False
                self.__cells[new_list[direction_selection][1]][new_list[direction_selection][2]].has_left_wall = False
            elif new_list[direction_selection][0] == "top":
                self.__cells[i][j].has_top_wall = False
                self.__cells[new_list[direction_selection][1]][new_list[direction_selection][2]].has_bottom_wall = False
            elif new_list[direction_selection][0] == "bottom":
                self.__cells[i][j].has_bottom_wall = False
                self.__cells[new_list[direction_selection][1]][new_list[direction_selection][2]].has_top_wall = False

            self.__break_walls_r(new_list[direction_selection][1],new_list[direction_selection][2])
            
    
    def __reset_cells_visited(self):
        for i in range(0, self.num_cols):
            for j in range(0, self.num_rows):
                self.__cells[i][j].visited = False

    def solve(self):
        self.__reset_cells_visited()
        self._solve_r(0, 0)

    def _solve_r(self, i, j):
        # print("Entering solve")
        self.__animate()
        # print("animated")
        self.__cells[i][j].visited = True
        check1 = False
        check2 = False
        check3 = False
        check4 = False
        if i == self.num_cols - 1 and j == self.num_rows - 1:
            # print("Exiting, reached finish")
            return True
        # print(f"Checking left: i-1={i-1} >= 0? {i-1 >= 0}, visited={self.__cells[i-1][j].visited}, has_left_wall={self.__cells[i][j].has_left_wall}")
        if i - 1 >= 0 and self.__cells[i-1][j].visited != True and self.__cells[i][j].has_left_wall == False:
            # print("Going left")
            self.__cells[i][j].draw_move(self.__cells[i-1][j])
            check1 = self._solve_r(i - 1, j)
            if not check1:
                self.__cells[i][j].draw_move(self.__cells[i-1][j], True)
        # print(f"Checking right: i+1={i+1} < {self.num_cols}? {i+1 < self.num_cols}, visited={self.__cells[i+1][j].visited}, has_right_wall={self.__cells[i][j].has_right_wall}")
        if i + 1 < self.num_cols and self.__cells[i+1][j].visited != True and self.__cells[i][j].has_right_wall == False:
            # print("Going right")
            self.__cells[i][j].draw_move(self.__cells[i+1][j])
            check2 = self._solve_r(i + 1, j)
            if not check2:
                self.__cells[i][j].draw_move(self.__cells[i+1][j], True)
        # print(f"Checking top: j-1={j-1} >= 0? {j-1 >= 0}, visited={self.__cells[i][j - 1].visited}, has_top_wall={self.__cells[i][j].has_top_wall}")
        if j - 1 >= 0 and self.__cells[i][j - 1].visited != True and self.__cells[i][j].has_top_wall == False:
            # print("Going up")
            self.__cells[i][j].draw_move(self.__cells[i][j - 1])
            check3 = self._solve_r(i, j - 1)
            if not check3:
                self.__cells[i][j].draw_move(self.__cells[i][j - 1], True)
        # print(f"Checking bottom: j+1={j+1} < {self.num_rows}? {j+1 < self.num_rows}, visited={self.__cells[i][j + 1].visited}, has_bottom_wall={self.__cells[i][j].has_bottom_wall}")
        if j + 1 < self.num_rows and self.__cells[i][j + 1].visited != True and self.__cells[i][j].has_bottom_wall == False:
            # print("Going down")
            self.__cells[i][j].draw_move(self.__cells[i][j + 1])
            check4 = self._solve_r(i, j + 1)
            if not check4:
                self.__cells[i][j].draw_move(self.__cells[i][j + 1], True)
        if check1 or check2 or check3 or check4:
            return True
        else:
            return False

        
