from random import randrange




def display_board(board):


    for row in board:
        print("+-------+-------+-------+")
        print("|       |       |       |")
        print("|", end='')
        for col in row:

            print(f"  {col}  ", end='  |')


        print("\n|       |       |       |")


        # print("+-------+-------+-------+")


    print("+-------+-------+-------+")
    # The function accepts one parameter containing the board's current status
    # and prints it out to the console.


def enter_move(board):
    try:
        UserStep = int(input("Your turn! PLease input your step:  "))
        UserStep -= 1


        while True:

            r = UserStep // 3
            c = UserStep - r*3

            if board[r][c] != "O" and board[r][c] != "X":
                board[r][c] = "O"
                print("It's done!!")
                break

            else:

                UserStep = int(input("Wrong step! The field is busy! Please ender your step: "))
                UserStep -= 1


        #display_board(board)

    except TypeError:
        print("Wrong Enter!!! Please input corret number")
        enter_move(board)






    # The function accepts the board's current status, asks the user about their move,
    # checks the input, and updates the board according to the user's decision.


def make_list_of_free_fields(board):

    # The function browses the board and builds a list of all the free squares;
    # the list consists of tuples, while each tuple is a pair of row and column numbers.
    freeList = []
    for i in range(len(board)):

        for j in range(len(board[i])):

            if board[i][j] != "O" and board[i][j] !="X":
                freeList.append((i, j))


    return freeList




def victory_for(board, sign):

    if sign == 0:
        checkSign = "X"
    else:
        checkSign = 'O'



    for i in range(len(board)):

        Flag1 = True
        Flag2 = True


        for j in range(len(board[0])):

            if board[i][j] != checkSign:
                Flag1 = False
            else:
                pass

            if board[j][i] != checkSign:
                Flag2 = False

            else:
                pass




        if Flag1 == True or Flag2 == True:
            return True


    Flag3 = True
    Flag4 = True

    for i in range(len(board)):


        if board[i][i] != checkSign:

            Flag3 = False
        else:
            pass

        if board[len(board)-i-1][j] != checkSign:
            Flag4 = False
        else:
            pass


    if Flag3 == True or Flag4 == True:
        return True

    return False






    # The function analyzes the board's status in order to check if
    # the player using 'O's or 'X's has won the game


def draw_move(board):

    step = 4

    if board[1][1] != "X" and board[1][1] != "O":

        board[1][1] = "X"
    else:

        while True:
            step = randrange(0,9)
            r = step // 3
            c = step - r*3

            if board[r][c] != "O" and board[r][c] != "X":
                board[r][c] = "X"
                break

    print(f"The computer enter is {step+1}")




    # The function draws the computer's move and updates the board.

# board[row][column]
#
# row = ["WHITE_PAWN" for i in range(8)]
# i = 0
# y = 0
# board = [[i + y  for i in range(1, 4)] for y in range(0, 3)]

# board = [ [3 * j + i + 1 for i in range(3)] for j in range(3) ]  better way to make board
board = []
d = 0
for i in range(3):
    row = [i + d for i in range(1, 4)]
    board.append(row)
    d +=3


print(board)
# print(board[1][3])

display_board(board)
print("Hello in my playgame")
print("First step is has been doing by computer:   \n")



while True:

    draw_move(board)
    display_board(board)
    if victory_for(board, 0) == True:
        print("The computer win!!! You lost")
        break
    if len(make_list_of_free_fields(board)) ==0:
        print("Not any free fields. It is pat")
        break

    enter_move(board)
    display_board(board)
    if victory_for(board, 1) == True:
        print("You win. The computer lost!!")
        break
    if len(make_list_of_free_fields(board)) ==0:
        print("Not any free fields. It is pat")
        break


