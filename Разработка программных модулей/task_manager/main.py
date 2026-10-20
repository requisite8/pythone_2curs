"""
Task Manager - консольное приложение для управления задачами.
Пользователь может создать задачу (имя + содержание), посмотреть все задачи,
отредактировать или удалить выбранную. Задачи хранятся в файле saves.txt.

Улучшения по версиям (подробнее в BACKLOG.md, найденные баги в BUGFIX.md):
v0.0.1 - разработан цикл приложения (структурное программирование)
v0.0.2 - внедрен i/o функционал для ввода задачи
v0.0.3 - разработаны функции для цикла (функциональное программирование)
v0.0.4 - добавлены проверки и подтверждения
v0.0.5 - созданы методы сохранения и загрузки (файловые сохранения)
v0.0.6 - созданы методы удаления, редактирования и создания задач, логика вынесена из цикла
v0.0.7 - основной цикл помещен в отдельный метод main
v0.0.8 - добавление контента задачи: имя + содержание
v0.0.9 - код разбит на модули config, core, utils, view, storage;
         добавлены BUGFIX.md и BACKLOG.md, приложение протестировано
v0.1.0 - исправлены все баги из BUGFIX.md
v0.1.1 - get_base_dir() определяет папку запуска (в том числе для exe), insure_save_file()
         создает файл сохранений при первом запуске, проект собирается в exe через PyInstaller
"""
import config
from config import collection, NAME_FILE_SAVES
from view import show_collection, show_menu
from core import add_task, edited_task, deleted_task
from storage import insure_save_file, load_file, save_file


def main():
    insure_save_file()
    load_file(collection)

    while config.is_running:
        show_menu()
        choice_user = input("Введите свой выбор: ").strip()

        match choice_user:
            case "1":
                show_collection(collection)

            case "2":
                add_task(collection)
                save_file(collection, NAME_FILE_SAVES)

            case "3":
                show_collection(collection)
                edited_task(collection)
                save_file(collection, NAME_FILE_SAVES)

            case "4":
                show_collection(collection)
                deleted_task(collection)
                save_file(collection, NAME_FILE_SAVES)

            case "5":
                save_file(collection, NAME_FILE_SAVES)
                config.is_running = False
                print("До свидания!")

            case _:
                print("Такого пункта нет...")


if __name__ == "__main__":
    main()
