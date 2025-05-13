import sys
import string
from tokenize_1 import tokenize


def main():
    if len(sys.argv) < 3:
        print("Usage: ./your_program.sh tokenize <filename>", file=sys.stderr)
        exit(1)

    command = sys.argv[1]
    filename = sys.argv[2]

    if command == "tokenize":
        print("Logs from your program will appear here!", file=sys.stderr)
        with open(filename) as file:
            file_contents = file.read()
        tokenize(file_contents)

    if command != "tokenize":
        print(f"Unknown command: {command}", file=sys.stderr)
        exit(1)

if __name__ == "__main__":
    main()
