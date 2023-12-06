from generic_functions import *
from math import floor, ceil
from random import choice
from copy import deepcopy
from os import system
import keyboard





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



def GetInput(is_pressed: bool):
    """
    Description
    """

    keys: list[str] = ["up", "left", "right", "down"]
    keys_axis: list[int] = [1, 0, 0, 1]
    keys_directions: list[int] = [-1, -1, 1, 1]

    while True:

        for index in range(4):
        
            if keyboard.is_pressed(keys[index]):

                if not is_pressed[index]:

                    is_pressed[index] = True
                    return keys_axis[index], keys_directions[index]

            else:
                is_pressed[index] = False

def Play(board: list[list[int]] , row_count: int , column_count: int) -> str:
    """
    Description
    """

    is_pressed: list[bool] = [False, False, False, False]
    saved_board: list[list[int]] = None
    
    Place_Number(board, row_count, column_count)
    Place_Number(board, row_count, column_count)

    while True:
        
        print(GameBoard(board, row_count, column_count))
        Shift(board, row_count, column_count, *GetInput(is_pressed))

        if saved_board != board:
            Place_Number(board, row_count, column_count)
            saved_board = deepcopy(board)





def GameBoard(board: list[list[int]] , row_count: int , column_count: int) -> str:
    """
    Description
    """

    system("cls")

    row_index: int ; column_index: int ; cell_value: int ; cell_lenght: int
    gameboard: str = ""


    for row_index in range(row_count):

        for column_index in range(column_count):

            cell_value = board[row_index][column_index]

            if cell_value:

                cell_lenght = len(str(cell_value))
                gameboard += " "*(4-floor((cell_lenght+1)/2)) + "\033[1m" + str(cell_value) + "\033[0m" + " "*(4-ceil((cell_lenght+1)/2))

            else:
                gameboard += "   ─   "
        
        gameboard += "\n\n"


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





def Shift(board: list[list[int]] , row_count: int , column_count: int , user_axis: int , user_direction: int):
    """
    Description
    """

    range_index: int = (user_direction+1)//2
    row_range = [[row_count], [row_count-1, -1, -1]][range_index]
    column_range = [[column_count], [column_count-1, -1, -1]][range_index]
    board_merged: list[list[bool]] = [[False for _ in range(column_count)] for _ in range(row_count)]

    for row_index in range(*row_range):

        for column_index in range(*column_range):

            if board[row_index][column_index] != 0: #Inverser l'algo mouvement
                Movement(board, board_merged, row_count, column_count, user_axis, user_direction, row_index, column_index)





def Movement(board: list[list[int]], board_merged: list[list[bool]] , row_count: int , column_count: int , user_axis: int , user_direction: int , row_index: int , column_index: int):
    """
    Description
    """

    new_row_index: int = row_index
    new_column_index: int = column_index

    while True:

        new_row_index = new_row_index + (user_axis * user_direction)
        new_column_index = new_column_index + ((1 - user_axis) * user_direction)

        if not (0 <= new_row_index < row_count and 0 <= new_column_index < column_count):
            break
        
        if board[new_row_index][new_column_index] != 0:

            if board[new_row_index][new_column_index] == board[row_index][column_index] and not board_merged[new_row_index][new_column_index]:

                board[new_row_index][new_column_index] *= 2
                board[row_index][column_index] = 0
                board_merged[new_row_index][new_column_index] = True
                break
    
    new_row_index = new_row_index - (user_axis * user_direction)
    new_column_index = new_column_index - ((1 - user_axis) * user_direction)

    if [new_row_index, new_column_index] != [row_index, column_index]:
        board[new_row_index][new_column_index] = board[row_index][column_index]
        board[row_index][column_index] = 0





# Shift(
#     [
#         [2, 0, 0, 0],
#         [2, 0, 0, 0],
#         [2, 0, 0, 0],
#         [2, 0, 0, 0]
#     ],
#     4,
#     4,
#     0,
#     1
# )





if __name__ == "__main__": StartGame()