from __future__ import annotations

import itertools

from pathlib import Path

# debugging
# from time import sleep
from typing_extensions import TypeAlias

CalibrationLine: TypeAlias = tuple[int, list[int]]
CalibrationList: TypeAlias = list[CalibrationLine]


def read_data(path: Path) -> CalibrationList:
    def extract_calibration_line(line: str) -> CalibrationLine:
        test_value, calibration_raw = line.split(":")
        calibration = calibration_raw.strip().split(" ")
        return (int(test_value), calibration)

    with open(path) as f:
        data = [
            extract_calibration_line(v.replace("\n", ""))
            for v in f.readlines()
            if v
        ]

    return data


def gen_ops_combinations(length: int) -> list[list[str]]:
    """
    Generate all possible combinations of '*' and '+' with a given length.

    Parameters
    ----------
    length : int
        The number of characters in each combination.
    """
    return [list(comb) for comb in itertools.product("*+", repeat=length)]


def interleave_lists(l1, l2):
    """
    Interleaves two lists where l1 has one more element than l2.

    Parameters
    ----------
    l1 : list
        The first list with N elements.
    l2 : list
        The second list with N-1 elements.

    Returns
    -------
    list
        A new list with elements interleaved.
    """
    return [item for pair in zip(l1, l2) for item in pair] + [l1[-1]]


def check_calibration_line(calibration_line: CalibrationLine) -> bool:
    test_value, calibration = calibration_line
    num_ops = len(calibration) - 1
    comb_ops = gen_ops_combinations(num_ops)
    for ops in comb_ops:
        eq = interleave_lists(calibration, ops)
        partial_eq = eq[0]
        for i in range(1, len(eq), 2):
            op = eq[i]
            rhs = eq[i + 1]
            partial_eq = eval(f"{partial_eq} {op} {rhs}")
        result = test_value == partial_eq
        if result:
            return True
    return False


def solve_problem(calibration_list: CalibrationList) -> int:
    calibration_valid = []
    for calibration_line in calibration_list:
        if check_calibration_line(calibration_line):
            calibration_valid.append(calibration_line[0])
    return sum(calibration_valid)


def main_test() -> None:
    calibration_list = read_data(Path("data/input-test.txt"))

    result = solve_problem(calibration_list)
    expected = 3749
    assert result == expected, f"Result = {result}, expected = {expected}"


def main() -> None:
    calibration_list = read_data(Path("data/input.txt"))
    result = solve_problem(calibration_list)
    print(result)


if __name__ == "__main__":
    main_test()
    main()
