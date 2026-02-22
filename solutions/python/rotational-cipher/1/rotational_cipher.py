def rotate(text, key):
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    alphabet_caps = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    index = 0
    answer_string = ''
    
    for i in range(len(text)):
        if text[i] in alphabet:
            for j in range(len(alphabet)):
                if text[i] == alphabet[j]:
                    index = j + key
                
            if index > 25:
                index -= 26

            answer_string += alphabet[index]
        elif text[i] in alphabet_caps:
            for j in range(len(alphabet_caps)):
                if text[i] == alphabet_caps[j]:
                    index = j + key
                
            if index > 25:
                index -= 26

            answer_string += alphabet_caps[index]
        else:
            answer_string += text[i]

    return answer_string
            
    
