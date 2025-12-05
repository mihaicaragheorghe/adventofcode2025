import time
import tracemalloc


def solve(ranges: list[str], ids: list[str]) -> int:
    fresh = 0
    intervals = parse_ranges(ranges)
    for id in map(int, ids):
        for interval in intervals:
            if interval[0] <= id and id <= interval[1]:
                fresh += 1
                break
    return fresh


def parse_ranges(ranges: list[str]) -> list[tuple[int, int]]:
    return [(int(start), int(end)) for r in ranges for start, end in [r.split("-")]]


def main():
    with open("day05/input.txt") as f:
        data = f.read()
    parts = data.split("\n\n")
    ranges = parts[0].splitlines()
    ids = parts[1].splitlines()

    tracemalloc.start()
    start = time.perf_counter()
    result = solve(ranges, ids)
    end = time.perf_counter()

    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    elapsed_ms = (end - start) * 1000

    print(f"Result: {result}")
    print(f"Elapsed: {elapsed_ms:.2f} ms")
    print(f"Current memory: {current / 1024:.2f} KB")
    print(f"Peak memory: {peak / 1024:.2f} KB")


if __name__ == "__main__":
    main()
