import os
import tkinter as tk


def create_window():
    root = tk.Tk()

    label = tk.Label(root, text="Task Manager")
    button = tk.Button(root, text="Выход", command=root.destroy)
    label.pack()
    button.pack()

    root.geometry("400x300")
    root.title("Task Manager")
    root.iconbitmap(os.path.join(os.path.dirname(os.path.abspath(__file__)), "icon.ico"))
    return root


def main():
    root = create_window()
    root.mainloop()


if __name__ == "__main__":
    main()
