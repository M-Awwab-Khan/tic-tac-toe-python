
class TicTacToe:
    def __init__(self) -> None:
        self.board = [
            ['   ', ' | ', '   ', ' | ', '   '], 
            ['   ', ' | ', '   ', ' | ', '   '], 
            ['   ', ' | ', '   ', ' | ', '   ']
        ]
        self.borders = ['---------------', '---------------', '']
        self.current_player = 'X'
        while True:
            self.current_player = 'O' if self.current_player == 'X' else 'X'
            self.print_board()
            self.make_move(self.current_player)

    def make_move(self, char):
        pos = input('Enter position of X in r,c form: ')
        r, c = map(int, pos.split(','))
        self.board[r-1][2*c - 2] = f' {char} '

    def print_board(self):
        for i in range(3):
            for j in range(5):
                print(self.board[i][j], end='')
            print()
            print(self.borders[i])

if __name__ == '__main__':
    game = TicTacToe()