import tkinter as tk

BOARD_SIZE = (10, 8)
CELL_SIZE = 25
board = []

class cell:
    position: (int, int)
    frame: tk.Frame
    button: tk.Button


    def __init__(self, x: int, y: int, parent):
        self.position = (x, y)
        self.button = tk.Button(parent, width=CELL_SIZE, height=CELL_SIZE)

        padd = 0
        self.button.pack(side=tk.TOP, padx=padd, pady=padd)
        self.button.place(x=x*(CELL_SIZE+padd), y=y*(CELL_SIZE+padd))


# Create a Tkinter root window
root = tk.Tk()
root.title("Colored Columns")

boardFrame = tk.Frame(root, width=480, height=320)
boardFrame.pack()


for y in range(BOARD_SIZE[1]):
    for x in range(BOARD_SIZE[0]):
        board.append(cell(x, y, boardFrame))

# Start the Tkinter main loop
root.mainloop()
