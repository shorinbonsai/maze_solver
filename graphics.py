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

    def draw_line(self, line: Line, fill_color):
        line.draw(self.__canv, fill_color )
