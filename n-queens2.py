def is_safe(row, col, board):
    # Checking horizontally
    for j in range(len(board)):
        if board[row][j] == 'Q':
            return False

    # Checking vertically
    for i in range(len(board)):
        if board[i][col] == 'Q':
            return False

    # Checking upper left diagonal
    r, c = row, col
    while r >= 0 and c >= 0:
        if board[r][c] == 'Q':
            return False
        r -= 1
        c -= 1

    # Checking upper right diagonal
    r, c = row, col
    while r >= 0 and c < len(board):
        if board[r][c] == 'Q':
            return False
        r -= 1
        c += 1

    # Checking lower left diagonal
    r, c = row, col
    while r < len(board) and c >= 0:
        if board[r][c] == 'Q':
            return False
        r += 1
        c -= 1

    # Checking lower right diagonal
    r, c = row, col
    while r < len(board) and c < len(board):
        if board[r][c] == 'Q':
            return False
        r += 1
        c += 1

    return True


# Forward checking algorithm to solve n-queens
def forward_check(row, col, board, remaining):
    n = len(board)

    # Checking horizontally
    for j in range(len(board)):
        if board[row][j] == 'Q':
            if j in remaining[col]:
                remaining[col].remove(j)

    # Checking upper left diagonal
    r, c = row, col
    while r >= 0 and c >= 0:
        if board[r][c] == 'Q':
            if r in remaining[col]:
                remaining[col].remove(r)
        r -= 1
        c -= 1

    # Checking upper right diagonal
    r, c = row, col
    while r >= 0 and c < n:
        if board[r][c] == 'Q':
            if r in remaining[col]:
                remaining[col].remove(r)
        r -= 1
        c += 1

    return remaining


def print_board_and_remaining(board, remaining):
    print("Board configuration:")
    for row in board:
        print(' '.join(row))
    print("Remaining values:")
    for col, values in remaining.items():
        print(f"Column {col}: {values}")
    print()


def solve_forward(board, remaining, col):
    if col == len(board):
        return True

    for row in remaining[col][:]:
        if is_safe(row, col, board):
            board[row][col] = 'Q'
            updated_remaining = {key: value[:] for key, value in remaining.items()}  # Create a deep copy
            updated_remaining = forward_check(row, col, board, updated_remaining)
            print_board_and_remaining(board, updated_remaining)  # Print board and remaining values
            if solve_forward(board, updated_remaining, col + 1):
                return True
            board[row][col] = '*'
    return False



def solution_forward(n):
    board = [['*' for _ in range(n)] for _ in range(n)]
    remaining = {i: list(range(n)) for i in range(n)}  # remaining values for each column
    if solve_forward(board, remaining, 0):
        print("Solution found:")
        for row in board:
            print(' '.join(row))
    else:
        print("No solution found")


if __name__ == "__main__":
    solution_forward(4)
