def evaluate(file_contents):
    t = ["true", "false", "nil"]
    s = ['+', '-']
    str = ''
    long_string = file_contents
    for token in file_contents.split():
        if '(' in token or ')' in token:
            token = token.replace('(', "").replace(')', "")
        if token[0] >= '0' and token[0] <= '9':
            if '.' in token:
                print(float(token))
            else:
                print(token)
        elif token[0] == '"':
            for i in long_string:
                if i != '(' and i != ')' and i != '"':
                    str += i
            print(str)