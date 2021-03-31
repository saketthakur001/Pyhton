pos = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']

def board():
    print(f' {pos[0]} | {pos[1]} | {pos[2]} ')
    print(f'---+---+---')
    print(f' {pos[3]} | {pos[4]} | {pos[5]} ')
    print(f'---+---+---')
    print(f' {pos[6]} | {pos[7]} | {pos[8]} ')


print('X will play fisrt')
board()
wins = False
while True:
    player1 = int(input('player1: '))
    for num in pos:
        pass
    break
pos[pos.index(num)] = 'X'
print(pos)