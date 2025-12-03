import time


def solve(banks: list[str]) -> int:
    output = 0
    for bank in banks:
        output += find_largest_joltages(bank, 12)
    return output


def find_largest_joltages(bank: str, count: int) -> int:
    largest_indexes = []
    for i in range(0, count):
        start = int(largest_indexes[-1]) + 1 if largest_indexes else 0
        end = len(bank) - count + i + 1
        largest_indexes.append(int(find_largest_joltage(bank, start, end)))

    largest_joltages = ""
    for i in largest_indexes:
        largest_joltages += bank[i]

    return int(largest_joltages)


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
