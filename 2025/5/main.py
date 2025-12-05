"""Advent of Code 2025 - Day 5: Cafeteria"""

import argparse
import sys


def parse_args() -> tuple[int, list[str]]:
    """Analyze command line arguments."""
    parser = argparse.ArgumentParser(
        description="Advent of Code 2025 - Day 5: Cafeteria"
    )
    parser.add_argument(
        "--star",
        type=int,
        choices=[1, 2],
        default=2,
        help="Choose which star to solve (1 or 2)",
    )
    parser.add_argument(
        "--input",
        type=str,
        default="2025/5/test.txt",
        help="Path to the input file",
    )

    args = parser.parse_args()

    try:
        with open(args.input, "r", encoding="utf-8") as file:
            data = [line.strip() for line in file.readlines()]
    except FileNotFoundError:
        print(f"Error: The file '{args.input}' does not exist.")
        sys.exit(1)

    return args.star, data


def first_star(lines: list[str]) -> None:
    """Solve the first star."""
    separator_index = lines.index("")
    fresh_ingredient_id_ranges = [
        tuple(map(int, range.split("-"))) for range in lines[0:separator_index]
    ]
    available_ingredients_ids = [int(i) for i in lines[separator_index + 1 :]]
    fresh_ingredient_ids = dict(
        (
            ingredient_id,
            [
                corresponding_range
                for corresponding_range in fresh_ingredient_id_ranges
                if corresponding_range[0] <= ingredient_id <= corresponding_range[1]
            ],
        )
        for ingredient_id in available_ingredients_ids
    )
    for ingredient_id, corresponding_ranges in fresh_ingredient_ids.items():
        if not corresponding_ranges:
            print(
                f"ID {ingredient_id} is spoiled because it does not fall into any range."
            )
        else:
            print(
                f"ID {ingredient_id} is fresh because it falls into ranges {corresponding_ranges}."
            )
    count_fresh_ingredients = sum(
        1 for ranges in fresh_ingredient_ids.values() if ranges
    )
    print(f"{count_fresh_ingredients} of the available ingredient IDs are fresh.")


def combine_ranges(
    range1: tuple[int, int], range2: tuple[int, int]
) -> tuple[int, int] | None:
    """Combine two ranges if they overlap or are contiguous."""
    if range1[1] + 1 < range2[0] or range2[1] + 1 < range1[0]:
        return None
    return (min(range1[0], range2[0]), max(range1[1], range2[1]))


def second_star(ranges: list[str]) -> None:
    """Solve the second star."""
    ingredient_ranges = [
        tuple(map(int, range.split("-"))) for range in ranges[0 : ranges.index("")]
    ]
    ingredient_ranges.sort()
    combined_ingredient_ranges = []
    while len(ingredient_ranges) > 0:
        current_range = ingredient_ranges.pop(0)
        removed_ranges = []
        for other_range in ingredient_ranges:
            combined_range = combine_ranges(current_range, other_range)
            if combined_range is not None:
                current_range = combined_range
                removed_ranges.append(other_range)
        ingredient_ranges = [
            range for range in ingredient_ranges if range not in removed_ranges
        ]
        combined_ingredient_ranges.append(current_range)
    number_of_fresh_ingredients = sum(
        range[1] - range[0] + 1 for range in combined_ingredient_ranges
    )
    print(f"The total number of fresh ingredient IDs is {number_of_fresh_ingredients}.")


if __name__ == "__main__":
    star, input_data = parse_args()
    if star == 1:
        first_star(input_data)
    if star == 2:
        second_star(input_data)
