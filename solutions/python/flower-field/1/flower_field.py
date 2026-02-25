def annotate(garden):
    # Function body starts here
    if garden == []:
        return garden
    
    result = []
    temp_string = ''
    temp = []
    count = 0
    length = len(garden[0]) - 1

    
    
    for i, string in enumerate(garden):
        temp = list(string)
        if len(string) - 1 != length:
            raise ValueError("The board is invalid with current input.")
        for j, char in enumerate(temp):
            if char == "*":
                temp_string += '*'
            elif char == ' ':
                if j > 0:
                    if temp[j-1] == '*':
                        count += 1

                if j < length:
                    if temp[j+1] == '*':
                        count += 1

                if i > 0:
                    temp_1 = list(garden[i - 1])

                    if j > 0:
                        if temp_1[j-1] == '*':
                            count += 1

                    if temp_1[j] == '*':
                        count += 1
                            
                    if j < length:
                        if temp_1[j+1] == '*':
                            count += 1

                if i < len(garden) - 1:
                    temp_2 = list(garden[i + 1])
                    
                    if j > 0:
                        if temp_2[j-1] == '*':
                            count += 1
    
                    if temp_2[j] == '*':
                        count += 1
    
                    if j < length:
                        if temp_2[j+1] == '*':
                            count += 1
                
                if count == 0:
                    temp_string += ' '
                else:                    
                    temp_string += str(count)
                    count = 0
            else:
                raise ValueError("The board is invalid with current input.")
        result.append(temp_string)
        temp_string = ''

    return result