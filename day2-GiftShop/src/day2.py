# day 2 - main.py
import os
import sys
from typing import List

def getUser_YesNo(prompt: str = "Continue?") -> bool:
    while True:
        prompt += " (y/n): ";
        responce: str = input(prompt).lower();

        if responce == "y":
            return True;
        elif responce == "n":
            return False;
        else:
            print("Invalid input.\n");

def getPathExists(path: str) -> bool:
    if not os.path.exists(path):
        print(f"ERROR - Path does not Exist!, PATH: '{path}'")
        return False;

    return True;

def parseFileInput(path: str) -> tuple[list[str], str]:
    data: list[str] = [];

    with open(path, "r") as f:
        content: str = f.read();
        content = content.rstrip("\n");
        data = content.split(",");

    return data, None;

def isOddLength(value: str) -> bool:
    return len(value) % 2 == 0;

def isValidID(value: int) -> bool:
    strVal = str(value);
    center: str = len(strVal) // 2;
    a: str = strVal[:center];
    b: str = strVal[center:];
    if a == b:
        return False;

    return True;

def getFactors(value: int) -> list[int]:
    factors: list[int] = [];
    for i in range(1, value + 1):
        if (value % i) == 0: factors.append(i);
    return factors;

def main():
    if len(sys.argv[1:]) < 1:
        print("No input Given!");
        return;

    print("Arguments:", sys.argv[1:], "\n");

    path: str = sys.argv[1];
    if not getUser_YesNo(f"Is '{path}' Correct?"):
        print("Exiting...");
        return;

    if not getPathExists(path):
        return;

    data: list[str];
    err: str;
    data, err = parseFileInput(path)

    sumPairIDs: int = 0;
    for valRange in data:
        start: int;
        end: int;
        start, end = map(int, valRange.split("-"));

        for i in range(start, end + 1):

            if not isOddLength(str(i)): continue
            if not isValidID(i):
                sumPairIDs += i;

    print("ID Sum Pairs: ", sumPairIDs);

    sumRepeatIDs: int = 0;
    for valRange in data:
        start: int;
        end: int;
        start, end = map(int, valRange.split("-"));

        for i in range(start, end + 1):
            strID: str = str(i);
            factors: list[int] = getFactors(len(strID));
            factors.reverse();

            for factor in factors:
                if factor == 1: continue;
                head: int = 0;
                parts: set[str] = set();
                step: int = len(strID) // factor;
                while head < len(strID):
                    parts.add(strID[head:head+step])
                    head += step;

                if len(parts) == 1:
                    sumRepeatIDs += i;
                    break;
    print("ID Sum Repeats: ", sumRepeatIDs);

if __name__ == "__main__":
    main();
