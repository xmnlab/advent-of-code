from __future__ import annotations

from pathlib import Path


def read_data(path: Path) -> list[list[int]]:
    result = []
    with open(path) as f:
        for row in f.readlines():
            result.append([int(v) for v in row.split()])
    return result


def _check_report_safety(row: list[int]) -> bool:
    if row[1] == row[0]:
        return False

    factor = row[1] > row[0]

    for i in range(len(row) -1):
        v0 = row[i]
        next_i = i + 1

        if v0 == row[next_i]:
            return False

        if abs(v0 - row[next_i]) > 3:
            return False

        factor_result = row[next_i] > v0

        if factor != factor_result:
            return False

    return True


def check_total_safe_reports(data: list[list[int]]) -> int:
    total_safe: list[bool] = []
    for row in data:
        total_safe.append(_check_report_safety(row))
    return sum(total_safe)


def main_test() -> None:
    data = read_data(Path("input-test.txt"))
    assert check_total_safe_reports(data) == 2


def main() -> None:
    data = read_data(Path("input.txt"))
    print(check_total_safe_reports(data))


if __name__ == "__main__":
    main_test()
    main()
