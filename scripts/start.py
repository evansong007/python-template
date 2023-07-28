from subprocess import check_call

from colorama import Fore, Style


def start() -> None:
    print(Fore.LIGHTCYAN_EX + "Starting src")
    check_call(
        [
            "uvicorn",
            "src.app.main:app",
            "--no-server-header",
            "--reload",
        ]
    )
    print(Style.RESET_ALL)
