import sys
import string
from tokenize_1 import tokenize
from Parsing_1 import parse


def main():
    if len(sys.argv) < 3:
        print("Usage: ./your_program.sh tokenize <filename>", file=sys.stderr)
        exit(1)

    command = sys.argv[1]
    filename = sys.argv[2]
    commands = ["tokenize", "parse"]

    if command in commands:
        print("Logs from your program will appear here!", file=sys.stderr)
        with open(filename) as file:
            file_contents = file.read()
        if command == commands[0]:
            tokenize(file_contents)
        elif command == commands[1]:
            parse(file_contents)
    
    else:
        print(f"Unknown command: {command}", file=sys.stderr)
        exit(1)

if __name__ == "__main__":
    main()
