"""Advent of Code 2025 - Day 7: Laboratories"""

import argparse
import sys


def parse_args() -> tuple[int, list[list[str]]]:
    """Analyze command line arguments."""
    parser = argparse.ArgumentParser(
        description="Advent of Code 2025 - Day 7: Laboratories"
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
        default="2025/7/test.txt",
        help="Path to the input file",
    )

    args = parser.parse_args()

    try:
        with open(args.input, "r", encoding="utf-8") as file:
            data = [[char for char in line.strip()] for line in file.readlines()]
    except FileNotFoundError:
        print(f"Error: The file '{args.input}' does not exist.")
        sys.exit(1)

    return args.star, data


def display_lines(lines: list[list[str]]) -> None:
    """Display lines."""
    for line in lines:
        print("".join(line))


def first_star(lines: list[list[str]]) -> None:
    """Solve the first star."""
    counter = 0
    for y in range(1, len(lines)):
        for x in range(len(lines[y])):
            if lines[y - 1][x] == "S" and lines[y][x] == ".":
                lines[y][x] = "|"
            if lines[y - 1][x] == "|" and lines[y][x] == ".":
                lines[y][x] = "|"
            if lines[y - 1][x] == "|" and lines[y][x] == "^":
                counter += 1
                lines[y][x - 1] = "|" if lines[y][x - 1] == "." else lines[y][x - 1]
                lines[y][x + 1] = "|" if lines[y][x + 1] == "." else lines[y][x + 1]
    display_lines(lines)
    print(f"Result for the first star: {counter}")


def count_paths(l: list[list[str]], k: tuple[int, int], m: dict | None = None) -> int:
    """Count paths from `current` to the bottom following problem rules."""
    if m is None:
        m = {}

    x, y = k
    if k in m:
        return m[k]

    height = len(l)
    width = len(l[0]) if height > 0 else 0

    if y + 1 >= height:
        m[k] = 1
        return 1

    below = l[y + 1][x]
    if below == ".":
        path_count = count_paths(l, (x, y + 1), m)
        m[k] = path_count
        return path_count
    if below == "^":
        count = 0
        if x - 1 >= 0 and l[y][x - 1] == ".":
            count += count_paths(l, (x - 1, y), m)
        if x + 1 < width and l[y][x + 1] == ".":
            count += count_paths(l, (x + 1, y), m)
        m[k] = count
        return count

    m[k] = 0
    return 0


def second_star(lines: list[list[str]]) -> None:
    """Solve the second star."""
    result = 0
    height = len(lines)
    if height < 2:
        print("Result for the second star: 0")
        return

    width = len(lines[0])
    for x in range(width):
        if lines[0][x] == "S" and lines[1][x] == ".":
            result += count_paths(lines, (x, 1))
    print(f"Result for the second star: {result}")


if __name__ == "__main__":
    star, input_data = parse_args()
    if star == 1:
        first_star(input_data)
    elif star == 2:
        second_star(input_data)
