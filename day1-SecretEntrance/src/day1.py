# day 1 - main.py
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
        data = content.split("\n");

    return data, None;

def clampDial(value: int) -> int:
    if value < 0: value = 99;
    if value > 99: value = 0;
    return value;

def extractDialInput(action: str) -> tuple[int, int]:
    return (+1 if action[0].lower() == "r" else -1), (int(action[1:]));

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

    if err:
        print(f"ERROR: {err}");
        return;

    clicks = 0;
    zeroes = 0;
    head = 50;
    for action in data:
        direction: int;
        step: int;
        direction, step = extractDialInput(action);

        for i in range(step):
            head = clampDial(head + direction);
            if head == 0:
                zeroes += 1;
        if head == 0:
            clicks += 1;

    print(f"Num Clicks: {clicks}");
    print(f"Num Zeroes: {zeroes}");


if __name__ == "__main__":
    main();
