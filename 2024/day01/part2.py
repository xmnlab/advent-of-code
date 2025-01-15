from __future__ import annotations

from pathlib import Path


def read_data(path: Path) -> tuple[list[int], list[int]]:
    left_ids = []
    right_ids = []

    with open(path) as f:
        for values in f.readlines():
            if not values:
                continue

            l, r = values.split()

            left_ids.append(int(l))
            right_ids.append(int(r))

        return sorted(left_ids), sorted(right_ids)


def calc_similarity_score(left_ids, right_ids) -> int:
    return sum([l * right_ids.count(l) for l in left_ids])

def main_test() -> None:
    left_ids, right_ids = read_data(Path("input-test.txt"))
    assert calc_similarity_score(left_ids, right_ids) == 31


def main() -> None:
    left_ids, right_ids = read_data(Path("input.txt"))
    print(calc_similarity_score(left_ids, right_ids))


if __name__ == "__main__":
    main_test()
    main()
