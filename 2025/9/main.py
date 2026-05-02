"""Advent of Code 2025 - Day 9: Movie Theater"""

import argparse
import bisect
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


def first_star(red_tiles: list[tuple[int, int]]) -> None:
    """Solve the first star of the puzzle."""
    largest_area = 0
    for i, red_tile in enumerate(red_tiles):
        for other in red_tiles[i + 1 :]:
            # + 1 to include the red tile positions themselves
            area = abs(red_tile[0] - other[0] + 1) * abs(red_tile[1] - other[1] + 1)
            largest_area = max(largest_area, area)
    print(f"Largest area between red tiles: {largest_area}")


def second_star(red_tiles: list[tuple[int, int]]) -> int:
    """Trouve la plus grande aire d'un rectangle entièrement contenu dans le polygone."""
    n = len(red_tiles)

    # ---------------------------------------------------------
    xs = sorted(list(set(x for x, y in red_tiles)))
    ys = sorted(list(set(y for x, y in red_tiles)))

    def build_grid_samples(coords):
        """Crée une grille alternant coordonnées exactes et milieux entre ces coordonnées."""
        samples = []
        for i in range(len(coords) - 1):
            samples.append(float(coords[i]))  # Ligne exacte (le bord)
            samples.append((coords[i] + coords[i + 1]) / 2.0)  # Le milieu (l'intérieur)
        samples.append(float(coords[-1]))  # Dernière ligne exacte
        return samples

    grid_x = build_grid_samples(xs)
    grid_y = build_grid_samples(ys)
    nx, ny = len(grid_x), len(grid_y)

    # ---------------------------------------------------------
    vertical_segs = []
    horizontal_segs = []

    for i in range(n):
        x1, y1 = red_tiles[i]
        x2, y2 = red_tiles[(i + 1) % n]
        if y1 == y2:
            horizontal_segs.append((min(x1, x2), max(x1, x2), y1))
        else:
            vertical_segs.append((x1, min(y1, y2), max(y1, y2)))

    # ---------------------------------------------------------
    is_inside = [[False] * ny for _ in range(nx)]

    for j, py in enumerate(grid_y):
        active_verts = sorted(x for x, ymin, ymax in vertical_segs if ymin <= py < ymax)
        bounds_v = {x for x, ymin, ymax in vertical_segs if ymin <= py <= ymax}
        bounds_h = [(xmin, xmax) for xmin, xmax, y in horizontal_segs if y == py]

        for i, px in enumerate(grid_x):
            on_h_edge = any(xmin <= px <= xmax for xmin, xmax in bounds_h)
            on_v_edge = px in bounds_v

            if on_h_edge or on_v_edge:
                is_inside[i][j] = True
            else:
                crossings = len(active_verts) - bisect.bisect_right(active_verts, px)
                is_inside[i][j] = crossings % 2 == 1

    # ---------------------------------------------------------
    prefix = [[0] * (ny + 1) for _ in range(nx + 1)]
    for i in range(nx):
        for j in range(ny):
            outside_val = 0 if is_inside[i][j] else 1
            prefix[i + 1][j + 1] = (
                outside_val + prefix[i][j + 1] + prefix[i + 1][j] - prefix[i][j]
            )

    def contains_outside_area(x_idx1, y_idx1, x_idx2, y_idx2) -> bool:
        """S'il y a plus de 0 cases 'hors polygone' dans la zone, le rectangle est invalide."""
        total_outside = (
            prefix[x_idx2 + 1][y_idx2 + 1]
            - prefix[x_idx1][y_idx2 + 1]
            - prefix[x_idx2 + 1][y_idx1]
            + prefix[x_idx1][y_idx1]
        )
        return total_outside > 0

    # ---------------------------------------------------------
    max_area = 0
    x_to_idx = {x: 2 * i for i, x in enumerate(xs)}
    y_to_idx = {y: 2 * j for j, y in enumerate(ys)}

    for i in range(n):
        x1, y1 = red_tiles[i]
        for j in range(i + 1, n):
            x2, y2 = red_tiles[j]

            if x1 == x2 or y1 == y2:
                continue

            left, right = min(x1, x2), max(x1, x2)
            bottom, top = min(y1, y2), max(y1, y2)

            if not contains_outside_area(
                x_to_idx[left], y_to_idx[bottom], x_to_idx[right], y_to_idx[top]
            ):
                area = (right - left + 1) * (top - bottom + 1)
                max_area = max(max_area, area)

    print(f"Largest area using only red and green tiles: {max_area}")


if __name__ == "__main__":
    star, input_data = parse_args()
    if star == 1:
        first_star(input_data)
    elif star == 2:
        second_star(input_data)
