import tkinter as tk


root = tk.Tk()
root.geometry("600x480")
root.resizable(False, False)

def get_input(*args):
    user_input = entry.get().strip()
    if not user_input:
        user_input = "[No Input]"
    result_label.config(text=f'{user_input}')

# entry widget
bottom_frame = tk.Frame(root, bg="MediumPurple3")
bottom_frame.pack(side=tk.BOTTOM, fill=tk.X)

entry = tk.Entry(bottom_frame)
entry.grid(row=0, column=0, sticky="ew", padx=15, pady=5)
entry.bind('<Return>', get_input)

submit_button = tk.Button(bottom_frame, text="Submit", command=get_input)
submit_button.grid(row=0, column=1, padx=15, pady=5)

# configure the column 0
bottom_frame.columnconfigure(0, weight=1)
bottom_frame.columnconfigure(0, weight=1)

# result label widget
result_label = tk.Label(root, text="[No Input]")
result_label.pack(side=tk.TOP, pady=10, fill="x")



def main():
    # Start the Tkinter main loop
    root.title("Gayme")
    root.mainloop()


if __name__ == "__main__":
    main()