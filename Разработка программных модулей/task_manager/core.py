"""
Модуль который хранит главные функции
"""
from utils import check_confirm


"""Запрашивает имя и содержание, возвращает строку задачи или None если ввод пустой"""
def ask_task():
    task_name = input("Введите имя задачи: ").strip()
    task_content = input("Введите содержание задачи: ").strip()

    if not task_name or not task_content:
        print("Имя задачи и ее содержание не могут быть пустыми!")
        return None

    return f"{task_name} | {task_content}"


"""Функция удаления задачи"""
def deleted_task(task_collection):
    if not task_collection:
        print("Список задач пуст, удалять нечего!")
        return

    delete_task = input("Введите номер задачи: ")

    if check_confirm(delete_task, task_collection):
        task_collection.pop(int(delete_task) - 1)
        print(f"Задача {delete_task.strip()} удалена!")


"""Функция которая редактирует"""
def edited_task(task_collection):
    if not task_collection:
        print("Список задач пуст, редактировать нечего!")
        return

    edit_task_number = input("Введите номер задачи: ")

    if check_confirm(edit_task_number, task_collection):
        new_task = ask_task()
        if new_task:
            task_collection[int(edit_task_number) - 1] = new_task
            print(f"Задача {new_task} успешно изменена!")


"""функция добавления задач"""
def add_task(task_collection):
    new_task = ask_task()
    if new_task:
        task_collection.append(new_task)
        print(f"Задача {new_task} успешно добавлена!")
