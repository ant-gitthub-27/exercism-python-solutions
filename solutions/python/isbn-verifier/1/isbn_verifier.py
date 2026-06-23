def is_valid(isbn):
    bye_hyphen = "".join(isbn.split("-"))

    if len(bye_hyphen) != 10:
        return False

    total = 0
    for index, number in enumerate(bye_hyphen):
        weight = 10 - index
        if number == ("X") and index == 9:
            digit_value = 10
        elif number.isdigit():
            digit_value = int(number)
        else:
            return False
        total += weight * digit_value
    return total % 11 == 0