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
        if is_invalid(n):
            sum += n
    return sum


def is_invalid(n: int) -> bool:
    s = str(n)
    mid = int(len(s) // 2)
    return s[:mid] == s[mid:]


if __name__ == "__main__":
    with open("day02/input.txt") as f:
        data = f.read()
    start = time.perf_counter()
    print(solve(data.split(",")))
    end = time.perf_counter()

    elapsed_ms = (end - start) * 1000
    print(f"{elapsed_ms:.2f} ms")
