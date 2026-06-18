def is_armstrong_number(number):
    """Function determines if the given number is an armstrong number.
    """
    power = len(str(number))
    armstrong_sum = sum(int(digit) ** power for digit in str(number))
    return armstrong_sum == number
