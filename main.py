from pieces import *

board = [[None for i in range(8)] for j in range(8)]

for i in range(64):
    board[i // 8][i % 8] = Empty(i)

board[3][7] = Knight(31, PieceColor.WHITE)

print(board[3][7].find_moves(board))