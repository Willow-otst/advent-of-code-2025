# day 4 - main.py
from aocSTD import *;
from typing import List

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

    rangesSTR: list[str] = dataLines[:dataLines.index("")];
    itemsINT: list[int]  = [int(x) for x in dataLines[dataLines.index("")+1:]];
    itemsINT = sorted(itemsINT);
    ranges: list[list[int, int]] = [list(map(int, r.split('-'))) for r in rangesSTR];
    ranges = sorted(ranges, key=lambda x: x[0]);

    sumSpoiled: int = 0;
    for item in itemsINT:
        fresh: bool = False;
        for x, y in ranges:
            if item >= x and item <= y:
                fresh = True;
                continue;
        if not fresh: sumSpoiled += 1;

    ##############################################################

    merged: list[list[int, int]] = [];
    for start, end in ranges:
        if not merged or start > merged[-1][1]:
            merged.append([start, end]);
        else: merged[-1][1] = max(merged[-1][1], end);

    sumFreshIDs: int = 0;
    for x, y in merged:
        sumFreshIDs += ((y+1) - x);

    print(f"Sum Fresh: {len(itemsINT) - sumSpoiled}");
    print(f"Sum Fresh IDs: {sumFreshIDs}");

if __name__ == "__main__":
    main();
