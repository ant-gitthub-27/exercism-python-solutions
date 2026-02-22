def score(x, y):
    distance =  pow(pow(x, 2) + pow(y, 2), 1/2)
    if distance > 10:
        return 0
    elif distance > 5:
        return 1
    elif distance > 1:
        return 5
    else:
        return 10
