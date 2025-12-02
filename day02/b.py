import re
import time


def solve(ranges: list[str]) -> int:
    total = 0
    for r in ranges:
        start, end = map(int, r.split("-"))
        total += sum_invalid_ids(start, end + 1)
    return total


def sum_invalid_ids(start: int, end: int) -> int:
    sum = 0
    for n in range(start, end):
        if re.search(r"^(\d+)\1+$", str(n)):
            sum += n
    return sum


if __name__ == "__main__":
    with open("day02/input.txt", "r") as f:
        data = f.read()
    start = time.perf_counter()
    print(solve(data.split(",")))
    end = time.perf_counter()
    elapsed_ms = (end - start) * 1000
    print(f"{elapsed_ms:.2f} ms")
