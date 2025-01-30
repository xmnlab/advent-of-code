from __future__ import annotations

from pathlib import Path

import numpy as np

regex = r"mul\([0-9]+,[0-9]+\)"
SEARCH_KEY = "XMAS"
SEARCH_KEY_LEN = len(SEARCH_KEY)


def read_data(path: Path) -> tuple[int, int]:
    left_ids = []
    right_ids = []

    with open(path) as f:
        return f.readlines()


def matrix_from_txt(data: list[str]) -> np.ndarray:
    matrix = np.array([list(row.strip()) for row in data if row])
    return matrix


def count_xmas_horizontally(matrix: np.ndarray) -> int:
    count = 0
    for row in matrix:
        text = "".join(row)
        count += text.count(SEARCH_KEY)
        count += text[::-1].count(SEARCH_KEY)
    return count


def count_xmas_vertically(matrix: np.ndarray) -> int:
    count = 0
    for row in matrix.T:
        text = "".join(row)
        count += text.count(SEARCH_KEY)
        count += text[::-1].count(SEARCH_KEY)
    return count


def count_xmas_diagonally(matrix: np.ndarray) -> int:
    count = 0
    mirrored_matrix = matrix[:, ::-1]

    matrix_list = [matrix, mirrored_matrix]
    for m in matrix_list:
        for k in range(-m.shape[0], m.shape[0]):
            diag = np.diag(m, k=k)

            if diag.size < SEARCH_KEY_LEN:
                continue

            text = "".join(diag)
            count += text.count(SEARCH_KEY)
            count += text[::-1].count(SEARCH_KEY)
    return count


def count_xmas_occurrences(matrix: np.ndarray):
    return (
        count_xmas_horizontally(matrix)
        + count_xmas_vertically(matrix)
        + count_xmas_diagonally(matrix)
    )


def main_test() -> None:
    data = read_data(Path("data/input-test.txt"))
    matrix = matrix_from_txt(data)

    result = count_xmas_horizontally(matrix)
    expected = 5
    assert result == expected, f"Result = {result}, expected = {expected}"

    result = count_xmas_vertically(matrix)
    expected = 3
    assert result == expected, f"Result = {result}, expected = {expected}"

    result = count_xmas_diagonally(matrix)
    expected = 10
    assert result == expected, f"Result = {result}, expected = {expected}"

    result = count_xmas_occurrences(matrix)
    expected = 18
    assert result == expected, f"Result = {result}, expected = {expected}"


def main() -> None:
    data = read_data(Path("data/input.txt"))
    matrix = matrix_from_txt(data)
    print(count_xmas_occurrences(matrix))


if __name__ == "__main__":
    main_test()
    main()
