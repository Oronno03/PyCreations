import os
import shutil
import sys
import pathlib
from colorama import Fore


print(Fore.GREEN + "=" * 30)
print(f"{Fore.LIGHTCYAN_EX}Welcome to File Organizer".center(30))
print(Fore.GREEN + "=" * 30)
print("This is a simple file organizer, it Takes a directory path and organizes")
print("the files inside that directory according to the extensions of the files.")
input(f"{Fore.YELLOW}Press Enter to continue{Fore.WHITE}")

path = input(f"[{Fore.CYAN}+{Fore.WHITE}] {Fore.GREEN}Enter path:{Fore.WHITE} ")


try:
    path = pathlib.Path.home() / path
    files = os.listdir(path)
    print(f"{Fore.GREEN}Successfully found the path, here are ")
except Exception:
    print(
        f"[{Fore.RED}!{Fore.WHITE}] {Fore.RED}Could not find the path. Please run the program again."
    )
    sys.exit(1)

for file in files:
    filename, extension = os.path.splitext(file)
    extension = extension[1:]

    if not os.path.exists(f"{path}\\{extension}"):
        os.mkdir(f"{path}\\{extension}")
    shutil.move(f"{path}\\{file}", f"{path}\\{extension}\\{file}")

print(f"{Fore.GREEN}[*] Successfully organized the files")
input(f"{Fore.RED}Press enter to exit")
