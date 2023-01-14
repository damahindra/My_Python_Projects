# Importing random library for computer's turn
import random

# Importing time library for the sleep() function after player is done inserting character
import time

# Making Custom TictacToe Class
class TicTacToe :

    '''
    Board Initialization :
    Default Board at the start of the game is
    - - -
    - - -
    - - -
    '''
    def __init__(self) :
        self.board = [] # board : a list containing characters inserted
        self.size = 3 # size : an integer which represent board's size (3x3)
        for i in range(self.size) :
            row = []
            for j in range(self.size) :
                row.append("-")
            self.board.append(row)

    ''' Function to update board when player or computer is done inserting character 
        Parameters :
        - coordinate : a list containing 2 axes (x and y)
        - char : player's character or computer's character ("X" or "O")
    '''
    def updateBoard(self, coordinate, char) :
        row = coordinate[0]
        column = coordinate[1]
        self.board[row][column] = char

    ''' Function to print the board into terminal, the printBoard function 
        will print the board with numbers beside the board as x and y axis 
        so the player and computer can insert their character's location
        based on the numbers.

        Default Board Printed :
        0 1 2 3
        1 - - -
        2 - - -
        3 - - -
    '''
    def printBoard(self) :
        print("\n===================\n")
        for i in range(4) :
            print(i, end=" ")
        print()
        for number, row in enumerate(self.board) :
            print(number+1, end=" ")
            for elements in row :
                print(elements, end=" ")
            print()
    
    '''
    Function to decide player and computer's character ("X" or "O")
    '''
    def playerChar(self) :
        return random.randint(0,1)

    '''
    Function to convert user's input to a list so it can be used inside the
    updateBoard() function.
    Parameters :
    - coordinate :a string containing 2 axes with a space (" ") in between.
    '''
    def convertCoordinate(self, coordinate) :
        position = coordinate.split(" ")
        return [int(x)-1 for x in position]

    '''
    Function for computer's turn. It will generate a random x and y axis and
    store it in a list to be used in the updateBoard() function. The function
    will check whether the randomized axes already has player's character,
    if yes, it will randomize again until it gets a location where there
    isn't a player's character.
    '''
    def computerMove(self) :
        c_move1 = random.randint(0,2)
        c_move2 = random.randint(0,2)
        while self.board[c_move1][c_move2] != "-" :
            c_move1 = random.randint(0,2)
            c_move2 = random.randint(0,2)
        return [c_move1, c_move2]       
    
    '''
    Conditions to win the game. If any of the condition is fulfilled,
    either the player or the computer can win the game.
    Parameters :
    - char : player or computer's character.
    '''
    def complete(self, char) :
        winConditions = (self.board[0][0] == char and self.board[0][1] == char and self.board[0][2] == char,
                         self.board[1][0] == char and self.board[1][1] == char and self.board[1][2] == char,
                         self.board[2][0] == char and self.board[2][1] == char and self.board[2][2] == char,
                         self.board[0][0] == char and self.board[1][0] == char and self.board[2][0] == char,
                         self.board[0][1] == char and self.board[1][1] == char and self.board[2][1] == char,
                         self.board[0][2] == char and self.board[1][2] == char and self.board[2][2] == char,
                         self.board[0][0] == char and self.board[1][1] == char and self.board[2][2] == char,
                         self.board[0][2] == char and self.board[1][1] == char and self.board[2][0] == char)
        if any(winConditions) :
            return True
        return False
    
    '''
    Function to determine that the game is a tie. It will check if there is
    still an empty spot on the board. If yes, than the game will continue.
    If there are no more empty spot and none of the win conditions are fulfilled
    it will return True
    
    '''
    def tie(self) :
        for i in range(self.size) :
            for j in range(self.size) :
                if self.board[i][j] == "-":
                    return False
        return True
    
    '''
    Function to print the winner of the game.
    Parameters :
    - winner : a string ("player" or "computer")
    '''
    def printWinner(self, winner) :
        print(f"{winner} wins!")
    
    '''
    Function to start the game.
    '''
    def start(self) :
        # Characters for player and computer
        player = ""
        computer = ""
        if self.playerChar() == 1 :
            player = "X"
            computer = "O"
        else :
            player = "O"
            computer = "X"

        # Header
        print("Let's play TicTacToe!")
        print("How to play : \nInsert the row and column you want to place your character on according to the board map (Ex : 1 2). Good Luck!\n")
        print(f"Player : {player}\nComputer : {computer}")
        playerWins = False

            # player always goes first
        while not playerWins :
            self.printBoard()
            if self.complete(computer) :
                break
            # player's turn
            p_move = input("Insert a coordinate : ")
            self.updateBoard(self.convertCoordinate(p_move), player)
            self.printBoard()
            if self.complete(player) :
                playerWins = True
                break
            if self.tie() :
                break
            # computer's turn
            self.updateBoard(self.computerMove(), computer)
            time.sleep(3)
            
        # winner
        if self.tie() :
            print("It's a tie!")
        elif playerWins :
            self.printWinner("Player")
        else :
            self.printWinner("Computer")

# object instantiation
game = TicTacToe()

# game start
game.start()

