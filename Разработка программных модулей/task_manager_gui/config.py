import os
import sys


def get_base_dir():
    if getattr(sys, "frozen", False):
        return os.path.dirname(sys.executable)
    return os.path.dirname(os.path.abspath(__file__))


BASE_DIR = get_base_dir()
FILE_TASKS = os.path.join(BASE_DIR, "tasks.json")
ICON_PATH = os.path.join(BASE_DIR, "icon.ico")

WINDOW_TITLE = "Task Manager"
WINDOW_SIZE = "600x500"

MAX_NAME_LEN = 50
MAX_CONTENT_LEN = 200
