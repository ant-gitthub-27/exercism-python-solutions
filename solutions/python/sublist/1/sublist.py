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
SUBLIST = 1
SUPERLIST = 2
EQUAL = 3
UNEQUAL = 4

def subset(list_one, list_two):
    if not list_one:
        return True
    len1, len2 = len(list_one), len(list_two)
    if len1 > len2:
        return False
    else:
        return any(list_two[i : i + len1] == list_one for i in range(len2 - len1 + 1))

    
        

def sublist(list_one, list_two):
    if list_one == list_two:
        return EQUAL
    elif subset(list_one, list_two):
        return SUBLIST
    elif subset(list_two,list_one):
        return SUPERLIST
    else:
        return UNEQUAL
    
