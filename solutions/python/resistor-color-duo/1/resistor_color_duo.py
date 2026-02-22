def value(colors):
    colours_list = ['black', 'brown', 'red', 'orange', 'yellow', 'green', 'blue', 'violet', 'grey', 'white']

    sum = 0
    for i, colour in enumerate(colours_list):
        if colors[0] == colour:
            sum = sum + 10*i

        if colors[1] == colour:
            sum = sum + i

    return sum
