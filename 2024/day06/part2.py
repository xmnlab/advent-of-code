from __future__ import annotations

from copy import copy
from pathlib import Path

# debugging
from time import sleep
from typing import Optional

import numpy as np

from typing_extensions import TypeAlias

LabMap: TypeAlias = np.ndarray
CoordMap: TypeAlias = tuple[int, int]

# DIRECTIONS
DIR_NORTH = "^"
DIR_SOUTH = "v"
DIR_WEST = "<"
DIR_EAST = ">"

DIRECTIONS = [
    DIR_NORTH,
    DIR_EAST,
    DIR_SOUTH,
    DIR_WEST,
]


def read_data(path: Path) -> LabMap:
    with open(path) as f:
        data = [v.replace("\n", "") for v in f.readlines()]

    return np.array([list(row) for row in data if row])


def get_direction(lab_map: LabMap) -> str:
    for d in DIRECTIONS:
        count = int(np.char.count(lab_map, d).sum())
        if count:
            return d


def get_current_position(lab_map: LabMap) -> CoordMap:
    direction = get_direction(lab_map)
    mask = np.char.find(lab_map, direction) != -1
    indices = np.argwhere(mask)
    return tuple(indices[0].tolist())


def is_path_blocked(lab_map: LabMap, position: CoordMap) -> bool:
    # uses try/except for the case when the position is off of the map
    try:
        return bool(lab_map[position] == "#")
    except:
        return False


def is_off_of_map(lab_map: LabMap, position: CoordMap) -> bool:
    max_shape = np.array([v - 1 for v in lab_map.shape])
    min_shape = np.array([0, 0])
    arr_pos = np.array(position)

    return any(arr_pos > max_shape) or any(arr_pos < min_shape)


def rotate_dir_90_degrees(dir) -> str:
    idx = DIRECTIONS.index(dir) + 1
    new_idx = idx if idx < len(DIRECTIONS) else 0
    return DIRECTIONS[new_idx]


def calc_next_position(
    cur_pos: tuple[int, int], dir: str
) -> Optional[tuple[int, int]]:
    _next_pos = list(copy(cur_pos))

    if dir == DIR_NORTH:
        _next_pos[0] = _next_pos[0] - 1
    elif dir == DIR_SOUTH:
        _next_pos[0] = _next_pos[0] + 1
    elif dir == DIR_WEST:
        _next_pos[1] = _next_pos[1] - 1
    else:
        _next_pos[1] = _next_pos[1] + 1

    return tuple(_next_pos)


def get_next_position(lab_map: LabMap) -> Optional[tuple[CoordMap, str]]:
    cur_pos = get_current_position(lab_map)
    dir = str(lab_map[cur_pos])

    for turns in range(2):
        next_pos = calc_next_position(cur_pos, dir)

        if not is_path_blocked(lab_map, next_pos):
            return next_pos, dir

        dir = rotate_dir_90_degrees(dir)

    # no possible movement
    return None


def move_guard(
    lab_map: LabMap,
    position: CoordMap,
    dir: str,
) -> LabMap:
    path_map = copy(lab_map)
    cur_pos = get_current_position(path_map)

    if dir in ["^", "v"]:
        mark = "|"
    elif dir in ["<", ">"]:
        mark = "-"
    else:
        mark = "+"

    path_map[cur_pos] = mark
    path_map[position] = dir
    # debugging
    print("=" * 80)
    print(path_map)
    sleep(0.2)
    return path_map


def trace_guard_path(lab_map: LabMap) -> LabMap:
    path_map = copy(lab_map)

    next_position, dir = get_next_position(path_map)
    current_position = next_position

    while next_position is not None:
        path_map = move_guard(path_map, current_position, dir)
        next_position, dir = get_next_position(path_map)

        if is_off_of_map(lab_map, next_position):
            path_map[current_position] = "X"
            break

        current_position = next_position
    return path_map


def is_path_in_loop(lab_map: LabMap) -> bool:
    return False


def solve_path(lab_map: LabMap) -> tuple[LabMap, int]: ...


def solve_problem(lab_map: LabMap) -> tuple[LabMap, int]:
    solve_path = trace_guard_path(lab_map)
    counter = is_path_in_loop(path_map)
    return path_map, counter


def main_test() -> None:
    lab_map = read_data(Path("data/input-test.txt"))
    counter = solve_problem(lab_map)
    expected_counter = 6

    assert counter == expected_counter, (
        f"Result = {counter}, expected = {expected_counter}"
    )


def main() -> None:
    lab_map = read_data(Path("data/input.txt"))
    _, counter = solve_problem(lab_map)
    print(counter)


if __name__ == "__main__":
    main_test()
    main()
