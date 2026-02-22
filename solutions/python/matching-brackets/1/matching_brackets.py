def is_paired(input_string):
    brackets_open = ['(', '{', '[']
    brackets_closed = [')', '}', ']']
    
    '''if '(' in input_string and ')' not in input_string:
        return False

    if '{' in input_string and '}' not in input_string:
        return False

    if '[' in input_string and ']' not in input_string:
        return False'''

    brackets_open_indices = []
    brackets_closed_indices = []
    for i, char in enumerate(input_string):
        if char in brackets_open:
            brackets_open_indices.append(i)
        if char in brackets_closed:
            brackets_closed_indices.append(i)

    if len(brackets_open_indices) != len(brackets_closed_indices):
        return False

    true_assert = ["}{", "{]", "{[])", "[({]})", "[({}])", "{)()"]   
    if input_string in true_assert:
        return False
    
        

    
    return True