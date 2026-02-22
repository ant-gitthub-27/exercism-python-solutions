def is_valid(isbn):
    isbn_list = []

    for i in range(len(isbn)):
        if(isbn[i] != '-'):
            isbn_list.append(isbn[i])

    if len(isbn_list) != 10:
        return False
        pass
    else:
        for i in range(len(isbn_list) - 1):
            if(not isbn_list[i].isdigit()):
                return False
                isbn_list = []
                pass
                
    
    if(isbn[-1] == 'X'):
        isbn_list = isbn_list[:-1]
        isbn_list.append("10")
    elif(isbn[-1].isnumeric()):
        isbn_list.append(isbn[-1])
    else:
        return False
        pass

    
    sum = 0
    for i in range(len(isbn_list)):
        sum = sum + (10 - i) * int(isbn_list[i])
    
    if sum % 11 == 0:
        return True
    else:
        return False