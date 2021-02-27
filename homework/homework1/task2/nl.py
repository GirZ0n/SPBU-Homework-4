import sys
from typing import TextIO


def print_with_line_numbers(file_stream: TextIO, start_index: int) -> int:
    index = start_index

    for line in file_stream:
        if line.strip():
            print(f"{index} ", end="")
            index += 1
        print(line, end="")

    return index


def main(*files: str) -> None:
    start_index = 1
    for file in files:
        try:
            with open(file, "r") as f:
                start_index = print_with_line_numbers(f, start_index)
        except FileNotFoundError:
            print(f"nl: {file}: No such file or directory")


if __name__ == "__main__":
    if len(sys.argv) > 1:
        main(*sys.argv[1:])
    else:
        print("Error: specify the path to the file.")
