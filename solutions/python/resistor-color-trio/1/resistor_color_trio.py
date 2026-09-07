def label(colors):
    code_dict = dict(black = 0, brown = 1, red = 2, orange = 3, yellow = 4, green = 5, blue = 6, violet = 7, grey = 8, white = 9)
    resistance = (((code_dict[colors[0]] * 10) + code_dict[colors[1]]) * (10 ** (code_dict[colors[2]])))
    string = str(resistance)
    if string.endswith("000000000"):
        return f"{resistance//(10 ** 9)} gigaohms"
    if string.endswith("000000"):
        return f"{resistance//(10 ** 6)} megaohms"
    if string.endswith("000"):
        return f"{resistance//(10**3)} kiloohms"
    else:   
        return f"{resistance} ohms"
