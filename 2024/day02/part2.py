from __future__ import annotations

import copy

from pathlib import Path


def read_data(path: Path) -> list[list[int]]:
    result = []
    with open(path) as f:
        for row in f.readlines():
            result.append([int(v) for v in row.split()])
    return result


def check_status(v0: int, v1: int, factor: int) -> bool:
    status = True

    if v0 == v1:
        status = False

    if abs(v0 - v1) > 3:
        status = False

    factor_result = v1 > v0

    return status and (factor == factor_result)


def check_report_safety(row: list[int]) -> bool:
    total_levels = len(row)
    total_levels_check = total_levels - 1

    factor = row[1] > row[0]

    for i in range(total_levels_check):
        next_i = i + 1
        v0 = row[i]
        v1 = row[next_i]
        status = check_status(v0, v1, factor)
        if not status:
            return False
    return True


def check_report_safety_combination(row: list[int]) -> bool:
    initial_status = check_report_safety(row)

    if initial_status:
        return True

    total_levels = len(row)

    for unsafe_level_id in range(total_levels):
        new_row = copy.copy(row)
        new_row.pop(unsafe_level_id)

        report_status = check_report_safety(new_row)

        if report_status:
            return True

    return False


def check_total_safe_reports(data: list[list[int]]) -> int:
    total_safe = []
    for row in data:
        total_safe.append(check_report_safety_combination(row))
    return sum(total_safe)


def main_test() -> None:
    data = read_data(Path("input-test.txt"))
    result = check_total_safe_reports(data)
    expected = 4
    assert result == expected, f"Expected {expected}, but result is {result}"


def main() -> None:
    print("=" * 80)
    data = read_data(Path("input.txt"))
    print(check_total_safe_reports(data))


if __name__ == "__main__":
    main_test()
    main()
