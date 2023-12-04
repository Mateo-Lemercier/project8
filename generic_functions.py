from random import randint


def AskInt(question:str) -> int:
    """
    Description
    """

    statement: str = question
    statement_wrong_answer: str = "\nPlease enter a valid number"
    answer: str

    while True:

        answer = input(statement + "\n> ")

        if answer.isdecimal():
            return int(answer)
        
        statement = statement_wrong_answer
        





def AskInt_Minimum(question:str, minimum:int) -> int:
    """
    Description
    """

    statement: str = question
    statement_wrong_answer: str = "\nPlease enter a number above or equal to " + str(minimum)
    value: int

    while True:

        value = AskInt(statement)

        if value >= minimum:
            return value
        
        statement = statement_wrong_answer





def AskInt_Maximum(question:str, maximum:int) -> int:
    """
    Description
    """

    statement: str = question
    statement_wrong_answer: str = "\nPlease enter a number below or equal to " + str(maximum)
    value: int

    while True:

        value = AskInt(statement)

        if value <= maximum:
            return value
        
        statement = statement_wrong_answer





def AskInt_Range(question:str, minimum:int, maximum:int) -> int:
    """
    Description
    """

    statement: str = question
    statement_wrong_answer: str = "\nPlease enter a number between " + str(minimum) + " and " + str(maximum)
    value: int

    while True:

        value = AskInt(statement)

        if (minimum <= value <= maximum):
            return value
        
        statement = statement_wrong_answer





def AskInput(question:str, authorized:list[str], lenght:int=1, case_sensitive:bool=False) -> str:
    """
    Description
    """

    statement: str = question
    statement_wrong_answer_1: str = "\nPlease enter only these : "
    for loop in range(len(authorized)): statement_wrong_answer_1 += authorized[loop] + ", "
    statement_wrong_answer_2: str = "\nPlease enter a " + str(lenght) + " letter(s) word"
    answer: str

    if not case_sensitive:
        authorized = [word.lower() for word in authorized]
    
    while True:

        answer = input(statement + "\n> ")
            
        if len(answer) != lenght:
            statement = statement_wrong_answer_2
            continue
        
        if not case_sensitive:
            answer = answer.lower()
        
        for text in answer:
            
            if text not in authorized:
                statement = statement_wrong_answer_1
                break
        
        else:
            return answer





def AskInput_str(question:str, authorized:str, lenght:int=1, case_sensitive:bool=False) -> str:
    """
    Description
    """

    return AskInput(question, [char for char in authorized], lenght, case_sensitive)





def AskReplay() -> bool:
    """
    Description
    """

    answer = AskInput_str("\nWanna replay ? (o/n)", "on", 1, False)

    if answer == "n":
        return False

    return True





def ChoiceWithChances(choices: list , chances: list[float] , precision: int = 2):
    """
    Description
    """

    random: int = randint(1, 10**precision) / 10**precision
    minimum: float = 0.0
    maximum: float = 0.0

    for loop in range(len(chances)):

        maximum += chances[loop]

        if minimum < random <= maximum:
            break

        minimum += chances[loop]
    
    return choices[loop]