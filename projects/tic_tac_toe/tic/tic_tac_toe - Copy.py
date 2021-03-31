import os


pos = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']

def board():
    print(f' {pos[0]} | {pos[1]} | {pos[2]} ')
    print(f'---+---+---')
    print(f' {pos[3]} | {pos[4]} | {pos[5]} ')
    print(f'---+---+---')
    print(f' {pos[6]} | {pos[7]} | {pos[8]} ')

os.system('cls')
print('X will play fisrt')
board()
wins = False
while True:
    try:
        player1 = int(input('player1: '))
        for num in pos:
            if player1 == pos.index(num)+1 and pos[pos.index(num)] == ' ':
                pos[pos.index(num)] = 'X'
                board()
#-----------------------------------------------------------
        
            if pos[0] == 'X' and pos[1] == 'X' and pos[2] == 'X':
                print("Player1 wins :)")
                break
            elif pos[3] == 'X' and pos[4] == 'X' and pos[5] == 'X':
                print("Player1 wins :)")
                break
            elif pos[6] == 'X' and pos[7] == 'X' and pos[8] == 'X':
                print("Player1 wins :)")
                break
            elif pos[0] == 'X' and pos[3] == 'X' and pos[6] == 'X':
                print("Player1 wins :)")
                break
            elif pos[1] == 'X' and pos[4] == 'X' and pos[7] == 'X':
                print("Player1 wins :)")
                break
            elif pos[2] == 'X' and pos[5] == 'X' and pos[8] == 'X':
                print("Player1 wins :)")
                break
            elif pos[0] == 'X' and pos[4] == 'X' and pos[8] == 'X':
                print("Player1 wins :)")
                break
            elif pos[6] == 'X' and pos[4] == 'X' and pos[2] == 'X':
                print("Player1 wins :)")
                break
#-----------------------------------------------------------
        player2 = int(input('player2: '))
        if player2 == 1 and pos[0] == ' ':
            pos[0] = 'O'
        elif player2 == 2 and pos[1] == ' ':
            pos[1] = 'O'
        elif player2 == 3 and pos[2] == ' ':
            pos[2] = 'O'
        elif player2 == 4 and pos[3] == ' ':
            pos[3] = 'O'
        elif player2 == 5 and pos[4] == ' ':
            pos[4] = 'O'
        elif player2 == 6 and pos[5] == ' ':
            pos[5] = 'O'
        elif player2 == 7 and pos[6] == ' ':
            pos[6] = 'O'
        elif player2 == 8 and pos[7] == ' ':
            pos[7] = 'O'
        elif player2 == 9 and pos[8] == ' ':
            pos[8] = 'O'
#-------------------------------------------------------------------
        if pos[0] == 'O' and pos[1] == 'O' and pos[2] == 'O':
            print("player2 wins :)")
            break
        elif pos[3] == 'O' and pos[4] == 'O' and pos[5] == 'O':
            print("player2 wins :)")
            break
        elif pos[6] == 'O' and pos[7] == 'O' and pos[8] == 'O':
            print("player2 wins :)")
            break
        elif pos[0] == 'O' and pos[3] == 'O' and pos[6] == 'O':
            print("player2 wins :)")
            break
        elif pos[1] == 'O' and pos[4] == 'O' and pos[7] == 'O':
            print("player2 wins :)")
            break
        elif pos[2] == 'O' and pos[5] == 'O' and pos[8] == 'O':
            print("player2 wins :)")
            break
        elif pos[0] == 'O' and pos[4] == 'O' and pos[8] == 'O':
            print("player2 wins :)")
            break
        elif pos[6] == 'O' and pos[4] == 'O' and pos[2] == 'O':
            print("player2 wins :)")
            break
    except ValueError:
        print('invalid input ¯\_(ツ)_/¯')
    board()