def commands(binary_str):

    binary_str = int(binary_str)
    result = []
    if binary_str%10 == 1:
        result.append('wink')
    
    binary_str //= 10

    if binary_str%10 == 1:
        result.append('double blink')
    
    binary_str //= 10

    if binary_str%10 == 1:
        result.append('close your eyes')
    
    binary_str //= 10

    if binary_str%10 == 1:
        result.append('jump')
    
    binary_str //= 10

    if binary_str == 1:
        result.reverse()

    return result