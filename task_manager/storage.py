"""
Модуль который загружает и сохраняет задачи
"""
import os

from config import NAME_FILE_SAVES


def insure_save_file():
    if not os.path.exists(NAME_FILE_SAVES):
        with open(NAME_FILE_SAVES, "w", encoding="utf-8"):
            pass


def load_file(task_list):
    with open(NAME_FILE_SAVES, "r", encoding="utf-8") as file:
        for line in file:
            task = line.strip()
            if task:
                task_list.append(task)


def save_file(task_list, file_name):
    with open(file_name, "w", encoding="utf-8") as file:
        for task in task_list:
            file.writelines(f"{task}\n")
