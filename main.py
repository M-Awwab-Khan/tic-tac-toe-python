
class TicTacToe:
    def __init__(self) -> None:
        self.board = [['   ', ' | ', '   ', ' | ', '   '], ['   ', ' | ', '   ', ' | ', '   '], ['   ', ' | ', '   ', ' | ', '   ']]
        self.borders = ['---------------', '---------------', '']

        for i in range(3):
            for j in range(5):
                print(self.board[i][j], end='')
            print()
            print(self.borders[i])
        self.make_move()

    def make_move(self):
        pos = input('Enter position of X in r,c form: ')
        r, c = map(int, pos.split(','))
        print(r, c)

if __name__ == '__main__':
    game = TicTacToe()