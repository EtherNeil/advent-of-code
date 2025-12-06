"""Advent of Code 2025 - Day 6: Trash Compactor"""

import argparse
import sys


def parse_args() -> tuple[int, list[str]]:
    """Analyze command line arguments."""
    parser = argparse.ArgumentParser(
        description="Advent of Code 2025 - Day 6: Trash Compactor"
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
        default="2025/6/input.txt",
        help="Path to the input file",
    )

    args = parser.parse_args()

    try:
        with open(args.input, "r", encoding="utf-8") as file:
            data = [line for line in file.readlines()]
    except FileNotFoundError:
        print(f"Error: The file '{args.input}' does not exist.")
        sys.exit(1)

    return args.star, data


def first_star(matrix: list[str]) -> None:
    """Solve the first star."""
    matrix = [list(line.strip().split(" ")) for line in matrix]
    matrix = [[item for item in row if item != ""] for row in matrix]
    print(matrix)
    result = 0
    for x_index in range(len(matrix[0])):
        operator = matrix[-1][x_index]
        value = 0 if operator == "+" else 1
        for y_index in range(len(matrix) - 1):
            if operator == "+":
                value += int(matrix[y_index][x_index])
            elif operator == "*":
                value *= int(matrix[y_index][x_index])
        print(f"Column {x_index}: {value}")
        result += value
    print(f"Sum of all columns: {result}")


def second_star(matrix: list[str]) -> None:
    """Solve the second star."""
    matrix = [list(line) for line in matrix]
    matrix = [[item for item in row if item != "\n"] for row in matrix]
    len_x = len(matrix[0])
    len_y = len(matrix)
    result = 0
    values = []
    for x_index in range(len_x - 1, -1, -1):
        operator = matrix[-1][x_index]
        value = ""
        for y_index in range(len_y - 1):
            v = matrix[y_index][x_index]
            if v != " ":
                value = value + v
        if value != "":
            values.append(value)
        if operator == "+":
            r = sum(int(digit) for digit in values)
            print(f"Adding {values} = {r}")
            result += r
            values = []
        elif operator == "*":
            r = 1
            for digit in values:
                r *= int(digit)
            print(f"Multiplying {values} = {r}")
            result += r
            values = []
    print(f"Sum of all columns: {result}")


if __name__ == "__main__":
    star, input_data = parse_args()
    if star == 1:
        first_star(input_data)
    elif star == 2:
        second_star(input_data)
