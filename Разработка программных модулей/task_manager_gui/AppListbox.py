import tkinter as tk


class AppListbox(tk.Frame):
    def __init__(self, parent, **kwargs):
        super().__init__(parent)
        self.listbox = tk.Listbox(self, activestyle="none", selectmode="single", exportselection=False, **kwargs)
        scrollbar = tk.Scrollbar(self, command=self.listbox.yview)
        self.listbox.config(yscrollcommand=scrollbar.set)
        self.listbox.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

    def set_items(self, items):
        self.listbox.delete(0, "end")
        for item in items:
            self.listbox.insert("end", item)

    def selected_index(self):
        selection = self.listbox.curselection()
        return selection[0] if selection else None

    def select(self, index):
        self.listbox.selection_clear(0, "end")
        self.listbox.selection_set(index)
        self.listbox.see(index)

    def bind_select(self, callback):
        self.listbox.bind("<<ListboxSelect>>", callback)
