def find_anagrams(word, candidates):
    word_new = word.lower()
    candidates_new = []
    result = []
    for item in candidates:
        candidates_new.append(item.lower())
   
    for index, item in enumerate(candidates_new):
        item_list = list(item)
        count = 0
        test = list(word_new)
        for char in item_list:
            if char in test:
                count += 1
                test.remove(char)
        if count == len(word) and len(item) == len(word) and item != word_new:
            result.append(candidates[index])

    return result