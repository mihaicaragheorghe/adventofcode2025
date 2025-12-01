def solve(rotations: list[str]) -> int:
    pos = 50
    count = 0

    for rotation in rotations:
        dir = rotation[0]
        count = int(rotation[1:])
        pos = rotate(pos, dir, count)
        if pos == 0:
            count += 1

    return count


def rotate(src: int, dir: str, count: int) -> int:
    if dir == "L":
        src -= count
    elif dir == "R":
        src += count
    else:
        raise ValueError(f"Invalid direction: {dir}")
    return src % 100


if __name__ == "__main__":
    with open("day01/input.txt", "r") as f:
        data = f.read()
    print(solve(data.split("\n")))
