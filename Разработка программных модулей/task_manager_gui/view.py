"""
Слой отображения: превращает задачи в строки и показывает их в виджетах
"""


def format_task(number, task):
    return f"{number}. {task['name']} | {task['content']}"


def show_tasks(app_listbox, tasks):
    app_listbox.set_items([format_task(number, task) for number, task in enumerate(tasks, 1)])


def show_counter(app_label, tasks):
    app_label.show(f"Всего задач: {len(tasks)}")
