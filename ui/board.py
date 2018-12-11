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

        gridHeight = int(height / (rows * 15))
        gridWidth = int(width / (columns * 8))

        label2 = Label(self.boardWindow, bg="#E1E5EC", text="Backtracking Search")
        label2.grid()

        oddColor = "#2F353B"
        evenColor = "#FFFFFF"

        gridColor = "#FFFFFF"

        for row in range(rows - 1):
            for col in range(columns - 1):
                v = StringVar()
                label = Label(self.boardWindow, height=gridHeight, width=gridWidth, bg=gridColor, textvariable=v)
                self.cells[row][col] = v
                label.grid(row=row, column=col)
                if (gridColor == evenColor):
                    gridColor = oddColor
                else:
                    gridColor = evenColor

    def render(self):
        t = Thread(target=self.handle_rend, args=())
        t.start()

    def handle_rend(self):
        while (self.shouldQuit != True):
            self.boardWindow.update_idletasks()
            self.boardWindow.update()

    def prettyPrint(self, positions):
        for cell in positions:
            self.cells[cell.row][cell.col].set("test")

    def close(self):
        self.shouldQuit = True


class Cell:
    def __init__(self, row, col, value):
        self.row = row
        self.col = col
        self.value = value


board = Board("CSP Backtrack", 800, 600, 4, 4)
cell = Cell(1, 1, "Q1")
board.render()
positions = [cell]
board.prettyPrint(positions)
time.sleep(4)
board.close()