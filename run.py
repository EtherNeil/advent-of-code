import argparse
import os
import subprocess
import sys


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Run an Advent of Code solution from the repo root.",
        prog="run.py",
    )
    parser.add_argument(
        "--year",
        type=int,
        default=2025,
        help="Puzzle year (default: 2025)",
    )
    parser.add_argument(
        "--day",
        type=int,
        required=True,
        help="Puzzle day (1-25)",
    )
    parser.add_argument(
        "--star",
        type=int,
        choices=[1, 2],
        default=None,
        help="Star to run (1 or 2); omit to run both",
    )

    input_group = parser.add_mutually_exclusive_group()
    input_group.add_argument(
        "--test",
        action="store_true",
        help="Use the test input file ({year}/{day}/test.txt)",
    )
    input_group.add_argument(
        "--input",
        type=str,
        dest="input_path",
        metavar="PATH",
        help="Path to a custom input file",
    )

    args = parser.parse_args()

    if not (1 <= args.day <= 25):
        parser.error(f"--day must be between 1 and 25, got {args.day}")

    return args


def resolve_input_path(args: argparse.Namespace) -> str:
    if args.test:
        return f"{args.year}/{args.day}/test.txt"
    if args.input_path is not None:
        return args.input_path
    return f"{args.year}/{args.day}/input.txt"


def main() -> None:
    args = parse_args()

    script_path = f"{args.year}/{args.day}/main.py"
    if not os.path.isfile(script_path):
        print(f"error: script not found: {script_path}", file=sys.stderr)
        sys.exit(1)

    input_path = resolve_input_path(args)
    if not os.path.isfile(input_path):
        print(f"error: input file not found: {input_path}", file=sys.stderr)
        sys.exit(1)

    stars = [args.star] if args.star is not None else [1, 2]

    for star in stars:
        if len(stars) > 1:
            print(f"--- Star {star} ---", flush=True)
        cmd = [sys.executable, script_path, "--star", str(star), "--input", input_path]
        result = subprocess.run(cmd)
        if result.returncode != 0:
            sys.exit(result.returncode)


if __name__ == "__main__":
    main()
