import Tkinter as tk
from Tkinter import *
from threading import Thread


class Board:
    def __init__(self, title, width, height, rows, columns):
        self.shouldQuit = False
        self.height = height
        self.width = width
        self.boardWindow = tk.Tk()
        self.boardWindow.title(title)
        self.boardWindow.geometry(str(width) + "x" + str(height))
        self.boardWindow.resizable(0, 0)
        self.cells = [[0 for x in range(columns)] for y in range(rows)]

        grid_height = 4
        grid_width = 10

        odd_color = "#2F353B"    # type: str
        even_color = "#FFFFFF"  # type: str

        grid_color = "#FFFFFF"   # type: str

        for row in range(rows):
            init_color = grid_color
            for col in range(columns):
                v = StringVar()
                label = Label(self.boardWindow, height=grid_height, width=grid_width, bg=grid_color, textvariable=v,
                              font=("Helvetica", 12, "bold italic"), fg="red")
                self.cells[row][col] = v
                label.grid(row=row, column=col)
                if grid_color == even_color:
                    grid_color = odd_color
                else:
                    grid_color = even_color

            if init_color == even_color:
                init_color = odd_color
            else:
                init_color = even_color
            grid_color = init_color

    def render(self):
        t = Thread(target=self.handle_rend, args=())
        t.start()

    def handle_rend(self):
        while not self.shouldQuit:
            self.boardWindow.update_idletasks()
            self.boardWindow.update()

    def pretty_print(self, positions):
        for cell in positions:
            self.cells[cell.row][cell.col].set("test")

    def close(self):
        self.shouldQuit = True


class Cell:
    def __init__(self, row, col, value):
        self.row = row
        self.col = col
        self.value = value


board = Board("CSP Backtrack", 1366, 780, 8, 8)
cell = Cell(1, 1, "Q1")
board.render()
positions = [cell]
board.pretty_print(positions)
#board.close()