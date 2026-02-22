def convert(number):
    plop = ''
    if(number % 3 != 0 and number % 5 != 0 and number % 7 != 0):
        plop = plop + str(number)

    if(number % 3 == 0):
        plop += 'Pling'

    if(number % 5 == 0):
        plop += 'Plang'

    if(number % 7 == 0):
        plop += 'Plong'

    return (plop)
