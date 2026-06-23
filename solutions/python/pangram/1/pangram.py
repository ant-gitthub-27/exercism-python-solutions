def is_pangram(sentence):
    text = sentence.lower()
    letters = "qwertyuiopasdfghjklzxcvbnm"
    for letter in letters:
        if letter not in text:
            return False
    return True
