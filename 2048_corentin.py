from random import randint

grid : list = []
for i in range(4):
    grid.append(["_"]*4)

def show_grid() :
    for i in range (len(grid)) :
        word = ""
        for j in range(len(grid[i])) :
            word += grid[i][j]
        print(word)

def game():
    show_grid()

def place_tiles():
    for elt in grid:
        

#Verify if Inputs is in authorized_inputs
def ask_input(message: str, authorized_inputs: list) -> str:
    while True :
        answer: str = input(message + str(authorized_inputs) + " : ")
        
        if answer in authorized_inputs :
            return answer

def start_game():
    while True :
        game()
        restart : str = ask_input("Start a new game ? ", ["y","Y","n","N"]).lower()
        if restart == "n" :
            break

start_game()
