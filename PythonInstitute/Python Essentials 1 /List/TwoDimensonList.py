def printTwoDimenson(TwoDim):

    for row in  TwoDim:

        for item in row:
            print(item, end=' / ')
        print()

board = []

for i in range(8):
    row = ["EMPTY" for i in range(8)]
    board.append(row)

print(board)

# nested comprehension

board1 = [["EMPTY11" for i in range(8)] for j in range(8)]

print(board1)
# chess
EMPTY = "EMPTY"
ROOK = "ROOK"
board2 = []
KNIGHT = "KNIGHT"

PAWN = "PAWN"

for i in range(8):
    row = [EMPTY for i in range(8)]
    board2.append(row)

board2[0][0] = ROOK
board2[0][7] = ROOK
board2[7][0] = ROOK
board2[7][7] = ROOK
board2[4][2] = KNIGHT
board2[3][4] = PAWN

print(board2)

printTwoDimenson(board2)
