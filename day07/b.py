from collections import deque
import time
import tracemalloc


def solve(grid: list[list[str]]) -> int:
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if grid[y][x] == "S":
                return simulate(grid, y, x)
    return -1


def simulate(manifold: list[list[str]], start_y: int, start_x: int) -> int:
    q = deque([(start_y, start_x)])
    visited = set()

    while q:
        y, x = q.popleft()

        if (y, x) in visited:
            continue

        visited.add((y, x))

        if y == len(manifold) - 1:
            continue

        below = manifold[y + 1][x]

        if below == "." or below.isdigit():
            next_y, next_x = y + 1, x
            q.append((next_y, next_x))
            propagate(manifold, y, x, next_y, next_x)
            continue

        if below == "^":
            for dx in (-1, +1):
                nx = x + dx
                if 0 <= nx < len(manifold[y]) and manifold[y + 1][nx] != "^":
                    next_y, next_x = y + 1, nx
                    q.append((next_y, next_x))
                    propagate(manifold, y, x, next_y, next_x)

    return sum(int(x) for x in manifold[-1] if x.isdigit())


def propagate(manifold: list[list[str]], y, x, ny, nx: int):
    w = int(manifold[y][x]) if manifold[y][x].isdigit() else 1
    nw = int(manifold[ny][nx]) if manifold[ny][nx].isdigit() else 0
    manifold[ny][nx] = str(w + nw)


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
            if grid[y][x].isdigit():
                grid[y][x] = "."


if __name__ == "__main__":
    main()
