def is_safe(board, row, col):
    # Check if a queen can be placed in a given cell
    # Check row on the left side
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check upper diagonal on the left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check lower diagonal on the left side
    for i, j in zip(range(row, len(board), 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True

def solve_n_queens(n):
    def solve(board, col):
        if col >= n:
            return True

        for i in range(n):
            if is_safe(board, i, col):
                board[i][col] = 1
                if solve(board, col + 1):
                    return True
                board[i][col] = 0

        return False

    board = [[0 for _ in range(n)] for _ in range(n)]
    if not solve(board, 0):
        print("No solution exists.")
        return

    for row in board:
        print(' '.join('Q' if cell == 1 else '.' for cell in row))

if __name__ == "__main__":
    n = 8  # Change this to the desired board size
    solve_n_queens(n)
