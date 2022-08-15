def solution(board):
    answer = 1 if 1 in board[0] or 1 in board[-1] else 0
    for i in range(1, len(board)):
        for j in range(1, len(board[0])):
            if board[i][j] == 1:
                board[i][j] = min(board[i][j-1], board[i-1][j-1], board[i-1][j]) + 1
            
    max_board = max(map(lambda x:max(x), board))
    return max(max_board, answer) ** 2