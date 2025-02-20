from os import system as os_system
from platform import system as platform_system

def clear_terminal() -> None:
    os_system("cls" if platform_system() == "Windows" else "clear")
    