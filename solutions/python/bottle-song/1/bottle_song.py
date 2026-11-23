def recite(start, take=1):
    number_words = {0: "no", 1: "one", 2: "two", 3: "three", 4:"four", 5:"five", 6:"six", 7:"seven", 8: "eight", 9:"nine", 10: "ten"}
    poem = []
    for i in range(take):
        current_bottle = "bottle" if start == 1 else "bottles"
        next_bottle = "bottle" if start -1 == 1 else "bottles"
        line1 = f"{number_words[start].capitalize()} green {current_bottle} hanging on the wall,"
        line3 = "And if one green bottle should accidentally fall,"
        line4 = f"There'll be {number_words[start - 1]} green {next_bottle} hanging on the wall."
        poem.extend([line1, line1, line3, line4])
        if i < take - 1:
            poem.append("")
        start -= 1
    return poem