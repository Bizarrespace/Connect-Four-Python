# use enums to represent a piece, either empty, red or yellow for example

from enum import Enum

class piece(Enum):
    EMPTY = 0
    RED = 1
    YELLOW = 2


class board():
    def __init__(self, row, col, connect_N):
        self.row = row
        self.col = col
        self.num_to_win = connect_N
        self.grid = self.init_board()

    def init_board(self):
        # Make a 2D matrix of just 0s
        return [[piece.EMPTY for c in range(self.col)] for r in range(self.row)]
    
    def get_grid(self):
        return self.grid

    # Need error handling, if the player inputs a invalid column
    # Need to return something to indicate if the placement was successful
    # Need to make a game class that does the placing of the piece instead of having it in board
        # The game class should also have a run that keeps on asking the user for placement and checks to see if they won.
    def place_piece(self, player_color):
        # Let the user choose which column they want to place a piece at
        column = int(input("Choose which column to place piece: "))

        # The piece then has to go to the lowest row possible, or stop when they hit another piece, their own piece, or the bottom
        for row in range(self.row - 1, -1, -1):
            # check to see if at that row if there is an empty space
            if (self.grid[row][column] == piece.EMPTY):
                # if empty space at the bottom or highest that the piece can land then place it 
                self.grid[row][column] = player_color
                break

        print(self.grid)
        


game = board(6, 6, 4)
game.place_piece(piece.RED)
