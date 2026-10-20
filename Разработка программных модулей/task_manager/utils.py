"""
Модуль который содержит утилы
"""


"""Функция для проверки подтверждения"""
def check_confirm(select_task, task_list):
    select_task = select_task.strip()

    if select_task.isdecimal():
        if 0 < int(select_task) <= len(task_list):
            return True
        else:
            print(f"Задачи с номером {select_task} нет в списке!")
            return False
    else:
        print("Введите именно номер задачи!")
        return False
