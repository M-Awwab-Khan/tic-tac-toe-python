
class TicTacToe:
    def __init__(self) -> None:
        self.board = [['   ', ' | ', '   ', ' | ', '   '], ['   ', ' | ', '   ', ' | ', '   '], ['   ', ' | ', '   ', ' | ', '   ']]
        self.borders = ['---------------', '---------------', '']

        self.print_board()
        self.make_move()

    def make_move(self):
        pos = input('Enter position of X in r,c form: ')
        r, c = map(int, pos.split(','))
        self.board[r-1][2*c - 2] = ' X '
        self.print_board()

    def print_board(self):
        for i in range(3):
            for j in range(5):
                print(self.board[i][j], end='')
            print()
            print(self.borders[i])

if __name__ == '__main__':
    game = TicTacToe()