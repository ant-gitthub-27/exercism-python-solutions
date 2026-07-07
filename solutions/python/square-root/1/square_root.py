def square_root(number):
    if number % 1 == 0 and number >= 1:
        x = 1
        while x * x < number:
            x = x + 1
    return x