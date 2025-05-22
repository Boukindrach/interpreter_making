def parse(file_contects):
    digit = []
    other = []
    string = []
    s = ''
    s_ = ""
    if file_contects:
        for token in file_contects.split():
            if token in ['nil', 'false', 'true']:
                print(token)
                exit(0)
            if token[0] == '"' and token[len(token) - 1] == '"':
                for i in token[1:-1]:
                    string.append(i)
                s = "".join(string)
            elif (token[0] == '(' and token[len(token) - 1] == ')') and (token[1] == '"' and token[len(token) - 2] == '"'):
                for i in token[2:-2]:
                    string.append(i)
                s_ = "".join(string)
            elif isinstance(float(token), float):
                digit.append(str(float(token)))
            else:
                other.append(token)
        if digit and other:
            print("(" + " ".join(other + digit) + ")")
        elif digit:
            print(" ".join(digit))
        elif s:
            print(s)
        elif s_:
            print("(" + "group" + " " + s_ + ")")