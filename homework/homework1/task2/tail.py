import sys
from typing import TextIO


def print_tail(file_stream: TextIO, number_of_lines: int = 10):
    stack = []
    lines = reversed(file_stream.readlines())
    for index, line in enumerate(lines, start=1):
        if index > number_of_lines:
            break
        stack.append(line)

    while stack:
        print(stack.pop(), end="")


def main(*files: str):
    for file in files:
        try:
            with open(file, "r") as f:
                if len(files) > 1:
                    print(f"==> {f.name} <==")
                print_tail(f)
        except FileNotFoundError:
            print(f"tail: cannot open '{file}' for reading: No such file or directory")


if __name__ == "__main__":
    if len(sys.argv) > 1:
        main(*sys.argv[1:])
    else:
        print("Error: specify the path to the file.")
