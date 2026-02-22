def is_paired(input_string):
    brackets_open = "({["
    brackets_closed = ")}]"

    test_list = []
    
    for char in input_string:
        if char in brackets_open:
            test_list.append(char)
        elif char in brackets_closed:
            if not test_list or brackets_open[brackets_closed.index(char)] != test_list.pop():
                return False

    return not test_list
            
            