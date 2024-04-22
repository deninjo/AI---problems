reference = '''https://en.wikipedia.org/wiki/Eight_queens_puzzle#:~:text=The%20eight%20queens%20puzzle%20is,in%20the%20mid%2D19th%20century.
               https://favtutor.com/blogs/n-queen-problem'''


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


# only used when a valid configuration is found
def save_board(board, all_boards):
    new_board = [''.join(row) for row in board]  # joining rows to a single string
    all_boards.append(new_board)  # saving current solution for printing


# Backtracking algorithm to solve n-queens
def solve(board, all_boards, col):
    if col == len(board):
        save_board(board, all_boards)
        return
    for row in range(len(board)):
        if is_safe(row, col, board):
            board[row][col] = 'Q'
            solve(board, all_boards, col + 1)  # recursive call to update the board
            board[row][col] = '*'


def solution(n):
    all_boards = []  # for storing all solutions
    board = [['*' for _ in range(n)] for _ in range(n)]
    solve(board, all_boards, 0)

    for aboard in all_boards:
        for row in aboard:
            print(row)
        print()


if __name__ == "__main__":
    solution(4)
