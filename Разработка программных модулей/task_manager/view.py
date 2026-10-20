"""
Модуль который тображает информацию в консоли
"""


"""информация для показа списка задач"""
def show_collection(task_collection):
    print("=" * 45)

    if len(task_collection) == 0:
        print("Список задач пуст!")
    else:
        for i, task in enumerate(task_collection):
            print(i + 1, task.strip())

    print("=" * 45)


def show_menu():
    print("1 - Показать задачи")
    print("2 - Добавить задачу")
    print("3 - Редактировать задачу")
    print("4 - Удаление задачи")
    print("5 - Выход")
