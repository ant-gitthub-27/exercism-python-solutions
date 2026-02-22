def encode(plain_text):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    reversed_alpha = 'zyxwvutsrqponmlkjihgfedcba'

    plain_text = plain_text.lower()
    plain_text = plain_text.replace(" ", '')
    
    result = ''
    for i, char in enumerate(plain_text):
        if char in alphabet:
            result += reversed_alpha[alphabet.index(char)]
        elif char in '0123456789':
            result += char

    result_spaced = ''
    for i, char in enumerate(result):
        if (i+1) % 5 == 0:
            result_spaced += result[i] + ' ' 
        else:
            result_spaced += result[i]
    
    
    return result_spaced.strip()

def decode(ciphered_text):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    reversed_alpha = 'zyxwvutsrqponmlkjihgfedcba'

    ciphered_text = ciphered_text.replace(" ", '')
    
    result = ''
    for i, char in enumerate(ciphered_text):
        if char in reversed_alpha:
            result += alphabet[reversed_alpha.index(char)]
        elif char in '0123456789':
            result += char

    
    
    
    return result
