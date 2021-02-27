import sys
from typing import TextIO


def print_with_line_numbers(file_stream: TextIO, start_index: int) -> None:
    index = start_index

    for line in file_stream:
        if line.strip():
            print(f"{index}\t", end="")
            index += 1
        print(line, end="")


def get_next_start_index(file_stream: TextIO, start_index: int) -> int:
    delta = 0
    for line in file_stream:
        if line.strip():
            delta += 1
    return start_index + delta


def main(*files: str) -> None:
    start_index = 1
    for file in files:
        try:
            with open(file, "r") as f:
                print_with_line_numbers(f, start_index)
                f.seek(0)
                start_index = get_next_start_index(f, start_index)
        except FileNotFoundError:
            print(f"nl: {file}: No such file or directory")


if __name__ == "__main__":
    if len(sys.argv) > 1:
        main(*sys.argv[1:])
    else:
        print("Error: specify the path to the file.")
