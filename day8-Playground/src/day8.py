# day 4 - main.py
from aocSTD import *;
from typing import List
from enum import Enum

class Coard:
    def __init__(self, x: float, y: float, z: float) -> None:
        self.x = x;
        self.y = y;
        self.z = z;

        self.packValue = 1;
        self.packed: bool = False;

    def __str__(self) -> str:
        return f"Coard({self.x}, {self.y}, {self.z})"

    def distance_to(self, other) -> float:
        dx: float = self.x - other.x;
        dy: float = self.y - other.y;
        dz: float = self.z - other.z;
        return ((dx * dx) + (dy * dy) + (dz * dz)) ** 0.5;

def FindAllCoardPairs(coards: list[Coard]) -> list[tuple[Coard, Coard, float]]:
    pairs: list[tuple[Coard, Coard, float]] = [];

    for i in range(len(coards)):
        for j in range(i + 1, len(coards)):
            dist = coards[i].distance_to(coards[j]);
            pairs.append((coards[i], coards[j], dist));

    return pairs

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

    Coards: list[Coard] = [];
    for line in dataLines:
        x: str;     y: str;     z: str;
        x, y, z = line.split(',');

        coard: Coard = Coard(float(x), float(y), float(z));
        Coards.append(coard);

    # for coard in Coards:
        # print(coard);
    # print();

    CoardPairs: list[tuple[Coard, Coard, float]] = FindAllCoardPairs(Coards);
    CoardPairs.sort(key=lambda pair: pair[2]);

    for pair in CoardPairs:
        c1: Coard;
        c2: Coard;
        dist: float;

        c1, c2, dist = pair;

        # print(c1, c2, dist);
    # print();

    # 10 for testInput, 1000 for regular Input
    MAX_PAIRS: int = 10 if ("test" in path) else 1000;

    CoardGroups: list[set[Coard]] = [];
    for pair in CoardPairs[:MAX_PAIRS]:
        c1: Coard;  c2: Coard;  dist: float;
        c1, c2, dist = pair;

        g1: set[Coard] = None;
        g2: set[Coard] = None;

        for group in CoardGroups:
            if c1 in group: g1 = group;
            if c2 in group: g2 = group;

        if g1 is not None and g1 is g2: continue;

        if g1 is not None and g2 is not None:
            g1.update(g2);
            CoardGroups.remove(g2);
            continue;

        if g1 is not None:
            g1.add(c2);
            continue;
        if g2 is not None:
            g2.add(c1);
            continue;

        CoardGroups.append({c1, c2});

    CoardGroups.sort(key=len, reverse=True);

    Product3Largest: int = 1;
    for group in CoardGroups[:3]:
        print(len(group))
        Product3Largest *= len(group);
        for coard in group:
            pass;
            print(coard);
        print();

    ##############################################################

    MergePair: list[Coard] = None;

    CoardGroups: list[set[Coard]] = [];
    for pair in CoardPairs:
        c1: Coard;  c2: Coard;  dist: float;
        c1, c2, dist = pair;

        g1: set[Coard] = None;
        g2: set[Coard] = None;

        for group in CoardGroups:
            if c1 in group: g1 = group;
            if c2 in group: g2 = group;

        if g1 is not None and g1 is g2: continue;

        if g1 is not None and g2 is not None:
            g1.update(g2);
            CoardGroups.remove(g2);

            MergePair = [c1, c2];

        elif g1 is not None:
            g1.add(c2);
            MergePair = [c1, c2];
        elif g2 is not None:
            g2.add(c1);
            MergePair = [c1, c2];

        else:
            CoardGroups.append({c1, c2});
            MergePair = [c1, c2];

        if len(CoardGroups) == 1 and len(next(iter(CoardGroups))) == len(Coards):
            break

    ProductMergePair: int = 1;
    c1: Coard;
    c2: Coard;
    c1, c2 = MergePair;

    ProductMergePair *= int(c1.x);
    ProductMergePair *= int(c2.x);

    print(c1, c2);
    print();

    ##############################################################
    print(f"Product 3 Largest: {Product3Largest}");
    print(f"Product Merge Pair: {ProductMergePair}");



if __name__ == "__main__":
    main();
