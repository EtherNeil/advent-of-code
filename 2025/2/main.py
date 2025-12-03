"""Advent of Code 2025 - Day 2: Gift Shop"""

import argparse
import sys


def parse_data(input_data: str) -> tuple[int, int]:
    """Parse the input data."""
    parts = input_data.split("-")
    return int(parts[0].strip()), int(parts[1].strip())


def parse_args() -> tuple[int, list[tuple[int, int]]]:
    """Analyze command line arguments."""
    parser = argparse.ArgumentParser(
        description="Advent of Code 2025 - Day 2: Gift Shop"
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
        default="2025/2/test.txt",
        help="Path to the input file",
    )

    args = parser.parse_args()

    try:
        with open(args.input, "r", encoding="utf-8") as f:
            raw_data = f.read().strip().split(",")
            data = list(map(parse_data, raw_data))
    except FileNotFoundError:
        print(f"Error: The file '{args.input}' does not exist.")
        sys.exit(1)

    return args.star, data


def first_star(data: list[tuple[int, int]]) -> None:
    """Solve the first star."""
    count_invalid_ids = 0
    for _, (start, end) in enumerate(data):
        invalid_ids = set()
        for number in range(start, end + 1):
            length = len(str(number))
            if length % 2 != 0:
                continue
            half = length // 2
            sequence = str(number)[0:half]
            if str(number).count(sequence) * half == length:
                invalid_ids.add(number)
        if invalid_ids:
            count_invalid_ids += sum(invalid_ids)
            string = f"- {start}-{end} has {len(invalid_ids)} invalid ID"
            string += "s." if len(invalid_ids) > 1 else "."
            print(string)
        else:
            print(f"- {start}-{end} contains no invalid IDs.")
    print(f"Total invalid IDs: {count_invalid_ids}.")


def second_star(data: list[tuple[int, int]]) -> None:
    """Solve the second star."""
    count_invalid_ids = 0
    for _, (start, end) in enumerate(data):
        invalid_ids = set()
        for number in range(start, end + 1):
            length = len(str(number))
            half = length // 2
            for i in range(1, half + 1):
                if length % i != 0:
                    continue
                sequence = str(number)[0:i]
                if str(number).count(sequence) * i == length:
                    invalid_ids.add(number)
        if invalid_ids:
            count_invalid_ids += sum(invalid_ids)
            string = f"- {start}-{end} has {len(invalid_ids)} invalid ID"
            string += "s." if len(invalid_ids) > 1 else "."
            print(string)
        else:
            print(f"- {start}-{end} contains no invalid IDs.")
    print(f"Total invalid IDs: {count_invalid_ids}.")


if __name__ == "__main__":
    star, lines = parse_args()
    if star == 1:
        first_star(lines)
    if star == 2:
        second_star(lines)
