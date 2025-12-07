from collections import deque
import time
import tracemalloc


def solve(grid: list[list[str]]) -> int:
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if grid[y][x] == "S":
                return move_down(grid, y, x)
    return -1


def move_down(grid: list[list[str]], y: int, x: int) -> int:
    q = deque([(y, x)])
    splits = 0

    while q:
        y, x = q.popleft()

        if y == len(grid) - 1:
            continue

        below = grid[y + 1][x]

        if below == ".":
            q.append((y + 1, x))
            grid[y + 1][x] = "|"
        elif below == "^":
            splits += 1
            if x > 0 and grid[y + 1][x - 1] != "^":
                q.append((y + 1, x - 1))
                grid[y + 1][x - 1] = "|"
            if x < len(grid[y]) - 1 and grid[y + 1][x + 1] != "^":
                q.append((y + 1, x + 1))
                grid[y + 1][x + 1] = "|"

    return splits


def main():
    with open("day07/input.txt") as f:
        grid = [list(line) for line in f.readlines()]

    start = time.perf_counter()
    result = solve(grid)
    end = time.perf_counter()
    elapsed_ms = (end - start) * 1000

    reset_grid(grid)
    tracemalloc.start()
    result = solve(grid)
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    print(f"Result: {result}")
    print(f"Elapsed: {elapsed_ms:.2f} ms")
    print(f"Current memory: {current / 1024:.2f} KB")
    print(f"Peak memory: {peak / 1024:.2f} KB")


def reset_grid(grid: list[list[str]]):
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if grid[y][x] == "|":
                grid[y][x] = "."


if __name__ == "__main__":
    main()
