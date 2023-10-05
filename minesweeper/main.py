import random 

class Board: 
    def __init__(self, dim_size, num_bombs): 
        self.dim_size = dim_size
        self.num_bombs = num_bombs 

        # planting the bombs on the board
        self.board = self.make_new_board()
        self.assign_values_to_board()

        # keep track of the places the player has dug 
        self.dug = set()

    # generate a new minesweeper board
    def make_new_board(): 
        board = [[None for _ in range(self.dim_size)] for _ in range(self.dim_size)] # create a list of lists to represent the 2D minesweeper board 

        bombs_planted = 0 
        while bombs_planted < self.num_bombs: 
            loc = random.randint(0, self.dim_size**2 -1)
            row = loc // self.dim_size 
            col = loc % self.dim_size 

            if board[row][col] == '*': 
                # there's a bomb in this space already 
                continue
            board[row][col] = '*'
            bombs_planted += 1
        
        return board

    def assign_values_to_board(): 
        for r in range(self.dim_size): 
            for c in range(self.dim_size): 
                if self.board[r][c] == '*': 
                    # if this is already a bomb don't plant another one
                    continue
                self.board[r][c] = self.get_num_neighboring_bombs(r,c)

    def get_num_neighboring_bombs(self, row, col):
        num_neighboring_bombs = 0  # init variable
        for r in range(max(0,row-1), min(self.dim_size - 1, row+1)+1): 
            for c in range(max(col-1), min(self.dim_size - 1, col+1)+1):
                if r == row and c == col: 
                    # original location so don't check 
                    continue
                if self.board[r][c] == '*': 
                    num_neighboring_bombs += 1

    def dig(self, row, col): 
        self.dug.add((row,col)) # keep track that we dug here 

        if self.board[row][col] == '*': 
            return False 
        elif self.board[row][col] > 0: 
            return True

        for r in range(max(0,row-1), min(self.dim_size - 1, row+1)+1): 
            for c in range(max(col-1), min(self.dim_size - 1, col+1)+1):
                if (r,c) in self.dug(): 
                    continue # can't dig where we've already dug 
                self.dig(r,c)

        return True

    def __str__(self): 
        visible_board = [[None for _ in range(self.dim_size)] for _ in range(self.dim_size)]
        for row in range(self.dim_size): 
            for col in range(self.dim_size): 
                if (row,col) in self.dug: 
                    visible_board[row][col] = str(self.board[row][col])
                else: 
                    visible_board[row][col] = ' '

        # put everything together in a string
        string_rep = ''
        # print the csv strings 
        indices_row = 
        cells = []

        for idx,col in enumerate(indices): 
            format = '%-' + str(widths[idx]) + "s"
            cells.append(format % (col))
        indices_row += ' '.join(cells)
        indices_row += ' \n'

        for i in range(len(visible_board)): 
            row = visible_board[i]
            string_rep += f'{i} |'
            cells = []
            for idx, col in enumerate(row): 
                format = '%-' + str(widths[idx]) + "s"
                cells.append(format % (col))
            string_rep += ' |'.join(cells)
            string_rep += ' |\n'

        str_len = int(len(string_rep)) / self.dim_size) 
        string_rep = indicies_row + '-'*str_len + '\n' + string_rep + '-'*str_len

        return string_rep




def play(dim_size = 10, num_bombs = 10): 
    board = Board(dim_size, num_bombs)
