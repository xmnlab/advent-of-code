from __future__ import annotations

import re

from pathlib import Path

regex = r"mul\([0-9]+,[0-9]+\)"


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
    for line in valid_terms:
        line_eval = [eval(term) for term in line]
        results.append(sum(line_eval))
    return sum(results)


def main_test() -> None:
    data = read_data(Path("input-test.txt"))
    assert process_terms(data) == 161


def main() -> None:
    data = read_data(Path("input.txt"))
    print(process_terms(data))


if __name__ == "__main__":
    main_test()
    main()
