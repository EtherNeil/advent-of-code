"""Advent of Code 2025 - Day 4: Printing Department"""

import argparse
import sys


def parse_args() -> tuple[int, list[str]]:
    """Analyze command line arguments."""
    parser = argparse.ArgumentParser(
        description="Advent of Code 2025 - Day 4: Printing Department"
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
        default="2025/4/test.txt",
        help="Path to the input file",
    )

    args = parser.parse_args()

    try:
        with open(args.input, "r", encoding="utf-8") as file:
            data = [list(line.strip()) for line in file.readlines()]
    except FileNotFoundError:
        print(f"Error: The file '{args.input}' does not exist.")
        sys.exit(1)

    return args.star, data


def display_matrix(matrix: list[list[str]]) -> None:
    """Display the matrix."""
    for row in matrix:
        print("".join(row))


def neighbors(
    matrix: list[list[str]], radius: int, row_number: int, column_number: int
) -> list[str]:
    """Collect the neighbors of a given cell in a matrix."""
    return [
        [
            (
                "O"
                if (i == row_number and j == column_number)
                else (
                    matrix[i][j]
                    if 0 <= i < len(matrix) and 0 <= j < len(matrix[0])
                    else " "
                )
            )
            for j in range(column_number - radius, column_number + radius + 1)
        ]
        for i in range(row_number - radius, row_number + radius + 1)
    ]


def check_paper_accessibility(
    matrix: list[list[str]], x_index: int, y_index: int
) -> bool | None:
    """Check the accessibility of a given roll of paper."""
    if matrix[y_index][x_index] != "@":
        return None
    neighbors_list = neighbors(matrix, 1, y_index, x_index)
    count_roll_neighbors = 0
    for row in neighbors_list:
        for element in row:
            if element == "@":
                count_roll_neighbors += 1
    return count_roll_neighbors < 4


def first_star(matrix: list[list[str]]) -> None:
    """Solve the first star."""
    display_matrix(matrix)
    final_matrix = [row.copy() for row in matrix]
    counter = 0
    print("-" * len(matrix[0]))
    for row_index, row in enumerate(matrix):
        for col_index, element in enumerate(row):
            if element == "@":
                accessible = check_paper_accessibility(matrix, col_index, row_index)
                if accessible is None:
                    continue
                if accessible:
                    final_matrix[row_index][col_index] = "x"
                    counter += 1
    display_matrix(final_matrix)
    print("-" * len(matrix[0]))
    print(f"Number of accessible rolls of paper: {counter}")

def second_star(matrix: list[list[str]]) -> None:
    """Solve the second star."""
    counter = 1
    while counter > 0:
        counter = 0
        final_matrix = [row.copy() for row in matrix]
        for row_index, row in enumerate(matrix):
            for col_index, element in enumerate(row):
                if element == "@":
                    accessible = check_paper_accessibility(matrix, col_index, row_index)
                    if accessible is None:
                        continue
                    if accessible:
                        final_matrix[row_index][col_index] = "x"
                        counter += 1
        matrix = final_matrix
    display_matrix(final_matrix)
    final_counter = 0
    for row in matrix:
        for element in row:
            if element == "x":
                final_counter += 1
    print(f"Total number of accessible rolls of paper: {final_counter}")

if __name__ == "__main__":
    star, input_data = parse_args()
    if star == 1:
        first_star(input_data)
    elif star == 2:
        second_star(input_data)
