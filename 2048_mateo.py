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

        answer = AskInput_str("In which direction would you like to play ? (z or 8 = top / q or 4 = left / s or 2 = down / d or 6 = right)", "zqsd8426")

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





if __name__ == "__main__": StartGame()