def parse(file_contects):
    if file_contects:
        num_list = []
        other = []
        i = 0
        num_str = ""
        while i < len(file_contects):
            num_str = ""
            while i < len(file_contects) and file_contects[i].isdigit():
                num_str += file_contects[i]
                i += 1
                if file_contects[i] == ' ':
                    num_list.append(num_str + '.0')
                    i += 1
                    break
            while i < len(file_contects) and not file_contects[i].isdigit():
                other.append(file_contects[i])
                i += 1
        print("(" + ''.join(other) + ' '.join(num_list) + ")")