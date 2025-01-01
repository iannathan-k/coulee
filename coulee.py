from copy import deepcopy
from evaluator import *
from math import inf

def move_state(game_board, origin_pos, target_pos):
    new_board = deepcopy(game_board)
    new_board[target_pos // 3][target_pos % 3] = new_board[origin_pos // 3][origin_pos % 3]
    new_board[origin_pos // 3][origin_pos % 3] = Empty()
    new_board[target_pos // 3][target_pos % 3].set_position(target_pos)
    return new_board

def get_possible_moves(board, side):
    # side = True --> White
    # side = False --> Black
    possible_moves = []
    if side:
        color = PieceColor.WHITE
    else:
        color = PieceColor.BLACK

    for i in range(9):
        if board[i // 3][i % 3].get_color() == color:
            for move in board[i // 3][i % 3].get_moves(board):
                possible_moves.append([i, move])

    return possible_moves

def minimax(board, depth, turn):
    if depth == 0 or determine_winner(board, turn) != PieceColor.EMPTY:
        return [evaluate_board(board, turn), []]

    if turn:
        max_eval = [-inf, []]
        for move in get_possible_moves(board, turn):
            new_board = move_state(board, move[0], move[1])
            evaluation = minimax(new_board, depth - 1, False)[0]
            if evaluation > max_eval[0]:
                max_eval = [evaluation, move]
        return max_eval

    else:
        min_eval = [+inf, []]
        for move in get_possible_moves(board, turn):
            new_board = move_state(board, move[0], move[1])
            evaluation = minimax(new_board, depth - 1, True)[0]
            if evaluation < min_eval[0]:
                min_eval = [evaluation, move]
        return min_eval