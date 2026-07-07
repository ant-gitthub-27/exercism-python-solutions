def score(x, y):
    squared = x**2 + y**2
    if squared <= 1:
        return 10
    elif squared <= 25:
        return 5
    elif squared <= 100:
        return 1
    else: 
        return 0