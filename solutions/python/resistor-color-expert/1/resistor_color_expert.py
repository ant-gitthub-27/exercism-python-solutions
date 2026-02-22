def label(colors):
    colours_list = ['black', 'brown', 'red', 'orange', 'yellow', 'green', 'blue', 'violet', 'grey', 'white']

    sum = 0
    for i, colour in enumerate(colours_list):
        if colors[0] == colour:
            sum = sum + 10*i

        if colors[1] == colour:
            sum = sum + i

    if len(colors) == 5:
        for i, colour in enumerate(colours_list):
            if colors[2] == colour:
                sum = sum * 10 + i

    for i, colour in enumerate(colours_list):
        
        if colors[-2] == colour:
            sum = sum * pow(10, i)

    if sum < 1000:
        return str(sum) + " ohms"
    elif sum < 1000000 and sum % 1000 == 0:
        return str(sum//1000) + " kiloohms"
    elif sum < 1000000 and sum % 1000 != 0:
        return str(sum/1000) + " kiloohms"
    elif sum < 1000000000 and sum % 1000000 == 0:
        return str(sum//1000000) + "megaohms"
    elif sum < 1000000000 and sum % 1000000 != 0:
        return str(sum/1000000) + " megaohms"
    else:
        return str(sum/1000000000) + " gigaohms"
    

def resistor_label(colors):

    tol_cols = ['grey', 'violet', 'blue', 'green', 'brown', 'red', 'gold', 'silver']
    tol_vals = [0.05, 0.1, 0.25, 0.5, 1, 2, 5, 10]

    test = 0

    if colors == ['black']:
        return '0 ohms'
    
    for ind, col in enumerate(tol_cols):
        if col == colors[-1]:
            return label(colors) + ' ±' + str(tol_vals[ind]) + '%'
            test = 1

    if not test:
        return label(colors)