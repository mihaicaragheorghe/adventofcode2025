import time
import tracemalloc


def solve(problems: list[list[str]]) -> int:
    total = 0
    for x in range(0, len(problems[0])):
        sign = problems[-1][x]
        res = 1 if sign == "*" else 0
        for y in range(0, len(problems) - 1):
            if sign == "+":
                res += int(problems[y][x])
            elif sign == "*":
                res *= int(problems[y][x])
        total += res
    return total


def main():
    with open("day06/input.txt") as f:
        data = f.read().splitlines()

    problems = [line.split() for line in data]
    start = time.perf_counter()
    result = solve(problems)
    end = time.perf_counter()
    elapsed_ms = (end - start) * 1000

    tracemalloc.start()
    result = solve(problems)
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    print(f"Result: {result}")
    print(f"Elapsed: {elapsed_ms:.2f} ms")
    print(f"Current memory: {current / 1024:.2f} KB")
    print(f"Peak memory: {peak / 1024:.2f} KB")


if __name__ == "__main__":
    main()
