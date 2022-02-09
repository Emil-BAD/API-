import random
import copy
import numpy

"""Я понял код из теории, но для облегчения дополнения игры, решил переписать код
вроде как работает без багов"""
"""У нас 4-ре столбца и 4-ре строки, то есть когда спрашивают какой столбец и какая строка мы смотрим на их
пересечении. Столбец - по вертикали, строка - по горизонтали"""
"""В питоне счёт идёт с нуля, но для облегчения счёт строки и столбца идёт с 1"""

win = False
board = [i for i in range(1, 16)]
board.append(0)
well_tabl = copy.copy(board)
random.shuffle(board)
for i in range(len(board)):
    if board[i] == 16:
        board[i] = 0
well_tabl = list(zip(*[iter(well_tabl)] * 4))
r_list = list(zip(*[iter(board)] * 4))
r_list = numpy.array(r_list)
well_tabl = numpy.array(well_tabl)
pos_void = None
for y in range(len(r_list)):
    for x in range(len(r_list[y])):
        if r_list[y][x] == 0:
            pos_void = x, y
print('У вас должно получиться так:')
print(well_tabl)
print('0 - это пустая клетка в пятнашках')
while win is False:
    print('Текущее поле:')
    print(r_list)
    from_x = int(input('Из какого столбца\n')) - 1
    from_y = int(input('Из какой строки\n')) - 1
    in_x = int(input('В какой столбец\n')) - 1
    in_y = int(input('В какую строку\n')) - 1
    if pos_void == (from_x, from_y):
        print("Эта клетка пуста")
    elif (in_x, in_y) != pos_void:
        print('Эта клетка занята')
    elif pos_void[0] != 0 and pos_void[0] != 3 and pos_void[1] != 0 and pos_void[1] != 3:
        if (from_x, from_y) != (pos_void[0] - 1, pos_void[1]) and (from_x, from_y) != (
                pos_void[0], pos_void[1] - 1) and (
                from_x, from_y) != (pos_void[0] + 1, pos_void[1]) and (from_x, from_y) != (
                pos_void[0], pos_void[1] + 1):
            print('Клетка слишком далеко от пустой')
        else:
            r_list[in_y][in_x] = r_list[from_y][from_x]
            r_list[from_y][from_x] = 0
    elif pos_void[0] == 0 and pos_void[1] != 0:
        if (from_x, from_y) != (pos_void[0], pos_void[1] - 1) and (from_x, from_y) != (
                pos_void[0], pos_void[1] + 1) and (
                from_x, from_y) != (pos_void[0] + 1, pos_void[1] - 1) and (from_x, from_y) != (
                pos_void[0] + 1, pos_void[1] + 1):
            print('Клетка далеко')
        else:
            r_list[in_y][in_x] = r_list[from_y][from_x]
            r_list[from_y][from_x] = 0
    elif pos_void[0] != 0 and pos_void[1] == 0:
        if (from_x, from_y) != (pos_void[0] - 1, pos_void[1]) and (from_x, from_y) != (
                pos_void[0] + 1, pos_void[1]) and (
                from_x, from_y) != (pos_void[0] + 1, pos_void[1] + 1) and (from_x, from_y) != (
                pos_void[0] - 1, pos_void[1] + 1):
            print('Клетка далеко')
        else:
            r_list[in_y][in_x] = r_list[from_y][from_x]
            r_list[from_y][from_x] = 0
    elif pos_void[0] == 3 and pos_void[1] != 3:
        if (from_x, from_y) != (pos_void[0], pos_void[1] - 1) and (from_x, from_y) != (
                pos_void[0], pos_void[1] + 1) and (
                from_x, from_y) != (pos_void[0] - 1, pos_void[1] - 1) and (from_x, from_y) != (
                pos_void[0] - 1, pos_void[1] + 1):
            print('Клетка далеко')
        else:
            r_list[in_y][in_x] = r_list[from_y][from_x]
            r_list[from_y][from_x] = 0
    elif pos_void[0] != 3 and pos_void[1] == 3:
        if (from_x, from_y) != (pos_void[0] - 1, pos_void[1]) and (from_x, from_y) != (
                pos_void[0] + 1, pos_void[1]) and (
                from_x, from_y) != (pos_void[0] + 1, pos_void[1] - 1) and (from_x, from_y) != (
                pos_void[0] - 1, pos_void[1] - 1):
            print('Клетка далеко')
        else:
            r_list[in_y][in_x] = r_list[from_y][from_x]
            r_list[from_y][from_x] = 0
    if r_list.tolist() == well_tabl.tolist():
        win = True
if win is True:
    print('Молодец, вы победили :-)')
