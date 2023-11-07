import heapq

class Node:
    def __init__(self, board, row, col):
        self.board = board  # The current state of the board
        self.row = row      # The row where a queen is placed
        self.col = col      # The column where a queen is placed

    def __lt__(self, other):
        return False

def is_safe(board, row, col):
    # Check if a queen can be placed in a given cell
    for i in range(col):
        if board[row][i] == 1:
            return False

    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    for i, j in zip(range(row, len(board), 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True

def solve_n_queens(n):
    board = [[0] * n for _ in range(n)]
    min_col = [n] * n
    min_row = [n] * n

    root = Node(board, 0, -1)
    heap = [(root, 0)]

    while heap:
        current, col = heapq.heappop(heap)
        col += 1

        for row in range(n):
            if is_safe(current.board, row, col):
                new_board = [row[:] for row in current.board]
                new_board[row][col] = 1
                new_node = Node(new_board, row, col)
                if col == n - 1:
                    return new_node.board
                heapq.heappush(heap, (new_node, col))

if __name__ == "__main__":
    n = 8  # Change this to the desired board size
    solution = solve_n_queens(n)
    if solution:
        for row in solution:
            print(' '.join('Q' if cell == 1 else '.' for cell in row))
    else:
        print("No solution exists.")
