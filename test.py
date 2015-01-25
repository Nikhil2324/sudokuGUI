board = []
for i in range(9):
    board.append([])
    for j in range(9):
        board[i].append('0')

print board

flat = [x for sublist in board for x in sublist]

print flat

string = ''.join(flat)

print string
