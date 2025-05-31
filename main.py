from classes.window import Window
from classes.line import Line
from classes.point import Point
from classes.cell import Cell
from classes.maze import Maze

def main():
    win = Window(1200, 1000)

    # p1 = Point(100, 100)
    # p2 = Point(200, 100)

    # p3 = Point(200, 100)
    # p4 = Point(200, 200)

    # p5 = Point(200, 200)
    # p6 = Point(100, 200)

    # p7 = Point(100, 200)
    # p8 = Point(100, 100)

    # p9 = Point(100, 100)
    # p10 = Point(200, 200)

    # l1 = Line(p1, p2)
    # l2 = Line(p3, p4)
    # l3 = Line(p5, p6)
    # l4 = Line(p7, p8)
    # l5 = Line(p9, p10)

    # win.draw_line(l1, "red")
    # win.draw_line(l2, "green")
    # win.draw_line(l3, "blue")
    # win.draw_line(l4, "orange")
    # win.draw_line(l5, "purple")

    # test_cell1 = Cell(win)
    # test_cell1.draw(100,100,200,200)

    # test_cell2 = Cell(win)
    # test_cell2.has_bottom_wall = False
    # test_cell2.draw(300,100,400,200)

    # test_cell3 = Cell(win)
    # test_cell3.has_left_wall = False
    # test_cell3.draw(500,100,600,200)

    # test_cell4 = Cell(win)
    # test_cell4.has_right_wall = False
    # test_cell4.draw(100,300,200,400)

    # test_cell5 = Cell(win)
    # test_cell5.has_top_wall = False
    # test_cell5.draw(300,300,400,400)

    # test_cell6 = Cell(win)
    # test_cell6.has_top_wall = False
    # test_cell6.has_bottom_wall = False
    # test_cell6.draw(500,300,600,400)

    # test_cell7 = Cell(win)
    # test_cell7.has_left_wall = False
    # test_cell7.has_right_wall = False
    # test_cell7.draw(100,500,200,600)

    # test_cell2.draw_move(test_cell5)
    # test_cell3.draw_move(test_cell4)

    the_maze = Maze(50, 50, 20, 20, 20, 20, win)
    the_maze.solve()
    win.wait_for_close()
    


main()