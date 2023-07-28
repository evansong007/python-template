import importlib
import json
import sys
from typing import Any

from colorama import Fore, Style


def openapi() -> None:
    check: bool = len(sys.argv) == 2 and sys.argv[1] == "--check"
    spec = _get_spec()

    if check:
        _check_openapi(spec)
    else:
        _generate_openapi(spec)

    print(Style.RESET_ALL)


def _get_spec():
    mod = importlib.import_module("src.app.main")
    app = getattr(mod, "app")
    spec = app.openapi()

    return spec


def _check_openapi(spec: Any) -> None:
    print(Fore.LIGHTMAGENTA_EX + "Checking openapi.json is up do date")

    with open("openapi.json", "r") as spec_file:
        current_spec = json.load(spec_file)

    if current_spec == spec:
        print(Fore.GREEN + "\nSpec matches")
    else:
        print(
            Fore.RED
            + "\nSpec is not up to date. Generate it by running poetry run openapi"
        )
        sys.exit(1)


def _generate_openapi(spec: Any) -> None:
    print(Fore.LIGHTMAGENTA_EX + "Generating openapi.json")

    with open("openapi.json", "w") as spec_file:
        json.dump(spec, spec_file)
