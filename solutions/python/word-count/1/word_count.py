def count_words(sentence):
    cleaned = sentence.lower()
    for char in ".:,\n!&@$%^\t\"_":
        cleaned = cleaned.replace(char, " ")
    mapping = dict()
    for word in cleaned.split():
        w = word.lower().strip(" \' ")
        if w:
            if w not in mapping:
                mapping[w] = 1
            else:
                mapping[w] += 1
    return mapping
        
