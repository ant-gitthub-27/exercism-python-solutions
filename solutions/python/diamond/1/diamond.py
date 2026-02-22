def rows(letter):
    alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    index = 0
    
    if letter in alphabet:
        index = alphabet.index(letter) + 1

    half_diamond = []
    string = ''
    for i in range(0, index):
        if i == 0:
            string += ' ' * max(index - 1 - i, 0) + alphabet[i] + ' ' * max(index - 1 - i, 0)
        else:
            string += ' ' * max(index - 1 - i, 0) + alphabet[i] + ' ' * max(2*i - 1, 0) + alphabet[i] + ' ' * max(index - 1 - i, 0)

        half_diamond.append(string)
        string = ''

    full_diamond = half_diamond
    i = index - 2
    while i >= 0:
        full_diamond.append(half_diamond[i])
        i -= 1

    return full_diamond