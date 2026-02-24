def roman(number):
    roman_string = ''
    num_list = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    rom_list = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L' ,'XL', 'X', 'IX', 'V', 'IV', 'I']

    while number > 0:
        for i, num in enumerate(num_list):
            if number >= num:
                while number >= num:
                    number -= num
                    roman_string += rom_list[i]

    return roman_string