from __future__ import annotations

from pathlib import Path

# debugging
# from time import sleep
import numpy as np

from typing_extensions import Iterable, TypeAlias

RawData: TypeAlias = np.ndarray


def read_data(path: Path) -> RawData:
    map_path = []
    with open(path) as f:
        for row in f.readlines():
            row = row.replace("\n", "")
            if not row:
                continue
            map_path.append(list(map(int, row)))
    return np.array(map_path)


def identify_headtrails(data: RawData) -> Iterable[int]:
    return np.argwhere(data == 0)


def solve_problem(data: RawData) -> int:
    return 0


def main_test() -> None:
    data = read_data(Path("data/input-test.txt"))
    assert data.shape == (8, 8)

    headtrails = identify_headtrails(data)
    assert len(headtrails) == 9
    assert headtrails == [
        (0, 2),
        (0, 4),
        (2, 4),
        (4, 6),
        (5, 2),
        (5, 5),
        (6, 0),
        (6, 6),
        (7, 1),
    ]
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
