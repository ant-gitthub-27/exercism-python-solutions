def digitise(input_grid):    
    if input_grid[0] == '   ':
        if input_grid[1] == '  |' and input_grid[2] == '  |':
            return '1'
        elif input_grid[1] == '|_|' and input_grid[2] == '  |':
            return '4'
        else:
            return '?'
    elif input_grid[0] == ' _ ':
        if input_grid[1] == '| |' and input_grid[2] == '|_|':
            return '0'
        elif input_grid[1] == '  |' and input_grid[2] == '  |':
                return '7'
        elif input_grid[1] == ' _|':
            if input_grid[2] == '|_ ':
                return '2'
            elif input_grid[2] == ' _|':
                return '3'
            else:
                return '?'
        elif input_grid[1] == '|_|':
            if input_grid[2] == '|_|':
                return '8'
            elif input_grid[2] == ' _|':
                return '9'
            else:
                return '?'
        elif input_grid[1] == '|_ ':
            if input_grid[2] == ' _|':
                return '5'
            elif input_grid[2] == '|_|':
                return '6'
            else:
                return '?'
        else:
            return '?'
    else:
        return '?'

def create_answer(input_grid):
    num_digits = len(input_grid[0]) // 3

    result_string = ''
    rows = input_grid[:3]
    digit = []
    for i in range(num_digits):
        start = i * 3
        end = start + 3
        digit_block = [row[start:end] for row in rows]
        digit.append(digit_block)

    for lis in digit:
        result_string += digitise(lis)

    return result_string
 
def convert(input_grid):
    if len(input_grid) % 4 != 0:
        raise ValueError("Number of input lines is not a multiple of four")
    for char in input_grid:
        if len(char) % 3 != 0:
            raise ValueError("Number of input columns is not a multiple of three")
    result_string = ''
    
    
    list_length = len(input_grid) // 4
    each_set = []
    for i in range(list_length):
        list_rows = input_grid[4*i:4*(i)+4]
        each_set.append(list_rows)

    for listss in each_set:
        result_string += create_answer(listss)
        result_string += ','


    return result_string[:-1]