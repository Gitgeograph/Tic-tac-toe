from random import randint


board = [['-', '-', '-'],
         ['-', '-', '-'],
         ['-', '-', '-']]


def print_board(board):
    print('  0 1 2')
    for i in range(3):
        print(str(i), *board[i])


def player_input(cell):
    while True:
        place = input('Введите две координаты: ').split()
        if len(place) != 2:
            print('Введите две координаты')
            continue
        if not (place[0].isdigit() and place[1].isdigit):
            print('Введите числа')
            continue
        x, y = map(int, place)
        if not (0 <= x < 3 and 0 <= y < 3):
            print('Вы вышли из диапозона')
            continue
        if cell[x][y] != '-':
            print('Ячейка занята')
            continue
        else:
            cell[x][y] = 'x'
        break
    return cell[x][y]


def move_computer(cell):
    while True:
        x = randint(0, 2)
        y = randint(0, 2)
        if cell[x][y] != '-':
            continue
        else:
            cell[x][y] = 'o'
        break

    return cell[x][y]


def win(cell, val):
    def check_win(a1, a2, a3, val):
        if a1 == val and a2 == val and a3 == val:
            return True

    for i in range(3):
        if check_win(cell[i][0], cell[i][1], cell[i][2], val) or \
                check_win(cell[0][i], cell[1][i], cell[2][i], val) or \
                check_win(cell[0][0], cell[1][1], cell[2][2], val) or \
                check_win(cell[2][0], cell[1][1], cell[0][2], val):
            return True
    return False


def greet():
    print("-------------------")
    print("  Приветсвуем вас  ")
    print("      в игре       ")
    print("  крестики-нолики  ")
    print("-------------------")
    print(" формат ввода: x y ")
    print(" x - номер строки  ")
    print(" y - номер столбца ")

         
def start(board):
    count = 0
    greet()
    while True:
        print_board(board)
        if count % 2 == 0:
            player_input(board)
            player = 'x'
        else:
            move_computer(board)
            player = 'o'
        count += 1

        if win(board, player):
            print_board(board)
            print(f'Выиграл {player}')
            break
        if count == 9:
            print_board(board)
            print('Ничья')
            break


start(board)
