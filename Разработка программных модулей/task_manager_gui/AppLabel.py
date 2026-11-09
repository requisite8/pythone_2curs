import tkinter as tk


class AppLabel(tk.Label):
    COLORS = {"info": "#333333", "success": "#2E7D32", "error": "#C62828"}

    def __init__(self, parent, text="", **kwargs):
        kwargs.setdefault("anchor", "w")
        super().__init__(parent, text=text, **kwargs)

    def show(self, text, kind="info"):
        self.config(text=text, fg=self.COLORS[kind])
