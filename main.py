import numpy as np

class TicTacToe:
    def __init__(self) -> None:
        self.p1 = input('Player 1 name: ')
        p1_char = input('Player 1 character: ')
        self.p2 = input('Player 2 name: ')
        p2_char = input('Player 2 character: ')
        self.board = [
            ['   ', ' | ', '   ', ' | ', '   '], 
            ['   ', ' | ', '   ', ' | ', '   '], 
            ['   ', ' | ', '   ', ' | ', '   ']
        ]
        self.player_chars_positions = {
            self.p1: [p1_char, np.zeros((3, 3))],
            self.p2: [p2_char, np.zeros((3, 3))]
        }
        self.borders = ['---------------', '---------------', '']
        self.current_player = self.p1
        self.game_is_on = True
        while self.game_is_on:
            self.print_board()
            self.make_move(self.current_player)

    def make_move(self, cp):
        pos = input(f'{cp}, place {self.player_chars_positions[cp][0]} in r,c form: ')
        try:
            r, c = map(int, pos.split(','))
        except Exception as e:
            print('Invalid position. Please follow the format.')
        else:
            if self.board[r-1][2*c - 2] == '   ':
                self.board[r-1][2*c - 2] = f' {self.player_chars_positions[cp][0]} '
                self.player_chars_positions[cp][1][r-1, c-1] = 1
                # print(self.player_chars_positions[cp]) # for debugging
                if self.check_winner(self.current_player):
                    self.print_board()
                    print(f"{self.current_player} has won this game.")
                    self.game_is_on = False
                    return
                if self.check_draw():
                    self.print_board()
                    print(f"Draw")
                    self.game_is_on = False
                    return
                self.current_player = self.p1 if self.current_player == self.p2 else self.p2
            else:
                print('Position Already Marked!')

    def print_board(self):
        for i in range(3):
            for j in range(5):
                print(self.board[i][j], end='')
            print()
            print(self.borders[i])
    
    def check_winner(self, cp):
        winner = None
        for row_sum in self.player_chars_positions[cp][1].sum(axis=1):
            if row_sum == 3:
                winner = cp
        for col_sum in self.player_chars_positions[cp][1].sum(axis=0):
            if col_sum == 3:
                winner = cp
        if np.trace(self.player_chars_positions[cp][1]) == 3:
            winner = cp
        elif np.trace(np.fliplr(self.player_chars_positions[cp][1])) == 3:
            winner = cp
        return winner
    
    def check_draw(self):
        s = 0
        for cp, info in self.player_chars_positions.items():
            s += info[1].sum()
        return s == 9
if __name__ == '__main__':
    game = TicTacToe()