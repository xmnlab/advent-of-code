from __future__ import annotations

import re

from pathlib import Path

import numpy as np

from numpy.lib.stride_tricks import sliding_window_view


regex = r"mul\([0-9]+,[0-9]+\)"
SEARCH_KEY = "MAS"
SEARCH_KEY_LEN = len(SEARCH_KEY)


def read_data(path: Path) -> tuple[int, int]:
    left_ids = []
    right_ids = []

    with open(path) as f:
        return f.readlines()


def matrix_from_txt(data: list[str]) -> np.ndarray:
    matrix = np.array(
        [list(row.strip()) for row in data if row]
    )
    return matrix


def count_x_mas_diagonally(kernel: np.ndarray) -> int:
    count = 0
    mirrored_kernel = kernel[:, ::-1]

    kernel_list = [kernel, mirrored_kernel]
    for m in kernel_list:
        diag = np.diag(m)

        text = "".join(diag)
        count += text.count(SEARCH_KEY)
        count += text[::-1].count(SEARCH_KEY)
    return count


def count_x_mas_occurrences(matrix: np.ndarray):
    # Kernel size
    N = M = SEARCH_KEY_LEN

    # Generate sliding windows
    windows = sliding_window_view(matrix, (N, M))

    # Iterate over the kernels
    count = 0
    for i in range(windows.shape[0]):
        for j in range(windows.shape[1]):
            kernel = windows[i, j]
            c = count_x_mas_diagonally(kernel)
            # 2 == both direction
            if c == 2:
                count += 1
    return count


def main_test() -> None:
    data = read_data(Path("data/input-test.txt"))
    matrix = matrix_from_txt(data)

    result = count_x_mas_occurrences(matrix)
    expected = 9
    assert result == expected, f"Result = {result}, expected = {expected}"


def main() -> None:
    data = read_data(Path("data/input.txt"))
    matrix = matrix_from_txt(data)
    print(count_x_mas_occurrences(matrix))


if __name__ == "__main__":
    main_test()
    main()
