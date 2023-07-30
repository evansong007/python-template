import os

from colorama import Fore, Style


def type() -> None:
    print(Fore.LIGHTYELLOW_EX + "Type check with pyright")
    status: int = os.system(
        "yarn global list --patern | grep -c -q 'pyright'"
    ) and os.system("npm list -g --depth=0 | grep -c -q 'pyright'")
    if status != 0:
        print("Please install Pyright globally via npm or yarn")
        print(Style.RESET_ALL)
        quit()

    os.system("pyright")
    print(Style.RESET_ALL)
