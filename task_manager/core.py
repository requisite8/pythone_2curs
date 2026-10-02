"""
Модуль который хранит главные функции
"""
from utils import check_confirm


"""Функция удаления задачи"""
def deleted_task(task_collection):
    delete_task = input("Введите номер задачи: ")

    if check_confirm(delete_task, task_collection):
        task_collection.pop(int(delete_task) - 1)
        print(f"Задача {delete_task} удалена!")
    else:
        print("Неверный номер задачи!")


"""Функция которая редактирует"""
def edited_task(task_collection):
    edit_task_number = input("Введите номер задачи: ")
    if check_confirm(edit_task_number, task_collection):
        edit_name = input("Новое имя задачи: ")
        task_collection[int(edit_task_number) - 1] = edit_name
        print(f"Задача {edit_name} успешно изменена!")


"""функция добавления задач"""
def add_task(task_collection):
    task_name = input("Введите имя задачи для добавления: ").strip()
    task_content = input("Введите содержание задачи: ").strip()

    if not task_name or not task_content:
        print("Имя задачи и ее содержание не могут быть пустыми!")
        return

    full_name = f"{task_name} | {task_content}"
    task_collection.append(full_name)
    print(f"Задача {full_name} успешно добавлена!")
