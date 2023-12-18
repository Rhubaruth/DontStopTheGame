import customtkinter


class MyFrame(customtkinter.CTkFrame):
    def __init__(self, master, text, buttAction, **kwargs):
        super().__init__(master, **kwargs)

        # add widgets onto the frame, for example:
        self.label = customtkinter.CTkLabel(self, text=text)
        self.label.grid(row=0, column=0, padx=20)

        self.button = customtkinter.CTkButton(self, text="Button", 
                                              command= buttAction)
        self.button.grid(row=0, column=1, padx=20)


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("400x200")
        self.grid_rowconfigure(0, weight=1)  # configure grid system
        self.grid_columnconfigure(0, weight=1)

        self.frame_idx = 0
        self.frames = [
            MyFrame(master=self, text="first",
                    buttAction= lambda: self.changeFrame(1)),
            MyFrame(master=self, text="second",
                    buttAction= lambda: self.changeFrame(2)),
            MyFrame(master=self, text="third",
                    buttAction= lambda: self.changeFrame(0)),
        ]

        for frame in self.frames:
            frame.grid(row=0, column=0, padx=20, pady=20, sticky="n")
        self.changeFrame(0)

    def changeFrame(self, id: int):
        print(id)
        frame = self.frames[id]
        frame.lift()


app = App()
app.mainloop()
