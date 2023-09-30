import tkinter as tk


root = tk.Tk()
root.geometry("480x320")
root.resizable(False, False)

# Frame with player buttons
player_frame = tk.Frame(root, bg="lightgreen", width=200)
player_frame.pack(side=tk.LEFT, fill="y")

def game():
    # Start the Tkinter main loop
    root.title("Gayme")
    root.mainloop()


if __name__ == "__main__":
    game()