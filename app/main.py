import sys
import string


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
                        '=': "EQUAL = null",
                        '!': "BANG ! null",
                        '>': "GREATER > null",
                        '<': "LESS < null",
                        '"': "String"
                        }
        Error = False
        i = 0
        line = 1
        while i < len(file_contents):
            if file_contents[i] in ('\n', '\t', ' '):
                if file_contents[i] == '\n':
                    line += 1
                i += 1
            elif file_contents[i] in valid_tokens and file_contents[i] != '"':
                if file_contents[i] == "=" and i + 1 < len(file_contents) and file_contents[i + 1] == '=':
                    print(f"EQUAL_EQUAL == null")
                    i += 2
                elif file_contents[i] == "!" and i + 1 < len(file_contents) and file_contents[i + 1] == '=':
                    print(f"BANG_EQUAL != null")
                    i += 2
                elif file_contents[i] == "<" and i + 1 < len(file_contents) and file_contents[i + 1] == '=':
                    print(f"LESS_EQUAL <= null")
                    i += 2
                elif file_contents[i] == ">" and i + 1 < len(file_contents) and file_contents[i + 1] == '=':
                    print(f"GREATER_EQUAL >= null")
                    i += 2
                elif file_contents[i] == "/" and i + 1 < len(file_contents) and file_contents[i + 1] == '/':
                    while i < len(file_contents) and file_contents[i] != '\n':
                        i += 1
                else:
                    print(valid_tokens[file_contents[i]])
                    i += 1
            elif file_contents[i].isdigit():
                num_str=''
                while i < len(file_contents) and file_contents[i].isdigit():
                    num_str += file_contents[i]
                    i += 1
                    if i + 1 < len(file_contents) and file_contents[i] == '.' and file_contents[i + 1].isdigit():
                        num_str += file_contents[i]
                        i += 1
                if '.' not in num_str:
                    f = num_str
                    f += '.0'
                    print(f"NUMBER {num_str} {f}")
                else:
                    print(f"NUMBER {num_str} {float(num_str)}")
            elif file_contents[i] == '"':
                q = 1
                str = ""
                while i < len(file_contents) and file_contents[i] != '\n':
                    str += file_contents[i]
                    i += 1
                    if i < len(file_contents) and file_contents[i] == '"':
                        q += 1
                        i += 1
                        str += '"'
                        break
                if q == 2:
                    print(f"STRING {str} {str[1:-1]}")
                else:
                    print(f"[line {line}] Error: Unterminated string.", file=sys.stderr)
                    Error = True
            else:
                print(f"[line {line}] Error: Unexpected character: {file_contents[i]}", file=sys.stderr)
                i += 1
                Error = True
            
        print("EOF  null")
        if Error:
            sys.exit(65)
    else:
        print("EOF  null") # Placeholder, remove this line when implementing the scanner

if __name__ == "__main__":
    main()
