"""Advent of Code 2025 - Day 1: Secret Entrance"""

import argparse
import sys

def parse_args() -> tuple[int, list[str]]:
    """Analyze command line arguments."""
    parser = argparse.ArgumentParser(
        description="Advent of Code 2025 - Day 1: Secret Entrance"
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
        default="2025/1/input.txt",
        help="Path to the input file",
    )

    args = parser.parse_args()

    try:
        with open(args.input, "r", encoding="utf-8") as file:
            data = file.readlines()
    except FileNotFoundError:
        print(f"Error: The file '{args.input}' does not exist.")
        sys.exit(1)

    return args.star, data


def turn_dial(rotation: int, direction: str, dial: int) -> int:
    """Turn the dial."""
    if direction == "L":
        dial -= rotation
    elif direction == "R":
        dial += rotation
    return dial % 100


def turn_dial_iterative(rotation: int, direction: str, dial: int) -> tuple[int, int]:
    """Turn the dial iteratively to count the passages through zero."""
    count = 0
    if direction == "L":
        for _ in range(rotation):
            dial -= 1
            dial = dial % 100
            if dial == 0:
                count += 1
    elif direction == "R":
        for _ in range(rotation):
            dial += 1
            dial = dial % 100
            if dial == 0:
                count += 1
    return count, dial


def first_star(data: list[str]) -> None:
    """Solve the first star."""
    dial = 50
    password = 0
    print(f"- The dial starts by pointing at {dial}.")
    for _, line in enumerate(data):
        line = line.strip()
        dial = turn_dial(int(line[1:]), line[0], dial)
        print(f"- The dial is rotated {line} to point at {dial}.")
        if dial == 0:
            password += 1
    print(f"Final password: {password}.")


def second_star(data: list[str]) -> None:
    """Solve the second star."""
    dial = 50
    password = 0
    print(f"- The dial starts by pointing at {dial}.")
    for _, line in enumerate(data):
        line = line.strip()
        rotation = int(line[1:])
        direction = line[0]
        zeros_count, dial = turn_dial_iterative(rotation, direction, dial)
        text = f"- The dial is rotated {line} to point at {dial}"
        if zeros_count == 1:
            text += f"; during this rotation, it points at zero {zeros_count} time."
        elif zeros_count > 1:
            text += f"; during this rotation, it points at zero {zeros_count} times."
        else:
            text += "."
        print(text)
        password += zeros_count
    print(f"Final password: {password}.")


if __name__ == "__main__":
    star, lines = parse_args()
    if star == 1:
        first_star(lines)
    elif star == 2:
        second_star(lines)
