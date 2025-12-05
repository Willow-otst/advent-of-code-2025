import os
import sys
from typing import List

def aocSTD_getUser_YesNo(prompt: str = "Continue?") -> bool:
    while True:
        prompt += " (y/n): ";
        responce: str = input(prompt).lower();

        if responce == "y":
            return True;
        elif responce == "n":
            return False;
        else:
            print("Invalid input.\n");

def aocSTD_getPathExists(path: str) -> bool:
    if not aocSTD_getUser_YesNo(f"Is '{path}' Correct?"):
        print(f"WARNING - User Denied Path, PATH: '{path}'");
        return False;

    if not os.path.exists(path):
        print(f"ERROR - Path does not Exist!, PATH: '{path}'")
        return False;

    return True;

def aocSTD_parseFileInput_Lines(path: str) -> list[str]:
    dataLines: list[str] = [];

    with open(path, "r") as f:
        content: str = f.read();
        content = content.rstrip("\n");
        dataLines = content.split("\n");

    return dataLines;

def aocSTD_parseDataParts(dataLine: str, delimiter: chr) -> list[str]:
    dataParts: list[str] = [];
    if delimiter == '': return list(dataLine);
    dataParts = dataLine.split(delimiter);

    return dataParts;
