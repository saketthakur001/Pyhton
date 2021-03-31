def display_board(board):
    print("\n" * 100)
    print(board[7]+"|"+ board[8] + "|" + board[9])
    print(board[4]+"|"+ board[5] + "|" + board[6])
    print(board[1]+"|"+ board[2] + "|" + board[3])

pl1 = input("Player 1: do you want to be X or O: ")

if pl1 == "X" or 'x':
    pl2 = "Y"
elif pl1 == "O" or 'o':
    pl2 = "X"
return pl1 and pl2