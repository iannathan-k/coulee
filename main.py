from pieces import *
from evaluator import *
from coulee import *

board = [
    [Empty(), Empty(), Empty()],
    [Empty(), Empty(), Empty()],
    [Empty(), Empty(), Empty()]
]

for i in range(3):
    board[i // 3][i % 3] = Pawn(i, PieceColor.WHITE, +1)

for i in range(6,9):
    board[i // 3][i % 3] = Pawn(i, PieceColor.BLACK, -1)

def print_board():
    print("+-+-+-+")
    for line in board:
        line_string = "|"
        for piece in line:
            if piece.get_color() == PieceColor.EMPTY:
                line_string += " |"
            elif piece.get_color() == PieceColor.WHITE:
                line_string += "P|"
            else:
                line_string += "p|"
        print(line_string)
        print("+-+-+-+")

def move_piece(origin_pos, target_pos):
    board[target_pos // 3][target_pos % 3] = board[origin_pos // 3][origin_pos % 3]
    board[origin_pos // 3][origin_pos % 3] = Empty()
    board[target_pos // 3][target_pos % 3].set_position(target_pos)

def __main__():
    depth = int(input("Recursion Depth?: "))
    turn = input("Black or White?: ")
    if turn.lower() in ['b', 'black', 'false']:
        turn = False
    else:
        turn = True

    print_board()

    while True:
        if turn:
            origin = int(input("Player piece: "))
            target = int(input("Player move: "))
            move_piece(origin, target)
            print_board()
            turn = not turn

        else:
            coulee_move = minimax(board, depth, turn)
            print(coulee_move)
            move_piece(coulee_move[1][0], coulee_move[1][1])
            print("Evaluation,", coulee_move[0])
            print_board()
            turn = not turn

        if determine_winner(board, turn) == PieceColor.WHITE:
            print("WHITE WON")
            break
        if determine_winner(board, turn) == PieceColor.BLACK:
            print("BLACK WON")
            break

if __name__ == "__main__":
    __main__()