import platform


def show_system_info():
    try:
        os_name = platform.freedesktop_os_release()["PRETTY_NAME"]
    except OSError:
        os_name = platform.system()

    print(f"OS name: {os_name}")
    print(f"OS version (kernel): {platform.release()}")
    print(f"Python version: {platform.python_version()}")


if __name__ == "__main__":
    show_system_info()
