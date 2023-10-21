def check_win():
    # Check rows
    for row in range(3):
        if board[row][:] == "XXX" or board[row][:] == "OOO":
            return True

    # Check columns
    for col in range(3):
        if board[:][col] == "XXX" or board[:][col] == "OOO":
            return True

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] or board[0][2] == board[1][1] == board[2][0]:
        return True

    return False

    print(check_win())
