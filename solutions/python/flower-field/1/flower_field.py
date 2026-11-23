def annotate(garden):
    
    if not garden:
        return []

    rows = len(garden)
    cols = len(garden[0])

    for row in garden:
        if len(row) != cols:
            raise ValueError("The board is invalid with current input.")
        for cell in row:
            if cell not in " *":
                raise ValueError("The board is invalid with current input.")
                

    if cols == 0:
        return ["" for _ in range(rows)]

    # Convert rows to mutable lists and pad with spaces on all sides
    grid = [[" "] + list(row) + [" "] for row in garden]
    blank = [" "] * (cols + 2)
    padded = [blank] + grid + [blank]

    ans = [[" " for _ in range(cols)] for _ in range(rows)]

    for j in range(1, rows + 1):
        for k in range(1, cols + 1):
            if padded[j][k] == "*":
                ans[j - 1][k - 1] = "*"
            else:
                neighbors = [
                    padded[j - 1][k - 1], padded[j - 1][k], padded[j - 1][k + 1],
                    padded[j][k - 1],                     padded[j][k + 1],
                    padded[j + 1][k - 1], padded[j + 1][k], padded[j + 1][k + 1],
                ]
                count = neighbors.count("*")
                ans[j - 1][k - 1] = str(count) if count > 0 else " "

    return ["".join(row) for row in ans]