from tkinter import Tk, BOTH, Canvas

class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

class Line:
    def __init__(self, p1: Point, p2: Point):
        self.p1 = p1
        self.p2 = p2

    def draw(self, canv: Canvas, fill_color="black"):
        canv.create_line(self.p1.x, self.p1.y, self.p2.x, self.p2.y, fill=fill_color, width=2)
        canv.pack(fill=BOTH, expand=1)

class Window:
    
    def __init__(self, width, height):
        # self.__width = width
        # self.__height = height
        self.__root = Tk()
        self.__root.title("Maze Solver")
        self.__canv = Canvas(self.__root, bg="white", height=height, width=width)
        self.__canv.pack(fill=BOTH, expand=1)
        self.__is_running = False
        self.__root.protocol("WM_DELETE_WINDOW", self.close)
    
    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self):
        self.__is_running = True
        while self.__is_running:
            self.redraw()

    def close(self):
        self.__is_running = False

    def draw_line(self, line: Line, fill_color="black"):
        line.draw(self.__canv, fill_color )

class Cell:
    def __init__(self, win: Window):
        self.__x1 = None
        self.__x2 = None
        self.__y1 = None
        self.__y2 = None
        self.__win = win
        self.visited = False
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        
    def draw(self,  x1, y1, x2, y2):
        if self.has_left_wall:
            line = Line(Point(x1,y1), Point(x1,y2))
            self.__win.draw_line(line)
        if self.has_top_wall:
            line = Line(Point(x1,y1), Point(x2,y1))
            self.__win.draw_line(line)
        if self.has_right_wall:
            line = Line(Point(x2,y1), Point(x2,y2))
            self.__win.draw_line(line)
        if self.has_bottom_wall:
            line = Line(Point(x1,y2), Point(x2,y2))
            self.__win.draw_line(line)
