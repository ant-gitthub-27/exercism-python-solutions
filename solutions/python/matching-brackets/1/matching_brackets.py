def is_paired(input_string):
    
    a = input_string.count("(")
    b = input_string.count(")")
    c = input_string.count("[")
    d = input_string.count("]")
    e = input_string.count("{")
    f = input_string.count("}")


    list = []
    bracket_dict = {')':'(', ']':'[', '}':'{'}
    for char in input_string:
        if char in bracket_dict.values():
            list.append(char)
        elif char in bracket_dict:
            if not list or list.pop() != bracket_dict[char]:
                return False
    
    return len(list) == 0
    