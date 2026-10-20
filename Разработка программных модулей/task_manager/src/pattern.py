import math
import tkinter as tk

root = tk.Tk()
root.geometry("400x400")
root.title("Круг из кнопок")
i = 0
while i < 12:
    tk.Button(root, text=i + 1, bg="gold" if i % 2 else "skyblue").place(x=178 + 140 * math.cos(i * math.pi / 6), y=178 + 140 * math.sin(i * math.pi / 6), width=44, height=44)
    i += 1
root.mainloop()
