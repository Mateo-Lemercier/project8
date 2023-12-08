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





def Play(board: list[list[int]] , row_count: int , column_count: int) -> str:
    """
    Description
    """

    is_pressed: list[bool] = [False, False, False, False]
    
    Place_Number(board, row_count, column_count)
    Place_Number(board, row_count, column_count)

    while True:
        
        print(GameBoard(board, row_count, column_count))

        if Shift(board, row_count, column_count, *GetInput(is_pressed)):
            Place_Number(board, row_count, column_count)





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





def Shift(board: list[list[int]] , row_count: int , column_count: int , user_axis: int , user_direction: int) -> bool:
    """
    Description
    """

    range_index: int = (user_direction+1)//2
    row_range = [[row_count], [row_count-1, -1, -1]][range_index]
    column_range = [[column_count], [column_count-1, -1, -1]][range_index]
    moved: bool = False

    for row_index in range(*row_range):

        for column_index in range(*column_range):

            moved = Movement(board, row_count, column_count, user_axis, user_direction, row_index, column_index) or moved
    
    return moved





def Movement(board: list[list[int]] , row_count: int , column_count: int , user_axis: int , user_direction: int , row_index: int , column_index: int) -> bool:
    """
    Description
    """

    new_row_index:int = row_index
    new_column_index: int = column_index
    changed: bool = False

    while True:
        
        new_row_index -= user_axis * user_direction
        new_column_index -= (1 - user_axis) * user_direction

        if not (0 <= new_row_index < row_count and 0 <= new_column_index < column_count):
            break

        if board[new_row_index][new_column_index]:
            
            if board[row_index][column_index] == board[new_row_index][new_column_index]:

                board[row_index][column_index] += board[new_row_index][new_column_index]
                board[new_row_index][new_column_index] = 0
                changed = True
                break

            if board[row_index][column_index] == 0:

                board[row_index][column_index] += board[new_row_index][new_column_index]
                board[new_row_index][new_column_index] = 0
                changed = True
                continue
            
            break
    
    return changed





def ShiftVerification(board_start: list[list[int]] , board_end: list[list[int]] , user_axis: int , user_direction: int):
    """
    Description
    """

    row_count: int = len(board_start)
    column_count: int = len(board_start[0])
    
    Shift(board_start, row_count, column_count, user_axis, user_direction)

    if board_start == board_end:
        return True

    else:
        return False





def HardCodeBoardTry():
    """
    Description
                [0, 0, 0, 0], # 
    """

    to_verify: list[list] = [
        [
            [2, 0, 0, 0], # The 2 on the left should go on the right
            [2, 0, 0, 2], # The 2 on the left should merge with the 2 on the right
            [2, 2, 0, 0], # The 2s on the left should merge together and the right
            [2, 0, 2, 2], # The 2s on the right should merge and the 2 on the left should move to their left
            [4, 0, 2, 2], # The 2s on the right should merge and the 4 on the left should not merge with them and only move to their left
            [2, 2, 2, 2], # Both 2s on the right and 2s on the left should to merge (but not together after already merging)
            [4, 2, 0, 0], # Both 4 and 2 should to move
            [2, 0, 4, 2], # The 2 on the left isn't supposed to merge with the 2 on the right because there's a 4 in the middle
            [0, 0, 0, 2], # Nothing is supposed to move
        ],
        [
            [0, 0, 0, 2],
            [0, 0, 0, 4],
            [0, 0, 0, 4],
            [0, 0, 2, 4],
            [0, 0, 4, 4],
            [0, 0, 4, 4],
            [0, 0, 4, 2],
            [0, 2, 4, 2],
            [0, 0, 0, 2],
        ],
        0,
        1,
    ]

    for loop in range(4):
        to_verify[0] = TableTurnLeft(to_verify[0])
        to_verify[1] = TableTurnLeft(to_verify[1])
        to_verify[2] = 1 - loop%2
        to_verify[3] = 2*(loop//2) - 1
        print("To the " + ["top", "left", "bottom", "right"][loop] + " : " + str(ShiftVerification(*deepcopy(to_verify))))






# HardCodeBoardTry()
if __name__ == "__main__": StartGame()