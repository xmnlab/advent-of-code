from __future__ import annotations

from copy import copy
from pathlib import Path


def read_data(path: Path) -> dict[str, list[tuple[int, ...]]]:
    with open(path) as f:
        data = [v.replace("\n", "") for v in f.readlines()]

    rules = [tuple(map(int, v.split("|"))) for v in data[: data.index("")]]
    pages_sq = [
        tuple(map(int, v.split(","))) for v in data[data.index("") :] if v
    ]
    return {
        "rules": rules,
        "pages_sq": pages_sq,
    }


def check_valid_pages(
    rules: list[tuple[int, ...]],
    pages: tuple[int, ...],
) -> bool:
    n_pages = len(pages)
    results = []
    for i in range(n_pages - 1):
        j = i + 1
        result = (pages[i], pages[j]) in rules
        results.append(result)
    return all(results)


def fix_pages_order(
    rules: list[tuple[int, ...]],
    pages: tuple[int, ...],
) -> tuple[int, ...]:
    ordered_pages = list(copy(pages))
    n_pages = len(pages)
    is_sorted = False

    while not is_sorted:
        is_sorted = True
        for i in range(n_pages - 1):
            j = i + 1
            val_i = ordered_pages[i]
            val_j = ordered_pages[j]
            if (val_i, val_j) in rules:
                continue
            ordered_pages[i], ordered_pages[j] = val_j, val_i
            is_sorted = False

    return tuple(ordered_pages)


def get_invalid_pages_sq(
    rules: list[tuple[int, ...]],
    pages_sq: list[tuple[int, ...]],
) -> list[tuple[int, ...]]:
    sorted_pages_sq = []

    for pages in pages_sq:
        if not check_valid_pages(rules, pages):
            sorted_pages_sq.append(pages)

    return sorted_pages_sq


def count_middle_page_from_incorrect_sequence(
    rules: list[tuple[int, ...]],
    pages_sq: list[tuple[int, ...]],
) -> int:
    invalid_pages_sq = get_invalid_pages_sq(rules, pages_sq)
    middle_pages = []
    for pages in invalid_pages_sq:
        fixed_pages = fix_pages_order(rules, pages)
        n_pages = len(fixed_pages)
        middle_page_idx = ((n_pages // 2) + n_pages % 2) - 1
        middle_pages.append(fixed_pages[middle_page_idx])

    return sum(middle_pages)


def main_test() -> None:
    data = read_data(Path("data/input-test.txt"))
    rules = data["rules"]
    pages_sq = data["pages_sq"]

    result = count_middle_page_from_incorrect_sequence(rules, pages_sq)
    expected = 123
    assert result == expected, f"Result = {result}, expected = {expected}"


def main() -> None:
    data = read_data(Path("data/input.txt"))
    rules = data["rules"]
    pages_sq = data["pages_sq"]

    valid_pages = get_invalid_pages_sq(rules, pages_sq)
    assert valid_pages

    print(count_middle_page_from_incorrect_sequence(rules, pages_sq))


if __name__ == "__main__":
    main_test()
    main()
