def parse(file_contents):
    if not file_contents:
        return

    tokens = list(file_contents.replace("(", " ( ").replace(")", " ) ").split())
    i = 0

    def parse_expression():
        nonlocal i

        if i >= len(tokens):
            return None

        token = tokens[i]

        if token == "(":
            i += 1
            expr = parse_expression()
            if i >= len(tokens) or tokens[i] != ")":
                print("Error: unmatched '('")
                exit(1)
            i += 1
            return f"(group {expr})"

        elif token.startswith('"') and token.endswith('"'):
            i += 1
            return token[1:-1]

        elif token in ["true", "false", "nil"]:
            i += 1
            return token

        else:
            try:
                float(token)
                i += 1
                return token.rstrip('0').rstrip('.') if '.' in token else token
            except ValueError:
                pass

        i += 1
        return token

    while i < len(tokens):
        expr = parse_expression()
        if expr:
            print(expr, end=" ")
    print("")

