def translate(sentence):
    vowels = "aeiou"
    consonents = "qwrtpsdfghjklzxcvbnm"
    def translate_word(text):
        if text[0] in vowels or text[0:2] == "xr" or text[0:2] == "yt":
            return text + "ay"

        if text[0].startswith("y"):
            return text[1:] + "yay"
    
    
        shifts = 0
        while text[0] in consonents and text[0] != "y":
            if text.startswith("qu"):
                text = text[2:] + text [0:2]
                break
            else:
                text = text[1:] + text[0]
                shifts += 1
            if shifts == len(text):
                break
        return text + "ay"
    return " ".join([translate_word(word) for word in sentence.split()])
            
    
        
    
        
    
