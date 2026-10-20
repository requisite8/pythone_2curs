import os
import sys


def get_base_dir():
    if getattr(sys, "frozen", False):
        return os.path.dirname(sys.executable)
    return os.path.dirname(os.path.abspath(__file__))


collection = []
is_running = True
NAME_FILE_SAVES = os.path.join(get_base_dir(), "saves.txt")
