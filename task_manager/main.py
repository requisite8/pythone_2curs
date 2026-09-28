import config
from config import collection, NAME_FILE_SAVES
from view import show_collection, show_menu
from core import add_task, edit_task, delete_tasks
from storage import load_file, save_file


def main():
    load_file(collection)

    while config.is_running:
        show_menu()
        choice_user = input("Введите свой выбор: ")

        match choice_user:
            case "1":
                show_collection(collection)

            case "2":
                add_task(collection)
                save_file(collection, NAME_FILE_SAVES)

            case "3":
                show_collection(collection)
                edit_task(collection)
                save_file(collection, NAME_FILE_SAVES)

            case "4":
                show_collection(collection)
                delete_tasks(collection)
                save_file(collection, NAME_FILE_SAVES)

            case "5":
                save_file(collection, NAME_FILE_SAVES)
                config.is_running = False
                print("До свидания!")

            case _:
                print("Такого пункта нет...")


if __name__ == "__main__":
    main()
