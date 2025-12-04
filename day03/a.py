import time


def solve(banks: list[str]) -> int:
    output = 0
    for bank in banks:
        output += max_jolts(bank)
    return output


def max_jolts(bank: str) -> int:
    first = max_jolt(bank, 0, len(bank) - 1)
    second = max_jolt(bank, first + 1, len(bank))
    return int(bank[first] + bank[second])


def max_jolt(bank: str, start: int, end) -> int:
    max_idx = start
    for i, d in enumerate(bank[start:end], start):
        if int(d) > int(bank[max_idx]):
            max_idx = i
    return max_idx


def main():
    with open("day03/input.txt") as f:
        data = f.read().splitlines()
    start = time.perf_counter()
    result = solve(data)
    end = time.perf_counter()
    elapsed_ms = (end - start) * 1000

    print(result)
    print(f"{elapsed_ms:.2f} ms")


if __name__ == "__main__":
    main()
