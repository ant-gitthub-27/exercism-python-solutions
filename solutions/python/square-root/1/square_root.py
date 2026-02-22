def square_root(number):
    low = 0
    high = number
    guess = (low + high)/2

    if number == 1:
        return number
    
    
    while abs(guess * guess - number) > 0.0001 or guess * guess == number:
        if guess * guess > number:
            high = guess
        else:
            low = guess

        guess = (low + high)/2

    return round(guess)