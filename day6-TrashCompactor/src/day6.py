# day 4 - main.py
from aocSTD import *;
from typing import List
from enum import Enum

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

    problems: list[list[str]] = [];
    for line in dataLines:
        problems.append(line.split());
    stackLength: int = len(problems);

    class sumType(Enum):
        ADD = 0,
        MULT = 1

    sumTotalProblems: int = 0;
    for i in range(len(problems[0])):
        numbers: list[int] = [];
        sType: sumType = None;
        for j in range(stackLength -1, -1, -1):
            value: str = problems[j][i];
            if value == '*': sType = sumType.MULT;
            if value == '+': sType = sumType.ADD;
            if value == "*" or value == "+": continue;
            numbers.append(int(value))

        smallSum: int = 0;
        match sType:
            case sumType.ADD:
                for num in numbers:
                    smallSum += num;
            case sumType.MULT:
                smallSum = 1;
                for num in numbers:
                    smallSum *= num;
        sumTotalProblems += smallSum;

    ##############################################################

    newData: list[str] = [];
    for line in dataLines:
        newData.append(line.replace(" ", "=") + "=");

    sectionIndexs: list[int] = [];
    lengthLines: int = len(newData);
    lengthChars: int = len(newData[0]);

    badMathTotal: int = 0;
    sType: sumType = None;
    numbers: list[int] = []
    for i in range(lengthChars):
        smallNumbers: list[str] = [];
        breakSum: int = 0;
        for j in range(lengthLines):
            value: str = newData[j][i];
            if value == '*': sType = sumType.MULT;
            if value == '+': sType = sumType.ADD;
            if value in "*+=":
                breakSum += 1;
                continue;
            smallNumbers.append(value);
        if smallNumbers != []:
            numbers.append(int("".join(smallNumbers)));
        if breakSum == lengthLines:
            print(numbers, sType)
            smallSum: int = 0;
            match sType:
                case sumType.ADD:
                    for num in numbers:
                        smallSum += num;
                case sumType.MULT:
                    smallSum = 1;
                    for num in numbers:
                        smallSum *= num;
            numbers = [];
            badMathTotal += smallSum;


    print(f"Problem Total: {sumTotalProblems}");
    print(f"Bad-Math Total: {badMathTotal}");




if __name__ == "__main__":
    main();
