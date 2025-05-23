def parse(file_contents):
    if not file_contents:
        return

    tokens = list(file_contents.replace("(", " ( ").replace(")", " ) ").split())
    i = 0

    def parse_expression():
        return parse_term()

    def parse_term():
        nonlocal i
        expr = parse_factor()

        while i < len(tokens) and tokens[i] in ['+', '-']:
            op = tokens[i]
            i += 1
            right = parse_factor()
            expr = f"({op} {expr} {right})"

        return expr

    def parse_factor():
        nonlocal i

        if i >= len(tokens):
            print("Error: Unexpected end of input")
            exit(1)

        token = tokens[i]

        if token == "(":
            i += 1
            expr = parse_expression()
            if i >= len(tokens) or tokens[i] != ")":
                print("Error: unmatched '('")
                exit(1)
            i += 1
            return f"(group {expr})"

        elif token in ("-", "!"):
            op = token
            i += 1
            right = parse_factor()
            if op == "-":
                return f"(negate {right})"
            else:
                return f"(! {right})"

        elif token in ["true", "false", "nil"]:
            i += 1
            return token

        elif token.startswith('"') and token.endswith('"'):
            i += 1
            return token[1:-1]

        else:
            try:
                num = float(token)
                i += 1
                return f"{num:.1f}"
            except ValueError:
                i += 1
                return token

    while i < len(tokens):
        print(parse_expression())


