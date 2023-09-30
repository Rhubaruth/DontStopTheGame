import tkinter as tk


root = tk.Tk()
root.geometry("600x480")
root.resizable(False, False)

def get_input():
    user_input = entry.get().strip()
    if not user_input:
        user_input = "[No Input]"
    result_label.config(text=f'{user_input}')

# entry widget
bottom_frame = tk.Frame(root)
bottom_frame.pack(side=tk.BOTTOM, fill="x")

entry = tk.Entry(bottom_frame)
entry.pack(side=tk.LEFT, pady=10, fill="x")

submit_button = tk.Button(bottom_frame, text="Submit", command=get_input)
submit_button.pack(side=tk.RIGHT, padx=15, pady=10)

# result label widget
result_label = tk.Label(root, text="[No Input]")
result_label.pack(side=tk.TOP, pady=10, fill="x")



def main():
    # Start the Tkinter main loop
    root.title("Gayme")
    root.mainloop()


if __name__ == "__main__":
    main()