def rotate(text, key):
    
    answer = []
    for char in text:
        if char.isalpha():
            if char.isupper():
                new = chr((((ord(char) - ord("A")) + int(key)) % 26) + ord("A"))
            else: 
                new = chr((((ord(char) - ord("a")) + int(key)) % 26) + ord("a"))
            answer.append(new)
        else:
            answer.append(char)
        
    return "".join(answer)