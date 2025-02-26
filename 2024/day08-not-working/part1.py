from __future__ import annotations

from pathlib import Path

import numpy as np


# debugging
# from time import sleep
from typing_extensions import TypeAlias

Map: TypeAlias = np.ndarray


def read_data(path: Path) -> Map:
    with open(path) as f:
        data = [list(v.replace("\n", "")) for v in f.readlines() if v]

    return np.array(data)


def locate_antinodes(map: Map) -> Map:
    return map


def solve_problem(map: Map) -> int:
    antinodes_map = locate_antinodes(map)
    return np.char.count(map, "#").sum()


def main_test() -> None:
    map = read_data(Path("data/input-test.txt"))

    result = solve_problem(map)
    expected = 13
    assert result == expected, f"Result = {result}, expected = {expected}"


def main() -> None:
    map = read_data(Path("data/input.txt"))
    result = solve_problem(map)
    print(result)


if __name__ == "__main__":
    main_test()
    main()
