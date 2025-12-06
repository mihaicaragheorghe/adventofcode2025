import time
import tracemalloc


def solve(problems: list[str]) -> int:
    total = 0
    curr_sign = get_sign(problems, len(problems[0]) - 1)
    curr_res = 1 if curr_sign == "*" else 0

    for x in reversed(range(0, len(problems[0]))):
        curr_num = ""
        for y in range(0, len(problems) - 1):
            if problems[y][x].isdigit():
                curr_num += problems[y][x]

        if not curr_num:
            total += curr_res
            curr_sign = get_sign(problems, x)
            curr_res = 1 if curr_sign == "*" else 0
            continue

        if curr_sign == "+":
            curr_res += int(curr_num)
        elif curr_sign == "*":
            curr_res *= int(curr_num)

        if x == 0:
            total += curr_res

    return total


def get_sign(problems: list[str], x: int):
    while x > 0 and x < len(problems[0]) and problems[-1][x] == " ":
        x -= 1
    return problems[-1][x]


def main():
    with open("day06/input.txt") as f:
        data = f.read().splitlines()

    start = time.perf_counter()
    result = solve(data)
    end = time.perf_counter()
    elapsed_ms = (end - start) * 1000

    tracemalloc.start()
    result = solve(data)
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    print(f"Result: {result}")
    print(f"Elapsed: {elapsed_ms:.2f} ms")
    print(f"Current memory: {current / 1024:.2f} KB")
    print(f"Peak memory: {peak / 1024:.2f} KB")


if __name__ == "__main__":
    main()
