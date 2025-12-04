import time


N = (-1, 0)
W = (0, -1)
E = (0, 1)
S = (1, 0)
NW = (-1, -1)
NE = (-1, 1)
SW = (1, -1)
SE = (1, 1)


DIRECTIONS = [NW, N, NE, W, E, SW, S, SE]


def solve(grid: list[str]) -> int:
    removed_count = 0
    removed_items = []
    for y, _ in enumerate(grid):
        for x, c in enumerate(grid[y]):
            if c == "@" and find_neighbors(grid, y, x) < 4:
                removed_count += 1
                removed_items.append((y, x))

    for item in removed_items:
        remove(grid, item[0], item[1])

    if removed_count > 0:
        removed_count += solve(grid)

    return removed_count


def find_neighbors(grid: list[str], y: int, x: int) -> int:
    neighbors = 0
    for dy, dx in DIRECTIONS:
        if is_roll(grid, y + dy, x + dx):
            neighbors += 1
    return neighbors


def is_roll(grid: list[str], y: int, x: int) -> bool:
    if y < 0 or y >= len(grid) or x < 0 or x >= len(grid[y]):
        return False
    return grid[y][x] == "@"


def remove(grid: list[str], y: int, x: int):
    s = grid[y][:x] + "x" + grid[y][x + 1 :]
    grid[y] = s


if __name__ == "__main__":
    with open("day04/input.txt") as f:
        data = f.read()

    start = time.perf_counter()
    print(solve(data.splitlines()))
    end = time.perf_counter()

    elapsed_ms = (end - start) * 1000
    print(f"{elapsed_ms:.2f} ms")
