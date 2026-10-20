import json
import os
import platform

import psutil

GB = 1024 ** 3


def main():
    data = search_data()
    save_data(data)
    print(json.dumps(data, ensure_ascii=False, indent=2))


def search_data():
    memory = psutil.virtual_memory()
    drive = os.getenv("SystemDrive", "C:") + "\\"

    threads = 0
    for process in psutil.process_iter():
        try:
            threads += process.num_threads()
        except (psutil.AccessDenied, psutil.NoSuchProcess):
            continue

    data = {
        "Имя компьютера": platform.node() + "#",
        "Общая память (Gb)": round(memory.total / GB, 2),
        "Свободная память (Gb)": round(memory.available / GB, 2),
        "Количество процессов": len(psutil.pids()),
        "Количество потоков": threads,
        "Занятая память HDD (Gb)": round(psutil.disk_usage(drive).used / GB, 2),
    }
    return data


def save_data(data: dict):
    with open("data.json", "w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=2)


if __name__ == "__main__":
    main()
