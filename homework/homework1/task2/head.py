import sys
from typing import TextIO


def print_head(file_stream: TextIO, number_of_lines: int = 10) -> None:
    for index, line in enumerate(file_stream, start=1):
        if index > number_of_lines:
            break
        print(line, end="")


def main(*files: str) -> None:
    for file in files:
        try:
            with open(file, "r") as f:
                if len(files) > 1:
                    print(f"==> {f.name} <==")
                print_head(f)
        except FileNotFoundError:
            print(f"head: cannot open '{file}' for reading: No such file or directory")


if __name__ == "__main__":
    if len(sys.argv) > 1:
        main(*sys.argv[1:])
    else:
        print("Error: specify the path to the file.")
