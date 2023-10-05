import random
import math

class Player: 
    def __init__(self, letter):
        # x or o
        self.letter = letter

    def get_move(self, game):
        pass

class ComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        square = random.choice(game.available_moves())
        return square

class HumanPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        valid_square = False
        val = None
        while not valid_square:
            square = input(self.letter + '\'s turn! Input move (0-9): ')
            # check if the player's move is actually valid
            try:
                val = int(square)
                if val not in game.available_moves():
                    raise ValueError
                valid_square = True
            except ValueError:
                print("Invalid move! Try again...")

        return val
