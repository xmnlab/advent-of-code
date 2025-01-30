from __future__ import annotations

import re

from pathlib import Path

regex = r"mul\([0-9]+,[0-9]+\)|don't\(\)|do\(\)"


def read_data(path: Path) -> tuple[int, int]:
    left_ids = []
    right_ids = []

    with open(path) as f:
        return f.readlines()


def mul(x: int, y: int) -> int:
    return x * y


def extract_valid_terms(data) -> list[int]:
    results = []
    for line in data:
        result_line = []
        matches = re.finditer(regex, line)
        for match in matches:
            result_line.append(match.group())
        results.append(result_line)

    return results


def process_terms(data) -> int:
    valid_terms = extract_valid_terms(data)
    results = []
    do_flag = True
    for line in valid_terms:
        line_eval = []
        for term in line:
            if term == "do()":
                do_flag = True
                continue

            if term == "don't()":
                do_flag = False
                continue

            if do_flag:
                line_eval.append(eval(term))

        results.append(sum(line_eval))
    return sum(results)


def main_test() -> None:
    data = read_data(Path("input-test-2.txt"))
    result = process_terms(data)
    expected = 48
    assert result == expected, f"Expected={expected}, result={result}"


def main() -> None:
    data = read_data(Path("input.txt"))
    print(process_terms(data))


if __name__ == "__main__":
    main_test()
    main()
