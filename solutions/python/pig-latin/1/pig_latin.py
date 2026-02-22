def translate_word(text):
    result = ""
    vowels = ['a', 'e', 'i', 'o', 'u']
    
    if text[:2] in ("xr", "yt"):
        result = text + "ay"
        return result
    elif not any(v in text for v in vowels):
        if text[0] == 'y':
            result = text + 'ay'
        elif 'y' in text:
            num = text.find('y')
            result = text[num:] + text[:num] + 'ay'
        else:
            result = text + 'ay'

        return result
    elif text[0] not in vowels:
        i = 0

        
        while text[i] not in vowels:
            i += 1
            
        if text[i-1] == "q" and text[i] == "u":
            result = text[i+1:] + text[:i+1] + "ay"
        elif text[0] == 'y':
            result = text[i:] + text[:i] + "ay"
        else:     
            result = text[i:] + text[:i] + "ay"
        
        '''elif i > 0:
            for num in range(0, i):
                if text[num] == 'y':
                    result = text[i-1] + text[:i-1] + 'ay' 
                    '''
            
        
        return result
    else:
        return text + 'ay'
    
def translate(text):
    words_input = text.split()
    result = ''
    for word in words_input:
        result += translate_word(word) + ' '

    return result[:-1]

    

