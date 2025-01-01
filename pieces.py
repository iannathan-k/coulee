from enum import Enum

class PieceColor(Enum):
    BLACK = 0
    WHITE = 1
    EMPTY = 2

class Empty:
    def __init__(self):
        self._color = PieceColor.EMPTY

    def get_color(self):
        return self._color

class Pawn:
    def __init__(self, position, color, direction):
        self._position = position
        self._color = color
        self._direction = direction # +1 downward, -1 upward

    def get_position(self):
        return self._position

    def set_position(self, new_position):
        self._position = new_position

    def get_color(self):
        return self._color

    def get_direction(self):
        return self._direction

    def get_moves(self, board):
        possible_moves = []
        moves = [
            self._position + self._direction * 3, # advance 1
            self._position + self._direction * 3 + 1, # capture right
            self._position + self._direction * 3 - 1 # capture left
        ]

        if board[moves[0] // 3][moves[0] % 3].get_color() == PieceColor.EMPTY:
            possible_moves.append(moves[0])

        if self._position % 3 != 2:
            if board[moves[1] // 3][moves[1] % 3].get_color() != PieceColor.EMPTY:
                if board[moves[1] // 3][moves[1] % 3].get_color() != self._color:
                    possible_moves.append(moves[1])

        if self._position % 3 != 0:
            if board[moves[2] // 3][moves[2] % 3].get_color() != PieceColor.EMPTY:
                if board[moves[2] // 3][moves[2] % 3].get_color() != self._color:
                    possible_moves.append(moves[2])

        return possible_moves