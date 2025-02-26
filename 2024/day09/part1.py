from __future__ import annotations

from copy import copy
from itertools import batched  # python>=3.12
from pathlib import Path
from typing import List

# debugging
# from time import sleep
from typing_extensions import TypeAlias

RawData: TypeAlias = List[int]
DiskMap: TypeAlias = List[str]


def create_disk_map(raw_data: RawData) -> DiskMap:
    disk_map = []

    chunks = list(batched(raw_data[:-1], 2))
    n_chunks = len(chunks)

    for i, disk_pair in enumerate(chunks):
        disk_map.extend([str(i)] * disk_pair[0])
        disk_map.extend(["."] * disk_pair[1])
    last_file = raw_data[-1]
    disk_map.extend([str(n_chunks)] * last_file)
    return disk_map


def read_data(path: Path) -> DiskMap:
    with open(path) as f:
        line = list(f.readlines()[0].replace("\n", "").strip())
    return create_disk_map([int(v) for v in line])


def is_defrag_complete(data: DiskMap) -> bool:
    total_spaces = len(data)
    total_free = data.count(".")
    first_idx = data.index(".")
    return total_spaces - total_free == first_idx


def defrag(data: DiskMap) -> DiskMap:
    data = copy(data)
    size = len(data)

    for i in range(size):
        if is_defrag_complete(data):
            break

        if data[i] != ".":
            continue

        for j in range(size - 1, 0, -1):
            if data[j] == ".":
                continue

            data[i], data[j] = data[j], data[i]
            break

    return data


def checksum(data: DiskMap) -> int:
    try:
        last_block = data.index(".")
    except Exception:
        return 0

    result = [i * int(v) for i, v in enumerate(data[:last_block])]

    return sum(result)


def solve_problem(data: DiskMap) -> int:
    defragmented = defrag(data)
    return checksum(defragmented)


def main_test() -> None:
    data = read_data(Path("data/input-test.txt"))

    result = data
    expected = list("0..111....22222")
    assert result == expected, f"Result = {result}, expected = {expected}"

    result = defrag(data)
    expected = list("022111222......")
    assert result == expected, f"Result = {result}, expected = {expected}"

    result = solve_problem(data)
    expected = 60
    assert result == expected, f"Result = {result}, expected = {expected}"


def main() -> None:
    data = read_data(Path("data/input.txt"))
    result = solve_problem(data)
    print(result)


if __name__ == "__main__":
    main_test()
    main()
