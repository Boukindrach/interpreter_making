def evaluate(file_contents):
    t = ["true", "false", "nil"]
    s = ['+', '-', '*', '/']
    str_content = ''
    s_ = []
    number = []
    long_string = file_contents
    
    # Check if we have parentheses - if so, use eval for proper precedence
    has_parentheses = '(' in file_contents or ')' in file_contents
    
    # If we have parentheses, handle the expression differently
    if has_parentheses:
        # First check if it's a string
        if '"' in file_contents:
            for i in long_string:
                if i != '(' and i != ')' and i != '"':
                    str_content += i
            print(str_content.strip())
            return
        
        # Check for boolean or negation tokens (but be careful with negative numbers)
        temp_tokens = file_contents.replace('(', ' ').replace(')', ' ').split()
        for token in temp_tokens:
            if token in t:
                print(token)
                return
            elif token and token[0] == '!' and len(token) > 1:  # Make sure it's not just a minus sign
                j = 0
                for i in range(0, len(token)):
                    if token[i] == '!':
                        j += 1
                    else:
                        break
                if j % 2 != 0:
                    remaining = token[j:]
                    if remaining == "true":
                        print('false')
                        return
                    elif remaining == "false" or remaining == "nil":
                        print('true')
                        return
                    else:
                        print('false')
                        return
                else:
                    remaining = token[j:]
                    if remaining in t:
                        print(remaining)
                        return
                    else:
                        print('true')
                        return
        
        # Check for non-arithmetic identifiers (but exclude numbers and operators)
        for token in temp_tokens:
            if (token and 
                token not in s and 
                token not in t and
                not (token and token[0] >= '0' and token[0] <= '9') and
                not (token and token[0] == '-' and len(token) > 1 and token[1] >= '0' and token[1] <= '9') and
                token[0] != '!'):
                print(token)
                return
        
        # Use eval for arithmetic expressions with parentheses
        try:
            result = eval(file_contents.strip())
            if isinstance(result, float) and result.is_integer():
                print(int(result))
            else:
                print(result)
            return
        except:
            print("Error: Invalid expression")
            return
    
    for token in file_contents.split():
        original_token = token
        if '(' in token or ')' in token:
            token = token.replace('(', "").replace(')', "")
        
        if token in t:
            print(token)
            return
        
        if token and token[0] >= '0' and token[0] <= '9':
            if '.' in token:
                number.append(float(token))
            else:
                number.append(int(token))
        elif token and token[0] == '"':
            for i in long_string:
                if i != '(' and i != ')' and i != '"':
                    str_content += i
            print(str_content.strip())
            return
        elif token and token[0] == '!':
            j = 0
            for i in range(0, len(token)):
                if token[i] == '!':
                    j += 1
                else:
                    break
            if j % 2 != 0:
                remaining = token[j:]
                if remaining == "true":
                    print('false')
                    return
                elif remaining == "false" or remaining == "nil":
                    print('true')
                    return
                else:
                    print('false')
                    return
            else:
                remaining = token[j:]
                if remaining in t:
                    print(remaining)
                    return
                else:
                    print('true')
                    return
        elif token in s:
            s_.append(token)
        elif token:
            print(token)
            return

    if number and not s_:
        print(" ".join(map(str, number)))
        return

    elif number and s_:
        
        expression = []
        
        for i in range(len(number)):
            expression.append(number[i])
            if i < len(s_):
                expression.append(s_[i])
        
        i = 1
        while i < len(expression):
            if i < len(expression) and expression[i] == '*':
                result = expression[i-1] * expression[i+1]
                expression = expression[:i-1] + [result] + expression[i+2:]
                i = max(1, i-1)
            elif i < len(expression) and expression[i] == '/':
                if expression[i+1] == 0:
                    print("Error: Division by zero")
                    return
                result = expression[i-1] / expression[i+1]
                expression = expression[:i-1] + [result] + expression[i+2:]
                i = max(1, i-1)
            else:
                i += 2
        
        i = 1
        while i < len(expression):
            if i < len(expression) and expression[i] == '+':
                result = expression[i-1] + expression[i+1]
                expression = expression[:i-1] + [result] + expression[i+2:]
                i = max(1, i-1)
            elif i < len(expression) and expression[i] == '-':
                result = expression[i-1] - expression[i+1]
                expression = expression[:i-1] + [result] + expression[i+2:]
                i = max(1, i-1)
            else:
                i += 2
        
        if len(expression) == 1:
            result = expression[0]
            if isinstance(result, float) and result.is_integer():
                print(int(result))
            else:
                print(result)
        else:
            print("Error: Invalid expression")