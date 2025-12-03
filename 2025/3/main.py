"""Advent of Code 2025 - Day 3: Lobby"""

import argparse
import sys


def parse_args() -> tuple[int, list[str]]:
    """Analyze command line arguments."""
    parser = argparse.ArgumentParser(description="Advent of Code 2025 - Day 3: Lobby")
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
        default="2025/3/test.txt",
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


def first_star(banks: list[str]) -> None:
    """Solve the first star."""
    total_output_joltage = 0
    for _, bank in enumerate(banks):
        bank = list(bank)
        first_index = bank.index(max(bank[:-1]))
        first_number = int(bank[first_index])
        second_index = bank.index(max(bank[first_index + 1 :]))
        second_number = int(bank[second_index])
        largest_joltage = int(first_number) * 10 + int(second_number)
        total_output_joltage += largest_joltage
        print(
            f"- In {''.join(bank)}, the largest joltage you can produce is {largest_joltage}."
        )
    print(f"Total output joltage: {total_output_joltage}.")


def compute_joltage(bank: list[int], r: int) -> int:
    """Compute the largest joltage for a given bank."""
    battery_index = bank.index(max(bank[: -(r - 1)] if r > 1 else bank))
    output_joltage = bank[battery_index] * (10 ** (r - 1))
    output_joltage += compute_joltage(bank[battery_index + 1 :], r - 1) if r > 1 else 0
    return output_joltage


def second_star(banks: list[str]) -> None:
    """Solve the second star."""
    total_output_joltage = 0
    for _, bank in enumerate(banks):
        joltage = compute_joltage(list(map(int, bank)), 12)
        print(f"- In {bank}, the largest joltage you can produce is {joltage}.")
        total_output_joltage += joltage
    print(f"Total output joltage: {total_output_joltage}.")


if __name__ == "__main__":
    star, lines = parse_args()
    if star == 1:
        first_star(lines)
    elif star == 2:
        second_star(lines)
