import time


def solve(rotations: list[str]) -> int:
    pos = 50
    clicks = 0
    for rotation in rotations:
        dir = rotation[0]
        count = int(rotation[1:])
        pos, clicks = rotate(pos, dir, count, clicks)
    return clicks


def rotate(pos: int, dir: str, count: int, clicks: int) -> tuple[int, int]:
    started_at_zero = pos == 0

    if dir == "L":
        pos -= count
    elif dir == "R":
        pos += count
    else:
        raise ValueError(f"Invalid direction: {dir}")

    while pos > 100:
        pos -= 100
        clicks += 1

    while pos < 0:
        pos += 100
        if not started_at_zero:
            clicks += 1
        started_at_zero = False

    if pos == 100:
        pos = 0

    if pos == 0:
        clicks += 1

    return pos, clicks


if __name__ == "__main__":
    with open("day01/input.txt") as f:
        data = f.readlines()
    start = time.perf_counter()
    print(solve(data))
    end = time.perf_counter()

    elapsed_ms = (end - start) * 1000
    print(f"{elapsed_ms:.2f} ms")
