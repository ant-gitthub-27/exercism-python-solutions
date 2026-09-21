def encode(plain_text):
    
    answer = []
    for char in plain_text:
        if char.isalpha():
            if char.isupper():
                new_ord = ord(char) - ord("A") + 1
                new_letter = 27 - new_ord
                new = chr(new_letter + ord("a") - 1)
                answer.append(new)
            if char.islower():
                new_ord = ord(char) - ord("a") + 1
                new_letter = 27 - new_ord
                new = chr(new_letter + ord("a") - 1)
                answer.append(new)
            
        elif char.isdigit():
            answer.append(char)
    answer_string = "".join(answer)
    
    return " ".join(answer_string[i : i+5] for i in range(0, len(answer_string), 5))
    
            
            


def decode(ciphered_text):
    no_space = "".join(ciphered_text.split())
    answer = []
    for char in no_space:
        if char.isalpha():
            new_ord = ord(char) - ord("a") + 1
            new_letter = 27 - new_ord
            new = chr(new_letter + ord("a") - 1)
        else:
            new = char

        answer.append(new)
    return "".join(answer)
    
