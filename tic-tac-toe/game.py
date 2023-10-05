import random 
import player
import math 

class TicTacToe: 
    def __init__(self): 
        self.board = [' ' for _ in range(9)] # 3x3 board 
        self.current_winner = None 

    def print_board(self): 
        # getting the rows in the game board 
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
            print('| ' + ' | '.join(row) + ' |')
        
    @staticmethod
    def print_board_nums(): 
        number_board = [[str(i) for i in range(j*3, (j+1)*3)] for j in range(3)]
        for number in number_board: 
            print('| ' + ' | '.join(number) + ' |')

    def available_moves(self): 
        return [i for i, spot in enumerate(self.board) if spot == ' ']

    def empty_squares(self):
        return ' ' in self.board

    def num_empty_squares(self):
        return self.board(' ')

    def make_move(self, square, letter):
        # if it's a valid move, make it
        if self.board[square] == ' ':
            self.board[letter] = letter
            if self.winner(square, letter):
                self.current_winner = letter
            return True
        return False

    def winner(self, square, letter): 
        # the winner is declared if they get 3 in a row
        row_ind = square // 3
        row = self.board[row_ind*3 : (row_ind + 1) * 3]
        if all([spot == letter for spot in row]):
            return True

        # check columns
        col_ind = square % 3
        column = [self.board[col_ind+i*3] for i in range(3)]
        if all([spot == letter for spot in column]): 
            return True

        # check diagonals
        if square % 2 == 0:
            diag1 = [self.board[i] for i in [0, 4, 8]] # left to right diagonal
            if all([spot == letter for spot in diag1]):
                return True
            diag2 = [self.board[i] for i in [2, 4, 6]] # right to left diagonal
            if all ([spot == letter for spot in diag2]):
                return True

def play(game, x_player, o_player, print_game = True):
    # returns the winner of the game or None for a tie
    if print_game:
        game.print_board_nums()

    # human player goes first
    letter = 'X' # starting letter

    # iterate while the board still has empty squares
    while game.empty_squares():
        # get the move from the right player
        if letter == 'O':
            square = o_player.get_move(game)
        else:
            square = x_player.get_move(game)

    if game.make_move(square, letter):
        if print_game:
            print(letter + f' makes a move to square {square}')
            game.print_board()
            print('') # just print an empty line

        if game.current_winner:
            if print_game:
                print(letter + ' wins!!')
            return letter

        # switch letters
        letter = 'O' if letter == 'X' else 'X'

    if print_game:
        print("It\'s a tie!")


if __name__ == "__main__":
    x_player = player.HumanPlayer('X')
    o_player = player.ComputerPlayer('O')
    t = TicTacToe()

    play(t, x_player, o_player, print_game=True)
