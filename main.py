board = [['   ', ' | ', '   ', ' | ', '   '], ['   ', ' | ', '   ', ' | ', '   '], ['   ', ' | ', '   ', ' | ', '   ']]
borders = ['---------------', '---------------', '']

for i in range(3):
    for j in range(5):
        print(board[i][j], end='')
    print()
    print(borders[i])
