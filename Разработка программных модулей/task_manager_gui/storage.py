"""
Слой хранения: загрузка и сохранение задач в файл json
"""
import json
import os
import shutil

import config


def insure_save_file(path=None):
    path = path or config.FILE_TASKS
    if not os.path.exists(path):
        save_tasks([], path)


def save_tasks(tasks, path=None):
    path = path or config.FILE_TASKS
    temp_path = path + ".tmp"
    with open(temp_path, "w", encoding="utf-8") as file:
        json.dump(tasks, file, ensure_ascii=False, indent=2)
    os.replace(temp_path, path)


def load_tasks(path=None):
    """Возвращает (список задач, текст ошибки или None)."""
    path = path or config.FILE_TASKS
    insure_save_file(path)
    try:
        with open(path, "r", encoding="utf-8") as file:
            data = json.load(file)
        if not isinstance(data, list) or not all(
                isinstance(task, dict) and "name" in task and "content" in task for task in data):
            raise ValueError("wrong structure")
        return [{"name": str(task["name"]), "content": str(task["content"])} for task in data], None
    except ValueError:
        shutil.copyfile(path, path + ".broken")
        return [], f"Файл сохранений поврежден, его копия лежит в {os.path.basename(path)}.broken"
