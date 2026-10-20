import processes


def show_collection(collection):
    print('=' * 30)
    for i, j in enumerate(collection):
        print(f"{i + 1}. {j}")
    print("=" * 30)


def show_menu():
    print("1 посмотреть задачу \n2 добавить задачу \n3 редактировать задачу \n4 удалить задачу \n5 выход")


def show_message(action, success, task_name=None):
    if action == 'add':
        if success:
            print(f"Задача '{task_name}' успешно добавлена")
        else:
            print("Задача не может быть пустой")
    elif action == 'edit':
        if success:
            print(f"Задача успешно изменена на '{task_name}'")
        else:
            print("НЕТ В СПИСКЕ")
    elif action == 'delete':
        if success:
            print(f"Задача '{task_name}' удалена")
        else:
            print("НЕТ В СПИСКЕ")


def check_confirm(select_task, task_list):
    if select_task.isdigit() and 0 < int(select_task) <= len(task_list):
        return True
    return False


def add_tasks(task_collection):
    task_name = input("Введите задачу: ").strip()
    if task_name:
        task_collection.append(task_name)
        show_message('add', True, task_name)
    else:
        show_message('add', False)


def edit_task(task_collection):
    show_collection(task_collection)
    select_edit = input("Введите номер задачи: ")
    if check_confirm(select_edit, task_collection):
        edit_name = input("Новое имя задачи: ").strip()
        task_collection[int(select_edit) - 1] = edit_name
        show_message('edit', True, edit_name)
    else:
        show_message('edit', False)


def delete_tasks(task_collection):
    show_collection(task_collection)
    select_delete = input("Введите номер задачи для удаления: ")
    if check_confirm(select_delete, task_collection):
        removed = task_collection.pop(int(select_delete) - 1)
        show_message('delete', True, removed)
    else:
        show_message('delete', False)


def main():
    is_running = True
    collection = []
    while is_running:
        show_menu()
        clause_user = input("введите свой выбор: ")
        match clause_user:
            case '1':
                show_collection(collection)
                processes.main()
            case '2':
                add_tasks(collection)
            case '3':
                edit_task(collection)
            case '4':
                delete_tasks(collection)
            case '5':
                is_running = False
                print('Адьес амиго')
            case _:
                print('НЕМА')


if __name__ == '__main__':
    main()
