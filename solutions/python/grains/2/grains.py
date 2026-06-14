def square(number):
    # amount of grains on a single square
    if 1 <= number <= 64:
        return 2 ** (number - 1)
    raise ValueError ("square must be between 1 and 64")

def total():
    # amount of grains on the whole chess board
    return sum(2 ** (n - 1) for n in range(1,65))

