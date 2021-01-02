import tkinter as tk


class mainWindow(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.geometry("{}x{}".format(800, 600))
        self.title("Mancala")


if __name__ == "__main__":
    window = mainWindow()
    window.mainloop()
