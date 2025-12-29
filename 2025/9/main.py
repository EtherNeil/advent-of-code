"""Advent of Code 2025 - Day 9: Movie Theater"""

import argparse
import sys


def parse_args() -> tuple[int, list[tuple[int, int]]]:
    """Analyze command line arguments."""
    parser = argparse.ArgumentParser(
        description="Advent of Code 2025 - Day 9: Movie Theater"
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
        default="2025/9/test.txt",
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


def draw_theater(seats: list[tuple[int, int]]) -> None:
    """Draw the movie theater seating arrangement."""
    if not seats:
        print("No seats to display.")
        return

    max_x = max(seat[0] for seat in seats)
    max_y = max(seat[1] for seat in seats)

    theater = [["." for _ in range(max_x + 1)] for _ in range(max_y + 1)]

    for x, y in seats:
        theater[y][x] = "#"

    for row in theater:
        print("".join(row))


def first_star(seats: list[tuple[int, int]]) -> None:
    """Solve the first star of the puzzle."""
    largest_area = 0
    for i, seat in enumerate(seats):
        for other in seats[i + 1 :]:
            # + 1 to include the seat positions themselves
            area = abs(seat[0] - other[0] + 1) * abs(seat[1] - other[1] + 1)
            largest_area = max(largest_area, area)
    print(f"Largest area between seats: {largest_area}")


def second_star(red_tiles: list[tuple[int, int]]) -> None:
    """Solve the second star of the puzzle."""
    green_tiles: set[tuple[int, int]] = set()
    for i, red_tile in enumerate(red_tiles):
        for other in red_tiles[i + 1 :]:
            if red_tile[0] == other[0]:
                for y in range(
                    min(red_tile[1], other[1]) + 1, max(red_tile[1], other[1])
                ):
                    green_tiles.add((red_tile[0], y))
            if red_tile[1] == other[1]:
                for x in range(
                    min(red_tile[0], other[0]) + 1, max(red_tile[0], other[0])
                ):
                    green_tiles.add((x, red_tile[1]))
    for i, green_tile in enumerate(list(green_tiles)):
        for other in list(green_tiles)[i + 1 :]:
            if green_tile[0] == other[0]:
                for y in range(
                    min(green_tile[1], other[1]) + 1, max(green_tile[1], other[1])
                ):
                    if (green_tile[0], y) not in red_tiles and (
                        green_tile[0],
                        y,
                    ) not in green_tiles:
                        green_tiles.add((green_tile[0], y))
            if green_tile[1] == other[1]:
                for x in range(
                    min(green_tile[0], other[0]) + 1, max(green_tile[0], other[0])
                ):
                    if (x, green_tile[1]) not in red_tiles and (
                        x,
                        green_tile[1],
                    ) not in green_tiles:
                        green_tiles.add((x, green_tile[1]))
    print(f"Total green tiles added: {len(green_tiles)}")


if __name__ == "__main__":
    star, input_data = parse_args()
    if star == 1:
        first_star(input_data)
    elif star == 2:
        second_star(input_data)
