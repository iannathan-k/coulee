from pieces import *

def determine_winner(board, turn):
    # turn = True --> White
    # turn = False --> Black
    white_move = False
    black_move = False
    for i in range(9):
        piece = board[i // 3][i % 3]

        if piece.get_color() == PieceColor.WHITE:
            if piece.get_position() in range(6, 9):
                return PieceColor.WHITE
            if piece.get_moves(board):
                white_move = True

        elif piece.get_color() == PieceColor.BLACK:
            if piece.get_position() in range(0, 3):
                return PieceColor.BLACK
            if piece.get_moves(board):
                black_move = True

    if white_move == False and turn:
        return PieceColor.BLACK
    elif black_move == False and not turn:
        return PieceColor.WHITE

    return PieceColor.EMPTY

def evaluate_board(board, turn):
    if determine_winner(board, turn) == PieceColor.BLACK:
        return -100
    elif determine_winner(board, turn) == PieceColor.WHITE:
        return 100

    white_advantage = 0
    black_advantage = 0

    for i in range(9):
        piece = board[i // 3][i % 3]
        if piece.get_color() == PieceColor.WHITE:
            white_advantage += 1 # piece count advantage
            white_advantage += (i // 3) * 2 # distance advantage
            white_advantage += len(piece.get_moves(board)) # freedom advantage
        elif board[i // 3][i % 3].get_color() == PieceColor.BLACK:
            black_advantage += 1
            black_advantage += (2 - i // 3) * 2
            black_advantage += len(piece.get_moves(board))

    return white_advantage - black_advantage