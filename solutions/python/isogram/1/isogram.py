def is_isogram(string):
    text = string.lower()

    for letter in text:
        if letter.isalpha():
            if text.count(letter) > 1:
                return False
    return True
