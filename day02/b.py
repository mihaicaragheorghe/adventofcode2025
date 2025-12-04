import re
import time

PATTERN = re.compile(r"^(\d+)\1+$")


def solve(ranges: list[str]) -> int:
    total = 0
    for r in ranges:
        start, end = map(int, r.split("-"))
        total += sum_invalid_ids(start, end)
    return total


def sum_invalid_ids(start: int, end: int) -> int:
    sum = 0
    for n in range(start, end + 1):
        if PATTERN.search(str(n)):
            sum += n
    return sum


def main():
    with open("day02/input.txt") as f:
        data = f.read()
    start = time.perf_counter()
    result = solve(data.split(","))
    end = time.perf_counter()
    elapsed_ms = (end - start) * 1000

    print(f"{elapsed_ms:.2f} ms")
    print(result)


if __name__ == "__main__":
    main()
