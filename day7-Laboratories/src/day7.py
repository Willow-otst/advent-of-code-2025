# day 4 - main.py
from aocSTD import *;
from typing import List
from enum import Enum

class Coard:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return isinstance(other, Coard) and self.x == other.x and self.y == other.y

    def __hash__(self):
        return hash((self.x, self.y))


def main():
    path: str;
    path = "input/testInput.txt"  if len(sys.argv[1:]) < 1 else sys.argv[1];

    print("Arguments:", sys.argv[1:]);
    print("Path:", path, "\n");

    if not aocSTD_getPathExists(path):
        return;

    dataLines: list[str];
    dataLines = aocSTD_parseFileInput_Lines(path);

    ##############################################################

    TotalBeamSplits: int = 0
    beamCoards: set[Coard] = set();

    for y in range(len(dataLines)):
        for x in range(len(dataLines[y])):
            match dataLines[y][x]:
                case 'S':
                    beamCoards.add(Coard(x, y+1));
                case '^':
                    if Coard(x, y-1) in beamCoards:
                        TotalBeamSplits += 1;
                    beamCoards.add(Coard(x-1, y));
                    beamCoards.add(Coard(x+1, y));
                case '.':
                    if Coard(x, y-1) in beamCoards:
                        beamCoards.add(Coard(x, y));
                case '|':
                    pass
                case _:
                    raise ValueError(f"Unexpected character: {char}");

    dataLinesNew: list[str] = [];
    for y in range(len(dataLines)):
        newLineChars: list[chr] = []
        for x in range(len(dataLines[y])):
            char: chr = '|' if Coard(x, y) in beamCoards else dataLines[y][x];
            print(char, end="");

            char = '0' if char == '|' else char;
            newLineChars.append(char);
        dataLinesNew.append("".join(newLineChars));

        print();

    ##############################################################
    print();

    dataGrid: list[list[str]] = [];

    dataLinesNew.reverse();
    for y in range(len(dataLinesNew)):
        lineChars: list[str] = [];
        for x in range(len(dataLinesNew[y])):
            char: chr = dataLinesNew[y][x];
            # print(char, end="");

            lineChars.append(char);
        dataGrid.append(lineChars);
        # print();

    TotalTimeLines: int = 0;

    print();
    for y in range(len(dataGrid)):
        for x in range(len(dataGrid[y])):
            char: str = dataGrid[y][x];

            if y == 0 and char.isdigit() and int(char) == 0:
                dataGrid[y][x] = str(1);
                print(" " + dataGrid[y][x], end="");

                continue;

            if char == "0":
                dataGrid[y][x] = dataGrid[y-1][x];

            print(" " + dataGrid[y][x], end="");

        for x in range(len(dataGrid[y])):
            char: str = dataGrid[y][x];
            if char == "^":
                a: int = int(dataGrid[y][x-1]);
                b: int = int(dataGrid[y][x+1]);
                dataGrid[y+1][x] = str(a+b);

            if char == "S":
                TotalTimeLines = dataGrid[y-1][x];
        print();

    ##############################################################
    print(f"Total Beam Splits: {TotalBeamSplits}");
    print(f"Total Time Lines: {TotalTimeLines}");




if __name__ == "__main__":
    main();
