"""
Collatz Conjecture.
This code calculates the number of steps to reach 1 using the Collatz rules.
"""

def steps(number):
    """Find the number of steps to reach 1."""
    if number <= 0:
        raise ValueError("Only positive integers are allowed")

    step_counter = 0

    while number > 1:
        if number % 2 == 0:
            number = number // 2
        else:
            number = (number * 3) + 1
    
        step_counter = step_counter + 1
    
    return step_counter