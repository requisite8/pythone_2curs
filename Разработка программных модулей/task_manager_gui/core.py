"""
Слой логики: добавление, редактирование и удаление задач.
Не зависит от Tkinter, каждая функция возвращает (успех, сообщение).
"""
from config import MAX_CONTENT_LEN, MAX_NAME_LEN


def make_task(name, content):
    name = name.strip()
    content = content.strip()

    if not name or not content:
        return None, "Название и содержание не могут быть пустыми!"
    if len(name) > MAX_NAME_LEN:
        return None, f"Название длиннее {MAX_NAME_LEN} символов!"
    if len(content) > MAX_CONTENT_LEN:
        return None, f"Содержание длиннее {MAX_CONTENT_LEN} символов!"
    return {"name": name, "content": content}, None


def is_valid_index(tasks, index):
    return index is not None and 0 <= index < len(tasks)


def add_task(tasks, name, content):
    task, error = make_task(name, content)
    if error:
        return False, error
    tasks.append(task)
    return True, f"Задача «{task['name']}» добавлена"


def edited_task(tasks, index, name, content):
    if not is_valid_index(tasks, index):
        return False, "Выберите задачу в списке!"
    task, error = make_task(name, content)
    if error:
        return False, error
    tasks[index] = task
    return True, f"Задача «{task['name']}» изменена"


def deleted_task(tasks, index):
    if not is_valid_index(tasks, index):
        return False, "Выберите задачу в списке!"
    task = tasks.pop(index)
    return True, f"Задача «{task['name']}» удалена"
