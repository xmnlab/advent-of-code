from __future__ import annotations

from pathlib import Path


def read_data(path: Path) -> tuple[int, int]:
    left_ids = []
    right_ids = []

    with open(path) as f:
        for values in f.readlines():
            if not values:
                continue

            l, r = values.split()
            left_ids.append(int(l))
            right_ids.append(int(r))
        return tuple(zip(sorted(left_ids), sorted(right_ids)))


def calc_distance(data) -> int:
    return sum([abs(v[0] - v[1]) for v in data])

def main_test() -> None:
    data = read_data(Path("input-test.txt"))
    assert calc_distance(data) == 11


def main() -> None:
    data = read_data(Path("input.txt"))
    print(calc_distance(data))


if __name__ == "__main__":
    main_test()
    main()
