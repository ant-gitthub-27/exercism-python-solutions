"""
This exercise stub and the test suite contain several enumerated constants.

Enumerated constants can be done with a NAME assigned to an arbitrary,
but unique value. An integer is traditionally used because it’s memory
efficient.
It is a common practice to export both constants and functions that work with
those constants (ex. the constants in the os, subprocess and re modules).

You can learn more here: https://en.wikipedia.org/wiki/Enumerated_type
"""

# Possible sublist categories.
# Change the values as you see fit.
SUBLIST = 0
SUPERLIST = 1
EQUAL = 2
UNEQUAL = 3

def sublist(list_one, list_two):
    if list_one == list_two:
        return EQUAL
    '''elif list_one in list_two:
        return SUBLIST
    elif list_two in list_one:
        return SUPERLIST
    else:
        return UNEQUAL
    '''

    # Convert lists to strings to use the 'in' operator for sequences
    # We add commas/brackets to ensure [1, 2] isn't found in [12, 3]
    str_one = str(list_one)[1:-1] + ','
    str_two = str(list_two)[1:-1] + ','

    if not list_one or str_one in str_two:
        return SUBLIST
    elif not list_two or str_two in str_one:
        return SUPERLIST
    
    return UNEQUAL