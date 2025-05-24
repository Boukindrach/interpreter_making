def evaluate(file_contents):
    t = ["true", "false", "nil"]
    s = ['+', '-']
    str = ''
    long_string = file_contents
    for token in file_contents.split():
        if '(' in token or ')' in token:
            token = token.replace('(', "").replace(')', "")
        if token in t:
            print(token)
            return
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
            return
        elif token[0] == '!':
            j = 0
            for i in range(0, len(token)):
                if token[i] == '!':
                    j += 1
                else:
                    break
            if j % 2 != 0:
                if token[1:] == "true":
                    print('false')
                    return
                elif token[1:] == "false" or token[1:] == "nil":
                    print('true')
                    return
                else:
                    print('false')
            else:
                if token[1:] in t:
                    print(token[1:])
                    return
                else:
                    print('true')
                    return
        else:
            print(token)