def egg_count(display_value):

    output = []
    while display_value != 0:
        temp = display_value%2
        output.insert(0, temp)
        display_value = display_value // 2

    return output.count(1)