from subprocess import check_call

from colorama import Fore, Style


def requirements() -> None:
    print(Fore.LIGHTGREEN_EX + "Updating requirements.txt")
    check_call(
        ["poetry", "export", "-f", "requirements.txt", "--output", "requirements.txt"]
    )
    print(Style.RESET_ALL)
