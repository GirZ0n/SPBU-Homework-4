import sys
from dataclasses import dataclass
from typing import TextIO


@dataclass
class FileInformation:
    file_name: str
    number_of_lines: int = 0
    number_of_words: int = 0
    number_of_bytes: int = 0

    def __str__(self) -> str:
        return f"{self.number_of_lines}\t{self.number_of_words}\t{self.number_of_bytes}\t{self.file_name}"


def get_file_information(file_stream: TextIO) -> FileInformation:
    info = FileInformation(file_stream.name)

    for line in file_stream:
        info.number_of_lines += 1
        info.number_of_words += len(line.split())
        info.number_of_bytes += len(bytes(line, encoding="utf8"))

    return info


def main(*files: str) -> None:
    total = FileInformation("total")

    for file in files:
        try:
            with open(file) as f:
                info = get_file_information(f)
                total.number_of_lines += info.number_of_lines
                total.number_of_words += info.number_of_words
                total.number_of_bytes += info.number_of_bytes
                print(info)
        except FileNotFoundError:
            print(f"wc: {file}: No such file or directory")

    if len(files) > 1:
        print(total)


if __name__ == "__main__":
    if len(sys.argv) > 1:
        main(*sys.argv[1:])
    else:
        print("Error: specify the path to the file.")
