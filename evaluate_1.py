def evaluate(file_contents):
    t = ["true", "false", "nil"]
    s = ['+', '-']
    str = ''
    long_string = file_contents
    for token in file_contents.split():
        if token[0] >= '0' and token[0] <= '9':
            if '.' in token:
                print(float(token))
            else:
                print(token)
        else:
            if token[0] == '"':
                q = 1
                for i in long_string[1:]:
                    str += i
                    if i == '"':
                        print(str[:-1])
                        return

            else:
                print(token)