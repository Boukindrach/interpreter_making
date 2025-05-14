import re

def parse(file_contents):
    if not file_contents:
        return

    # Regex: match strings in quotes, or parentheses, or other non-space sequences
    token_pattern = r'"[^"\n]*"|[()]|\S+'
    tokens = re.findall(token_pattern, file_contents)
    i = 0

    def is_boolean(token):
        return token in ["true", "false", "nil"]

    def is_number(token):
        try:
            float(token)
            return True
        except ValueError:
            return False

    def is_string(token):
        return token.startswith('"') and token.endswith('"')

    def parse_expression():
        nonlocal i
        if i >= len(tokens):
            return None

        token = tokens[i]

        if token == "(":
            i += 1
            inner = parse_expression()
            if i >= len(tokens) or tokens[i] != ")":
                print("Error: unmatched '('")
                exit(1)
            i += 1
            return f"(group {inner})"
        elif is_string(token):
            i += 1
            return token[1:-1]  # Strip surrounding quotes
        elif is_boolean(token):
            i += 1
            return token
        elif is_number(token):
            i += 1
            return str(float(token)).rstrip("0").rstrip(".") if "." in token else token
        else:
            i += 1
            return token

    while i < len(tokens):
        expr = parse_expression()
        if expr:
            print(expr)

