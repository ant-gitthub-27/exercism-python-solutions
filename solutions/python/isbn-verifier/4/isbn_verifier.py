def is_valid(isbn):
    
    isbn_list = [c for c in isbn if c != '-']

    '''
    the above line is doing this:
    
    isbn_list = []
    for i in range(len(isbn)):
        if(isbn[i] != '-'):
            isbn_list.append(isbn[i])
    '''


    
    if len(isbn_list) != 10:
        return False
    if any(not c.isdigit() for c in isbn_list[:-1]):
        return False
    '''for c in isbn_list[:-1]:
        if not c.isdigit():
            return False'''
    
    
    '''for i in range(len(isbn_list) - 1):
        if(not isbn_list[i].isdigit()):
            return False
            isbn_list = []   '''         

    
    if(isbn[-1] == 'X'):
        isbn_list[-1] = "10"
    elif not isbn[-1].isnumeric():
        return False
        

    
    sum = 0
    for i, d in enumerate(isbn_list):
        sum = sum + (10 - i) * int(d)

    return sum % 11 == 0
    '''
    original code for the previous line
    if sum % 11 == 0:
        return True
    else:
        return False
    '''