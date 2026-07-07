def classify(number):
    """ A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """
    if number >= 1 and  number % 1 == 0:
        factors = []
        for i in range(1, number//2 + 1):
            if number % i == 0:
                factors.append(i)

        sum_factor = sum(factors)

        if sum_factor == number and number != 1:
            return "perfect"
        if sum_factor < number or number == 1:
            return "deficient"
        if sum_factor > number:
            return "abundant"
    else:
        raise ValueError("Classification is only possible for positive integers.")
