import os
import tkinter as tk


class Interface:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("400x300")
        self.root.title("Task Manager")
        self.root.iconbitmap(os.path.join(os.path.dirname(os.path.abspath(__file__)), "icon.ico"))
        self.create_widgets()

    def create_widgets(self):
        tk.Label(self.root, text="Task Manager").pack()
        tk.Button(self.root, text="Выход", command=self.root.destroy).pack()

    def run(self):
        self.root.mainloop()


if __name__ == "__main__":
    Interface().run()
