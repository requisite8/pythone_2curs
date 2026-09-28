import json
import os
import platform

import psutil

def main():
    data = search_data()
    save_data(data)

def search_data():
    comp_name = str(platform.node()) + " " + str(os.getlogin())
    total_memory = psutil.virtual_memory().total
    used_memory = psutil.virtual_memory().used
    active_processes = len(psutil.pids())
    logical_cpu_count = psutil.cpu_count(logical=True)
    cpu_percent = psutil.cpu_percent(interval=1)
    disk_used = psutil.disk_usage(os.getenv("SystemDrive", "C:") + "\\").used
    cpu_freq = psutil.cpu_freq()
    cpu_speed = cpu_freq.current if cpu_freq else None

    data = {
        "Имя Компа": comp_name,
        "Общая память": total_memory,
        "Используемая память": used_memory,
        "Число процессов - активных": active_processes,
        "Число потоков": logical_cpu_count,
        "Загрузка процессора, %": cpu_percent,
        "Занято памяти на HDD": disk_used,
        "Скорость процессора": cpu_speed
    }
    return data

def save_data(data:dict):
    name = "data.json"
    file = open(name, "w", encoding="utf-8")
    file.write(json.dumps(data, ensure_ascii=False, indent=2))
    file.close()

if __name__ == '__main__':
    main()
