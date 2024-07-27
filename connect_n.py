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
    def place_piece(self, player_color):
        # Let the user choose which column they want to place a piece at
        try:
            column = int(input(f"Choose which column to place piece{player_color.name}: "))
        except:
            print("FOR NOW EXIT IF NOT AN INT")
            return -1

        # The piece then has to go to the lowest row possible, or stop when they hit another piece, their own piece, or the bottom
        for row in range(self.row - 1, -1, -1):
            # check to see if at that row if there is an empty space
            if (self.grid[row][column] == piece.EMPTY):
                # if empty space at the bottom or highest that the piece can land then place it 
                self.grid[row][column] = player_color
                break

        return (row, column)
    
    def print_board(self):
        return_board = ""

        for r in range(len(self.grid)):
            for c in self.grid[r]:
                if c == piece.RED:
                    return_board += "R "
                elif c == piece.YELLOW:
                    return_board += "Y "
                elif c == piece.EMPTY:
                    return_board += "0 "
            return_board += "\n"

        print(return_board)
        

class Game():
    def __init__(self, row, col, connect_n):
        self.game = board(row, col, connect_n)
        self.connect_n = connect_n
        self.player = 1
        self.run()

    def run(self):
        game_running = True 
        while game_running:
            if self.player == 1:
                place_tuple = self.game.place_piece(piece.RED)
                win = self.check_win(*place_tuple, piece.RED)
                if win == True:
                    print(f"Player Red has won!")
                    self.game.print_board()
                    break
            elif self.player == 2:
                place_tuple = self.game.place_piece(piece.YELLOW)
                win = self.check_win(*place_tuple, piece.YELLOW)
                if win == True:
                    print(f"Player Red has Yellow!")
                    self.game.print_board()
                    break

            if place_tuple == -1:
                game_running = False
            else:
                self.game.print_board()
                if self.player == 1:
                    self.player = 2
                else:
                    self.player = 1

    def check_win(self, r, c, player):
        grid = self.game.get_grid()
        

        # Check for vertical 
        pieces_in_a_row = 0
        for r in range(len(grid)):
            if grid[r][c] == player:
                pieces_in_a_row += 1

                if pieces_in_a_row == self.connect_n:
                    return True
            else: 
                pieces_in_a_row = 0

game = Game(6, 6, 4)
