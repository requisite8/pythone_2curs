import os
import time
import multiprocessing as mp


def main():
    print("Starting")
    time.sleep(5)
    print("PID " + str(os.getpid()))
    print("PPID " + str(os.getppid()))
    proc = mp.Process(target=welcome)
    proc.start()
    proc.join()


def welcome():
    print('Hello')
    time.sleep(5)
    print("PID " + str(os.getpid()))
    print("PPID " + str(os.getppid()))


def work():
    print('working')
    time.sleep(5)


def finish():
    print("PID " + str(os.getpid()))
    print('finished')
    time.sleep(5)


if __name__ == '__main__':
    main()
