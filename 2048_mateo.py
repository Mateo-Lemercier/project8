from generic_functions import *
from random import choice, randint
from os import system





def StartGame(row_count: int = 4 , column_count: int = 4):
    """
    Description
    """

    board: list[list[int]]

    while True:

        board = [[0 for _ in range(column_count)] for _ in range(row_count)]

        print(Play(board, row_count, column_count))

        if not AskReplay():
            break





def Play(board: list[list[int]] , row_count: int , column_count: int) -> str:
    """
    Description
    """

    answer: str

    while True:

        Place_Number(board, row_count, column_count)

        print(GameBoard(board, row_count, column_count))

        answer = AskInput_str("In which direction would you like to play ? (z or 8 = top / q or 4 = left / s or 2 = down / d or 6 = right)", "zqsd8426").replace("z", "8").replace("q", "4").replace("s", "2").replace("d", "6").replace("8", "1-1").replace("4", "0-1").replace("2", "11").replace("6", "01")

        Movement(board, row_count, column_count, int(answer[0]), int(answer[1:]))

        break





def GameBoard(board: list[list[int]] , row_count: int , column_count: int) -> str:
    """
    Description
    """

    system("cls")

    row_index: int ; column_index: int ; cell_value: int
    gameboard: str = ""


    for row_index in range(row_count):

        for column_index in range(column_count):

            cell_value = board[row_index][column_index]

            if cell_value:
                gameboard += str(cell_value) + " "

            else:
                gameboard += "- "
        
        gameboard += "\n"


    return gameboard[:-1]





def Place_Number(board: list[list[int]] , row_count: int , column_count: int):
    """
    Description
    """

    bot_row: int ; bot_column: int


    playable_board: list[int] = [[row_index, column_index] for row_index in range(row_count) for column_index in range(column_count) if board[row_index][column_index] == 0]
    
    bot_row, bot_column = choice(playable_board)
    numbers: list[int] = [2, 4]
    chances: list[float] = [0.9, 0.1]

    board[bot_row][bot_column] = ChoiceWithChances(numbers, chances, 1)




def GetCoord(board, i, j):
    return board[i][j]

def GetReverseCoord(board, i, j):
    return board[j][i]


def function(i, j):
    return (i, i)

def Shift(board: list[list[int]] , row_count: int , column_count: int , user_axis: int , user_direction: int):
    """
    Description
    """
    print(board[0])
    print(board[1])
    print(board[2])
    print(board[3])
    print("")

    # get_normal_coord = lambda i,j : (i, j)
    # get_reverse_coord = lambda i,j : (j, i)

    range_index: int = (user_direction+1)//2
    row_range = [[row_count], [row_count-1, -1, -1]][range_index]
    column_range = [[column_count], [column_count-1, -1, -1]][range_index]

    for row_index in range(*row_range):

        for column_index in range(*column_range):

            # index1, index2 = coord_getter[range_index](row_index, column_index)

            # index1 =

            new_row_index = row_index + (user_axis * user_direction)
            new_column_index = column_index + ((1 - user_axis) * user_direction)

            if not (0 <= new_row_index < row_count and 0 <= new_column_index < column_count):
                continue
            
            if board[new_row_index][new_column_index] != 0:

                if board[new_row_index][new_column_index] == board[row_index][column_index]:

                    board[new_row_index][new_column_index] *= 2
                    board[row_index][column_index] = 0

                continue
            
            board[new_row_index][new_column_index] = board[row_index][column_index]
            board[row_index][column_index] = 0
    
    print("")
    print(board[0])
    print(board[1])
    print(board[2])
    print(board[3])





def Movement(board: list[list[int]] , row_count: int , column_count: int):
    """
    Description
    """

    pass



Shift(
    [
        [1, 0, 0, 2],
        [0, 3, 4, 0],
        [0, 5, 6, 0],
        [7, 0, 0, 8]
    ],
    4,
    4,
    0,
    1
)

# if __name__ == "__main__": StartGame()