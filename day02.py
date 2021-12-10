from dataclasses import dataclass
import argparse


@dataclass
class Position:
    depth: int
    position_horizontal: int

    def __add__(self, other):
        return Position(
            self.depth + other.depth,
            self.position_horizontal + other.position_horizontal,
        )

@dataclass
class PositionAim:
    depth: int
    position_horizontal: int
    aim: int

    def apply_position(self, position):
        self.aim += position.depth
        self.position_horizontal += position.position_horizontal
        self.depth += self.aim * position.position_horizontal


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("input")
    args = parser.parse_args()

    positions = []
    with open(args.input, "r", encoding="utf-8") as input_file:
        for line in input_file:
            value = int(line.strip().split(" ")[-1])
            if line.startswith("forward"):
                positions.append(Position(0, value))
            elif line.startswith("up"):
                positions.append(Position(-1 * value, 0))
            elif line.startswith("down"):
                positions.append(Position(value, 0))
            else:
                raise Exception("Invalid input")
    final = sum(positions, start=Position(0, 0))
    final_aim = PositionAim(0, 0, 0)
    for position in positions:
        final_aim.apply_position(position)
    print(f"Part 1: {final.position_horizontal * final.depth}")
    print(f"Part 2: {final_aim.position_horizontal * final_aim.depth}")

if __name__ == "__main__":
    main()
