import time


def solve(banks: list[str]) -> int:
    output = 0
    for bank in banks:
        output += find_largest_joltages(bank)
    return output


def find_largest_joltages(bank: str) -> int:
    first = find_largest_joltage(bank, 0, len(bank) - 1)
    second = find_largest_joltage(bank, first + 1, len(bank))
    return int(bank[first] + bank[second])


def find_largest_joltage(bank: str, start: int, end) -> int:
    max_idx = start
    for i, d in enumerate(bank[start:end], start):
        if int(d) > int(bank[max_idx]):
            max_idx = i
    return max_idx


if __name__ == "__main__":
    with open("day03/input.txt") as f:
        data = f.read().splitlines()
    start = time.perf_counter()
    print(solve(data))
    end = time.perf_counter()

    elapsed_ms = (end - start) * 1000
    print(f"{elapsed_ms:.2f} ms")
