from __future__ import annotations

from pathlib import Path

# debugging
# from time import sleep
import numpy as np

from typing_extensions import TypeAlias

RawData: TypeAlias = np.ndarray


def read_data(path: Path) -> RawData:
    map_path = []
    with open(path) as f:
        for row in f.readlines():
            row = row.replace("\n", "")
            if not row:
                continue
            map_path.append(list(row))
    return np.array(map_path)


def calculate_perimeter_per_plant(farm_map: RawData, plant_type: str) -> int:
    rows, cols = farm_map.shape

    perimeter = 0

    for row in range(rows):
        for col in range(cols):
            data_row = farm_map[row]
            data_col = farm_map.T[col]
            if data_row[col] != plant_type:
                continue

            pos_left, pos_right = col - 1, col + 1
            pos_top, pos_bottom = row - 1, row + 1

            if pos_left < 0 or data_row[pos_left] != plant_type:
                perimeter += 1

            if pos_right >= rows or data_row[pos_right] != plant_type:
                perimeter += 1

            if pos_top < 0 or data_col[pos_top] != plant_type:
                perimeter += 1

            if pos_bottom >= rows or data_col[pos_bottom] != plant_type:
                perimeter += 1

    return perimeter


def calculate_total_perimeter(farm_map: RawData) -> dict[str, int]:
    plant_types = set(sum(farm_map.tolist(), []))

    plants_perimeter = {k: 0 for k in plant_types}

    for plant_type in plant_types:
        plants_perimeter[plant_type] = calculate_perimeter_per_plant(
            farm_map, plant_type
        )

    return plants_perimeter


def calculate_area_per_plant(farm_map: RawData, plant_type: str) -> int:
    return np.argwhere(farm_map == plant_type).shape[0]


def calculate_total_area(farm_map: RawData) -> dict[str, int]:
    plant_types = set(sum(farm_map.tolist(), []))

    plants_area = {k: 0 for k in plant_types}

    for plant_type in plant_types:
        plants_area[plant_type] = calculate_area_per_plant(
            farm_map, plant_type
        )

    return plants_area


def calculate_total_price(
    perimeters: dict[str, int], areas: dict[str, int]
) -> dict[str, int]:
    plants_type = perimeters.keys()
    prices: dict[str, int] = {}

    for plant_type in plants_type:
        prices[plant_type] = perimeters[plant_type] * areas[plant_type]

    return prices


def solve_problem(farm_map: RawData) -> int:
    total_perimeters = calculate_total_perimeter(farm_map)
    total_areas = calculate_total_perimeter(farm_map)
    total_prices = calculate_total_price(total_perimeters, total_areas)

    return sum(total_prices.values())


def main_test() -> None:
    print("=" * 80)
    print("main_test")
    data = read_data(Path("data/input-test-3.txt"))

    print(data)

    expected_perimeters = {
        "O": 36,
        "X": 16,
    }
    expected_areas = {
        "O": 21,
        "X": 4,
    }

    for plant_type in expected_perimeters:  # noqa
        print(">>>", plant_type)

        result = calculate_area_per_plant(data, plant_type)
        expected = expected_areas[plant_type]
        assert result == expected, f"Result = {result}, expected = {expected}"
        print(">>>", plant_type, "area ok")

        result = calculate_perimeter_per_plant(data, plant_type)
        expected = expected_perimeters[plant_type]
        assert result == expected, f"Result = {result}, expected = {expected}"
        print(">>>", plant_type, "perimeter ok")


def main_test_2() -> None:
    print("=" * 80)
    print("main_test_2")
    data = read_data(Path("data/input-test-2.txt"))

    expected_areas = {
        "R": 12,
        "I": 0,
        "C": 0,
        "F": 10,
        "V": 13,
        "J": 11,
        "E": 13,
        "M": 5,
        "S": 3,
    }
    expected_perimeters = {
        "R": 18,
        "I": 0,
        "C": 0,
        "F": 18,
        "V": 20,
        "J": 20,
        "E": 18,
        "M": 12,
        "S": 8,
    }

    for plant_type in expected_perimeters:  # noqa
        print(">>>", plant_type)

        result = calculate_area_per_plant(data, plant_type)
        expected = expected_areas[plant_type]
        assert result == expected, f"Result = {result}, expected = {expected}"
        print(">>>", plant_type, "area ok")

        result = calculate_perimeter_per_plant(data, plant_type)
        expected = expected_perimeters[plant_type]
        assert result == expected, f"Result = {result}, expected = {expected}"
        print(">>>", plant_type, "perimeter ok")

    result = solve_problem(data)
    expected = 1930
    assert result == expected, f"Result = {result}, expected = {expected}"


def main() -> None:
    print("=" * 80)
    data = read_data(Path("data/input.txt"))
    result = solve_problem(data)
    print(result)


if __name__ == "__main__":
    main_test()
    main_test_2()
    main()
