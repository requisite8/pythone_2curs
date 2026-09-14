import os, sys, platform, datetime, time, math

os_name = platform.system()
os_version = platform.version()
os_arch = platform.architecture()[0]
now = datetime.datetime.now()

sys_in = sys.path
print(f"{os_name}, {os_version}, {os_arch}, {now}, {sys_in}")

os_processor = platform.processor()
print(f"{os_processor}")

user = os.environ.get("USERNAME") or os.environ.get("USER")
print(f"{user}")

a = int(input("Напиши число и узнаешь его корень, факториал числа, степень, модуль"))

print(f'Math: корень: {math.sqrt(a)}, {math.factorial(a)}, {math.pow(a, a)}, {math.fabs(a)}')

while