import tkinter as tk
from tkinter import messagebox

import config
import core
import storage
import view
from AppButton import AppButton
from AppLabel import AppLabel
from AppListbox import AppListbox


class Interface:
    def __init__(self):
        self.tasks, load_error = storage.load_tasks()

        self.root = tk.Tk()
        self.root.geometry(config.WINDOW_SIZE)
        self.root.title(config.WINDOW_TITLE)
        try:
            self.root.iconbitmap(config.ICON_PATH)
        except tk.TclError:
            pass

        self.name_var = tk.StringVar()
        self.content_var = tk.StringVar()
        self.create_widgets()
        self.refresh()
        if load_error:
            self.status.show(load_error, "error")

    def create_widgets(self):
        form = tk.Frame(self.root)
        form.pack(fill="x", padx=12, pady=(12, 6))
        form.columnconfigure(1, weight=1)
        tk.Label(form, text="Название").grid(row=0, column=0, sticky="w")
        tk.Entry(form, textvariable=self.name_var).grid(row=0, column=1, sticky="we", padx=(8, 0), pady=2)
        tk.Label(form, text="Содержание").grid(row=1, column=0, sticky="w")
        tk.Entry(form, textvariable=self.content_var).grid(row=1, column=1, sticky="we", padx=(8, 0), pady=2)

        buttons = tk.Frame(self.root)
        buttons.pack(fill="x", padx=12, pady=6)
        AppButton(buttons, "Добавить", self.on_add).pack(side="left", padx=(0, 6))
        AppButton(buttons, "Изменить", self.on_edit).pack(side="left", padx=6)
        AppButton(buttons, "Удалить", self.on_delete).pack(side="left", padx=6)

        self.counter = AppLabel(self.root)
        self.counter.pack(fill="x", padx=12)

        self.listbox = AppListbox(self.root)
        self.listbox.pack(fill="both", expand=True, padx=12, pady=6)
        self.listbox.bind_select(self.on_select)

        self.status = AppLabel(self.root)
        self.status.pack(fill="x", padx=12, pady=(0, 10))

    def refresh(self, select=None):
        view.show_tasks(self.listbox, self.tasks)
        view.show_counter(self.counter, self.tasks)
        if select is not None and select < len(self.tasks):
            self.listbox.select(select)

    def finish(self, ok, message, select=None):
        if ok:
            try:
                storage.save_tasks(self.tasks)
            except OSError as error:
                self.status.show(f"Не удалось сохранить файл: {error}", "error")
                return
            self.name_var.set("")
            self.content_var.set("")
        self.refresh(select if ok else self.listbox.selected_index())
        self.status.show(message, "success" if ok else "error")

    def confirm(self, text):
        return messagebox.askokcancel(config.WINDOW_TITLE, text)

    def on_add(self):
        ok, message = core.add_task(self.tasks, self.name_var.get(), self.content_var.get())
        self.finish(ok, message, len(self.tasks) - 1)

    def on_edit(self):
        index = self.listbox.selected_index()
        ok, message = core.edited_task(self.tasks, index, self.name_var.get(), self.content_var.get())
        self.finish(ok, message, index)

    def on_delete(self):
        index = self.listbox.selected_index()
        if core.is_valid_index(self.tasks, index) and not self.confirm(f"Удалить задачу «{self.tasks[index]['name']}»?"):
            return
        ok, message = core.deleted_task(self.tasks, index)
        self.finish(ok, message)

    def on_select(self, event=None):
        index = self.listbox.selected_index()
        if core.is_valid_index(self.tasks, index):
            self.name_var.set(self.tasks[index]["name"])
            self.content_var.set(self.tasks[index]["content"])

    def run(self):
        self.root.mainloop()
