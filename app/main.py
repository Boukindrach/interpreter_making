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
        valid_tokens = ['(', ')', '{', '}', '-', '+', '.', '*', '/', ';', ',']
        for i in file_contents:
            if i in valid_tokens:
                if i == '(':
                    print(f"LEFT_PAREN {i} null")
                elif i == ')':
                    print(f"RIGHT_PAREN {i} null")
                elif i == '{':
                    print(f"LEFT_BRACE {i} null")
                elif i == "}":
                    print(f"RIGHT_BRACE {i} null")
                elif i == ",":
                    print(f"COMMA {i} null")
                elif i == ".":
                    print(f"DOT {i} null")
                elif i == "-":
                    print(f"MINUS {i} null")
                elif i == "+":
                    print(f"PLUS {i} null")
                elif i == "*":
                    print(f"STAR {i} null")
                elif i == "/":
                    print(f"SLASH {i} null")
                elif i == ";":
                    print(f"SEMICOLON {i} null")
            else:
                print(f"[line 1] Error: Unexpected character: {i}", file=sys.stderr)
                Error = True
            
        print("EOF  null")
        if Error:
            sys.exit(65)

    else:
        print("EOF  null") # Placeholder, remove this line when implementing the scanner


if __name__ == "__main__":
    main()
