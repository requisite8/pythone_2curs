import multiprocessing
import os
import time


def first_task():
    print(f"[first_task] запущена, PID = {os.getpid()}")
    time.sleep(2)
    print("[first_task] завершена")


def second_task():
    print(f"[second_task] запущена, PID = {os.getpid()}")
    time.sleep(3)
    print("[second_task] завершена")


def third_task():
    print(f"[third_task] запущена, PID = {os.getpid()}")
    time.sleep(1)
    print("[third_task] завершена")


def fourth_task():
    print(f"[fourth_task] запущена, PID = {os.getpid()}")
    time.sleep(2)
    print("[fourth_task] завершена")


def main():
    process_1 = multiprocessing.Process(target=first_task)
    process_2 = multiprocessing.Process(target=second_task)
    process_3 = multiprocessing.Process(target=third_task)
    processes = [process_1, process_2, process_3]

    for process in processes:
        process.start()
        print(f"Запущен {process.name}, ID процесса = {process.pid}")

    fourth_task()

    for process in processes:
        process.join()

    print("Результаты работы процессов:")
    for process in processes:
        print(f"{process.name}: PID = {process.pid}, exitcode = {process.exitcode}")


if __name__ == '__main__':
    main()
