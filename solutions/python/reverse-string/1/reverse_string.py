def reverse(text):
    text_list = list(text)
    txet_list = []

    for char in text_list:
        txet_list.insert(0, char)

    return ''.join(txet_list)