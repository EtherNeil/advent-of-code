"""Advent of Code 2025 - Day 8: Playground"""

import argparse
import sys


def parse_args() -> tuple[int, list[list[str]]]:
    """Analyze command line arguments."""
    parser = argparse.ArgumentParser(
        description="Advent of Code 2025 - Day 8: Playground"
    )
    parser.add_argument(
        "--star",
        type=int,
        choices=[1, 2],
        default=1,
        help="Choose which star to solve (1 or 2)",
    )
    parser.add_argument(
        "--input",
        type=str,
        default="2025/8/test.txt",
        help="Path to the input file",
    )

    args = parser.parse_args()

    try:
        with open(args.input, "r", encoding="utf-8") as file:
            data = [
                tuple(map(int, line.strip().split(","))) for line in file.readlines()
            ]
    except FileNotFoundError:
        print(f"Error: The file '{args.input}' does not exist.")
        sys.exit(1)

    return args.star, data


def euclidean_distance(
    point1: tuple[int, int, int], point2: tuple[int, int, int]
) -> float:
    """Calculate the Euclidean distance between two 3D points."""
    return (
        (point1[0] - point2[0]) ** 2
        + (point1[1] - point2[1]) ** 2
        + (point1[2] - point2[2]) ** 2
    ) ** 0.5


def first_star(lines: list[tuple[int, int, int]]) -> None:
    """Solve the first star."""
    dict_of_distances = {}
    for _ in range(len(lines)):
        point = lines.pop(0)
        for other_point in lines:
            distance = euclidean_distance(point, other_point)
            dict_of_distances[(point, other_point)] = distance


def second_star(lines: list[tuple[int, int, int]]) -> None:
    """Solve the second star."""
    print("Second star solution not implemented yet.")


if __name__ == "__main__":
    star, input_data = parse_args()
    if star == 1:
        first_star(input_data)
    elif star == 2:
        second_star(input_data)
