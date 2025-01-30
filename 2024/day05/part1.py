from __future__ import annotations

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


def get_valid_pages_sq(
    rules: list[tuple[int, ...]],
    pages_sq: list[tuple[int, ...]],
) -> list[tuple[int, ...]]:
    sorted_pages_sq = []

    for pages in pages_sq:
        if check_valid_pages(rules, pages):
            sorted_pages_sq.append(pages)

    return sorted_pages_sq


def count_middle_page_from_correct_sequence(
    rules: list[tuple[int, ...]],
    pages_sq: list[tuple[int, ...]],
) -> int:
    valid_pages_sq = get_valid_pages_sq(rules, pages_sq)
    middle_pages = []
    for pages in valid_pages_sq:
        n_pages = len(pages)
        middle_page_idx = ((n_pages // 2) + n_pages % 2) - 1
        middle_pages.append(pages[middle_page_idx])

    return sum(middle_pages)


def main_test() -> None:
    data = read_data(Path("data/input-test.txt"))
    rules = data["rules"]
    pages_sq = data["pages_sq"]

    result = get_valid_pages_sq(rules, pages_sq)
    expected = [(75, 47, 61, 53, 29), (97, 61, 53, 29, 13), (75, 29, 13)]
    assert result == expected, f"Result = {result}, expected = {expected}"

    result = count_middle_page_from_correct_sequence(rules, pages_sq)
    expected = 143
    assert result == expected, f"Result = {result}, expected = {expected}"


def main() -> None:
    data = read_data(Path("data/input.txt"))
    rules = data["rules"]
    pages_sq = data["pages_sq"]

    valid_pages = get_valid_pages_sq(rules, pages_sq)
    assert valid_pages

    print(count_middle_page_from_correct_sequence(rules, pages_sq))


if __name__ == "__main__":
    main_test()
    main()
