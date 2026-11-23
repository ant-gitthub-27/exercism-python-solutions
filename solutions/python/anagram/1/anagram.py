def find_anagrams(word, candidates):
    ans = []
    for i in candidates:
        if sorted(i.lower()) == sorted(word.lower()) and i.lower() != word.lower():
            ans.append(i)
    return ans
