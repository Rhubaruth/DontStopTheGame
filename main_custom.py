import customtkinter as ctk


root = ctk.CTk()
root.title("Gayme")
root.geometry("600x480")

def get_input(*args):
    user_input = entry.get().strip()
    if not user_input:
        user_input = "[No Input]"
    result_label."configure(text=f'{user_input}')

# entry widget
bottom_frame = ctk.CTkFrame(root)
bottom_frame.pack(side=ctk.BOTTOM, fill=ctk.X)

entry = ctk.CTkEntry(bottom_frame)
entry.grid(row=0, column=0, sticky="ew", padx=15, pady=5)
entry.bind('<Return>', get_input)

submit_button = ctk.CTkButton(bottom_frame, text="Submit", command=get_input)
submit_button.grid(row=0, column=1, padx=15, pady=5)

# configure the column 0
bottom_frame.columnconfigure(0, weight=1)
bottom_frame.columnconfigure(0, weight=1)

# result label widget
result_label = ctk.CTkLabel(root, text="[No Input]")
result_label.pack(side=ctk.TOP, pady=10, fill="x")



def main():
    # Start the Tkinter main loop
    root.mainloop()


if __name__ == "__main__":
    main()