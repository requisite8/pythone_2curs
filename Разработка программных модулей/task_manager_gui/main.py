"""
Task Manager с окном на Tkinter (слоистая архитектура).

Слои:
    storage.py                      - хранение задач в tasks.json
    core.py                         - логика: добавить, изменить, удалить
    view.py                         - показ задач в виджетах
    AppButton, AppLabel, AppListbox - собственные виджеты
    Interface.py                    - окно, связывает все слои

Улучшения по версиям - в BACKLOG.md, идеи и найденные проблемы - в BUGFIX.md.
"""
from Interface import Interface

if __name__ == "__main__":
    Interface().run()
