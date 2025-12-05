# day 3 - main.py
from aocSTD import *;
from typing import List

def main():
    if len(sys.argv[1:]) < 1:
        print("No input Given!");
        return;

    print("Arguments:", sys.argv[1:], "\n");

    path: str = sys.argv[1];
    if not aocSTD_getPathExists(path):
        return;

    dataLines: list[str];
    dataLines = aocSTD_parseFileInput_Lines(path);

    ##############################################################

    sumBatteries: int = 0;
    for line in dataLines:
        print("Line: ", line);

        pair: list[int] = [];
        for i in range(len(line)):
            value: int = int(line[i]);
            if len(pair) < 2:
                pair.append(value);
                if value > pair[0] and i != len(line)-1:
                    pair.clear();
                    pair.append(value);
                continue;

            if value > pair[0] and i != len(line)-1:
                pair.clear();
                pair.append(value);
                continue;
            if value > pair[1]:
                pair[1] = value;

        join: int = int("".join(map(str, pair)));
        print("Pair: ", pair, "| Join: ", join);
        sumBatteries += join;
        print("\n###########################################\n");

        ###############################################################
    print("###########################################");
    print("###########################################");
    print("###########################################");
    print("###########################################");

    sum12Batteries: int = 0;
    for line in dataLines:
        print("Line:", line);

        trimmed: list[str] = list(line);
        removals: int = len(trimmed) - 12;

        i: int = 0;
        while i < len(trimmed) - 1 and removals > 0:
            if trimmed[i] < trimmed[i + 1]:
                trimmed.pop(i)
                removals -= 1
                if i > 0: i -= 1;
            else: i += 1;

        # drop from the end if removals remain
        while removals > 0:
            trimmed.pop();
            removals -= 1;

        bank: str = "".join(trimmed);
        print(trimmed, "|", bank);

        sum12Batteries += int(bank);
        print("\n###########################################\n");

    print("Sum Batteries: ", sumBatteries);
    print("Sum 12 Batteries: ", sum12Batteries);

if __name__ == "__main__":
    main();
