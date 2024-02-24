import numpy as np

class TicTacToe:
    def __init__(self) -> None:
        self.board = [
            ['   ', ' | ', '   ', ' | ', '   '], 
            ['   ', ' | ', '   ', ' | ', '   '], 
            ['   ', ' | ', '   ', ' | ', '   ']
        ]
        self.player_positions = {
            'O': np.zeros((3, 3)),
            'X': np.zeros((3, 3))
        }
        self.borders = ['---------------', '---------------', '']
        self.current_player = 'X'
        while True:
            self.print_board()
            self.make_move(self.current_player)

    def make_move(self, char):
        pos = input('Enter position of X in r,c form: ')
        r, c = map(int, pos.split(','))
        if self.board[r-1][2*c - 2] == '   ':
            self.board[r-1][2*c - 2] = f' {char} '
            self.player_positions[char][r-1, c-1] = 1
            print(self.player_positions[char]) # for debugging
            print(self.check_winner(self.current_player))
            self.current_player = 'O' if self.current_player == 'X' else 'X'
        else:
            print('Position Already Marked!')

    def print_board(self):
        for i in range(3):
            for j in range(5):
                print(self.board[i][j], end='')
            print()
            print(self.borders[i])
    
    def check_winner(self, char):
        winner = None
        for row_sum in self.player_positions[char].sum(axis=1):
            if row_sum == 3:
                winner = char
        for col_sum in self.player_positions[char].sum(axis=0):
            if col_sum == 3:
                winner = char
        if np.trace(self.player_positions[char]) == 3:
            winner = char
        elif np.trace(np.fliplr(self.player_positions[char])) == 3:
            winner = char
        return winner


if __name__ == '__main__':
    game = TicTacToe()