"""
Модуль который загружает и сохраняет задачи
"""
from config import NAME_FILE_SAVES


def load_file(task_list):
    try:
        with open(NAME_FILE_SAVES, "r", encoding="utf-8") as file:
            for line in file:
                task_list.append(line.strip())
    except FileNotFoundError:
        pass


def save_file(task_list, file_name):
    with open(file_name, "w", encoding="utf-8") as file:
        for task in task_list:
            file.writelines(f"{task}\n")
