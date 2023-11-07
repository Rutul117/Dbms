def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def minimax(board, depth, is_maximizing, alpha, beta):
    if check_win(board, 'O'):
        return 1
    if check_win(board, 'X'):
        return -1
    if check_tie(board):
        return 0

    if is_maximizing:
        max_eval = float('-inf')
        for row in range(3):
            for col in range(3):
                if board[row][col] == '':
                    board[row][col] = 'O'
                    eval = minimax(board, depth + 1, False, alpha, beta)
                    board[row][col] = ''
                    max_eval = max(max_eval, eval)
                    alpha = max(alpha, eval)
                    if beta <= alpha:
                        break
        return max_eval
    else:
        min_eval = float('inf')
        for row in range(3):
            for col in range(3):
                if board[row][col] == '':
                    board[row][col] = 'X'
                    eval = minimax(board, depth + 1, True, alpha, beta)
                    board[row][col] = ''
                    min_eval = min(min_eval, eval)
                    beta = min(beta, eval)
                    if beta <= alpha:
                        break
        return min_eval

def find_best_move(board):
    best_move = None
    best_eval = float('-inf')
    for row in range(3):
        for col in range(3):
            if board[row][col] == '':
                board[row][col] = 'O'
                eval = minimax(board, 0, False, float('-inf'), float('inf'))
                board[row][col] = ''
                if eval > best_eval:
                    best_eval = eval
                    best_move = (row, col)
    return best_move

def check_win(board, player):
    for i in range(3):
        if all(board[i][j] == player for j in range(3)) or all(board[j][i] == player for j in range(3)):
            return True
    return all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3))

def check_tie(board):
    return all(cell != '' for row in board for cell in row)

def main():
    board = [['' for _ in range(3)] for _ in range(3)]
    while True:
        print_board(board)
        row, col = map(int, input("Enter your move (row col): ").split())
        if board[row][col] != '':
            print("Invalid move. Cell already occupied.")
            continue
        board[row][col] = 'X'

        if check_win(board, 'X'):
            print_board(board)
            print("You win!")
            break

        if check_tie(board):
            print_board(board)
            print("It's a tie!")
            break

        row, col = find_best_move(board)
        print_board(board)
        print(f"AI's move: {row} {col}")
        board[row][col] = 'O'

        if check_win(board, 'O'):
            print_board(board)
            print("AI wins!")
            break

        if check_tie(board):
            print_board(board)
            print("It's a tie!")
            break

if __name__ == "__main__":
    main()
