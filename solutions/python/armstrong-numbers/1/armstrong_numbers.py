def is_armstrong_number(number):
    
    degree = 0
    test = number
    while test>0:
        test //= 10
        degree += 1

    dummy = number
    sum = 0
    count = 0
    while dummy>0:
        count += 1
        rem = dummy%10
        dummy //= 10
        sum += pow(rem, degree)

    if(sum == number):
        return(True)
    else:
        return(False)
    