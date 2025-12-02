import time


def solve(rotations: list[str]) -> int:
    pos = 50
    zeros = 0
    for rotation in rotations:
        dir = rotation[0]
        count = int(rotation[1:])
        pos = rotate(pos, dir, count)
        if pos == 0:
            zeros += 1
    return zeros


def rotate(src: int, dir: str, count: int) -> int:
    if dir == "L":
        src -= count
    elif dir == "R":
        src += count
    else:
        raise ValueError(f"Invalid direction: {dir}")
    return src % 100


if __name__ == "__main__":
    with open("day01/input.txt") as f:
        data = f.readlines()
    start = time.perf_counter()
    print(solve(data))
    end = time.perf_counter()

    elapsed_ms = (end - start) * 1000
    print(f"{elapsed_ms:.2f} ms")
