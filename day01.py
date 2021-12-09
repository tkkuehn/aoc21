import argparse


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("input")
    args = parser.parse_args()

    with open(args.input, "r", encoding="utf-8") as input_file:
        depths = [int(line) for line in input_file.readlines()]

    counter = 0
    for i, depth in enumerate(depths):
        if i > 0 and depths[i - 1] < depth:
            counter += 1
    print(f"Part 1: {counter}")

    windows = [sum(depths[i - 2 : i + 1]) for i in range(2, len(depths))]
    counter = 0
    for i, window in enumerate(windows):
        if i > 0 and windows[i - 1] < window:
            counter += 1
    print(f"Part 2: {counter}")


if __name__ == "__main__":
    main()
