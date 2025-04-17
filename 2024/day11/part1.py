from __future__ import annotations

from pathlib import Path

# debugging
# from time import sleep
from typing_extensions import TypeAlias

RawData: TypeAlias = list[str]


def read_data(path: Path) -> RawData:
    stone_state: list[int] = []
    with open(path) as f:
        stone_state = list(map(int, f.read().strip().split(" ")))
    return stone_state


def change_after_blink(stone_state: RawData) -> int:
    new_stone_state = []

    for stone in stone_state:
        if stone == 0:
            new_stone_state.append(1)
        elif len(str(stone)) % 2 == 0:
            stone_str = str(stone)
            idx = len(stone_str) // 2
            lhs = int(stone_str[:idx])
            rhs = int(stone_str[idx:])
            new_stone_state.append(lhs)
            new_stone_state.append(rhs)
        else:
            new_stone_state.append(stone * 2024)

    return new_stone_state


def change_after_multiple_blinks(
    stone_state: RawData, total_blinks: int = 1
) -> list[int]:
    for x in range(total_blinks):
        stone_state = change_after_blink(stone_state)
    return stone_state


def solve_problem(stone_state: RawData, total_blinks: int = 1) -> int:
    stone_state = change_after_multiple_blinks(stone_state, total_blinks)
    return len(stone_state)


def main_test() -> None:
    data = read_data(Path("data/input-test.txt"))
    assert data == [125, 17]

    result = change_after_multiple_blinks(data, 1)
    expected = [253000, 1, 7]
    assert result == expected, f"Result = {result}, expected = {expected}"

    result = change_after_multiple_blinks(data, 2)
    expected = [253, 0, 2024, 14168]
    assert result == expected, f"Result = {result}, expected = {expected}"

    result = change_after_multiple_blinks(data, 3)
    expected = [512072, 1, 20, 24, 28676032]
    assert result == expected, f"Result = {result}, expected = {expected}"

    result = change_after_multiple_blinks(data, 4)
    expected = [512, 72, 2024, 2, 0, 2, 4, 2867, 6032]
    assert result == expected, f"Result = {result}, expected = {expected}"

    result = change_after_multiple_blinks(data, 5)
    expected = [1036288, 7, 2, 20, 24, 4048, 1, 4048, 8096, 28, 67, 60, 32]
    assert result == expected, f"Result = {result}, expected = {expected}"

    result = change_after_multiple_blinks(data, 6)
    expected = [
        2097446912,
        14168,
        4048,
        2,
        0,
        2,
        4,
        40,
        48,
        2024,
        40,
        48,
        80,
        96,
        2,
        8,
        6,
        7,
        6,
        0,
        3,
        2,
    ]
    assert result == expected, f"Result = {result}, expected = {expected}"

    result = solve_problem(data, 6)
    expected = 22
    assert result == expected, f"Result = {result}, expected = {expected}"


def main() -> None:
    data = read_data(Path("data/input.txt"))
    result = solve_problem(data, 25)
    print(result)


if __name__ == "__main__":
    main_test()
    main()
