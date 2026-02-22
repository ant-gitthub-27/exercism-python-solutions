def label(colors):
    colours_list = ['black', 'brown', 'red', 'orange', 'yellow', 'green', 'blue', 'violet', 'grey', 'white']

    sum = 0
    for i, colour in enumerate(colours_list):
        if colors[0] == colour:
            sum = sum + 10*i

        if colors[1] == colour:
            sum = sum + i

    for i, colour in enumerate(colours_list):
        
        if colors[2] == colour:
            sum = sum * pow(10, i)

    if sum // 1000 == 0:
        return str(sum) + " ohms"
    elif sum // 1000000 == 0:
        return str(sum//1000) + " kiloohms"
    elif sum // 1000000000 == 0:
        return str(sum//1000000) + " megaohms"
    else:
        return str(sum//1000000000) + " gigaohms"
    
    
    
