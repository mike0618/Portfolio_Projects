from random import getrandbits
# from tic_tac_toe_miked.classes import AI  # For package
from classes import AI
from time import sleep

cells = [' '] * 10


def ai(hard):
    sleep(0.5)
    ai_player = AI(cells)
    ai_player.hard = hard
    ai_player.check()
    weight = 0
    ind = None
    for cell in ai_player.g_cells:
        if cell.weight > weight:
            weight = cell.weight
            ind = cell.index
    cells[ind] = 'A'
    return True


def show_cells():
    print('\n' * 100)
    print(f' {cells[7]} | {cells[8]} | {cells[9]}\n'
          f'---|---|---\n'
          f' {cells[4]} | {cells[5]} | {cells[6]}\n'
          f'---|---|---\n'
          f' {cells[1]} | {cells[2]} | {cells[3]}')


def win_check(p):
    p = p * 3
    return ((cells[1] + cells[2] + cells[3] == p) or
            (cells[4] + cells[5] + cells[6] == p) or
            (cells[7] + cells[8] + cells[9] == p) or
            (cells[1] + cells[4] + cells[7] == p) or
            (cells[2] + cells[5] + cells[8] == p) or
            (cells[3] + cells[6] + cells[9] == p) or
            (cells[1] + cells[5] + cells[9] == p) or
            (cells[3] + cells[5] + cells[7] == p))


def make_turn(p, h):
    if p == 'A':
        ai(h)
        return True

    while True:
        cell = input(f'Player {p} enter your number (1-9): ')
        if len(cell) != 1 or cell not in '123456789':
            continue
        cell = int(cell)
        if cells[cell] != ' ':
            print('---Occupied!---', end=' ')
            continue
        cells[cell] = p
        return True


def play():
    print('*' * 32 + '\nWelcome to the Tic-Tac-Toe game!\n' + '*' * 32)
    ai_player = input('Play with AI? (y/N): ').lower() == 'y'
    hard = False
    if ai_player:
        hard = input('*' * 32 + '\nHard level? (y/N): ').lower() == 'y'
    show_cells()

    x_first = getrandbits(1)
    if x_first:
        print('X plays first')
    elif ai_player:
        print('AI plays first')
    else:
        print('O plays first')

    for turn in range(0+x_first, 9+x_first):
        if turn % 2:
            player = 'X'
        elif ai_player:
            player = 'A'
        else:
            player = 'O'

        make_turn(player, hard)
        show_cells()

        if win_check(player):
            print(f'***Player "{player}" won!***', end=' ')
            break
    else:
        print('***DRAW***', end=' ')

    if input('Play again? (y/N): ').lower() == 'y':
        for i in range(10):  # wipe cells
            cells[i] = ' '
        play()
    else:
        print('\nGood bye!\n' + '*' * 32)


if __name__ == '__main__':
    play()
