def roman(number):
    roman_string = ''
    '''cases = [(4, 'IV'), (9, 'IX'), (40, 'XL'), (90, 'XC'), (400, 'CD'), (900, 'CM')]'''
    num_list = [4, 9, 40, 90, 400, 900]
    rom_list = ['IV', 'IX', 'XL', 'XC', 'CD', 'CM']

    if number >= 1000:
        while number >= 1000:
            number -= 1000
            roman_string += 'M'

    if number >= 900:
        number -= 900
        roman_string += 'CM'

    if number >= 500:
        number -= 500
        roman_string += 'D'

    if number >= 400:
        number -= 400
        roman_string += 'CD'

    if number >= 100:
        while number >= 100:
            number -= 100
            roman_string += 'C'

    if number >= 90:
        number -= 90
        roman_string += 'XC'

    if number >= 50:
        number -= 50
        roman_string += 'L'

    if number >= 40:
        number -= 40
        roman_string += 'XL'

    if number >= 10:
        while number > 10:
            number -= 10
            roman_string += 'X'
     
    if number >= 9:
        number -= 9
        roman_string += 'IX'

    if number >= 5:
        number -= 5
        roman_string += 'V'

    if number >= 4:
        number -= 4
        roman_string += 'IV'

    if number >= 1:
        while number >= 1:
            number -= 1
            roman_string += 'I'
    

    return roman_string
    