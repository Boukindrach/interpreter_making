def evaluate(file_contents):
    t = ["true", "false", "nil"]
    s = ['+', '-']
    str = ''
    i = 0
    for token in file_contents.split():
        print(token)