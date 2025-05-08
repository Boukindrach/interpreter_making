import sys


def main():
    if len(sys.argv) < 3:
        print("Usage: ./your_program.sh tokenize <filename>", file=sys.stderr)
        exit(1)

    command = sys.argv[1]
    filename = sys.argv[2]

    if command != "tokenize":
        print(f"Unknown command: {command}", file=sys.stderr)
        exit(1)

    with open(filename) as file:
        file_contents = file.read()

    # You can use print statements as follows for debugging, they'll be visible when running tests.
    print("Logs from your program will appear here!", file=sys.stderr)

    # Uncomment this block to pass the first stage
    if file_contents:
        valid_tokens = {'(': "LEFT_PAREN ( null",
                        ')': "RIGHT_PAREN ) null",
                        '{': "LEFT_BRACE { null",
                        '}': "RIGHT_BRACE } null",
                        '-': "MINUS - null",
                        '+': "PLUS + null",
                        '.': "DOT . null",
                        '*': "STAR * null",
                        '/': "SLASH / null",
                        ';': "SEMICOLON ; null",
                        ',': "COMMA , null",
                        '=': "EQUAL = null"
                        }
        Error = False
        i = 0
        while i < len(file_contents):
            if file_contents[i] in valid_tokens:
                if file_contents[i] == "=" and file_contents[i + 1] == '=' and i + 1 < len(file_contents):
                    print(f"EQUAL_EQUAL == null")
                    i += 2
                else:
                    print(valid_tokens[file_contents[i]])
                    i += 1
            else:
                print(f"[line 1] Error: Unexpected character: {file_contents[i]}", file=sys.stderr)
                i += 1
                Error = True
            
        print("EOF  null")
        if Error:
            sys.exit(65)

    else:
        print("EOF  null") # Placeholder, remove this line when implementing the scanner


if __name__ == "__main__":
    main()
