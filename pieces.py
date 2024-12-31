from enum import Enum

class PieceType(Enum):
    EMPTY = 0
    PAWN = 1
    KNIGHT = 2
    BISHOP = 3
    ROOK = 4
    QUEEN = 5
    KING = 6

class PieceColor(Enum):
    NULL = 0
    BLACK = 1
    WHITE = 2

class Empty:
    def __init__(self, position):
        self._position = position
        self._type = PieceType.EMPTY
        self._color = PieceColor.NULL
        self._points = 0

    def get_position(self):
        return self._position

    def get_type(self):
        return self._type

    def get_color(self):
        return self._color

    def get_points(self):
        return self._points

class Pawn:
    def __init__(self, position, color, direction):
        self._position = position
        self._type = PieceType.PAWN
        self._color = color
        self._direction = direction # +1 downward, -1 upward
        self._points = 1

    def get_position(self):
        return self._position

    def get_type(self):
        return self._type

    def get_color(self):
        return self._color

    def get_direction(self):
        return self._direction

    def get_points(self):
        return self._points

    def find_moves(self, board):
        possible_moves = []
        moves = [
            self._position + self._direction * 8, # advance 1
            self._position + self._direction * 16, # advance 2
            self._position + self._direction * 8 + 1, # capture right
            self._position + self._direction * 8 - 1 # capture left
        ]

        if board[moves[0] // 8][moves[0] % 8].get_type() == PieceType.EMPTY:
            possible_moves.append(moves[0])

        if 8 <= self._position <= 15 and possible_moves:
            if board[moves[1] // 8][moves[1] % 8].get_type() == PieceType.EMPTY:
                possible_moves.append(moves[1])

        if self._position % 8 != 7:
            if board[moves[2] // 8][moves[2] % 8].get_type() != PieceType.EMPTY:
                if board[moves[2] // 8][moves[2] % 8].get_color() != self._color:
                    possible_moves.append(moves[2])

        if self._position % 8 != 0:
            if board[moves[3] // 8][moves[3] % 8].get_type() != PieceType.EMPTY:
                if board[moves[3] // 8][moves[3] % 8].get_color() != self._color:
                    possible_moves.append(moves[3])

        return possible_moves

class Knight:
    def __init__(self, position, color):
        self._position = position
        self._type = PieceType.KNIGHT
        self._color = color
        self._points = 3

    def get_position(self):
        return self._position

    def get_type(self):
        return self._type

    def get_color(self):
        return self._color

    def get_points(self):
        return self._points

    def find_moves(self, board):
        possible_moves = []
        moves = [
            self._position + 16 + 1,
            self._position + 16 - 1,
            self._position - 16 + 1,
            self._position - 16 - 1,
            self._position + 8 + 2,
            self._position + 8 - 2,
            self._position - 8 + 2,
            self._position - 8 - 2,
        ]

        boundaries = [
            [range(6, 7 + 1), range(7, 7 + 1)],
            [range(6, 7 + 1), range(0, 0 + 1)],
            [range(0, 1 + 1), range(7, 7 + 1)],
            [range(0, 1 + 1), range(0, 0 + 1)],
            [range(7, 7 + 1), range(6, 7 + 1)],
            [range(7, 7 + 1), range(0, 1 + 1)],
            [range(0, 0 + 1), range(6, 7 + 1)],
            [range(0, 0 + 1), range(0, 1 + 1)],
        ]

        for i in range(8):
            if self._position // 8 not in boundaries[i][0] and self._position % 8 not in boundaries[i][1]:
                if board[moves[i] // 8][moves[i] % 8].get_color() != self._color:
                    possible_moves.append(moves[i])

        return possible_moves

