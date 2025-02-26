from __future__ import annotations

from pathlib import Path
from typing import Any

# debugging
# from time import sleep
from typing_extensions import TypeAlias

RawData: TypeAlias = Any


def read_data(path: Path) -> RawData:
    with open(path) as f:
        return f.readlines()


def solve_problem(data: RawData) -> int:
    return 0


def main_test() -> None:
    data = read_data(Path("data/input-test.txt"))
    result = solve_problem(data)
    expected = 0
    assert result == expected, f"Result = {result}, expected = {expected}"


def main() -> None:
    data = read_data(Path("data/input.txt"))
    result = solve_problem(data)
    print(result)


if __name__ == "__main__":
    main_test()
    main()
