import sys
from subprocess import check_call

from colorama import Fore, Style


def test() -> None:
    print(Fore.CYAN + "Test with pytest")
    pytest_args = [
        "pytest",
        "--cov-report=xml",
        "--cov-fail-under=80",
        "--cov=src",
        "tests/",
    ]

    args: list[str] = sys.argv[1:]
    if "nofail" in args:
        print("Running tests without failing if under coverage")
        pytest_args: list[str] = [
            "pytest",
            "--cov-report=xml",
            "--cov=src",
            "tests/",
        ]

    check_call(pytest_args)
    print(Style.RESET_ALL)
