import tkinter as tk


class AppButton(tk.Button):
    def __init__(self, parent, text, command, **kwargs):
        kwargs.setdefault("width", 14)
        kwargs.setdefault("pady", 4)
        kwargs.setdefault("cursor", "hand2")
        super().__init__(parent, text=text, command=command, **kwargs)
