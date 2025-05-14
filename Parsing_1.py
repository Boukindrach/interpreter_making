def parse(file_contects):
    if file_contects:
        i = 0
        num_list = []
        other = []
        str_ = ''
        while i < len(file_contects):
            if 'a' <= file_contects[i] <= 'z':
                a_str = ""
                while i < len(file_contects) and 'a' <= file_contects[i] <= 'z':
                    a_str += file_contects[i]
                    if file_contects[i] == " ":
                        break
                    i += 1
                print(a_str)
                exit(0)
            elif file_contects[i].isdigit():
                num = []
                while (i < len(file_contects)) and (file_contects[i].isdigit() or file_contects[i] == '.'):
                    num.append(file_contects[i])
                    i += 1
                if '.' not in num:
                    num += ".0"
                    num_list.append(''.join(num))
                else:
                    num_list.append(''.join(num))
            elif file_contects[i] == '"':
                str_1 = ""
                i += 1
                while i < len(file_contects):
                    str_1 += file_contects[i]
                    i += 1
                    if i < len(file_contects) and file_contects[i] == '"':
                        i += 1
                        break
                    if not i < len(file_contects):
                        exit(1)
                print(str_1)
            elif not file_contects[i].isspace():
                str_ = []
                while i < len(file_contects) and not file_contects[i].isspace() and not file_contects[i].isdigit():
                    str_.append(file_contects[i])
                    i += 1
                other.append(''.join(str_))
            else:
                i += 1
        if other and num_list:
            print("("+ ''.join(other) + ' ' + ' '.join(num_list) + ")")
        elif other:
            print("("+ ''.join(other) + ")")
        elif num_list:
            print(' '.join(num_list))