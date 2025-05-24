def evaluate(file_contents):
    t = ["true", "false", "nil"]
    s = ['+', '-']
    str = ''
    i = 0
    for token in file_contents.split():
        if token[0] >= '0' and token[0] <= '9':
            if '.' in token:
                print(float(token))
            else:
                print(token)
        else:
            if token[0] == '"' and token[-1] == '"':
                print(token[1: -1])
            else:
                print(token)