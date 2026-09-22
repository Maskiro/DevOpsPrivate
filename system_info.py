import getpass
import platform
OS = platform.system()
Kernel = platform.release()
username = getpass.getuser()
print("Имя:" + username)
print("Система:" + OS)
print("Версия ядра:" + Kernel)