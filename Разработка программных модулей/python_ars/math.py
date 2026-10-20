import tkinter as tk
root = tk.Tk()
root.geometry("500x500")

collection = ["task1 create menu", "task2 create menu", "task3 create menu", "task4 create menu"]

frame_menu = None
frame_tasks = None

root.mainloop()
frame_menu = tk.Frame(root, background="#d9d9d9", width=400, height=400)


def show_all_tasks():
    frame_menu.pack_forget()
    frame_tasks.pack(


def create_menu():
    frame_tasks.pack_forget()
    frame_menu.pack()

main()
root.mainloop()