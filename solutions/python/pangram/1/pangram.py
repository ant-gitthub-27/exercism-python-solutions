def is_pangram(sentence):
    alphabet_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'] 
    alphabet_list_caps = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

    sentence_list = list(sentence)
    verdict = True
    for i in range(len(alphabet_list)):
        letter_1 = alphabet_list[i]
        letter_2 = alphabet_list_caps[i]
        if letter_1 not in sentence and letter_2 not in sentence_list:
             verdict = False

    return verdict
