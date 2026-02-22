def gamestate(board):

    count = 0
    board_list = []
    for i in range(0, 3):
        board_list.append(list(board[i]))

    countX = 0
    countO = 0
    for i in range(0, 3):
        for char in board_list[i]:
            if char == 'X':
                countX += 1
            elif char == 'O':
                countO += 1

    if countO > countX:
        raise ValueError("Wrong turn order: O started")
    elif countX - countO > 1:
        raise ValueError("Wrong turn order: X went twice")

    for i in range(0, 3):
        if (board_list[0][i] == 'X' and board_list[1][i] == 'X' and board_list[2][i] == 'X') or (board_list[0][i] == 'O' and board_list[1][i] == 'O' and board_list[2][i] == 'O'):
            count+= 1
        elif board[i] == 'XXX' or board[i] == 'OOO':
            count+=  1

    for char in ['X', 'O']:
        if (board_list[0][0] == char and board_list[1][1] == char and board_list[2][2] == char) or (board_list[0][2] == char and board_list[1][1] == char and board_list[2][0] == char):
            count += 1

    if count == 1:
        return 'win'    
    elif count == 0:
        for i in range(0, 3):
            if ' ' in board_list[i]:
                return 'ongoing'
        else:
            return 'draw'
    else:
        raise ValueError("Impossible board: game should have ended after the game was won")