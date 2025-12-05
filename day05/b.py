import time
import tracemalloc


class Interval:
    def __init__(self, start: int, end: int) -> None:
        self.start = start
        self.end = end

    def overlaps(self, other: "Interval") -> bool:
        return self.start <= other.end + 1

    @classmethod
    def from_strings(cls, ranges: list[str]) -> list["Interval"]:
        return [cls(*map(int, r.split("-"))) for r in ranges]


def solve(ranges: list[str]) -> int:
    intervals = Interval.from_strings(ranges)
    merged = merge(intervals)
    return sum(interval.end - interval.start + 1 for interval in merged)


def merge(intervals: list[Interval]) -> list[Interval]:
    if not intervals:
        return []

    intervals.sort(key=lambda x: (x.start, x.end))

    merged = [intervals[0]]
    for curr in intervals[1:]:
        last = merged[-1]
        if curr.overlaps(last):
            last.end = max(curr.end, last.end)
        else:
            merged.append(curr)

    return merged


def main():
    with open("day05/input.txt") as f:
        ranges = f.read().split("\n\n")[0].splitlines()

    tracemalloc.start()
    start = time.perf_counter()
    result = solve(ranges)
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
