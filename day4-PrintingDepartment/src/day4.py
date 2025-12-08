# day 4 - main.py
from aocSTD import *;
from typing import List

class Vec2:
    def __init__(self, x:int = 0, y: int = 0):
        self.x = x;
        self.y = y;

    def __str__(self):
        return f"({self.x}, {self.y})";

    def __add__(self, other):
        return Vec2(self.x + other.x, self.y + other.y);

    def __sub__(self, other):
        return Vec2(self.x - other.x, self.y - other.y);

    def __lt__(self, other):
        return self.x < other.x and self.y < other.y;

    def __gt__(self, other):
        return self.x > other.x and self.y > other.y;

    def __eq__(self, other):
        return (self.x == other.x) and (self.y == other.y);

    def __ne__(self, other):
        return not self.__eq__(other);


def cellIsPaper(pos: Vec2, grid: list[str]) -> bool:
    return grid[pos.y][pos.x] == '@';

def sumPaperInSlice(pos: Vec2, grid: list[str]) -> int:
    start = Vec2(max(pos.x - 1, 0), max(pos.y - 1, 0));
    end   = Vec2(min(pos.x + 2, len(grid[0])), min(pos.y + 2, len(grid)));

    count = 0;
    for y in range(start.y, end.y):
        for x in range(start.x, end.x):
            if cellIsPaper(Vec2(x, y), grid):
                count += 1;

    if cellIsPaper(pos, grid):
        count -= 1;

    return count


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

    initialPickablePaper: int = 0;

    gridSize: Vec2 = Vec2(len(dataLines[0]), len(dataLines));
    for y in range(gridSize.y):
        for x in range(gridSize.x):
            pos: Vec2 = Vec2(x, y);
            hits: int = sumPaperInSlice(pos, dataLines);
            if hits < 4 and cellIsPaper(pos, dataLines): initialPickablePaper += 1;

    ##############################################################

    totalPickablePaper: int = 0;
    gridSize: Vec2 = Vec2(len(dataLines[0]), len(dataLines));

    picked: bool = True;
    newGrid: list[str] = dataLines;
    while picked:
        picked = False;
        for y in range(gridSize.y):
            line: str = "";
            for x in range(gridSize.x):
                pos: Vec2 = Vec2(x, y);
                hits: int = sumPaperInSlice(pos, dataLines);
                if hits < 4 and cellIsPaper(pos, dataLines):
                    picked = True;
                    line += '.';
                    totalPickablePaper += 1;
                else:
                    line += dataLines[pos.y][pos.x];
            newGrid[y] = line;

    print(f"Init Pickable Paper: {initialPickablePaper}");
    print(f"Total Pickable Paper: {totalPickablePaper}");

if __name__ == "__main__":
    main();
